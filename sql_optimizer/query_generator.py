"""Generate semantically equivalent join-order rewrites."""

from __future__ import annotations

from dataclasses import dataclass, field
from itertools import permutations

from sql_optimizer.parser import QueryStructure, parse_sql


@dataclass
class JoinTree:
    """Leaf = alias string; internal = (left, right) nested tuples."""

    value: str | tuple
    aliases: frozenset[str] = field(default_factory=frozenset)

    @staticmethod
    def leaf(alias: str) -> "JoinTree":
        return JoinTree(alias, frozenset([alias]))

    @staticmethod
    def join(left: "JoinTree", right: "JoinTree") -> "JoinTree":
        return JoinTree((left, right), left.aliases | right.aliases)


class EqualityClasses:
    """Union-find over (alias, column) so transitive join keys can be recovered."""

    def __init__(self) -> None:
        self.parent: dict[tuple[str, str], tuple[str, str]] = {}

    def add(self, col: tuple[str, str]) -> None:
        self.parent.setdefault(col, col)

    def find(self, col: tuple[str, str]) -> tuple[str, str]:
        self.add(col)
        while self.parent[col] != col:
            self.parent[col] = self.parent[self.parent[col]]
            col = self.parent[col]
        return col

    def union(self, a: tuple[str, str], b: tuple[str, str]) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[rb] = ra

    def members(self, col: tuple[str, str]) -> list[tuple[str, str]]:
        root = self.find(col)
        return [c for c in self.parent if self.find(c) == root]


def build_join_graph(structure: QueryStructure) -> tuple[dict[str, set[str]], EqualityClasses]:
    graph: dict[str, set[str]] = {alias: set() for alias in structure.tables}
    eq = EqualityClasses()
    for pred in structure.join_predicates:
        if pred.left is None or pred.right is None:
            continue
        a, b = pred.left.table, pred.right.table
        if a not in graph or b not in graph:
            continue
        graph[a].add(b)
        graph[b].add(a)
        eq.union(pred.left.key(), pred.right.key())
    _close_transitive(graph)
    return graph, eq


def _close_transitive(graph: dict[str, set[str]]) -> None:
    """Treat equality-join connectivity as undirected reachability for legal orders."""
    aliases = list(graph)
    reachable = {a: set(graph[a]) | {a} for a in aliases}
    changed = True
    while changed:
        changed = False
        for a in aliases:
            extra: set[str] = set()
            for b in list(reachable[a]):
                extra |= reachable[b]
            if extra - reachable[a]:
                reachable[a] |= extra
                changed = True
    # Keep original adjacency for "direct" edges; add nothing here.
    # Connectivity checks use BFS on the original (possibly incomplete) graph
    # plus transitive column equalities via ON generation, not extra edges.


def connected(graph: dict[str, set[str]], group: set[str]) -> bool:
    if not group:
        return True
    start = next(iter(group))
    seen = {start}
    stack = [start]
    while stack:
        node = stack.pop()
        for nxt in graph.get(node, ()):
            if nxt in group and nxt not in seen:
                seen.add(nxt)
                stack.append(nxt)
    return seen == group


def generate_join_trees(structure: QueryStructure, max_orders: int = 16) -> list[JoinTree]:
    aliases = list(structure.tables.keys())
    if len(aliases) <= 1:
        return [JoinTree.leaf(aliases[0])] if aliases else []

    graph, _ = build_join_graph(structure)
    trees: list[JoinTree] = []
    seen: set[str] = set()

    def record(tree: JoinTree) -> None:
        key = _tree_key(tree)
        if key in seen:
            return
        seen.add(key)
        trees.append(tree)

    _left_deep(aliases, graph, trees, record, max_orders)
    if len(trees) < max_orders and len(aliases) >= 4:
        _bushy(aliases, graph, record, max_orders)
    if not trees:
        record(_from_sequence(aliases))
    return trees[:max_orders]


def _left_deep(
    aliases: list[str],
    graph: dict[str, set[str]],
    trees: list[JoinTree],
    record,
    max_orders: int,
) -> None:
    n = len(aliases)
    # Enumerate permutations but prune to connected prefixes.
    if n > 6:
        # Limit explosion: try each table as first, then greedy remaining neighbors.
        for start in aliases:
            used = [start]
            remaining = [a for a in aliases if a != start]
            while remaining and len(trees) < max_orders:
                placed = False
                for cand in list(remaining):
                    if connected(graph, set(used + [cand])):
                        used.append(cand)
                        remaining.remove(cand)
                        placed = True
                        break
                if not placed:
                    used.append(remaining.pop(0))
            if len(used) == n:
                record(_from_sequence(used))
        return

    for perm in permutations(aliases):
        if len(trees) >= max_orders:
            return
        ok = True
        for i in range(2, n + 1):
            if not connected(graph, set(perm[:i])):
                ok = False
                break
        if ok:
            record(_from_sequence(list(perm)))


def _from_sequence(seq: list[str]) -> JoinTree:
    tree = JoinTree.leaf(seq[0])
    for alias in seq[1:]:
        tree = JoinTree.join(tree, JoinTree.leaf(alias))
    return tree


def _bushy(aliases: list[str], graph: dict[str, set[str]], record, max_orders: int) -> None:
    n = len(aliases)
    if n == 4:
        a, b, c, d = aliases
        pairs = [((a, b), (c, d)), ((a, c), (b, d)), ((a, d), (b, c))]
        for (x1, x2), (y1, y2) in pairs:
            left_ok = connected(graph, {x1, x2})
            right_ok = connected(graph, {y1, y2})
            all_ok = connected(graph, {x1, x2, y1, y2})
            if left_ok and right_ok and all_ok:
                left = JoinTree.join(JoinTree.leaf(x1), JoinTree.leaf(x2))
                right = JoinTree.join(JoinTree.leaf(y1), JoinTree.leaf(y2))
                record(JoinTree.join(left, right))
    elif n >= 5:
        for i, last in enumerate(aliases):
            rest = aliases[:i] + aliases[i + 1 :]
            if connected(graph, set(rest)) and connected(graph, set(rest) | {last}):
                record(JoinTree.join(_from_sequence(rest), JoinTree.leaf(last)))


def _tree_key(tree: JoinTree) -> str:
    def rec(node: JoinTree) -> str:
        if isinstance(node.value, str):
            return node.value
        left, right = node.value
        return f"({rec(left)}⋈{rec(right)})"

    return rec(tree)


def rewrite_join_order(structure: QueryStructure, tree: JoinTree) -> str:
    """Rebuild SELECT with explicit JOIN ... ON while keeping filters and meaning."""
    if not structure.parse_ok or structure.n_relations <= 1:
        return structure.original_sql

    graph, eq = build_join_graph(structure)
    used_join_sql: set[str] = set()
    from_sql = _tree_to_from(tree, structure, graph, eq, used_join_sql)
    remaining = []
    for pred in structure.predicates:
        if pred.is_equality_join and pred.sql in used_join_sql:
            continue
        remaining.append(pred.sql)
    where = f" WHERE {' AND '.join(remaining)}" if remaining else ""

    parsed = parse_sql(structure.original_sql)
    select_list = _select_list_sql(structure.original_sql)
    tail = _tail_clauses(structure.original_sql)
    return f"SELECT {select_list} FROM {from_sql}{where}{tail}"


def _select_list_sql(sql: str) -> str:
    ast = sqlglot_select(sql)
    if ast is None:
        return "*"
    return ", ".join(e.sql(dialect="postgres") for e in ast.expressions)


def _tail_clauses(sql: str) -> str:
    ast = sqlglot_select(sql)
    if ast is None:
        return ""
    parts: list[str] = []
    for key, keyword in (
        ("group", "GROUP BY"),
        ("having", "HAVING"),
        ("order", "ORDER BY"),
        ("limit", "LIMIT"),
        ("offset", "OFFSET"),
    ):
        node = ast.args.get(key)
        if node is None:
            continue
        if key == "group":
            exprs = node.expressions if hasattr(node, "expressions") else []
            if exprs:
                parts.append("GROUP BY " + ", ".join(e.sql(dialect="postgres") for e in exprs))
        elif key == "having":
            parts.append("HAVING " + node.sql(dialect="postgres").removeprefix("HAVING").strip())
        elif key == "order":
            parts.append(node.sql(dialect="postgres"))
        elif key == "limit":
            parts.append(node.sql(dialect="postgres"))
        elif key == "offset":
            parts.append(node.sql(dialect="postgres"))
    return (" " + " ".join(parts)) if parts else ""


def sqlglot_select(sql: str):
    import sqlglot
    from sqlglot import exp

    try:
        ast = sqlglot.parse_one(sql, dialect="postgres")
    except Exception:
        return None
    return ast if isinstance(ast, exp.Select) else ast.find(exp.Select)


def _tree_to_from(
    tree: JoinTree,
    structure: QueryStructure,
    graph: dict[str, set[str]],
    eq: EqualityClasses,
    used_join_sql: set[str],
) -> str:
    def table_sql(alias: str) -> str:
        name = structure.tables[alias]
        if alias.lower() == name.lower():
            return name
        return f"{name} AS {alias}"

    def rec(node: JoinTree) -> str:
        if isinstance(node.value, str):
            return table_sql(node.value)
        left, right = node.value
        lsql = rec(left)
        rsql = rec(right)
        on_sql, consumed = _on_clause(left.aliases, right.aliases, structure, eq)
        used_join_sql.update(consumed)
        return f"({lsql} JOIN {rsql} ON {on_sql})"

    return rec(tree)


def _on_clause(
    left_aliases: frozenset[str],
    right_aliases: frozenset[str],
    structure: QueryStructure,
    eq: EqualityClasses,
) -> tuple[str, list[str]]:
    consumed: list[str] = []
    parts: list[str] = []
    for pred in structure.join_predicates:
        if pred.left is None or pred.right is None:
            continue
        a, b = pred.left.table, pred.right.table
        if (a in left_aliases and b in right_aliases) or (b in left_aliases and a in right_aliases):
            parts.append(pred.sql)
            consumed.append(pred.sql)
    if parts:
        return " AND ".join(parts), consumed

    # Transitive equality: find a left column and right column in the same class.
    left_cols = [
        col
        for pred in structure.join_predicates
        for col in (pred.left, pred.right)
        if col is not None and col.table in left_aliases
    ]
    right_cols = [
        col
        for pred in structure.join_predicates
        for col in (pred.left, pred.right)
        if col is not None and col.table in right_aliases
    ]
    for lc in left_cols:
        members = set(eq.members(lc.key()))
        for rc in right_cols:
            if rc.key() in members:
                sql = f"{lc.sql()} = {rc.sql()}"
                return sql, consumed
    # Last resort: keep equivalence via WHERE (ON TRUE). Still semantically
    # equivalent because original join predicates remain in WHERE.
    return "TRUE", consumed


def describe_tree(tree: JoinTree) -> str:
    def rec(node: JoinTree) -> str:
        if isinstance(node.value, str):
            return node.value
        left, right = node.value
        return f"({rec(left)} JOIN {rec(right)})"

    return rec(tree)
