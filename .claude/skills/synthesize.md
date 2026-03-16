---
name: synthesize
description: Process for converting trade outcomes into structured, actionable knowledge — the difference between data and learning
type: strategy
performance:
  uses: 0
  wins_contributed: 0
  losses_contributed: 0
  status: ACTIVE
  last_reviewed: 2026-03-16
---

# Synthesize Learnings Skill

## The Core Principle

**Raw data ≠ learning. A learning is a pattern that changes future behavior.**

Bad synthesis: "I should research more"
Good synthesis: "Before betting on Oscars Best Picture, I must check ALL nominees including those priced < 5%, not just the top 2 frontrunners"

## For Each Resolved Trade

### 1. Classify the Error Type (Losses) or Edge Source (Wins)

**Loss error types:**
- `information_error` — you didn't know something the market knew
- `model_error` — your probability estimation framework was wrong
- `calibration_error` — right framework, wrong weights
- `resolution_error` — you misunderstood the resolution criteria
- `black_swan` — genuinely unpredictable tail event (rare — be honest, don't overuse)

**Win edge sources:**
- `information` — you had data others lacked
- `framework` — you applied base rates others ignored
- `market_inefficiency` — thin market, overreaction, or stale price
- `calibration` — market was miscalibrated, you correctly identified it
- `luck` — be honest about this; don't build strategy on one lucky trade

### 2. Extract the Specific Rule (Losses)

Template:
```
Category: <category>
Rule: Before betting on <X>, I must <specific action>.
Trigger condition: When I see <specific signal>.
Added: knowledge/market_types/<category>.md on <date>
```

### 3. Update the Knowledge Base

**For losses:**
```bash
# Append to category learnings
echo "## {date} — Lesson from {market}
**Rule**: {specific rule}
**Why**: {what happened}
**Apply when**: {trigger}" >> /root/workspace/polymarket/knowledge/market_types/<category>.md
```

**For wins:**
```bash
# Update edge sources if reproducible
# Edit knowledge/edge_sources.md — find or add the source, update success_rate
```

**Always:**
```bash
# Record to calibration database (SQLite-backed)
python3 /root/workspace/polymarket/scripts/calibration.py --record \
  --market-id <id> --category <cat> --stated-prob <X> --outcome <WIN|LOSS> --pnl <amount>
```

## Cross-Trade Pattern Recognition

After every 5 resolved trades in a category, ask:
1. Is there a systematic bias? (always underestimate underdogs? always overestimate favorites?)
2. Is there a type of market within this category we consistently beat?
3. Is there a type we consistently lose?

If yes to any: document as a strategy in `knowledge/strategies.md`.

## Synthesis Quality Check

A good synthesis answers:
- What specifically will I do differently next time?
- Where in the workflow does this rule apply (research / evaluation / sizing)?
- How do I know if I'm applying it correctly?

A poor synthesis:
- "I need to be more careful"
- "I should do more research"
- "I was unlucky"

## Speed Synthesis (for cron — limited context)

When running as automated synthesis, minimum required:
1. Add one row to `knowledge/calibration.csv`
2. Add one bullet to `knowledge/market_types/<category>.md` if a loss
3. Update `output/bankroll.json`

Full synthesis happens in `/learn` command with synthesizer agent.
