Generate the daily performance report. Runs automatically at 02:47 via cron.

## Steps

### 1. Gather Data
```bash
python3 /root/workspace/polymarket/scripts/portfolio.py --full
python3 /root/workspace/polymarket/scripts/calibration.py --summary
```

Read:
- All `output/trades/{today}_*.md` — trades placed today
- All `output/passes/{today}_*.md` — markets passed today
- Latest `output/reports/scan_*.md` — scan results from today

### 2. Write Daily Report

Write to `output/reports/daily_{date}.md`:

```markdown
# Daily Report — {date}

## Session Overview
- Session type: {automated-cron / manual / hybrid}
- Markets scanned: {N across N categories}
- Candidates evaluated: {N}
- Trades placed: {N}
- Trades resolved: {N}

## P&L
| | Amount |
|--|--|
| Starting bankroll | $X |
| Cash in/out today | $X |
| Open positions (MTM) | $X |
| Ending portfolio | $X |
| Session P&L | ${+/-} |
| All-time P&L | ${+/-} |
| All-time return | {+/-%} |

## Trades Placed Today
{For each: market name, direction, entry price, size, edge, one-line reasoning}

## Passes Today
{For each: market name, one-line reason — was the pass correct in hindsight?}

## Key Decisions
{2–3 most important decisions and reasoning. Include at least one "what I almost did wrong"}

## Calibration Check
{Table from calibration.py — any categories drifting?}

## Open Positions Snapshot
{Table of all open positions with current MTM value}

## Priority for Next Session
- Resolving soon: {list markets expiring in next 24h}
- Monitor: {list markets with developing news}
- Research needed: {list candidate markets not yet deeply researched}

## Open Questions
{What do you not know that you need to research? Max 3.}
```

### 3. Weekly Report (Mondays Only)

If today is Monday, also write `output/reports/weekly_{date}.md`:

```markdown
# Weekly Report — Week of {date}

## Win/Loss Stats
| Category | Trades | Wins | Win% | P&L |
|----------|--------|------|------|-----|

## Calibration Table (7-day)
{stated prob vs actual win rate by category}

## Strategies: What's Working
{strategies with positive edge this week}

## Strategies: What's Not
{strategies with negative edge this week — retire or adjust?}

## Top 3 Lessons This Week
1. {specific, actionable}
2. {specific, actionable}
3. {specific, actionable}

## Strategy Adjustments Made
{any changes to knowledge/strategies.md this week}

## Next Week Focus
{what to prioritize — markets, categories, research}
```

### 4. Archive

Scan report files older than 7 days: leave in place (never delete output).
