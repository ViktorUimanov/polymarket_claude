---
name: correlated-position-check
description: Check if a new bet is correlated with existing open positions before sizing
type: tool
performance:
  uses: 0
  wins_contributed: 0
  losses_contributed: 0
  status: ACTIVE
  last_reviewed: 2026-03-16
---

# Correlated Position Check Skill

**GOLDEN_RULES Rule 6**: Before placing any new bet, check if it is positively
correlated with existing open positions. Max correlated exposure: 10% bankroll.

## What "Correlated" Means Here

Two positions are correlated if they **both lose in the same scenario**.

Example of dangerous correlation:
- Oil $100 YES (loses if oil stays calm)
- Iran regime NO (loses if Iran conflict escalates sharply and oil spikes)

Wait — these are *opposite* correlations. The dangerous case:
- Oil $100 YES (wins if oil spikes above $100 — requires conflict escalation)
- Iran regime fall NO (also wins if regime holds and conflict continues)

These are not correlated. But:
- Oil $100 YES (wins if Iran conflict escalates)
- Iran regime fall YES (also wins if conflict escalates → regime falls)

These ARE correlated — both lose if conflict de-escalates.

## Step-by-Step Check

### 1. List your open positions
```bash
python3 scripts/portfolio.py
```
Or read `output/positions.json` directly.

### 2. For the NEW proposed bet, define the loss scenario
"This bet loses if: ___"

### 3. For each existing open position, check the same
"This existing position loses if: ___"

### 4. Identify overlapping loss scenarios

| Scenario | Positions at Risk | Combined Exposure |
|----------|------------------|------------------|
| [e.g., oil price drops] | [list them] | $X |
| [e.g., Iran conflict ends] | [list them] | $X |

### 5. Apply the limit

**Max correlated exposure in one scenario: 10% bankroll**

Current bankroll: read from `output/bankroll.json`
```python
import json
b = json.loads(open("output/bankroll.json").read())
max_correlated = b["cash"] * 0.10
```

If adding the new position would push correlated exposure in any single scenario
above 10% bankroll → reduce new position size until it fits.

### 6. Special Case: Directional Macro Bets

If you have multiple positions that all depend on the same macro condition
(e.g., US-Iran relations, oil price direction, election outcome):

- Treat them as a single "macro bet"
- Apply extra scrutiny: max 15% total bankroll in one macro theme
- If uncertain about correlation, assume it's there (conservative)

## Output Template

Write this in your trade file before sizing:

```markdown
## Correlation Check

**New position loses if**: [scenario]

**Existing positions and their loss scenarios**:
- [Position 1] loses if: [scenario] — CORRELATED? [yes/no]
- [Position 2] loses if: [scenario] — CORRELATED? [yes/no]

**Correlated exposure in worst case**:
- Scenario: [worst shared loss scenario]
- Positions at risk: $X (existing) + $Y (proposed) = $Z
- Limit: 10% bankroll = $[amount]
- **STATUS**: [WITHIN LIMIT / EXCEEDS LIMIT — reduce size]

**Final size after correlation adjustment**: $[amount]
```

## When This Skill Was Critical

- **Oil $100 YES + Iran regime NO**: Both depended on Iran conflict continuing.
  Not classic correlation (one needed conflict, other needed regime stability),
  but they shared the same macro theme — flagged for review.
