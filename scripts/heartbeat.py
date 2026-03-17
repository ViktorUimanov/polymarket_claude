#!/usr/bin/env python3
"""
Lightweight heartbeat — runs every ~15 min via cron (NOT an LLM call).

Writes signal.json flags that the ralph orchestrator loop reads to
decide whether to trigger an expensive LLM operation.

Logic:
  - scan_needed:    True if no scan in last 4 hours
  - resolve_needed: True if any position's end_date is within 24h OR
                    it's been > 1 hour since last resolve
  - learn_needed:   True if new resolved trades since last learn run

Output: knowledge/signal.json (read by trading-loop / /scan / /resolve)
"""

import json
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

BASE = Path("/root/workspace/polymarket")
SIGNAL_FILE = BASE / "knowledge" / "signal.json"
POSITIONS_FILE = BASE / "output" / "positions.json"
REPORTS_DIR = BASE / "output" / "reports"
DB_PATH = BASE / "knowledge" / "polymarket.db"

NOW = datetime.now(timezone.utc)


def latest_report_time(prefix: str) -> datetime | None:
    """Return the mtime of the most recent report file matching prefix."""
    files = list(REPORTS_DIR.glob(f"{prefix}*.md"))
    if not files:
        return None
    latest = max(files, key=lambda f: f.stat().st_mtime)
    return datetime.fromtimestamp(latest.stat().st_mtime, tz=timezone.utc)


def scan_needed() -> bool:
    t = latest_report_time("scan_")
    if t is None:
        return True
    return (NOW - t) > timedelta(minutes=45)


def resolve_needed(positions: list) -> bool:
    # Check if any position expires within 24h
    for p in positions:
        end = p.get("end_date")
        if end:
            try:
                end_dt = datetime.fromisoformat(end).replace(tzinfo=timezone.utc)
                if end_dt - NOW < timedelta(hours=24):
                    return True
            except ValueError:
                pass
    # Fallback: check if last resolve was > 1 hour ago
    t = latest_report_time("resolve_")
    if t is None:
        return True
    return (NOW - t) > timedelta(hours=1)


def learn_needed() -> bool:
    """True if there are resolved trades in DB newer than the last learn run."""
    import sqlite3
    if not DB_PATH.exists():
        return False
    t = latest_report_time("learn_")
    cutoff = t.strftime("%Y-%m-%d") if t else "1970-01-01"
    try:
        conn = sqlite3.connect(DB_PATH)
        row = conn.execute(
            "SELECT COUNT(*) FROM trades WHERE outcome != 'OPEN' AND resolved_date > ?",
            (cutoff,)
        ).fetchone()
        conn.close()
        return row[0] > 0
    except Exception:
        return False


def expiring_soon(positions: list) -> list[str]:
    """Return market questions expiring within 48 hours."""
    result = []
    for p in positions:
        end = p.get("end_date")
        if end:
            try:
                end_dt = datetime.fromisoformat(end).replace(tzinfo=timezone.utc)
                if timedelta(0) < end_dt - NOW < timedelta(hours=48):
                    result.append(p.get("question", p.get("market_id", "unknown")))
            except ValueError:
                pass
    return result


def main():
    # Load current positions
    positions = []
    if POSITIONS_FILE.exists():
        try:
            data = json.loads(POSITIONS_FILE.read_text())
            positions = data.get("positions", [])
        except Exception:
            pass

    signal = {
        "generated_at": NOW.isoformat(),
        "scan_needed": scan_needed(),
        "resolve_needed": resolve_needed(positions),
        "learn_needed": learn_needed(),
        "expiring_soon": expiring_soon(positions),
        "open_positions": len(positions),
    }

    SIGNAL_FILE.parent.mkdir(parents=True, exist_ok=True)
    SIGNAL_FILE.write_text(json.dumps(signal, indent=2))

    print(f"[heartbeat] {NOW.strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"  scan_needed:    {signal['scan_needed']}")
    print(f"  resolve_needed: {signal['resolve_needed']}")
    print(f"  learn_needed:   {signal['learn_needed']}")
    print(f"  expiring_soon:  {signal['expiring_soon']}")
    print(f"  open_positions: {signal['open_positions']}")
    print(f"  → wrote {SIGNAL_FILE}")


if __name__ == "__main__":
    main()
