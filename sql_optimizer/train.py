"""Train PPO (MultiDiscrete) and DQN (Discrete) on measured PostgreSQL rewards.

Training loop:
  1. Connect to PostgreSQL and bootstrap the demo schema if needed.
  2. Load and parse SQL workload queries.
  3. Split into train/val/test without cost-based sorting.
  4. For each algorithm:
     a. Create Gymnasium environment with real PostgreSQL backend.
     b. Train the agent (each step = real EXPLAIN ANALYZE).
     c. Evaluate on val and test splits.
     d. Write per-query reports with plan comparisons.
  5. Save metadata for reproducibility.

CRITICAL: All training rewards come from real PostgreSQL execution.
Nothing is simulated or artificially scaled.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from sql_optimizer.agents import dqn_agent, ppo_agent
from sql_optimizer.database import PostgresDB
from sql_optimizer.demo_schema import bootstrap_demo_db, schema_is_ready
from sql_optimizer.environment import SQLOptimizerEnv
from sql_optimizer.evaluation import evaluate_policy, write_report
from sql_optimizer.utils import ROOT, dump_json, ensure_dir, load_yaml, set_seed
from sql_optimizer.workload import load_workload, split_queries


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Train RL SQL optimizer against PostgreSQL")
    p.add_argument("--config", default=str(ROOT / "configs" / "train.yaml"))
    p.add_argument("--algo", choices=("ppo", "dqn", "both"), default="both")
    p.add_argument("--skip-bootstrap", action="store_true")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    cfg = load_yaml(args.config)
    seed = int(cfg.get("seed", 42))
    set_seed(seed)

    db = PostgresDB(
        dsn=cfg.get("database_url"),
        statement_timeout_ms=int(cfg.get("statement_timeout_ms", 15_000)),
    )
    if not db.ping():
        raise SystemExit(
            "Cannot connect to PostgreSQL. Start the demo database:\n"
            "  docker compose up -d\n"
            "  python -m sql_optimizer.train\n"
            "Or set DATABASE_URL to an existing server."
        )

    if not args.skip_bootstrap and not schema_is_ready(db):
        print("Bootstrapping demo schema (JOB-light compatible, synthetic rows)...")
        counts = bootstrap_demo_db(db, n_titles=int(cfg.get("n_titles", 4000)), seed=seed)
        print("Loaded tables:", counts)

    wl = cfg.get("workload", {})
    queries = load_workload(
        wl.get("files") or ["job_light.sql", "synthetic.sql"],
        min_relations=int(wl.get("min_relations", 2)),
        max_relations=int(wl.get("max_relations", 4)),
        max_queries=int(wl.get("max_queries", 60)),
    )
    if len(queries) < 6:
        raise SystemExit(f"Need more parseable join queries, found {len(queries)}")

    # ── Split: random, not by cost ────────────────────────────────────
    train_q, val_q, test_q = split_queries(
        queries,
        seed=seed,
        train_frac=float(cfg.get("train_frac", 0.70)),
        val_frac=float(cfg.get("val_frac", 0.15)),
    )
    out_dir = ensure_dir(ROOT / cfg.get("output_dir", "results"))

    # ── Save reproducibility metadata ─────────────────────────────────
    pg_settings = db.settings()
    dump_json(
        out_dir / "run_metadata.json",
        {
            "seed": seed,
            "postgres": pg_settings,
            "schema": db.schema_info(),
            "dataset_files": wl.get("files"),
            "dataset_version": cfg.get("dataset_version", "unknown"),
            "n_queries_loaded": len(queries),
            "split": {"train": len(train_q), "val": len(val_q), "test": len(test_q)},
            "config": cfg,
            "architecture": {
                "state_dim": "52 features from sqlglot parse + EXPLAIN ANALYZE metrics",
                "action_space": "MultiDiscrete([8, 4, 4, 7]) = join_order × join_method × scan_method × index",
                "reward": "α*time_improvement + β*buffer_improvement - γ*planning_overhead",
                "algorithms": ["PPO (MultiDiscrete)", "DQN (flattened Discrete)"],
            },
        },
    )
    print(
        f"Split (normalized-SQL, random, seed={seed}): "
        f"train={len(train_q)} val={len(val_q)} test={len(test_q)}"
    )

    algos = ["ppo", "dqn"] if args.algo == "both" else [args.algo]
    for algo in algos:
        print(f"\n{'=' * 60}")
        print(f"  Training {algo.upper()}")
        print(f"{'=' * 60}")
        _train_one(algo, db, train_q, val_q, test_q, cfg, out_dir, seed)
    db.close()
    print(f"\nDone. Reports are under {out_dir}")


def _train_one(algo, db, train_q, val_q, test_q, cfg, out_dir: Path, seed: int) -> None:
    flat = algo == "dqn"
    train_env = SQLOptimizerEnv(
        train_q, db,
        discrete_flat=flat,
        warmup=bool(cfg.get("warmup", True)),
    )
    val_env = SQLOptimizerEnv(
        val_q or test_q, db,
        discrete_flat=flat,
        warmup=True,
    )
    test_env = SQLOptimizerEnv(
        test_q, db,
        discrete_flat=flat,
        warmup=True,
    )

    if algo == "ppo":
        model = ppo_agent.make_ppo(
            train_env,
            seed=seed,
            learning_rate=float(cfg.get("ppo", {}).get("learning_rate", 3e-4)),
            n_steps=int(cfg.get("ppo", {}).get("n_steps", 32)),
            batch_size=int(cfg.get("ppo", {}).get("batch_size", 16)),
        )
        steps = int(cfg.get("ppo", {}).get("timesteps", 256))
        print(f"  Training PPO for {steps} timesteps...")
        model.learn(total_timesteps=steps)
        ppo_agent.save_model(model, out_dir / "ppo_optimizer")
    else:
        model = dqn_agent.make_dqn(
            train_env,
            seed=seed,
            learning_rate=float(cfg.get("dqn", {}).get("learning_rate", 1e-4)),
            buffer_size=int(cfg.get("dqn", {}).get("buffer_size", 5000)),
            batch_size=int(cfg.get("dqn", {}).get("batch_size", 16)),
        )
        steps = int(cfg.get("dqn", {}).get("timesteps", 256))
        print(f"  Training DQN for {steps} timesteps...")
        model.learn(total_timesteps=steps)
        dqn_agent.save_model(model, out_dir / "dqn_optimizer")

    # ── Evaluate ──────────────────────────────────────────────────────
    print(f"  Evaluating {algo.upper()} on val ({len(val_q or test_q)} queries)...")
    val_result = evaluate_policy(model, val_env, val_q or test_q)
    print(f"  Evaluating {algo.upper()} on test ({len(test_q)} queries)...")
    test_result = evaluate_policy(model, test_env, test_q)

    write_report(val_result, out_dir / f"{algo}_val")
    md = write_report(test_result, out_dir / f"{algo}_test")

    agg = test_result["aggregates"]
    print(f"\n  {algo.upper()} Test Results:")
    print(f"    Queries: {agg.get('n_queries')}")
    print(f"    Improved: {agg.get('pct_improved')}%")
    print(f"    Unchanged: {agg.get('pct_unchanged')}%")
    print(f"    Degraded: {agg.get('pct_degraded')}%")
    print(f"    Failed: {agg.get('pct_failed')}%")
    print(f"    Mean time improvement: {agg.get('mean_time_improvement')}")
    print(f"    Mean planning overhead: {agg.get('mean_planning_overhead_ms')} ms")
    print(f"  Report: {md}")

    train_env.close()
    val_env.close()
    test_env.close()


if __name__ == "__main__":
    main()
