"""Create a JOB-light-compatible demo schema when full IMDB is unavailable.

Table and column names match job_light.sql / synthetic.sql so the same
workload files can run. Data volume is small enough for closed-loop
EXPLAIN ANALYZE training but large enough that join order and indexes matter.

Existing indexes: PRIMARY KEY on title(id) only. Foreign-key columns are
intentionally unindexed so index-selection actions are meaningful.
"""

from __future__ import annotations

import random

from sql_optimizer.database import PostgresDB, _quote_ident

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS title (
    id INTEGER PRIMARY KEY,
    kind_id INTEGER NOT NULL,
    production_year INTEGER,
    title TEXT
);
CREATE TABLE IF NOT EXISTS movie_companies (
    movie_id INTEGER NOT NULL,
    company_id INTEGER NOT NULL,
    company_type_id INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS movie_info (
    movie_id INTEGER NOT NULL,
    info_type_id INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS movie_info_idx (
    movie_id INTEGER NOT NULL,
    info_type_id INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS movie_keyword (
    movie_id INTEGER NOT NULL,
    keyword_id INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS cast_info (
    movie_id INTEGER NOT NULL,
    person_id INTEGER NOT NULL,
    role_id INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS info_type (
    id INTEGER PRIMARY KEY,
    info TEXT
);
CREATE TABLE IF NOT EXISTS company_type (
    id INTEGER PRIMARY KEY,
    kind TEXT
);
CREATE TABLE IF NOT EXISTS keyword (
    id INTEGER PRIMARY KEY,
    keyword TEXT
);
"""

TABLES = [
    "movie_companies",
    "movie_info",
    "movie_info_idx",
    "movie_keyword",
    "cast_info",
    "title",
    "info_type",
    "company_type",
    "keyword",
]


def schema_is_ready(db: PostgresDB, min_titles: int = 1000) -> bool:
    try:
        n = db.execute_scalar("SELECT COUNT(*) FROM title")
        return int(n or 0) >= min_titles
    except Exception:
        return False


def bootstrap_demo_db(
    db: PostgresDB,
    *,
    n_titles: int = 4000,
    seed: int = 42,
    force: bool = False,
) -> dict[str, int]:
    conn = db.connect()
    with conn.cursor() as cur:
        if force:
            for table in TABLES:
                cur.execute(f"DROP TABLE IF EXISTS {_quote_ident(table)} CASCADE")
        for stmt in SCHEMA_SQL.split(";"):
            stmt = stmt.strip()
            if stmt:
                cur.execute(stmt)
        cur.execute("SELECT COUNT(*) FROM title")
        existing = int(cur.fetchone()[0])
        if existing >= n_titles and not force:
            return {"title": existing, "skipped": 1}

        rng = random.Random(seed)
        titles = []
        for i in range(1, n_titles + 1):
            titles.append((i, rng.randint(1, 7), rng.randint(1950, 2017), f"m{i}"))
        _copy(cur, "title", "(id, kind_id, production_year, title)", titles)

        info_types = [(i, f"it{i}") for i in range(1, 120)]
        _copy(cur, "info_type", "(id, info)", info_types)
        _copy(cur, "company_type", "(id, kind)", [(1, "distributor"), (2, "production companies")])
        _copy(cur, "keyword", "(id, keyword)", [(i, f"k{i}") for i in range(1, 2001)])

        mc, mi, mii, mk, ci = [], [], [], [], []
        for tid in range(1, n_titles + 1):
            for _ in range(rng.randint(1, 4)):
                mc.append((tid, rng.randint(1, 30000), rng.choice([1, 2, 2])))
            for _ in range(rng.randint(1, 6)):
                mi.append((tid, rng.randint(1, 20)))
            for _ in range(rng.randint(0, 3)):
                mii.append((tid, rng.choice([99, 100, 101, 112, 113])))
            for _ in range(rng.randint(1, 8)):
                mk.append((tid, rng.randint(1, 2000)))
            for _ in range(rng.randint(2, 12)):
                ci.append((tid, rng.randint(1, 500000), rng.randint(1, 8)))

        _copy(cur, "movie_companies", "(movie_id, company_id, company_type_id)", mc)
        _copy(cur, "movie_info", "(movie_id, info_type_id)", mi)
        _copy(cur, "movie_info_idx", "(movie_id, info_type_id)", mii)
        _copy(cur, "movie_keyword", "(movie_id, keyword_id)", mk)
        _copy(cur, "cast_info", "(movie_id, person_id, role_id)", ci)
        cur.execute("ANALYZE")

    counts = {}
    for table in TABLES:
        counts[table] = int(db.execute_scalar(f"SELECT COUNT(*) FROM {table}"))
    return counts


def _copy(cur, table: str, cols: str, rows: list[tuple]) -> None:
    if not rows:
        return
    with cur.copy(f"COPY {table} {cols} FROM STDIN") as copy:
        for row in rows:
            copy.write_row(row)
