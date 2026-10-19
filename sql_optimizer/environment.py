"""Gymnasium environment: one query, one real PostgreSQL optimization step.

Closed loop architecture
────────────────────────
  SQL query
    → parse (sqlglot)
    → candidate join orders + indexes
    → RL action (discrete: join order × join method × scan method × index)
    → rewrite SQL / SET join GUCs / SET scan GUCs / CREATE INDEX
    → EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) — *actual PostgreSQL execution*
    → measured time, cost, buffers, plan tree
    → reward from measured performance
    → index rollback

CRITICAL INVARIANT: The reward is NEVER computed as
    original_cost * (1 - cost_reduction)
or any equivalent artificial formula.  All reward components come from real
PostgreSQL EXPLAIN ANALYZE output.
"""

from __future__ import annotations

from typing import Any

import numpy as np
from gymnasium import Env, spaces

from sql_optimizer.actions import (
    MAX_INDEX_CANDIDATES,
    MAX_JOIN_ORDERS,
    N_JOIN_METHODS,
    N_SCAN_METHODS,
    decode_flat,
    decode_multi,
    flatten_dims,
)
from sql_optimizer.database import PostgresDB
from sql_optimizer.optimizer import (
    AppliedOptimization,
    CandidateSet,
    apply_action,
    build_candidates,
    execute_applied,
    rollback_applied,
)
from sql_optimizer.parser import parse_sql
from sql_optimizer.plan_parser import PlanMetrics
from sql_optimizer.reward import RewardWeights, classify_outcome, compute_reward
from sql_optimizer.state import STATE_DIM, encode_state


class SQLOptimizerEnv(Env):
    """Closed loop: parse → act → execute EXPLAIN ANALYZE → measured reward.

    Each episode is a single query. ``reset`` runs the unmodified query to
    obtain a PostgreSQL baseline. ``step`` applies a discrete optimization
    action and measures the resulting plan.  Temporary indexes are dropped
    after the step.

    Action space (MultiDiscrete)
    ────────────────────────────
    [join_order_idx, join_method_idx, scan_method_idx, index_idx]

    - join_order_idx  : 0 = original SQL, 1..k = equivalent JOIN rewrite
    - join_method_idx : 0=default, 1=hash, 2=merge, 3=nestloop
    - scan_method_idx : 0=default, 1=seqscan, 2=indexscan, 3=bitmapscan
    - index_idx       : 0 = no index, 1..k = candidate column

    Flattened Discrete mode (for DQN) encodes the same 4D action as a
    single integer.

    Observation space
    ─────────────────
    Fixed-size vector of STATE_DIM floats derived from:
    - sqlglot parse structure (tables, joins, predicates, etc.)
    - PostgreSQL EXPLAIN ANALYZE metrics (cost, time, rows, buffers)
    - Join graph density and operator fractions
    - Existing index flags and candidate counts
    """

    metadata = {"render_modes": []}

    def __init__(
        self,
        queries: list[str],
        db: PostgresDB | None = None,
        *,
        discrete_flat: bool = False,
        warmup: bool = True,
        warmup_runs: int = 1,
        reward_weights: RewardWeights | None = None,
        max_join_orders: int = MAX_JOIN_ORDERS,
        max_indexes: int = MAX_INDEX_CANDIDATES,
    ) -> None:
        super().__init__()
        if not queries:
            raise ValueError("SQLOptimizerEnv requires at least one query")
        self.queries = list(queries)
        self.db = db or PostgresDB()
        self.discrete_flat = discrete_flat
        self.warmup = warmup
        self.warmup_runs = warmup_runs
        self.reward_weights = reward_weights or RewardWeights()
        self.max_join_orders = max_join_orders
        self.max_indexes = max_indexes
        self.observation_space = spaces.Box(
            low=0.0, high=2.0, shape=(STATE_DIM,), dtype=np.float32
        )
        if discrete_flat:
            self.action_space = spaces.Discrete(flatten_dims())
        else:
            self.action_space = spaces.MultiDiscrete(
                [max_join_orders, N_JOIN_METHODS, N_SCAN_METHODS, max_indexes + 1]
            )
        self._idx = 0
        self._structure = None
        self._baseline: PlanMetrics | None = None
        self._candidates: CandidateSet | None = None
        self.last_info: dict[str, Any] = {}

    def close(self) -> None:
        self.db.drop_all_created_indexes()

    def reset(self, seed: int | None = None, options: dict | None = None):
        """Reset: select a query, run baseline EXPLAIN ANALYZE, build candidates.

        The baseline metrics come from real PostgreSQL execution.
        A warmup run is performed to stabilize buffer cache state.
        """
        super().reset(seed=seed)
        options = options or {}
        if "query_index" in options:
            self._idx = int(options["query_index"]) % len(self.queries)
        else:
            self._idx = int(self.np_random.integers(0, len(self.queries)))
        sql = self.queries[self._idx]
        self._structure = parse_sql(sql)

        # Warmup: stabilize buffer cache to reduce measurement noise
        if self.warmup:
            for _ in range(self.warmup_runs):
                try:
                    self.db.explain_analyze(self._structure.original_sql)
                except Exception:
                    pass

        # Baseline: real PostgreSQL EXPLAIN ANALYZE
        try:
            self._baseline = self.db.explain_analyze(self._structure.original_sql)
            failed = False
        except Exception as exc:  # noqa: BLE001
            self._baseline = PlanMetrics()
            failed = True
            self.last_info = {"reset_error": str(exc)}

        self._candidates = build_candidates(
            self.db,
            self._structure,
            max_orders=self.max_join_orders,
            max_indexes=self.max_indexes,
        )
        flags = [1.0 if s.exists else 0.0 for s in self._candidates.indexes]
        n_existing = len(self.db.list_indexes())
        obs = encode_state(
            self._structure,
            self._baseline,
            n_join_orders=len({s for s in self._candidates.join_sql}),
            n_index_candidates=len(self._candidates.indexes),
            existing_index_flags=flags,
            n_existing_indexes=n_existing,
        )
        info = {
            "query": self._structure.original_sql,
            "baseline_exec_ms": self._baseline.execution_time_ms,
            "baseline_cost": self._baseline.total_cost,
            "baseline_plan": self._baseline.signature,
            "n_join_candidates": len(set(self._candidates.join_sql)),
            "n_index_candidates": len(self._candidates.indexes),
            "reset_failed": failed,
        }
        self.last_info = info
        return obs, info

    def step(self, action):
        """Apply the RL action to PostgreSQL and measure real performance.

        This method:
        1. Decodes the action into join order + join method + scan method + index.
        2. Applies the optimization to PostgreSQL (SQL rewrite, GUCs, index).
        3. Runs EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) — real execution.
        4. Computes reward from measured performance.
        5. Rolls back any temporary index.
        6. Compares plan signatures to detect plan-unchanged outcomes.

        The reward is EXCLUSIVELY based on real PostgreSQL measurements.
        """
        assert self._structure is not None and self._baseline is not None
        parsed = decode_flat(int(action)) if self.discrete_flat else decode_multi(action)
        applied: AppliedOptimization | None = None
        failed = False
        error = ""
        try:
            applied = apply_action(self.db, self._structure, self._candidates, parsed)
            observed = execute_applied(self.db, applied)
        except Exception as exc:  # noqa: BLE001 - timeouts / planner errors
            failed = True
            error = str(exc)
            observed = PlanMetrics()
        finally:
            if applied is not None:
                rollback_applied(self.db, applied)

        reward, details = compute_reward(
            self._baseline,
            observed,
            created_index=bool(applied and applied.created_index_name),
            failed=failed,
            weights=self.reward_weights,
        )
        plan_unchanged = (not failed) and observed.signature == self._baseline.signature
        outcome = classify_outcome(
            self._baseline,
            observed,
            plan_unchanged=plan_unchanged,
            failed=failed,
            weights=self.reward_weights,
        )
        info = {
            **details,
            "query": self._structure.original_sql,
            "optimized_sql": applied.sql if applied else self._structure.original_sql,
            "action": parsed.as_tuple(),
            "action_description": applied.description if applied else "failed",
            "plan_unchanged": plan_unchanged,
            "outcome": outcome,
            "baseline_plan": self._baseline.signature,
            "observed_plan": observed.signature,
            "baseline_exec_ms": self._baseline.execution_time_ms,
            "observed_exec_ms": observed.execution_time_ms,
            "baseline_cost": self._baseline.total_cost,
            "observed_cost": observed.total_cost,
            "baseline_hits": self._baseline.shared_hit_blocks,
            "observed_hits": observed.shared_hit_blocks,
            "baseline_reads": self._baseline.shared_read_blocks,
            "observed_reads": observed.shared_read_blocks,
            "baseline_rows": self._baseline.actual_rows,
            "observed_rows": observed.actual_rows,
            "baseline_planning_ms": self._baseline.planning_time_ms,
            "observed_planning_ms": observed.planning_time_ms,
            "baseline_node_count": self._baseline.node_count,
            "observed_node_count": observed.node_count,
            "error": error,
        }
        self.last_info = info
        # Single-step MDP: the next observation is a dummy zero vector.
        next_obs = np.zeros(STATE_DIM, dtype=np.float32)
        return next_obs, float(reward), True, False, info
