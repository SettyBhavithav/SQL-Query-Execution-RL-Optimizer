"""Closed-loop RL-assisted PostgreSQL query optimizer.

This package replaces the historical simulated cost-reduction model with a
genuine reinforcement-learning pipeline that:

  1. Parses SQL with sqlglot (not regex heuristics).
  2. Generates candidate join orders, join-method GUC settings, and indexes.
  3. Runs EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) in PostgreSQL.
  4. Extracts real execution time, planning time, cost, buffers, operators.
  5. Computes reward exclusively from measured database metrics.
  6. Rolls back temporary indexes after every step.

No agent output ever scales an original cost by an artificial percentage.
"""

__version__ = "2.0.0"
