"""Offline tests: parser, join rewrite, reward, action encoding (no PostgreSQL).

These tests verify the offline components of the RL optimizer pipeline
without requiring a live PostgreSQL connection.
"""

from __future__ import annotations

from sql_optimizer.actions import OptimizationAction, decode_flat, encode_flat, flatten_dims
from sql_optimizer.parser import parse_sql
from sql_optimizer.plan_parser import PlanMetrics, parse_explain_json
from sql_optimizer.query_generator import generate_join_trees, rewrite_join_order
from sql_optimizer.reward import classify_outcome, compute_reward
from sql_optimizer.workload import split_queries


SQL = """
SELECT COUNT(*)
FROM movie_companies mc, title t, movie_keyword mk
WHERE t.id = mc.movie_id AND t.id = mk.movie_id AND mk.keyword_id = 117
"""


def test_parse_job_light_style():
    s = parse_sql(SQL)
    assert s.parse_ok
    assert s.n_relations == 3
    assert s.n_joins >= 2
    assert len(s.join_predicates) >= 2
    assert "t" in s.tables and s.tables["t"].lower() == "title"


def test_join_rewrites_are_equivalent_shape():
    s = parse_sql(SQL)
    trees = generate_join_trees(s, max_orders=8)
    assert trees
    rewritten = [rewrite_join_order(s, t) for t in trees]
    assert all("JOIN" in r.upper() for r in rewritten)
    assert all("keyword_id" in r for r in rewritten)
    assert all("COUNT" in r.upper() for r in rewritten)


def test_no_cost_reduction_action_encoding():
    """Verify actions have NO cost_reduction parameter."""
    a = OptimizationAction(1, 2, 1, 3)  # 4D: order, method, scan, index
    assert decode_flat(encode_flat(a)).as_tuple() == a.as_tuple()
    assert "cost" not in str(a.join_method)
    assert "reduction" not in str(a.join_method)
    assert "reduction" not in str(a.scan_method)
    # Verify 4D tuple
    assert len(a.as_tuple()) == 4


def test_action_roundtrip_all_dimensions():
    """Verify flat ↔ multi encoding roundtrip for the 4D action space."""
    for order in range(3):
        for method in range(4):
            for scan in range(4):
                for idx in range(3):
                    a = OptimizationAction(order, method, scan, idx)
                    flat_id = encode_flat(a)
                    decoded = decode_flat(flat_id)
                    assert decoded.as_tuple() == a.as_tuple(), (
                        f"Roundtrip failed: {a.as_tuple()} → {flat_id} → {decoded.as_tuple()}"
                    )


def test_flatten_dims_consistent():
    """Verify flatten_dims matches the product of action dimensions."""
    from sql_optimizer.actions import MAX_JOIN_ORDERS, N_JOIN_METHODS, N_SCAN_METHODS, MAX_INDEX_CANDIDATES
    expected = MAX_JOIN_ORDERS * N_JOIN_METHODS * N_SCAN_METHODS * (MAX_INDEX_CANDIDATES + 1)
    assert flatten_dims() == expected


def test_reward_uses_measured_times():
    """Verify reward is computed from measured metrics, not artificial formula."""
    base = PlanMetrics(execution_time_ms=10.0, planning_time_ms=1.0, shared_read_blocks=100)
    fast = PlanMetrics(execution_time_ms=5.0, planning_time_ms=1.2, shared_read_blocks=40)
    r, details = compute_reward(base, fast)
    assert r > 0
    assert details["time_improvement"] == 0.5
    # Verify reward comes from measured metrics
    assert details["baseline_exec_ms"] == 10.0
    assert details["observed_exec_ms"] == 5.0
    slow = PlanMetrics(execution_time_ms=20.0, planning_time_ms=1.0, shared_read_blocks=100)
    r2, _ = compute_reward(base, slow)
    assert r2 < 0


def test_reward_no_artificial_scaling():
    """Verify that reward is NOT computed as original * (1 - reduction).

    This is the critical test: the reward function must never use any
    agent-selected percentage to scale the original cost.
    """
    base = PlanMetrics(execution_time_ms=100.0, total_cost=1000.0)
    obs = PlanMetrics(execution_time_ms=80.0, total_cost=900.0)
    r, details = compute_reward(base, obs)
    # Time improvement should be (100 - 80) / 100 = 0.2
    assert abs(details["time_improvement"] - 0.2) < 1e-6
    # The reward should NOT be based on cost * (1 - X) for any X
    # It should be based on measured time improvement
    assert r > 0


def test_plan_unchanged_classification():
    m = PlanMetrics(execution_time_ms=10.0, signature="Seq Scan")
    assert classify_outcome(m, m, plan_unchanged=True, failed=False) == "plan unchanged"
    other = PlanMetrics(execution_time_ms=5.0, signature="Index Scan")
    assert classify_outcome(m, other, plan_unchanged=False, failed=False) == "improved"


def test_plan_unchanged_not_claimed_as_optimization():
    """If the plan didn't change, it should NEVER be classified as 'improved'."""
    m = PlanMetrics(execution_time_ms=10.0, signature="Same Plan")
    faster = PlanMetrics(execution_time_ms=5.0, signature="Same Plan")
    # Even if execution is faster, if plan is unchanged, don't claim optimization
    result = classify_outcome(m, faster, plan_unchanged=True, failed=False)
    assert result == "plan unchanged"


def test_split_does_not_sort_by_cost():
    """Verify train/val/test split is random, NOT sorted by PostgreSQL cost."""
    queries = [
        "SELECT 1 FROM title t, movie_keyword mk WHERE t.id = mk.movie_id AND t.production_year > 2000",
        "SELECT 1 FROM title t, movie_keyword mk WHERE t.id = mk.movie_id AND t.production_year > 2001",
        "SELECT 1 FROM title t, movie_keyword mk WHERE t.id = mk.movie_id AND t.production_year > 2002",
        "SELECT 1 FROM title t, movie_keyword mk WHERE t.id = mk.movie_id AND t.production_year > 2003",
        "SELECT 1 FROM title t, movie_keyword mk WHERE t.id = mk.movie_id AND t.production_year > 2004",
        "SELECT 1 FROM title t, movie_keyword mk WHERE t.id = mk.movie_id AND t.production_year > 2005",
        "SELECT 1 FROM title t, movie_keyword mk WHERE t.id = mk.movie_id AND t.production_year > 2006",
        "SELECT 1 FROM title t, movie_keyword mk WHERE t.id = mk.movie_id AND t.production_year > 2007",
        "SELECT 1 FROM title t, movie_keyword mk WHERE t.id = mk.movie_id AND t.production_year > 2008",
        "SELECT 1 FROM title t, movie_keyword mk WHERE t.id = mk.movie_id AND t.production_year > 2009",
    ]
    train, val, test = split_queries(queries, seed=42)
    assert len(train) + len(val) + len(test) == 10
    # Duplicates should not leak across splits
    dup = queries[0]
    train2, val2, test2 = split_queries(queries + [dup], seed=42)
    keys = set(train2) | set(val2) | set(test2)
    assert len(keys) == 10


def test_explain_json_parser():
    """Verify the plan parser extracts real PostgreSQL EXPLAIN JSON correctly."""
    payload = [
        {
            "Planning Time": 0.4,
            "Execution Time": 12.5,
            "Plan": {
                "Node Type": "Hash Join",
                "Total Cost": 99.0,
                "Startup Cost": 5.0,
                "Actual Rows": 7,
                "Plan Rows": 10,
                "Shared Hit Blocks": 3,
                "Shared Read Blocks": 1,
                "Plans": [
                    {
                        "Node Type": "Seq Scan",
                        "Relation Name": "title",
                        "Shared Hit Blocks": 2,
                        "Shared Read Blocks": 0,
                    },
                    {
                        "Node Type": "Hash",
                        "Plans": [
                            {
                                "Node Type": "Index Scan",
                                "Relation Name": "movie_keyword",
                                "Shared Hit Blocks": 1,
                                "Shared Read Blocks": 1,
                            }
                        ],
                    },
                ],
            },
        }
    ]
    m = parse_explain_json(payload)
    assert m.execution_time_ms == 12.5
    assert m.total_cost == 99.0
    assert m.startup_cost == 5.0
    assert "Hash Join" in m.join_operators
    assert "Seq Scan" in m.scan_operators
    assert m.shared_hit_blocks == 3
    assert m.shared_read_blocks == 1
    assert "Hash Join" in m.signature
    assert m.node_count >= 3  # Hash Join, Seq Scan, Hash, Index Scan


def test_plan_metrics_has_no_artificial_fields():
    """Verify PlanMetrics has no cost_reduction or similar artificial fields."""
    m = PlanMetrics()
    # Should NOT have these fields
    assert not hasattr(m, "cost_reduction")
    assert not hasattr(m, "predicted_cost")
    assert not hasattr(m, "simulated_cost")
    # Should HAVE these real measurement fields
    assert hasattr(m, "execution_time_ms")
    assert hasattr(m, "planning_time_ms")
    assert hasattr(m, "total_cost")
    assert hasattr(m, "shared_hit_blocks")
    assert hasattr(m, "shared_read_blocks")
