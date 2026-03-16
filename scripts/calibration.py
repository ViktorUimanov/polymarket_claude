#!/usr/bin/env python3
"""
Calibration tracker — records predictions and measures stated vs actual accuracy.

Backed by SQLite (knowledge/polymarket.db) via scripts/db.py.

Usage:
  python3 calibration.py --summary
  python3 calibration.py --category sports
  python3 calibration.py --category sports --last-n 10
  python3 calibration.py --record --market-id <id> --category <cat> \
      --stated-prob <X> --outcome WIN --pnl <amount>
"""

import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from db import record_calibration, get_calibration_stats

CATEGORIES = ["oscars", "sports", "commodities", "politics", "crypto", "other"]


def interpret_error(error, n_trades):
    if n_trades < 5:
        return "INSUFFICIENT DATA (< 5 trades)"
    if error > 20:
        return "UNDERCONFIDENT — can size up slightly"
    elif error > 10:
        return "Slightly underconfident"
    elif error >= -10:
        return "WELL CALIBRATED"
    elif error >= -20:
        return "Slightly OVERCONFIDENT — require +6pp edge, -25% size"
    elif error >= -30:
        return "OVERCONFIDENT — require +8pp edge, -50% size"
    else:
        return "SEVERELY OVERCONFIDENT — require +10pp edge, max 1% bankroll"


def print_summary(category=None, last_n=None):
    cats = [category] if category else CATEGORIES
    stats = get_calibration_stats(category=category, last_n=last_n)

    print(f"\n{'=' * 72}")
    label = f"CALIBRATION SUMMARY — {category.upper()}" if category else "CALIBRATION SUMMARY — ALL CATEGORIES"
    if last_n:
        label += f" (last {last_n} trades)"
    print(f"  {label}")
    print(f"{'=' * 72}")
    print(f"  {'Category':<14} {'Trades':>7} {'Wins':>5} {'Win%':>6} {'Stated%':>8} {'Error':>8} {'P&L':>12}")
    print(f"  {'─' * 68}")

    totals = {"total": 0, "wins": 0, "losses": 0, "pnl": 0.0, "stated_sum": 0.0}

    for cat in cats:
        s = stats.get(cat)
        if not s:
            print(f"  {cat:<14} {'—':>7}")
            continue
        err_str = f"{s['calibration_error']:+.0f}pp"
        print(
            f"  {cat:<14} {s['total']:>7} {s['wins']:>5} "
            f"{s['win_rate']*100:>5.0f}% {s['avg_stated']:>7.1f}% "
            f"{err_str:>8} ${s['total_pnl']:>11,.2f}"
        )
        totals["total"] += s["total"]
        totals["wins"] += s["wins"]
        totals["pnl"] += s["total_pnl"]
        totals["stated_sum"] += s["avg_stated"] * s["total"]

    if len(cats) > 1 and totals["total"] > 0:
        win_rate = totals["wins"] / totals["total"]
        avg_stated = totals["stated_sum"] / totals["total"]
        cal_error = win_rate * 100 - avg_stated
        err_str = f"{cal_error:+.0f}pp"
        print(f"  {'─' * 68}")
        print(
            f"  {'TOTAL':<14} {totals['total']:>7} {totals['wins']:>5} "
            f"{win_rate*100:>5.0f}% {avg_stated:>7.1f}% "
            f"{err_str:>8} ${totals['pnl']:>11,.2f}"
        )
        print(f"\n  Overall: {interpret_error(cal_error, totals['total'])}")

    if category:
        s = stats.get(category)
        if s:
            print(f"\n  Status: {interpret_error(s['calibration_error'], s['total'])}")

    print()


def main():
    parser = argparse.ArgumentParser(description="Calibration tracker for Polymarket agent")
    parser.add_argument("--summary", action="store_true", help="Print calibration summary")
    parser.add_argument("--category", help="Filter by category")
    parser.add_argument("--last-n", type=int, help="Only consider last N trades")
    parser.add_argument("--record", action="store_true", help="Record a new outcome")
    parser.add_argument("--market-id", help="Market ID (for --record)")
    parser.add_argument("--stated-prob", type=float, help="Your stated probability (for --record)")
    parser.add_argument("--outcome", choices=["WIN", "LOSS"], help="Trade outcome (for --record)")
    parser.add_argument("--pnl", type=float, help="P&L in dollars (for --record)")
    parser.add_argument("--notes", default="", help="Optional notes (for --record)")
    args = parser.parse_args()

    if args.record:
        missing = [
            name for name, val in [
                ("--market-id", args.market_id),
                ("--category", args.category),
                ("--stated-prob", args.stated_prob),
                ("--outcome", args.outcome),
                ("--pnl", args.pnl),
            ]
            if val is None
        ]
        if missing:
            print(f"ERROR: --record requires: {', '.join(missing)}", file=sys.stderr)
            sys.exit(1)
        record_calibration(
            args.market_id, args.category, args.stated_prob,
            args.outcome, args.pnl, args.notes
        )
        print(f"Recorded: {args.outcome} | market {args.market_id} | "
              f"category: {args.category} | stated: {args.stated_prob}% | P&L: ${args.pnl}")

    elif args.summary or args.category:
        print_summary(category=args.category, last_n=args.last_n)

    else:
        print_summary(last_n=args.last_n)


if __name__ == "__main__":
    main()
