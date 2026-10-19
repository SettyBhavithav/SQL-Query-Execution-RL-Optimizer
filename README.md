# SQL Query Execution RL Optimizer

Closed-loop reinforcement learning for **PostgreSQL query optimization**. The agent
selects a real join-order rewrite, join-method planner setting, scan-method planner
setting, and/or index, then receives a reward from `EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)`.

**Every optimization is verified against PostgreSQL.** If the EXPLAIN plan does not
actually change, the outcome is reported as "plan unchanged"—never as an optimization.

## Architecture

```text
SQL query
  → parse (sqlglot: tables, joins, predicates, aggregations)
  → generate candidate join orders (left-deep + bushy trees)
  → identify candidate indexes (join/filter/GROUP/ORDER columns)
  → RL agent selects action (join order × join method × scan method × index)
  → rewrite SQL / SET join GUCs / SET scan GUCs / CREATE INDEX
  → EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) — real PostgreSQL execution
  → extract: execution time, planning time, cost, buffers, operators
  → compare plan signature (before vs after)
  → compute reward from measured performance
  → roll back temporary index
  → return reward to agent
```

This is **not** a simulated model. The notebook (`Development_notebook.ipynb`)
still contains the old `predicted_cost = true_cost * (1 - cost_reduction)` gym,
which is **obsolete and must not be cited as a result**.

## Project layout

```text
sql_optimizer/
  __init__.py          Package version and docstring
  database.py          PostgreSQL connection, GUCs (join + scan), index lifecycle, EXPLAIN
  parser.py            sqlglot query structure (tables, predicates, joins, GROUP/ORDER)
  plan_parser.py       EXPLAIN JSON → PlanMetrics (time, cost, buffers, operators, signature)
  query_generator.py   Connected join trees (left-deep + bushy) + equivalent JOIN ... ON SQL
  optimizer.py         Apply a discrete action to SQL/plan/index
  environment.py       Gymnasium env (MultiDiscrete, measured reward only)
  state.py             52-dim padded plan/query feature vector from real PostgreSQL data
  actions.py           4D MultiDiscrete / flattened Discrete encoding
  reward.py            Reward = α·time + β·I/O − γ·planning (all from PostgreSQL)
  workload.py          Load SQL files; random deduped split (not by cost)
  demo_schema.py       JOB-light compatible synthetic IMDB-style tables
  evaluation.py        Per-query table + plan comparisons + aggregates (all outcomes)
  train.py             PPO + DQN training against live PostgreSQL
  eval_cli.py          Evaluate a saved policy
  agents/
    __init__.py        Algorithm selection rationale
    ppo_agent.py       PPO for MultiDiscrete actions
    dqn_agent.py       DQN for flattened Discrete actions
  utils.py             Seeds, YAML, JSON, reproducibility
configs/
  train.yaml           Training hyperparameters
  eval.yaml            Evaluation split (same seed)
docker-compose.yml     Postgres 16 on localhost:55432
requirements.txt       Python dependencies
tests/
  test_offline.py      Offline tests (no PostgreSQL required)
Development_notebook.ipynb   Historical simulation (DO NOT USE)
```

## Setup

```bash
python -m pip install -r requirements.txt
docker compose up -d
python -m sql_optimizer.train
```

Connection defaults to `postgresql://sqlopt:sqlopt@127.0.0.1:55432/sqlopt`
or `DATABASE_URL`. If tables are empty, training bootstraps a **synthetic**
JOB-light schema (thousands of rows). Point `DATABASE_URL` at a real IMDB/JOB
database to run the same code on full-scale data.

## Action space (discrete)

The agent chooses a 4-dimensional discrete action:

| Head | Values | Effect |
| ---- | ------ | ------ |
| Join order | 0 = original SQL, 1..k = equivalent `JOIN` trees | `join_collapse_limit=1` so written order is respected |
| Join method | `default`, `hash`, `merge`, `nestloop` | `enable_hashjoin` / `enable_mergejoin` / `enable_nestloop` |
| Scan method | `default`, `seqscan`, `indexscan`, `bitmapscan` | `enable_seqscan` / `enable_indexscan` / `enable_bitmapscan` |
| Index | 0 = none, 1..k = candidate column | create if missing, then `DROP INDEX` after the step |

PostgreSQL cannot *force* a physical operator. GUCs only disable alternatives.
If `EXPLAIN` shows the same operator tree as the baseline, the outcome is
**plan unchanged** — not an optimization.

**The agent never outputs a cost-reduction percentage.** There is no
`cost_reduction` action. All actions are concrete PostgreSQL interventions.

## State space (52 dimensions)

| Range | Features | Source |
| ----- | -------- | ------ |
| 0-7 | Query structure: tables, joins, predicates, GROUP/ORDER, aggregations | sqlglot parse |
| 8-11 | Join graph: subquery flag, SQL length, density, join types | sqlglot |
| 12-15 | Candidate counts: join orders, index candidates, existing indexes | PostgreSQL pg_indexes |
| 16-25 | Measured metrics: cost, time, rows, buffers, cache ratio | EXPLAIN ANALYZE |
| 26-36 | Operator fractions: join types, scan types | EXPLAIN JSON plan tree |
| 37-38 | Complexity features | sqlglot |
| 39-44 | Existing index flags | PostgreSQL pg_indexes |
| 45-51 | Additional metrics: temp blocks, memory, node count, cardinality error | EXPLAIN ANALYZE |

## Join-order optimization

For queries with multiple relations (e.g., `A JOIN B JOIN C JOIN D`):

1. Build a join graph from equality predicates.
2. Enumerate valid join orderings (left-deep + bushy trees).
3. Only connected orderings are generated (ensures valid ON clauses).
4. Rewrite SQL with explicit `JOIN ... ON` clauses.
5. Set `join_collapse_limit = 1` so PostgreSQL respects the written order.
6. Run EXPLAIN ANALYZE to measure actual performance.

Examples:
- `((A JOIN B) JOIN C) JOIN D` (left-deep)
- `(A JOIN (B JOIN C)) JOIN D` (right-deep)
- `(A JOIN B) JOIN (C JOIN D)` (bushy)

All rewrites are semantically equivalent to the original query.

## Index optimization

For columns appearing in JOIN, WHERE, ORDER BY, or GROUP BY:

1. Identify candidate columns from sqlglot parse.
2. Check `pg_indexes` to see if index already exists.
3. If the agent selects a new index:
   - `CREATE INDEX rl_tmp_<hash> ON table (column)`
   - `ANALYZE table`
   - Run EXPLAIN ANALYZE with the index
   - `DROP INDEX rl_tmp_<hash>` (cleanup)
4. If the index already exists, it is used as-is.
5. Maximum 6 candidate indexes per query to prevent explosion.

Indexes are ALWAYS rolled back after each step. The database is never
permanently polluted by RL experiments.

## Reward

```text
reward = α * (t_base - t_obs) / t_base          # execution time improvement
       + β * (reads_base - reads_obs) / reads_base  # I/O improvement
       - γ * extra_planning / (t_base + planning_base)  # planning overhead
       - δ if an index was created                       # DDL cost
```

**All terms come from PostgreSQL measurements.** Weights: α=1.0, β=0.25, γ=0.05, δ=0.02.

An outcome is `improved` only if execution time dropped by more than a noise
floor **and** the plan signature changed.

## RL algorithms

### PPO (Proximal Policy Optimization)
- **Why**: Supports MultiDiscrete actions natively, clipped objective prevents
  destructive updates from noisy PostgreSQL timing.
- **Space**: MultiDiscrete([8, 4, 4, 7]) = 4D action.

### DQN (Deep Q-Network)
- **Why**: Off-policy replay buffer efficiently reuses past EXPLAIN ANALYZE
  results, ε-greedy exploration discovers diverse strategies.
- **Space**: Discrete(896) = flattened 8×4×4×7.

### Why NOT SAC / DDPG?
SAC and DDPG require continuous action spaces. The historical `cost_reduction`
continuous action has been **completely removed**. All optimization actions are
now discrete PostgreSQL interventions.

## Split

Queries are normalized with sqlglot, duplicates collapsed, then shuffled with
seed 42 into 70% / 15% / 15%. They are **not** sorted by cost.

## Evaluation

Every query produces a result row:

| Query | Baseline Time | RL Time | Time Improvement | Baseline Cost | RL Cost | Buffer Improvement | Outcome |
| ----- | ------------- | ------- | ---------------- | ------------- | ------- | ------------------ | ------- |

Plus execution plan comparisons (before/after) for every query.

Aggregate metrics include:
- Mean/median execution time (baseline and RL)
- Mean/median improvement
- Percentage improved / unchanged / degraded / failed
- Mean planning overhead

**ALL queries are reported**, including failures and regressions.

## Reproduce

- Seed: `42` (`configs/train.yaml`)
- Dataset version: `job_light+synthetic@local-demo-schema-v2`
- Each run writes `results/run_metadata.json` (Postgres GUCs, table sizes, split)
- Models: `results/ppo_optimizer.zip`, `results/dqn_optimizer.zip`
- Reports: `results/ppo_test.md`, `results/dqn_test.md`

```bash
python -m sql_optimizer.train
python -m sql_optimizer.eval_cli --algo ppo
python -m sql_optimizer.eval_cli --algo dqn
python -m pytest tests/test_offline.py -q
```

## Limitations

1. **Synthetic data**: Demo data is synthetic unless you attach a real IMDB dump.
2. **Advisory join control**: Join-method control uses GUC disable, not optimizer
   hints like `pg_hint_plan`. PostgreSQL may ignore the preference.
3. **Single-column indexes**: Index actions are single-column and rolled back
   after each step. The agent cannot accumulate indexes across queries.
4. **Missing JOB tables**: JOB queries requiring aka_name, etc. are skipped on
   the demo schema.
5. **Short training budgets**: Default `timesteps` in `train.yaml` are for a
   reproducible CPU run. Increase for a serious study.
6. **Measurement noise**: PostgreSQL timing has inherent variance. Warmup runs
   help, but short-running queries may show noise-dominated results.
7. **Single-step episodes**: Each episode is one query optimization. Multi-step
   optimization (e.g., trying multiple strategies sequentially) is not implemented.
