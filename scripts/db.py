#!/usr/bin/env python3
"""
Shared SQLite database interface for the Polymarket trading agent.

Database: knowledge/polymarket.db
Tables:
  - trades       : completed trades with outcomes and lessons
  - calibration  : per-prediction accuracy tracking
"""

import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = Path("/root/workspace/polymarket/knowledge/polymarket.db")


def get_conn() -> sqlite3.Connection:
    """Return a connection with row_factory for dict-like access."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


def init_db():
    """Create tables if they don't exist."""
    with get_conn() as conn:
        conn.executescript("""
        CREATE TABLE IF NOT EXISTS trades (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            date            TEXT NOT NULL,
            market_id       TEXT NOT NULL,
            question        TEXT NOT NULL,
            category        TEXT NOT NULL,
            direction       TEXT NOT NULL CHECK(direction IN ('YES','NO')),
            entry_price     REAL NOT NULL,
            stated_prob     REAL NOT NULL,
            edge_pp         REAL NOT NULL,
            size            REAL NOT NULL,
            outcome         TEXT CHECK(outcome IN ('WIN','LOSS','OPEN')),
            pnl             REAL,
            error_type      TEXT,
            lesson          TEXT,
            trade_file      TEXT,
            resolved_date   TEXT
        );

        CREATE TABLE IF NOT EXISTS calibration (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            date            TEXT NOT NULL,
            market_id       TEXT NOT NULL,
            category        TEXT NOT NULL,
            stated_prob     REAL NOT NULL,
            outcome         TEXT NOT NULL CHECK(outcome IN ('WIN','LOSS')),
            pnl             REAL NOT NULL,
            notes           TEXT DEFAULT ''
        );

        CREATE INDEX IF NOT EXISTS idx_trades_category ON trades(category);
        CREATE INDEX IF NOT EXISTS idx_trades_outcome   ON trades(outcome);
        CREATE INDEX IF NOT EXISTS idx_cal_category     ON calibration(category);
        """)


def record_trade(market_id, question, category, direction, entry_price,
                 stated_prob, edge_pp, size, trade_file=None):
    """Insert a new open trade. Returns the new row id."""
    init_db()
    with get_conn() as conn:
        cur = conn.execute("""
            INSERT INTO trades
              (date, market_id, question, category, direction, entry_price,
               stated_prob, edge_pp, size, outcome, trade_file)
            VALUES (?,?,?,?,?,?,?,?,?,'OPEN',?)
        """, (
            datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            str(market_id), question, category.lower(), direction.upper(),
            float(entry_price), float(stated_prob), float(edge_pp),
            float(size), trade_file
        ))
        return cur.lastrowid


def resolve_trade(market_id, outcome, pnl, error_type=None, lesson=None):
    """Mark an open trade as resolved."""
    init_db()
    with get_conn() as conn:
        conn.execute("""
            UPDATE trades
               SET outcome=?, pnl=?, error_type=?, lesson=?,
                   resolved_date=?
             WHERE market_id=? AND outcome='OPEN'
        """, (
            outcome.upper(), float(pnl), error_type, lesson,
            datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            str(market_id)
        ))


def record_calibration(market_id, category, stated_prob, outcome, pnl, notes=""):
    """Record one prediction outcome to calibration table."""
    init_db()
    with get_conn() as conn:
        conn.execute("""
            INSERT INTO calibration
              (date, market_id, category, stated_prob, outcome, pnl, notes)
            VALUES (?,?,?,?,?,?,?)
        """, (
            datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            str(market_id), category.lower(),
            float(stated_prob), outcome.upper(), float(pnl), notes
        ))


def get_calibration_stats(category=None, last_n=None):
    """
    Return calibration stats dict for one or all categories.
    Keys per category: total, wins, losses, win_rate, avg_stated, calibration_error, total_pnl
    """
    init_db()
    with get_conn() as conn:
        base = "SELECT category, stated_prob, outcome, pnl FROM calibration"
        rows = conn.execute(base).fetchall()

    # Group
    from collections import defaultdict
    buckets = defaultdict(list)
    for r in rows:
        buckets[r["category"]].append(r)

    if category:
        buckets = {category.lower(): buckets.get(category.lower(), [])}

    results = {}
    for cat, rlist in buckets.items():
        if last_n:
            rlist = rlist[-last_n:]
        if not rlist:
            continue
        wins = [r for r in rlist if r["outcome"] == "WIN"]
        win_rate = len(wins) / len(rlist)
        avg_stated = sum(r["stated_prob"] for r in rlist) / len(rlist)
        total_pnl = sum(r["pnl"] for r in rlist)
        results[cat] = {
            "total": len(rlist),
            "wins": len(wins),
            "losses": len(rlist) - len(wins),
            "win_rate": win_rate,
            "avg_stated": avg_stated,
            "calibration_error": win_rate * 100 - avg_stated,
            "total_pnl": total_pnl,
        }
    return results


def search_trades(category=None, outcome=None, error_type=None, limit=20):
    """Query trades table with optional filters. Returns list of dicts."""
    init_db()
    clauses, params = [], []
    if category:
        clauses.append("category=?"); params.append(category.lower())
    if outcome:
        clauses.append("outcome=?"); params.append(outcome.upper())
    if error_type:
        clauses.append("error_type=?"); params.append(error_type)
    where = ("WHERE " + " AND ".join(clauses)) if clauses else ""
    with get_conn() as conn:
        rows = conn.execute(
            f"SELECT * FROM trades {where} ORDER BY date DESC LIMIT ?",
            params + [limit]
        ).fetchall()
    return [dict(r) for r in rows]


if __name__ == "__main__":
    init_db()
    print(f"Database initialised at {DB_PATH}")
    with get_conn() as conn:
        tables = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        ).fetchall()
    print("Tables:", [t["name"] for t in tables])
