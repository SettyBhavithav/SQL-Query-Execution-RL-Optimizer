"""Fixed-length state vector from SQL structure + measured PostgreSQL plans.

Variable-size plans are encoded by counting operators and taking fractions
(padded candidate flags).  Cardinalities and costs come from EXPLAIN JSON,
not from hand-tuned regex features.

All values in the state vector are derived from real database information:
  - Query structure parsed by sqlglot (table/join/predicate counts)
  - Join graph density
  - EXPLAIN ANALYZE metrics (cost, time, rows, buffers, operators)
  - Existing index information from pg_indexes
  - Candidate optimization counts

Nothing is fabricated or simulated.
"""

from __future__ import annotations

import math

import numpy as np

from sql_optimizer.actions import MAX_INDEX_CANDIDATES, MAX_JOIN_ORDERS
from sql_optimizer.parser import QueryStructure
from sql_optimizer.plan_parser import PlanMetrics
from sql_optimizer.query_generator import build_join_graph

# ── Feature vector layout ────────────────────────────────────────────────
# 0-7   : Query structure features
# 8-11  : Join graph features
# 12-13 : Candidate counts
# 14-15 : Index features
# 16-25 : PostgreSQL measured metrics (cost, time, rows, buffers)
# 26-28 : Join operator fractions
# 29-32 : Scan operator fractions
# 33-36 : Additional operator features
# 37-38 : Complexity features
# 39-44 : Existing index flags (padded to MAX_INDEX_CANDIDATES)
# 45-49 : Additional measured features (cache hit ratio, temp blocks, etc.)
# 50-51 : Plan tree features (node count, max loops)
STATE_DIM = 52

JOIN_NAMES = ["Hash Join", "Merge Join", "Nested Loop"]
SCAN_NAMES = ["Seq Scan", "Index Scan", "Index Only Scan", "Bitmap Heap Scan"]


def _logn(value: float, scale: float) -> float:
    """Log-normalize a non-negative value: log1p(value) / scale."""
    return float(math.log1p(max(value, 0.0)) / scale)


def encode_state(
    structure: QueryStructure,
    baseline: PlanMetrics,
    *,
    n_join_orders: int,
    n_index_candidates: int,
    existing_index_flags: list[float],
    n_existing_indexes: int,
) -> np.ndarray:
    """Build a fixed-size observation vector from real database information.

    Every value here is derived from sqlglot parse output or PostgreSQL
    EXPLAIN ANALYZE metrics.  No fabricated or simulated features.

    Parameters
    ----------
    structure : QueryStructure
        Parsed SQL query (from sqlglot).
    baseline : PlanMetrics
        Baseline EXPLAIN ANALYZE results from PostgreSQL.
    n_join_orders : int
        Number of valid candidate join orders generated.
    n_index_candidates : int
        Number of candidate indexes identified.
    existing_index_flags : list[float]
        1.0 if the corresponding candidate index already exists, 0.0 otherwise.
    n_existing_indexes : int
        Total number of existing indexes in the database.
    """
    graph, _ = build_join_graph(structure) if structure.parse_ok else ({}, None)
    n = max(structure.n_relations, 1)
    n_edges = sum(len(v) for v in graph.values()) / 2.0
    max_edges = n * (n - 1) / 2.0
    density = (n_edges / max_edges) if max_edges else 0.0

    joins = baseline.join_operators
    scans = baseline.scan_operators
    join_frac = _fractions(joins, JOIN_NAMES)
    scan_frac = _fractions(scans, SCAN_NAMES)

    flags = list(existing_index_flags[:MAX_INDEX_CANDIDATES])
    flags += [0.0] * (MAX_INDEX_CANDIDATES - len(flags))

    vec = [
        # ── Query structure (0-7) ────────────────────────────────────
        structure.n_relations / 8.0,                      # 0
        structure.n_joins / 8.0,                          # 1
        structure.n_predicates / 16.0,                    # 2
        len(structure.join_predicates) / 8.0,             # 3
        len(structure.filter_predicates) / 8.0,           # 4
        len(structure.group_by) / 8.0,                    # 5
        len(structure.order_by) / 8.0,                    # 6
        len(structure.aggregations) / 8.0,                # 7
        # ── Join graph features (8-11) ───────────────────────────────
        1.0 if structure.has_subquery else 0.0,           # 8
        min(len(structure.original_sql) / 2000.0, 1.0),   # 9
        float(density),                                    # 10
        len(structure.join_types) / 8.0,                  # 11
        # ── Candidate counts (12-13) ─────────────────────────────────
        n_join_orders / float(MAX_JOIN_ORDERS),           # 12
        n_index_candidates / float(MAX_INDEX_CANDIDATES), # 13
        # ── Index features (14-15) ───────────────────────────────────
        n_existing_indexes / 32.0,                        # 14
        sum(flags) / max(len(flags), 1),                  # 15  fraction existing
        # ── PostgreSQL measured metrics (16-25) ──────────────────────
        _logn(baseline.total_cost, 20.0),                 # 16
        _logn(baseline.startup_cost, 15.0),               # 17
        _logn(baseline.execution_time_ms, 10.0),          # 18
        _logn(baseline.planning_time_ms, 8.0),            # 19
        _logn(baseline.actual_rows, 20.0),                # 20
        _logn(baseline.plan_rows, 20.0),                  # 21
        _logn(baseline.shared_hit_blocks, 20.0),          # 22
        _logn(baseline.shared_read_blocks, 20.0),         # 23
        _logn(baseline.shared_written_blocks, 15.0),      # 24
        baseline.cache_hit_ratio,                          # 25
        # ── Join operator fractions (26-28) ──────────────────────────
        *join_frac,                                        # 26, 27, 28
        # ── Scan operator fractions (29-32) ──────────────────────────
        *scan_frac,                                        # 29, 30, 31, 32
        # ── Additional operator features (33-36) ─────────────────────
        joins.count("Nested Loop") / 8.0,                 # 33
        scans.count("Seq Scan") / 8.0,                    # 34
        scans.count("Index Scan") / 8.0,                  # 35
        scans.count("Index Only Scan") / 8.0,             # 36
        # ── Complexity features (37-38) ──────────────────────────────
        (structure.n_relations * structure.n_predicates) / 64.0,  # 37
        1.0 if structure.parse_ok else 0.0,               # 38
        # ── Existing index flags padded (39-44) ──────────────────────
        *flags,                                            # 39..44
        # ── Additional measured features (45-49) ─────────────────────
        _logn(baseline.temp_read_blocks + baseline.temp_written_blocks, 15.0),  # 45
        _logn(baseline.peak_memory_kb, 15.0),             # 46
        min(baseline.node_count / 20.0, 1.0),             # 47
        _logn(baseline.max_actual_loops, 10.0),           # 48
        # Cardinality estimation error (plan vs actual)
        _estimate_error(baseline.plan_rows, baseline.actual_rows),  # 49
        # ── Plan tree features (50-51) ───────────────────────────────
        len(baseline.all_operators) / 20.0,               # 50
        len(set(baseline.all_operators)) / 10.0,          # 51
    ]

    out = np.zeros(STATE_DIM, dtype=np.float32)
    clipped = np.clip(np.array(vec, dtype=np.float32), 0.0, 2.0)
    out[: min(STATE_DIM, clipped.size)] = clipped[:STATE_DIM]
    return out


def _fractions(ops: list[str], names: list[str]) -> list[float]:
    if not ops:
        return [0.0] * len(names)
    total = float(len(ops))
    return [ops.count(name) / total for name in names]


def _estimate_error(plan_rows: float, actual_rows: float) -> float:
    """Log-ratio of plan estimate vs actual rows, normalized to [0, 2]."""
    if plan_rows <= 0 or actual_rows <= 0:
        return 0.0
    ratio = max(plan_rows, actual_rows) / max(min(plan_rows, actual_rows), 1.0)
    return min(math.log1p(ratio) / 5.0, 2.0)
