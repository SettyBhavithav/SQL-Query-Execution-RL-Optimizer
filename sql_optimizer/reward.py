"""
Reward from *measured* PostgreSQL metrics only.

No agent output is allowed to scale or invent a cost. The environment compares
the baseline EXPLAIN ANALYZE of the original query against the EXPLAIN ANALYZE
of the action that was actually applied.

Conceptual form:

    reward = α * execution_time_improvement
           + β * buffer_read_improvement
           - γ * extra_planning_time
           - δ * index_creation_penalty

where each improvement term is (baseline - observed) / (baseline + eps),
clipped to a reasonable range so a single timeout does not explode gradients.

Justification
─────────────
- Execution time is the user-visible objective.  α=1.0 gives it the
  highest weight because users ultimately care about query latency.
- Shared read blocks proxy physical I/O; reducing them is valuable even
  when CPU time is noisy on a warm cache.  β=0.25 because I/O savings
  are secondary to total execution time.
- Extra planning time is the cost of trying exotic plans / building indexes.
  γ=0.05 is small because planning is usually ≪ execution time.
- Index creation carries a small penalty (δ=0.02) because DDL has
  real-world cost even though we drop the index after the step.
"""

from __future__ import annotations

from dataclasses import dataclass

from sql_optimizer.plan_parser import PlanMetrics


@dataclass
class RewardWeights:
    """Tunable weights for the multi-objective reward function.

    All reward components use REAL PostgreSQL measurements.
    No weight ever multiplies an agent-selected cost-reduction percentage.
    """

    # Weight on (baseline_time - observed_time) / baseline_time.
    # Highest weight because execution latency is the primary objective.
    alpha: float = 1.0

    # Weight on buffer read improvement (I/O proxy).
    # Lower than alpha because I/O is secondary to total execution time.
    beta: float = 0.25

    # Penalty weight on extra planning time.
    # Small because planning overhead is usually minor.
    gamma: float = 0.05

    # Flat penalty for creating a temporary index.
    # Reflects real DDL cost even though the index is rolled back.
    index_create_penalty: float = 0.02

    # Reward when the query fails (timeout, syntax error, etc.)
    timeout_penalty: float = -1.5

    # Relative time change smaller than this is treated as measurement noise.
    time_noise_floor: float = 0.02
    time_abs_floor_ms: float = 0.5


def compute_reward(
    baseline: PlanMetrics,
    observed: PlanMetrics,
    *,
    created_index: bool = False,
    failed: bool = False,
    weights: RewardWeights | None = None,
) -> tuple[float, dict[str, float]]:
    """Compute reward from REAL measured PostgreSQL performance.

    This function NEVER computes:
        predicted_cost = true_cost * (1 - cost_reduction)
    or any equivalent artificial formula.

    Parameters
    ----------
    baseline : PlanMetrics
        Metrics from running the original query.
    observed : PlanMetrics
        Metrics from running the RL-optimized query/plan.
    created_index : bool
        Whether a temporary index was created for this optimization.
    failed : bool
        Whether the optimized query failed (timeout, error).
    weights : RewardWeights
        Multi-objective weights.

    Returns
    -------
    reward : float
        Scalar reward signal for the RL agent.
    details : dict
        Breakdown of reward components for logging.
    """
    w = weights or RewardWeights()
    if failed:
        return float(w.timeout_penalty), {
            "time_improvement": 0.0,
            "buffer_improvement": 0.0,
            "planning_overhead": 0.0,
            "failed": 1.0,
        }

    eps = 1e-6

    # ── Execution time improvement (primary objective) ───────────────
    t_base = max(baseline.execution_time_ms, eps)
    t_obs = max(observed.execution_time_ms, 0.0)
    raw_time_imp = (t_base - t_obs) / t_base
    time_imp = float(max(min(raw_time_imp, 1.0), -2.0))

    # ── Buffer read improvement (I/O proxy) ──────────────────────────
    r_base = float(baseline.shared_read_blocks)
    r_obs = float(observed.shared_read_blocks)
    # Fall back to total shared blocks when both runs are fully cached.
    if r_base + r_obs == 0:
        r_base = float(baseline.shared_blocks)
        r_obs = float(observed.shared_blocks)
    raw_buf_imp = (r_base - r_obs) / (r_base + eps)
    buf_imp = float(max(min(raw_buf_imp, 1.0), -2.0))

    # ── Planning overhead penalty ────────────────────────────────────
    raw_plan_over = (observed.planning_time_ms - baseline.planning_time_ms) / (
        t_base + baseline.planning_time_ms + eps
    )
    plan_over = float(max(min(raw_plan_over, 2.0), 0.0))

    # ── Compute composite reward ─────────────────────────────────────
    reward = w.alpha * time_imp + w.beta * buf_imp - w.gamma * plan_over
    if created_index:
        reward -= w.index_create_penalty
    reward = float(max(min(reward, 2.0), -3.0))

    details = {
        "time_improvement": float(time_imp),
        "buffer_improvement": float(buf_imp),
        "planning_overhead": float(plan_over),
        "failed": 0.0,
        "baseline_exec_ms": baseline.execution_time_ms,
        "observed_exec_ms": observed.execution_time_ms,
        "baseline_cost": baseline.total_cost,
        "observed_cost": observed.total_cost,
        "baseline_read_blocks": baseline.shared_read_blocks,
        "observed_read_blocks": observed.shared_read_blocks,
        "baseline_hit_blocks": baseline.shared_hit_blocks,
        "observed_hit_blocks": observed.shared_hit_blocks,
    }
    return float(reward), details


def classify_outcome(
    baseline: PlanMetrics,
    observed: PlanMetrics,
    *,
    plan_unchanged: bool,
    failed: bool,
    weights: RewardWeights | None = None,
) -> str:
    """Classify the optimization outcome honestly.

    - 'failed'         : query errored or timed out
    - 'plan unchanged' : EXPLAIN shows the same operator tree
    - 'improved'       : execution time improved beyond noise floor
    - 'degraded'       : execution time worsened beyond noise floor
    - 'unchanged'      : execution time within noise floor

    An optimization is NEVER claimed unless the actual measured execution
    time improved AND the plan signature changed.
    """
    w = weights or RewardWeights()
    if failed:
        return "failed"
    if plan_unchanged:
        return "plan unchanged"
    delta = baseline.execution_time_ms - observed.execution_time_ms
    floor = max(w.time_abs_floor_ms, w.time_noise_floor * max(baseline.execution_time_ms, 1e-6))
    if delta > floor:
        return "improved"
    if delta < -floor:
        return "degraded"
    return "unchanged"
