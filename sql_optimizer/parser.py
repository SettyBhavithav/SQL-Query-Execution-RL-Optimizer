"""SQL parsing with sqlglot (structure, not regex heuristics)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import sqlglot
from sqlglot import exp


@dataclass
class ColumnRef:
    table: str
    column: str

    def key(self) -> tuple[str, str]:
        return (self.table.lower(), self.column.lower())

    def sql(self) -> str:
        return f"{self.table}.{self.column}"


@dataclass
class Predicate:
    sql: str
    tables: set[str]
    columns: list[ColumnRef]
    is_equality_join: bool = False
    left: ColumnRef | None = None
    right: ColumnRef | None = None


@dataclass
class QueryStructure:
    original_sql: str
    dialect: str
    tables: dict[str, str]  # alias -> table name
    predicates: list[Predicate]
    join_predicates: list[Predicate]
    filter_predicates: list[Predicate]
    group_by: list[str]
    order_by: list[str]
    aggregations: list[str]
    join_types: list[str]
    has_subquery: bool
    select_sql: str
    parse_ok: bool = True
    parse_error: str = ""
    extra: dict[str, Any] = field(default_factory=dict)

    @property
    def n_relations(self) -> int:
        return len(self.tables)

    @property
    def n_joins(self) -> int:
        return max(0, self.n_relations - 1) if self.n_relations else 0

    @property
    def n_predicates(self) -> int:
        return len(self.predicates)


def parse_sql(sql: str, dialect: str = "postgres") -> QueryStructure:
    original = sql.strip().rstrip(";")
    try:
        ast = sqlglot.parse_one(original, dialect=dialect)
    except Exception as exc:  # noqa: BLE001 - parser must not crash the env
        return QueryStructure(
            original_sql=original,
            dialect=dialect,
            tables={},
            predicates=[],
            join_predicates=[],
            filter_predicates=[],
            group_by=[],
            order_by=[],
            aggregations=[],
            join_types=[],
            has_subquery=False,
            select_sql=original,
            parse_ok=False,
            parse_error=str(exc),
        )

    select = ast if isinstance(ast, exp.Select) else ast.find(exp.Select)
    if select is None:
        return QueryStructure(
            original_sql=original,
            dialect=dialect,
            tables={},
            predicates=[],
            join_predicates=[],
            filter_predicates=[],
            group_by=[],
            order_by=[],
            aggregations=[],
            join_types=[],
            has_subquery=bool(ast.find(exp.Subquery)),
            select_sql=original,
            parse_ok=False,
            parse_error="Not a SELECT statement",
        )

    tables = _top_level_tables(select)
    predicates = _collect_predicates(select, tables)
    join_preds = [p for p in predicates if p.is_equality_join]
    filter_preds = [p for p in predicates if not p.is_equality_join]
    group_by = [e.sql(dialect=dialect) for e in (select.args.get("group") or [])]
    if select.args.get("group") and hasattr(select.args.get("group"), "expressions"):
        group_by = [e.sql(dialect=dialect) for e in select.args["group"].expressions]
    order = select.args.get("order")
    order_by = []
    if order is not None:
        order_by = [e.sql(dialect=dialect) for e in order.expressions]
    aggregations = [
        f.alias_or_name
        for f in select.find_all(exp.AggFunc)
        if _is_top_level(f, select)
    ]
    join_types = _join_types(select)
    has_subquery = any(True for _ in select.find_all(exp.Subquery))
    return QueryStructure(
        original_sql=original,
        dialect=dialect,
        tables=tables,
        predicates=predicates,
        join_predicates=join_preds,
        filter_predicates=filter_preds,
        group_by=group_by,
        order_by=order_by,
        aggregations=aggregations,
        join_types=join_types,
        has_subquery=has_subquery,
        select_sql=select.sql(dialect=dialect),
        parse_ok=True,
    )


def normalize_sql(sql: str, dialect: str = "postgres") -> str:
    text = " ".join(sql.strip().rstrip(";").split())
    try:
        return sqlglot.parse_one(text, dialect=dialect).sql(dialect=dialect)
    except Exception:
        return text.lower()


def _top_level_tables(select: exp.Select) -> dict[str, str]:
    tables: dict[str, str] = {}
    from_ = select.args.get("from_") or select.args.get("from")
    if from_ is None:
        return tables
    for table in from_.find_all(exp.Table):
        if _inside_subquery(table, select):
            continue
        alias = table.alias_or_name
        name = table.name
        tables[alias] = name
    for join in select.args.get("joins") or []:
        for table in join.find_all(exp.Table):
            if _inside_subquery(table, select):
                continue
            tables[table.alias_or_name] = table.name
    return tables


def _inside_subquery(node: exp.Expression, root: exp.Select) -> bool:
    parent = node.parent
    while parent is not None and parent is not root:
        if isinstance(parent, (exp.Subquery, exp.CTE)):
            return True
        parent = parent.parent
    return False


def _is_top_level(node: exp.Expression, root: exp.Select) -> bool:
    return not _inside_subquery(node, root)


def _join_types(select: exp.Select) -> list[str]:
    types: list[str] = []
    for join in select.args.get("joins") or []:
        kind = join.args.get("kind") or join.args.get("side") or "JOIN"
        types.append(str(kind).upper())
    return types


def _collect_predicates(select: exp.Select, tables: dict[str, str]) -> list[Predicate]:
    found: list[Predicate] = []
    seen: set[str] = set()

    def add_expr(node: exp.Expression | None) -> None:
        if node is None:
            return
        for part in _split_and(node):
            pred = _predicate_from_expr(part, tables)
            if pred.sql in seen:
                continue
            seen.add(pred.sql)
            found.append(pred)

    add_expr(select.args.get("where"))
    for join in select.args.get("joins") or []:
        add_expr(join.args.get("on"))
    return found


def _split_and(node: exp.Expression) -> list[exp.Expression]:
    if isinstance(node, exp.And):
        return _split_and(node.left) + _split_and(node.right)
    if isinstance(node, exp.Paren):
        return _split_and(node.this)
    if isinstance(node, exp.Where):
        return _split_and(node.this)
    return [node]


def _predicate_from_expr(node: exp.Expression, tables: dict[str, str]) -> Predicate:
    sql = node.sql(dialect="postgres")
    cols = _columns(node, tables)
    table_set = {c.table for c in cols}
    left_col = right_col = None
    is_eq_join = False
    if isinstance(node, exp.EQ):
        lcols = _columns(node.left, tables)
        rcols = _columns(node.right, tables)
        if len(lcols) == 1 and len(rcols) == 1 and lcols[0].table != rcols[0].table:
            is_eq_join = True
            left_col, right_col = lcols[0], rcols[0]
    return Predicate(
        sql=sql,
        tables=table_set,
        columns=cols,
        is_equality_join=is_eq_join,
        left=left_col,
        right=right_col,
    )


def _columns(node: exp.Expression, tables: dict[str, str]) -> list[ColumnRef]:
    refs: list[ColumnRef] = []
    for col in node.find_all(exp.Column):
        table = col.table
        if not table:
            if len(tables) == 1:
                table = next(iter(tables))
            else:
                continue
        refs.append(ColumnRef(table=table, column=col.name))
    return refs


def index_candidate_columns(structure: QueryStructure) -> list[tuple[str, str, str]]:
    """Return (alias, table, column) candidates from joins, filters, GROUP/ORDER."""
    seen: set[tuple[str, str, str]] = set()
    out: list[tuple[str, str, str]] = []

    def add(alias: str, column: str) -> None:
        table = structure.tables.get(alias, alias)
        key = (alias.lower(), table.lower(), column.lower())
        if key in seen:
            return
        seen.add(key)
        out.append((alias, table, column))

    for pred in structure.predicates:
        for col in pred.columns:
            add(col.table, col.column)
    for item in structure.group_by + structure.order_by:
        try:
            expr = sqlglot.parse_one(item, dialect=structure.dialect)
        except Exception:
            continue
        for col in expr.find_all(exp.Column):
            if col.table:
                add(col.table, col.name)
    return out
