"""Evaluate a trained policy against PostgreSQL baselines for every test query.

ALL queries are reported—including failures, regressions, and plan-unchanged
outcomes.  An optimization is claimed ONLY when:
  1. The EXPLAIN plan actually changed.
  2. Measured execution time improved beyond the noise floor.

Execution plan comparison (before/after) is included for every query.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any

import numpy as np

from sql_optimizer.environment import SQLOptimizerEnv
from sql_optimizer.utils import dump_json, ensure_dir


def evaluate_policy(
    model,
    env: SQLOptimizerEnv,
    queries: list[str],
    *,
    deterministic: bool = True,
) -> dict[str, Any]:
    """Evaluate a trained policy on every query in the list.

    For each query:
    1. Run original query (baseline) with EXPLAIN ANALYZE.
    2. Apply RL-selected action.
    3. Run optimized query/plan with EXPLAIN ANALYZE.
    4. Compare execution plans and measured performance.
    5. Report results honestly (including regressions).

    Returns a dict with per-query rows and aggregate statistics.
    """
    rows: list[dict[str, Any]] = []
    for i, sql in enumerate(queries):
        obs, _ = env.reset(options={"query_index": i})
        action, _ = model.predict(obs, deterministic=deterministic)
        _, reward, _, _, info = env.step(action)
        time_imp = _rel_improvement(info.get("baseline_exec_ms"), info.get("observed_exec_ms"))
        cost_imp = _rel_improvement(info.get("baseline_cost"), info.get("observed_cost"))
        buf_base = float(info.get("baseline_reads") or 0) + float(info.get("baseline_hits") or 0)
        buf_obs = float(info.get("observed_reads") or 0) + float(info.get("observed_hits") or 0)
        buf_imp = _rel_improvement(buf_base, buf_obs)
        improved = info.get("outcome") == "improved"

        # ── Plan comparison (before/after) ────────────────────────────
        baseline_plan = info.get("baseline_plan", "")
        observed_plan = info.get("observed_plan", "")
        plan_changed = baseline_plan != observed_plan

        rows.append(
            {
                "query_index": i,
                "query": _short(sql),
                "sql": sql,
                "baseline_time_ms": info.get("baseline_exec_ms"),
                "rl_time_ms": info.get("observed_exec_ms"),
                "time_improvement": time_imp,
                "baseline_cost": info.get("baseline_cost"),
                "rl_cost": info.get("observed_cost"),
                "cost_improvement": cost_imp,
                "buffer_improvement": buf_imp,
                "baseline_planning_ms": info.get("baseline_planning_ms"),
                "rl_planning_ms": info.get("observed_planning_ms"),
                "planning_overhead_ms": float(info.get("observed_planning_ms") or 0)
                - float(info.get("baseline_planning_ms") or 0),
                "baseline_rows": info.get("baseline_rows"),
                "rl_rows": info.get("observed_rows"),
                "baseline_hits": info.get("baseline_hits"),
                "rl_hits": info.get("observed_hits"),
                "baseline_reads": info.get("baseline_reads"),
                "rl_reads": info.get("observed_reads"),
                "outcome": info.get("outcome"),
                "plan_unchanged": info.get("plan_unchanged"),
                "plan_changed": plan_changed,
                "action": info.get("action_description"),
                "reward": float(reward),
                "claimed_optimization": bool(improved),
                "baseline_plan": baseline_plan,
                "rl_plan": observed_plan,
                "optimized_sql": info.get("optimized_sql", ""),
            }
        )
    return {"rows": rows, "aggregates": aggregate(rows)}


def aggregate(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """Compute aggregate statistics over ALL queries (including failures).

    No queries are excluded from these statistics.
    """
    if not rows:
        return {}
    times_b = np.array([float(r["baseline_time_ms"] or 0) for r in rows])
    times_r = np.array([float(r["rl_time_ms"] or 0) for r in rows])
    imps = np.array([float(r["time_improvement"] or 0) for r in rows])
    cost_imps = np.array([float(r.get("cost_improvement") or 0) for r in rows])
    plan_over = np.array([float(r["planning_overhead_ms"] or 0) for r in rows])
    counts = Counter(str(r["outcome"]) for r in rows)
    n = len(rows)
    return {
        "n_queries": n,
        "mean_baseline_time_ms": round(float(np.mean(times_b)), 3),
        "median_baseline_time_ms": round(float(np.median(times_b)), 3),
        "mean_rl_time_ms": round(float(np.mean(times_r)), 3),
        "median_rl_time_ms": round(float(np.median(times_r)), 3),
        "mean_time_improvement": round(float(np.mean(imps)), 4),
        "median_time_improvement": round(float(np.median(imps)), 4),
        "mean_cost_improvement": round(float(np.mean(cost_imps)), 4),
        "pct_improved": round(100.0 * counts.get("improved", 0) / n, 1),
        "pct_unchanged": round(
            100.0 * (counts.get("unchanged", 0) + counts.get("plan unchanged", 0)) / n, 1
        ),
        "pct_plan_unchanged": round(100.0 * counts.get("plan unchanged", 0) / n, 1),
        "pct_degraded": round(100.0 * counts.get("degraded", 0) / n, 1),
        "pct_failed": round(100.0 * counts.get("failed", 0) / n, 1),
        "mean_planning_overhead_ms": round(float(np.mean(plan_over)), 3),
        "median_planning_overhead_ms": round(float(np.median(plan_over)), 3),
        "outcome_counts": dict(counts),
    }


def write_report(result: dict[str, Any], path: Path) -> Path:
    """Write evaluation results as both JSON and a readable Markdown report.

    The Markdown report includes:
    1. Per-query table with all metrics.
    2. Execution plan comparison (before/after) for each query.
    3. Aggregate statistics over ALL queries.
    """
    ensure_dir(path.parent)
    dump_json(path.with_suffix(".json"), result)
    md = path.with_suffix(".md")
    rows = result["rows"]
    agg = result["aggregates"]
    lines = [
        "# PostgreSQL RL Optimizer Evaluation Report",
        "",
        "Improvements are claimed only when measured execution time improved",
        "and the EXPLAIN plan actually changed. `plan unchanged` is reported",
        "when the selected action did not change PostgreSQL's operator tree.",
        "",
        "## Per-query Results",
        "",
        "| Query | Baseline Time | RL Time | Time Improvement | Baseline Cost | RL Cost | Buffer Improvement | Outcome |",
        "| ----- | ------------- | ------- | ---------------- | ------------- | ------- | ------------------ | ------- |",
    ]
    for r in rows:
        lines.append(
            "| {query} | {baseline_time_ms:.3f} | {rl_time_ms:.3f} | {time_improvement:.3f} | "
            "{baseline_cost:.2f} | {rl_cost:.2f} | {buffer_improvement:.3f} | {outcome} |".format(
                query=_md_cell(r["query"]),
                baseline_time_ms=float(r["baseline_time_ms"] or 0),
                rl_time_ms=float(r["rl_time_ms"] or 0),
                time_improvement=float(r["time_improvement"] or 0),
                baseline_cost=float(r["baseline_cost"] or 0),
                rl_cost=float(r["rl_cost"] or 0),
                buffer_improvement=float(r["buffer_improvement"] or 0),
                outcome=r["outcome"],
            )
        )

    # ── Execution plan comparisons ────────────────────────────────────
    lines.extend([
        "",
        "## Execution Plan Comparisons",
        "",
        "For every query, the original and RL-selected plans are shown.",
        "If the plan did not change, it is reported as 'Plan unchanged'.",
        "",
    ])
    for r in rows:
        lines.append(f"### Query {r['query_index']}: {_md_cell(r['query'])}")
        lines.append(f"- **Action**: {r.get('action', 'N/A')}")
        lines.append(f"- **Outcome**: {r['outcome']}")
        if r.get("plan_unchanged"):
            lines.append("- **Plan**: unchanged")
        else:
            lines.append("")
            lines.append("**Original plan:**")
            lines.append("```")
            lines.append(r.get("baseline_plan", "N/A"))
            lines.append("```")
            lines.append("")
            lines.append("**RL-selected plan:**")
            lines.append("```")
            lines.append(r.get("rl_plan", "N/A"))
            lines.append("```")
        lines.append("")

    # ── Aggregate statistics ──────────────────────────────────────────
    lines.extend(
        [
            "## Aggregates (all queries, including failures and regressions)",
            "",
            f"- **Queries evaluated**: {agg.get('n_queries')}",
            f"- Mean baseline time (ms): {agg.get('mean_baseline_time_ms')}",
            f"- Median baseline time (ms): {agg.get('median_baseline_time_ms')}",
            f"- Mean RL time (ms): {agg.get('mean_rl_time_ms')}",
            f"- Median RL time (ms): {agg.get('median_rl_time_ms')}",
            f"- Mean time improvement: {agg.get('mean_time_improvement')}",
            f"- Median time improvement: {agg.get('median_time_improvement')}",
            f"- Mean cost improvement: {agg.get('mean_cost_improvement')}",
            f"- **Percent improved**: {agg.get('pct_improved')}%",
            f"- Percent unchanged (incl. plan unchanged): {agg.get('pct_unchanged')}%",
            f"- Percent plan unchanged: {agg.get('pct_plan_unchanged')}%",
            f"- **Percent degraded**: {agg.get('pct_degraded')}%",
            f"- Percent failed: {agg.get('pct_failed')}%",
            f"- Mean planning overhead (ms): {agg.get('mean_planning_overhead_ms')}",
            f"- Median planning overhead (ms): {agg.get('median_planning_overhead_ms')}",
            f"- Outcome counts: {agg.get('outcome_counts')}",
            "",
        ]
    )
    md.write_text("\n".join(lines), encoding="utf-8")
    return md


def _rel_improvement(baseline, observed) -> float:
    """Relative improvement: (baseline - observed) / baseline."""
    b = float(baseline or 0.0)
    o = float(observed or 0.0)
    if b <= 0:
        return 0.0
    return (b - o) / b


def _short(sql: str, n: int = 80) -> str:
    text = " ".join(sql.split())
    return text if len(text) <= n else text[: n - 3] + "..."


def _md_cell(text: str) -> str:
    return text.replace("|", "/")
