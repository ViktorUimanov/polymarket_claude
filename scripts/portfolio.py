#!/usr/bin/env python3
"""
Portfolio tracker — bankroll, open positions, P&L.

Usage:
  python3 portfolio.py                  # brief one-liner
  python3 portfolio.py --full           # detailed report
  python3 portfolio.py --bankroll-only  # just the cash number (for piping)
"""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import requests

BASE = Path("/root/workspace/polymarket")
POSITIONS_FILE = BASE / "output/positions.json"
BANKROLL_FILE = BASE / "output/bankroll.json"
GAMMA_BASE = "https://gamma-api.polymarket.com"


def load_bankroll():
    if not BANKROLL_FILE.exists():
        return {
            "starting": 10000.0,
            "cash": 10000.0,
            "total_pnl": 0.0,
            "last_updated": "never",
            "last_trade_date": None,
        }
    with open(BANKROLL_FILE) as f:
        return json.load(f)


def load_positions():
    if not POSITIONS_FILE.exists():
        return []
    with open(POSITIONS_FILE) as f:
        return json.load(f).get("positions", [])


def get_current_price(market_id):
    """Fetch current YES/NO prices for a market. Returns None on error."""
    try:
        r = requests.get(f"{GAMMA_BASE}/markets", params={"id": market_id}, timeout=10)
        r.raise_for_status()
        markets = r.json()
        if not markets:
            return None
        prices = json.loads(markets[0].get("outcomePrices") or "[0.5,0.5]")
        return {"yes": float(prices[0]), "no": float(prices[1])}
    except Exception:
        return None


def get_flags(pos, current):
    """Return alert flags for a position."""
    flags = []
    end_date = pos.get("end_date", "")
    if end_date:
        try:
            end_dt = datetime.fromisoformat(end_date + "T00:00:00+00:00")
            hours_left = (end_dt - datetime.now(timezone.utc)).total_seconds() / 3600
            if hours_left < 48:
                flags.append("[EXPIRING SOON]")
            if hours_left < -72:
                flags.append("[STALE]")
        except Exception:
            pass

    if current:
        direction = pos.get("direction", "YES")
        entry = float(pos.get("entry_price", 0.5))
        cur_price = current["yes"] if direction == "YES" else current["no"]
        move = (cur_price - entry) * 100
        if move < -15:
            flags.append("[REVIEW NEEDED]")

    return flags


def main():
    parser = argparse.ArgumentParser(description="Polymarket portfolio tracker")
    parser.add_argument("--full", action="store_true", help="Detailed portfolio report")
    parser.add_argument("--bankroll-only", action="store_true", help="Print cash as number only")
    args = parser.parse_args()

    bankroll = load_bankroll()
    positions = load_positions()

    if args.bankroll_only:
        print(f"{bankroll['cash']:.2f}")
        return

    starting = bankroll.get("starting", 10000.0)
    cash = bankroll.get("cash", starting)
    total_pnl = bankroll.get("total_pnl", 0.0)

    if not args.full:
        print(f"Bankroll: ${cash:,.2f} | Realized P&L: ${total_pnl:+,.2f} | Open positions: {len(positions)}")
        return

    # Full report
    print(f"\n{'=' * 65}")
    print(f"  PORTFOLIO STATUS — {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"{'=' * 65}")
    print(f"  Starting bankroll:   ${starting:>10,.2f}")
    print(f"  Cash available:      ${cash:>10,.2f}")

    open_cost = sum(float(p.get("size", 0)) for p in positions)
    open_mtm = 0.0
    unrealized_pnl = 0.0

    position_rows = []
    for pos in positions:
        market_id = pos.get("market_id")
        question = pos.get("question", "Unknown")[:34]
        direction = pos.get("direction", "YES")
        entry = float(pos.get("entry_price", 0.5))
        size = float(pos.get("size", 0))
        shares = size / entry if entry > 0 else 0
        end_date = pos.get("end_date", "?")[:10]

        current = get_current_price(market_id)
        if current:
            cur_price = current["yes"] if direction == "YES" else current["no"]
            mtm_value = shares * cur_price
            unreal = mtm_value - size
            cur_str = f"{cur_price * 100:.1f}%"
        else:
            mtm_value = size  # assume flat if no price
            unreal = 0.0
            cur_str = "N/A"

        open_mtm += mtm_value
        unrealized_pnl += unreal

        flags = get_flags(pos, current)
        flag_str = " ".join(flags)

        position_rows.append((question, direction, entry, cur_str, size, unreal, end_date, flag_str))

    print(f"  Open positions (MTM):${open_mtm:>10,.2f}")
    total_portfolio = cash + open_mtm
    print(f"  Total portfolio:     ${total_portfolio:>10,.2f}")

    print(f"\n{'─' * 65}")
    print(f"  P&L SUMMARY")
    print(f"{'─' * 65}")
    print(f"  Realized P&L:        ${total_pnl:>+10,.2f}")
    print(f"  Unrealized P&L:      ${unrealized_pnl:>+10,.2f}")
    print(f"  Total P&L:           ${total_pnl + unrealized_pnl:>+10,.2f}")
    print(f"  Total return:        {(total_portfolio / starting - 1) * 100:>+9.2f}%")

    if positions:
        print(f"\n{'─' * 65}")
        print(f"  OPEN POSITIONS ({len(positions)})")
        print(f"{'─' * 65}")
        header = f"  {'Market':<34} {'Dir':>4} {'Entry':>6} {'Cur':>6} {'Size':>6} {'Unreal':>8} {'Exp':>10}"
        print(header)
        print(f"  {'─' * 63}")
        for q, d, e, cur, sz, unr, exp, flg in position_rows:
            row = f"  {q:<34} {d:>4} {e*100:>5.1f}% {cur:>6} ${sz:>5,.0f} ${unr:>+7,.2f} {exp:>10}"
            print(row)
            if flg:
                print(f"  {'':>34} {flg}")

    print(f"{'=' * 65}\n")


if __name__ == "__main__":
    main()
