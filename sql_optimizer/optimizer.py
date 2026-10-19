"""Apply an RL action as a real SQL rewrite, GUC change, and/or index.

This module translates a discrete RL action into concrete PostgreSQL
interventions: join-order rewrite, join-method GUC, scan-method GUC,
and/or index creation.  The result is then executed with EXPLAIN ANALYZE
to obtain real measurements.

CRITICAL: No code path computes ``predicted_cost = true_cost * (1 - reduction)``
or any equivalent.  All costs come from PostgreSQL execution.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from sql_optimizer.actions import MAX_INDEX_CANDIDATES, MAX_JOIN_ORDERS, OptimizationAction
from sql_optimizer.database import IndexSpec, JOIN_METHOD_GUCS, SCAN_METHOD_GUCS, PostgresDB
from sql_optimizer.parser import QueryStructure, index_candidate_columns
from sql_optimizer.plan_parser import PlanMetrics
from sql_optimizer.query_generator import (
    JoinTree,
    describe_tree,
    generate_join_trees,
    rewrite_join_order,
)


@dataclass
class CandidateSet:
    """Pre-computed set of valid optimization candidates for a query.

    Generated once per query during ``reset()``, ensuring all candidates
    are semantically equivalent to the original query.
    """

    join_trees: list[JoinTree]
    join_sql: list[str]
    indexes: list[IndexSpec]


@dataclass
class AppliedOptimization:
    """Record of what was actually applied to PostgreSQL.

    Used to verify the optimization and roll it back afterwards.
    """

    sql: str
    original_sql: str
    gucs: dict[str, str]
    respect_join_order: bool
    created_index_name: str
    index_spec: IndexSpec | None
    join_description: str
    join_method: str
    scan_method: str
    description: str
    used_existing_index: bool = False


def build_candidates(
    db: PostgresDB,
    structure: QueryStructure,
    *,
    max_orders: int = MAX_JOIN_ORDERS,
    max_indexes: int = MAX_INDEX_CANDIDATES,
) -> CandidateSet:
    """Generate valid candidate optimizations for the query.

    Join orders: enumerate connected, semantically equivalent join trees.
    Indexes: identify candidate columns from joins, filters, GROUP/ORDER BY
    and check whether each already exists in the database.
    """
    trees = generate_join_trees(structure, max_orders=max(0, max_orders - 1))
    # Slot 0 is always the unmodified original SQL (no rewrite).
    join_sql = [structure.original_sql]
    join_trees: list[JoinTree] = []
    if structure.n_relations >= 1 and trees:
        join_trees.append(trees[0])
    for tree in trees:
        sql = rewrite_join_order(structure, tree)
        if sql.strip().rstrip(";") == structure.original_sql.strip().rstrip(";"):
            continue
        if sql in join_sql:
            continue
        join_sql.append(sql)
        join_trees.append(tree)
        if len(join_sql) >= max_orders:
            break
    while len(join_sql) < max_orders:
        join_sql.append(structure.original_sql)

    # ── Index candidates ──────────────────────────────────────────────
    specs: list[IndexSpec] = []
    seen: set[str] = set()
    for _alias, table, column in index_candidate_columns(structure):
        spec = IndexSpec(table=table, columns=(column,))
        if spec.signature() in seen:
            continue
        seen.add(spec.signature())
        spec.exists = db.index_exists(table, spec.columns)
        if spec.exists:
            spec.name = "existing"
        specs.append(spec)
        if len(specs) >= max_indexes:
            break
    return CandidateSet(join_trees=join_trees, join_sql=join_sql, indexes=specs)


def apply_action(
    db: PostgresDB,
    structure: QueryStructure,
    candidates: CandidateSet,
    action: OptimizationAction,
) -> AppliedOptimization:
    """Translate an RL action into a concrete PostgreSQL optimization.

    Returns an ``AppliedOptimization`` describing exactly what was done,
    for use by ``execute_applied`` and ``rollback_applied``.
    """
    # ── Join order ────────────────────────────────────────────────────
    order_idx = int(action.join_order_idx) % len(candidates.join_sql)
    sql = candidates.join_sql[order_idx]
    respect = order_idx != 0 and sql != structure.original_sql
    if respect:
        desc_tree = (
            describe_tree(candidates.join_trees[order_idx - 1])
            if order_idx - 1 < len(candidates.join_trees)
            else f"order[{order_idx}]"
        )
        join_desc = desc_tree
    else:
        join_desc = "original"

    # ── Index ─────────────────────────────────────────────────────────
    created = ""
    spec: IndexSpec | None = None
    used_existing = False
    if action.index_idx > 0 and candidates.indexes:
        spec = candidates.indexes[(action.index_idx - 1) % len(candidates.indexes)]
        if spec.exists:
            used_existing = True
        else:
            created = db.create_index(spec.table, spec.columns)
            if created:
                spec = IndexSpec(spec.table, spec.columns, exists=True, name=created)

    # ── GUCs (join method + scan method) ──────────────────────────────
    gucs = dict(JOIN_METHOD_GUCS.get(action.join_method, JOIN_METHOD_GUCS["default"]))
    gucs.update(SCAN_METHOD_GUCS.get(action.scan_method, SCAN_METHOD_GUCS["default"]))

    # ── Build description ─────────────────────────────────────────────
    parts = [
        f"join_order={join_desc}",
        f"join_method={action.join_method}",
        f"scan_method={action.scan_method}",
    ]
    if spec is None or action.index_idx == 0:
        parts.append("index=none")
    elif used_existing:
        parts.append(f"index=existing:{spec.signature()}")
    elif created:
        parts.append(f"index=created:{spec.signature()}")
    else:
        parts.append(f"index=skipped:{spec.signature()}")

    return AppliedOptimization(
        sql=sql,
        original_sql=structure.original_sql,
        gucs=gucs,
        respect_join_order=respect,
        created_index_name=created,
        index_spec=spec if action.index_idx > 0 else None,
        join_description=join_desc,
        join_method=action.join_method,
        scan_method=action.scan_method,
        description="; ".join(parts),
        used_existing_index=used_existing,
    )


def execute_applied(db: PostgresDB, applied: AppliedOptimization) -> PlanMetrics:
    """Execute the applied optimization in PostgreSQL and return real metrics.

    This is where the closed loop closes: the action is turned into a real
    PostgreSQL execution and real EXPLAIN ANALYZE results are returned.
    """
    return db.explain_analyze(
        applied.sql,
        gucs=applied.gucs,
        respect_join_order=applied.respect_join_order,
    )


def rollback_applied(db: PostgresDB, applied: AppliedOptimization) -> None:
    """Roll back any temporary index created for this optimization.

    Ensures the database is not permanently polluted by RL experiments.
    """
    if applied.created_index_name:
        db.drop_index(applied.created_index_name)
