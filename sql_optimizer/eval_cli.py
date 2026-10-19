"""CLI: evaluate a saved PPO/DQN policy on the test split.

Usage:
  python -m sql_optimizer.eval_cli --algo ppo
  python -m sql_optimizer.eval_cli --algo dqn --model results/dqn_optimizer.zip
"""

from __future__ import annotations

import argparse

from pathlib import Path

from sql_optimizer.agents import dqn_agent, ppo_agent
from sql_optimizer.database import PostgresDB
from sql_optimizer.demo_schema import bootstrap_demo_db, schema_is_ready
from sql_optimizer.environment import SQLOptimizerEnv
from sql_optimizer.evaluation import evaluate_policy, write_report
from sql_optimizer.utils import ROOT, load_yaml, set_seed
from sql_optimizer.workload import load_workload, split_queries


def main() -> None:
    p = argparse.ArgumentParser(description="Evaluate a trained RL SQL optimizer policy")
    p.add_argument("--config", default=str(ROOT / "configs" / "eval.yaml"))
    p.add_argument("--algo", choices=("ppo", "dqn"), default="ppo")
    p.add_argument("--model", default="")
    args = p.parse_args()
    cfg = load_yaml(args.config)
    seed = int(cfg.get("seed", 42))
    set_seed(seed)
    db = PostgresDB(
        dsn=cfg.get("database_url"),
        statement_timeout_ms=int(cfg.get("statement_timeout_ms", 15000)),
    )
    if not db.ping():
        raise SystemExit("PostgreSQL is not reachable")
    if not schema_is_ready(db):
        bootstrap_demo_db(db)
    wl = cfg.get("workload", {})
    queries = load_workload(
        wl.get("files") or ["job_light.sql", "synthetic.sql"],
        min_relations=int(wl.get("min_relations", 2)),
        max_relations=int(wl.get("max_relations", 4)),
        max_queries=int(wl.get("max_queries", 60)),
    )
    _, _, test_q = split_queries(queries, seed=seed)
    flat = args.algo == "dqn"
    env = SQLOptimizerEnv(test_q, db, discrete_flat=flat)
    model_path = args.model or str(
        ROOT / "results" / ("dqn_optimizer.zip" if flat else "ppo_optimizer.zip")
    )
    model = (dqn_agent if flat else ppo_agent).load_model(Path(model_path), env)
    print(f"Evaluating {args.algo.upper()} on {len(test_q)} test queries...")
    result = evaluate_policy(model, env, test_q)
    md = write_report(result, ROOT / "results" / f"{args.algo}_eval_cli")
    agg = result["aggregates"]
    print(f"\nResults:")
    print(f"  Queries: {agg.get('n_queries')}")
    print(f"  Improved: {agg.get('pct_improved')}%")
    print(f"  Unchanged: {agg.get('pct_unchanged')}%")
    print(f"  Degraded: {agg.get('pct_degraded')}%")
    print(f"  Mean time improvement: {agg.get('mean_time_improvement')}")
    print(f"  Report: {md}")
    db.close()


if __name__ == "__main__":
    main()
