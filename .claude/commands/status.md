Show the current portfolio status, open positions, P&L, and calibration snapshot.

## Steps

### 1. Full Portfolio Report
```bash
python3 /root/workspace/polymarket/scripts/portfolio.py --full
```

### 2. Mark Open Positions to Market
For each open position in `output/positions.json`, get current price:
```bash
python3 /root/workspace/polymarket/scripts/fetch_markets.py --market-id <id> --price-only
```
Calculate unrealized P&L: `(current_price - entry_price) × shares`

### 3. Calibration Snapshot
```bash
python3 /root/workspace/polymarket/scripts/calibration.py --summary
```

### 4. Output

```
# Portfolio Status — {datetime}

## Bankroll
- Starting:           $10,000.00
- Cash available:     ${amount}
- Open value (MTM):   ${amount}
- Total portfolio:    ${amount}
- P&L (realized):     ${+/-amount}
- P&L (unrealized):   ${+/-amount}
- Total return:       {+/-%}

## Open Positions ({N})

| Market | Dir | Entry | Current | Size | Unreal P&L | Expires | Flag |
|--------|-----|-------|---------|------|-----------|---------|------|
| ...    | YES | 88.8% | 91.2%   | $300 | +$7.19   | 2026-03-31 | |

## Resolved Trade Summary
- Wins:     {N} (+${total})
- Losses:   {N} (-${total})
- Win rate: {%}

## Calibration Snapshot
{table from calibration.py --summary}

## Alerts
{[EXPIRING SOON] — positions resolving within 48h}
{[REVIEW NEEDED] — positions that have moved >15pp against us}
{[STALE] — positions >72h past end date}
```

## Flags

- `[EXPIRING SOON]` — resolves within 48 hours → prioritize resolution check
- `[REVIEW NEEDED]` — current price has moved > 15pp against entry → consider if thesis still holds
- `[STALE]` — end date has passed but not marked resolved → investigate manually
