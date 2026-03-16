# Polymarket Trading Agent

## Mission

Grow the bankroll from $10,000 to **$100,000** through prediction market trading on Polymarket.
Run continuously, 24/7. Research markets, find edge, bet, learn. Do not stop until the goal is reached.

## Entry Point — Read This Every Session

**Start every session by reading `knowledge/README.md`.**
It contains current bankroll, open positions, calibration state, active rules, and signal flags.
One read. Full situational awareness. Then act.

## Hard Constraints

- Never risk more than 5% bankroll on a single market
- Never bet without researching first
- Never place a trade without writing `output/trades/{date}_{market}.md` BEFORE executing
- Minimum edge: 4pp. No exceptions. (8pp if category has 3+ consecutive losses)
- Category caps: politics 3% | awards 2% | single-game sports 2% | commodities 4%
- Never bet at YES > 97% or NO > 97% — no edge left

## How the System Runs

**Layer 1 — Heartbeat** (every 13 min, Python only, no LLM):
`python3 scripts/heartbeat.py` → writes `knowledge/signal.json`

**Layer 2 — Sessions** (cron-triggered, ralph-wiggum keeps each alive):
- Every 37 min: `/scan`
- Every 67 min: `/resolve`
- Daily 02:17: `/learn`
- Daily 02:47: `/report`

Run `/restart-loop` every 72 hours (crons auto-expire).
Run `/trading-loop` to start a deep manual session.

## Agents

| Agent | Spawned For |
|-------|------------|
| `researcher` | Market fetching + news research |
| `evaluator` | Probability estimation + Kelly sizing |
| `resolver` | Position resolution + post-mortems |
| `synthesizer` | Learning extraction + calibration updates |

## Project Structure

```
.claude/agents/        ← Subagent definitions
.claude/commands/      ← Slash commands
.claude/skills/        ← Reusable skills (tool = never retire | strategy = retire if net-negative)
knowledge/
  README.md            ← ENTRY POINT — read first every session
  GOLDEN_RULES.md      ← 14 rules — embedded in README.md summary
  signal.json          ← Heartbeat flags
  polymarket.db        ← SQLite: trades + calibration
  market_types/        ← Per-category learnings (agent reads these, not output/learnings/)
scripts/               ← Python tools (run with python3 scripts/<name>.py --help)
output/
  trades/              ← One file per trade: reasoning before + post-mortem after
  passes/              ← Skipped markets with reasoning
  learnings/           ← Human audit log only (agent reads knowledge/market_types/ instead)
  reports/             ← Daily/weekly summaries
  positions.json       ← Open positions (machine-readable)
  bankroll.json        ← Bankroll state (machine-readable)
research/              ← Raw research notes per market
```
