"""PostgreSQL interface: EXPLAIN ANALYZE, GUC knobs, index lifecycle.

This module is the ONLY code that communicates with PostgreSQL.  All metrics
consumed by the RL reward originate from EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)
executed here—never from any artificial formula.
"""

from __future__ import annotations

import json
import os
import uuid
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Any, Iterator

import psycopg
from psycopg.rows import dict_row

from sql_optimizer.plan_parser import PlanMetrics, parse_explain_json

DEFAULT_DSN = os.environ.get(
    "DATABASE_URL",
    "postgresql://sqlopt:sqlopt@127.0.0.1:55432/sqlopt",
)


# ── Join-method GUCs ─────────────────────────────────────────────────────
# PostgreSQL cannot *force* a join algorithm; these GUCs only disable
# alternatives. The execution plan is always verified from EXPLAIN JSON.
JOIN_METHOD_GUCS: dict[str, dict[str, str]] = {
    "default": {
        "enable_hashjoin": "on",
        "enable_mergejoin": "on",
        "enable_nestloop": "on",
    },
    "hash": {
        "enable_hashjoin": "on",
        "enable_mergejoin": "off",
        "enable_nestloop": "off",
    },
    "merge": {
        "enable_hashjoin": "off",
        "enable_mergejoin": "on",
        "enable_nestloop": "off",
    },
    "nestloop": {
        "enable_hashjoin": "off",
        "enable_mergejoin": "off",
        "enable_nestloop": "on",
    },
}

JOIN_METHOD_NAMES = ("default", "hash", "merge", "nestloop")

# ── Scan-method GUCs ─────────────────────────────────────────────────────
# Similarly, these settings bias the planner toward specific scan types.
# The actual plan is always verified with EXPLAIN JSON.
SCAN_METHOD_GUCS: dict[str, dict[str, str]] = {
    "default": {
        "enable_seqscan": "on",
        "enable_indexscan": "on",
        "enable_indexonlyscan": "on",
        "enable_bitmapscan": "on",
    },
    "seqscan": {
        "enable_seqscan": "on",
        "enable_indexscan": "off",
        "enable_indexonlyscan": "off",
        "enable_bitmapscan": "off",
    },
    "indexscan": {
        "enable_seqscan": "off",
        "enable_indexscan": "on",
        "enable_indexonlyscan": "on",
        "enable_bitmapscan": "off",
    },
    "bitmapscan": {
        "enable_seqscan": "off",
        "enable_indexscan": "off",
        "enable_indexonlyscan": "off",
        "enable_bitmapscan": "on",
    },
}

SCAN_METHOD_NAMES = ("default", "seqscan", "indexscan", "bitmapscan")


@dataclass
class IndexSpec:
    table: str
    columns: tuple[str, ...]
    exists: bool = False
    name: str | None = None

    def signature(self) -> str:
        cols = ",".join(c.lower() for c in self.columns)
        return f"{self.table.lower()}({cols})"


class PostgresDB:
    """Manages the PostgreSQL connection used for all closed-loop RL training.

    Every ``explain_analyze`` call runs real SQL and returns real metrics.
    Temporary indexes are tracked and cleaned up automatically.
    """

    def __init__(
        self,
        dsn: str | None = None,
        statement_timeout_ms: int = 30_000,
    ) -> None:
        self.dsn = dsn or DEFAULT_DSN
        self.statement_timeout_ms = statement_timeout_ms
        self._conn: psycopg.Connection | None = None
        self._created_indexes: list[str] = []

    def connect(self) -> psycopg.Connection:
        if self._conn is None or self._conn.closed:
            self._conn = psycopg.connect(self.dsn, autocommit=True)
            with self._conn.cursor() as cur:
                cur.execute(f"SET statement_timeout = {int(self.statement_timeout_ms)}")
        return self._conn

    def close(self) -> None:
        self.drop_all_created_indexes()
        if self._conn is not None and not self._conn.closed:
            self._conn.close()
        self._conn = None

    def ping(self) -> bool:
        try:
            with self.connect().cursor() as cur:
                cur.execute("SELECT 1")
                cur.fetchone()
            return True
        except Exception:
            return False

    def settings(self) -> dict[str, str]:
        """Return current PostgreSQL configuration for reproducibility."""
        keys = (
            "version",
            "shared_buffers",
            "work_mem",
            "effective_cache_size",
            "random_page_cost",
            "seq_page_cost",
            "cpu_tuple_cost",
            "cpu_index_tuple_cost",
            "cpu_operator_cost",
            "join_collapse_limit",
            "from_collapse_limit",
            "geqo_threshold",
            "enable_hashjoin",
            "enable_mergejoin",
            "enable_nestloop",
            "enable_indexscan",
            "enable_indexonlyscan",
            "enable_bitmapscan",
            "enable_seqscan",
            "enable_sort",
            "enable_material",
        )
        out: dict[str, str] = {}
        with self.connect().cursor() as cur:
            cur.execute("SHOW server_version")
            out["server_version"] = cur.fetchone()[0]
            for key in keys[1:]:
                try:
                    cur.execute(f"SHOW {key}")
                    out[key] = cur.fetchone()[0]
                except Exception:
                    out[key] = "N/A"
        return out

    def schema_info(self) -> list[dict[str, Any]]:
        """Return table-level statistics for documentation and state encoding."""
        sql = """
        SELECT c.relname AS table_name,
               c.reltuples::bigint AS est_rows,
               pg_indexes_size(c.oid) AS index_bytes,
               pg_relation_size(c.oid) AS heap_bytes
        FROM pg_class c
        JOIN pg_namespace n ON n.oid = c.relnamespace
        WHERE n.nspname = 'public' AND c.relkind = 'r'
        ORDER BY c.relname
        """
        with self.connect().cursor(row_factory=dict_row) as cur:
            cur.execute(sql)
            return list(cur.fetchall())

    def table_row_count(self, table: str) -> int:
        """Return estimated row count from pg_class (fast, no seq scan)."""
        sql = """
        SELECT c.reltuples::bigint
        FROM pg_class c
        JOIN pg_namespace n ON n.oid = c.relnamespace
        WHERE n.nspname = 'public' AND c.relname = %s
        """
        with self.connect().cursor() as cur:
            cur.execute(sql, (table.lower(),))
            row = cur.fetchone()
            return int(row[0]) if row else 0

    def list_indexes(self, table: str | None = None) -> list[dict[str, Any]]:
        sql = """
        SELECT tablename, indexname, indexdef
        FROM pg_indexes
        WHERE schemaname = 'public'
        """
        params: tuple = ()
        if table:
            sql += " AND tablename = %s"
            params = (table.lower(),)
        with self.connect().cursor(row_factory=dict_row) as cur:
            cur.execute(sql, params)
            return list(cur.fetchall())

    def index_exists(self, table: str, columns: tuple[str, ...]) -> bool:
        cols = [c.lower() for c in columns]
        sql = """
        SELECT i.relname
        FROM pg_class t
        JOIN pg_index x ON x.indrelid = t.oid
        JOIN pg_class i ON i.oid = x.indexrelid
        JOIN pg_namespace n ON n.oid = t.relnamespace
        JOIN pg_attribute a ON a.attrelid = t.oid AND a.attnum = ANY(x.indkey)
        WHERE n.nspname = 'public' AND t.relname = %s
        GROUP BY i.relname, x.indkey
        HAVING array_agg(a.attname::text ORDER BY array_position(x.indkey, a.attnum)) = %s
        """
        with self.connect().cursor() as cur:
            cur.execute(sql, (table.lower(), cols))
            return cur.fetchone() is not None

    def create_index(self, table: str, columns: tuple[str, ...]) -> str:
        """Create a temporary index for evaluation, tracked for cleanup.

        Before creating, checks if the index already exists to avoid
        unlimited index pollution.  After EXPLAIN ANALYZE, the caller
        should call ``drop_index`` or ``drop_all_created_indexes``.
        """
        if self.index_exists(table, columns):
            return ""
        name = f"rl_tmp_{uuid.uuid4().hex[:12]}"
        cols = ", ".join(_quote_ident(c) for c in columns)
        ddl = f"CREATE INDEX {_quote_ident(name)} ON {_quote_ident(table)} ({cols})"
        with self.connect().cursor() as cur:
            cur.execute(ddl)
            cur.execute(f"ANALYZE {_quote_ident(table)}")
        self._created_indexes.append(name)
        return name

    def drop_index(self, name: str) -> None:
        if not name:
            return
        with self.connect().cursor() as cur:
            cur.execute(f"DROP INDEX IF EXISTS {_quote_ident(name)}")
        if name in self._created_indexes:
            self._created_indexes.remove(name)

    def drop_all_created_indexes(self) -> None:
        """Clean up ALL indexes created by the RL agent.

        Called automatically on ``close()`` and at end of each episode
        to prevent database pollution.
        """
        for name in list(self._created_indexes):
            self.drop_index(name)

    def explain_analyze(
        self,
        sql: str,
        gucs: dict[str, str] | None = None,
        respect_join_order: bool = False,
    ) -> PlanMetrics:
        """Run EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) and parse measurements.

        This is the core function of the closed-loop architecture:
        it executes the query in PostgreSQL and returns real measurements.

        The returned PlanMetrics contains ONLY values from the database.
        Nothing is ever computed as ``original_cost * (1 - reduction)``.

        Parameters
        ----------
        sql : str
            The SQL query to analyze.
        gucs : dict
            PostgreSQL planner GUCs to SET for this query (e.g., join/scan knobs).
        respect_join_order : bool
            If True, sets ``join_collapse_limit = 1`` and
            ``from_collapse_limit = 1`` so the written join order is followed.
        """
        gucs = dict(gucs or {})
        if respect_join_order:
            # Collapse limits of 1 make the written join order meaningful.
            gucs.setdefault("join_collapse_limit", "1")
            gucs.setdefault("from_collapse_limit", "1")
        explain_sql = "EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) " + sql.rstrip().rstrip(";")
        conn = self.connect()
        with conn.cursor() as cur:
            for key, value in gucs.items():
                cur.execute("SELECT set_config(%s, %s, true)", (key, str(value)))
            cur.execute(explain_sql)
            row = cur.fetchone()
        payload = row[0]
        if isinstance(payload, str):
            payload = json.loads(payload)
        return parse_explain_json(payload)

    def explain_only(self, sql: str, gucs: dict[str, str] | None = None) -> PlanMetrics:
        """Run EXPLAIN without ANALYZE (plan cost only, no execution).

        Used for plan comparison when ANALYZE would be too expensive.
        """
        gucs = dict(gucs or {})
        explain_sql = "EXPLAIN (FORMAT JSON) " + sql.rstrip().rstrip(";")
        conn = self.connect()
        with conn.cursor() as cur:
            for key, value in gucs.items():
                cur.execute("SELECT set_config(%s, %s, true)", (key, str(value)))
            cur.execute(explain_sql)
            row = cur.fetchone()
        payload = row[0]
        if isinstance(payload, str):
            payload = json.loads(payload)
        return parse_explain_json(payload)

    def execute_scalar(self, sql: str) -> Any:
        with self.connect().cursor() as cur:
            cur.execute(sql)
            row = cur.fetchone()
            return row[0] if row else None

    @contextmanager
    def temporary_index(self, table: str, columns: tuple[str, ...]) -> Iterator[str]:
        """Context manager that creates an index and drops it on exit."""
        name = self.create_index(table, columns)
        try:
            yield name
        finally:
            if name:
                self.drop_index(name)


def quote_ident(name: str) -> str:
    return '"' + name.replace('"', '""') + '"'


# Backwards-compatible alias used by demo_schema bootstrap.
_quote_ident = quote_ident
