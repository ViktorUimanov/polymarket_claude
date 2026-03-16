Check all open positions for resolution and record outcomes. Runs every 67 minutes via cron.

Delegate to the **resolver** agent defined in `.claude/agents/resolver.md`.

## Quick Steps

### 1. Check All Positions
```bash
python3 /root/workspace/polymarket/scripts/check_resolutions.py --all
```

### 2. For Each Resolved Position

The resolver agent handles:
- Calculating win/loss P&L
- Updating `output/trades/{date}_{market}.md` with resolution section
- Recording to `knowledge/calibration.csv` via `scripts/calibration.py --record`
- Removing from `output/positions.json`
- Updating `output/bankroll.json`
- Writing post-mortem for any losses
- Updating `knowledge/edge_sources.md` for wins

### 3. After All Resolutions

Output summary:
```
## Resolution Check — {datetime}
Checked: {N} | Wins: {N} (+${total}) | Losses: {N} (-${total}) | Unresolved: {N}
Net P&L: ${+/-amount} | Running bankroll: ${amount}
```

If any losses occurred: suggest running `/learn` to synthesize lessons while context is fresh.
If any positions are [STALE] (> 72h past end date): flag for manual review.
