"""Load SQL workloads and split without leaking equivalent queries."""

from __future__ import annotations

import hashlib
import random
from pathlib import Path

from sql_optimizer.parser import normalize_sql, parse_sql
from sql_optimizer.utils import ROOT


def load_sql_statements(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    statements: list[str] = []
    buf: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("--") or stripped.startswith("#"):
            continue
        buf.append(line)
        if ";" in line:
            chunk = "\n".join(buf).strip()
            buf = []
            for part in chunk.split(";"):
                sql = part.strip()
                if sql:
                    statements.append(sql)
    if buf:
        leftover = "\n".join(buf).strip().rstrip(";")
        if leftover:
            statements.append(leftover)
    return statements


def load_workload(
    files: list[str],
    *,
    min_relations: int = 2,
    max_relations: int = 4,
    max_queries: int = 80,
    allow_parse_fail: bool = False,
) -> list[str]:
    seen: set[str] = set()
    queries: list[str] = []
    for rel in files:
        path = Path(rel)
        if not path.is_absolute():
            path = ROOT / rel
        if not path.exists():
            continue
        for sql in load_sql_statements(path):
            if not sql.lower().lstrip().startswith("select"):
                continue
            structure = parse_sql(sql)
            if not structure.parse_ok and not allow_parse_fail:
                continue
            nrel = structure.n_relations
            if nrel < min_relations or nrel > max_relations:
                continue
            key = normalize_sql(sql)
            if key in seen:
                continue
            seen.add(key)
            queries.append(structure.original_sql)
            if len(queries) >= max_queries:
                return queries
    return queries


def split_queries(
    queries: list[str],
    *,
    seed: int = 42,
    train_frac: float = 0.70,
    val_frac: float = 0.15,
) -> tuple[list[str], list[str], list[str]]:
    """Random split keyed by normalized SQL so duplicates cannot cross sets.

    Unlike the historical notebook, this does *not* sort by PostgreSQL cost.
    """
    buckets: dict[str, list[str]] = {}
    for sql in queries:
        buckets.setdefault(normalize_sql(sql), []).append(sql)
    keys = sorted(buckets)
    rng = random.Random(seed)
    rng.shuffle(keys)
    n = len(keys)
    n_train = int(n * train_frac)
    n_val = int(n * val_frac)
    train_keys = keys[:n_train]
    val_keys = keys[n_train : n_train + n_val]
    test_keys = keys[n_train + n_val :]
    train = _first(buckets, train_keys)
    val = _first(buckets, val_keys)
    test = _first(buckets, test_keys)
    return train, val, test


def _first(buckets: dict[str, list[str]], keys: list[str]) -> list[str]:
    return [buckets[k][0] for k in keys]


def query_id(sql: str) -> str:
    return hashlib.sha1(normalize_sql(sql).encode()).hexdigest()[:10]
