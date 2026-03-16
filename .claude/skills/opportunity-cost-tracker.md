---
name: opportunity-cost-tracker
description: Track markets you passed on and score the decision quality afterward
type: strategy
performance:
  uses: 0
  wins_contributed: 0
  losses_contributed: 0
  status: ACTIVE
  last_reviewed: 2026-03-16
---

# Opportunity Cost Tracker Skill

Tracks markets you passed on so you can score your PASS decisions after resolution.
A good PASS (market moved against your thesis) is as valuable as a WIN.
A bad PASS (you should have bet and would have profited) teaches the same lesson as a LOSS.

## When to Use

After every `/scan` run, for each market you PASS on with ≥ 4pp edge:
- Write a brief pass file to `output/passes/`
- Track the implied fair value and your reasoning
- After resolution, score it

## Recording a Pass

```bash
# Pass file format: output/passes/{date}_{market-slug}.md
```

Template:
```markdown
# PASS: [Market Question]
Date: {date}
Market ID: {id}
Category: {category}

## Decision
**PASS** — not betting

## Pricing at Decision
Market price: {X}%
My fair value: {Y}%
Implied edge: {Y-X}pp
Kelly suggested: ${size}

## Reason for Pass (pick one or more)
- [ ] Edge below 4pp minimum (Rule 5)
- [ ] Too close to resolution — insufficient time for thesis to play out
- [ ] Insufficient research — could not verify fair value
- [ ] Category on losing streak (Rule 10) — need 8pp+ edge
- [ ] Correlated with existing positions over limit (Rule 6)
- [ ] Market priced above 97% — no edge left (Rule 7)
- [ ] Calibration concern — overconfident in this category (Rule 3)
- [ ] Other: {explain}

## What Would Need to Change to Bet
{describe the conditions under which this becomes a bet}

## Resolution (fill in after market closes)
Resolved: {YES/NO/N/A}
Market price at resolution: {X}%
Was pass correct? {YES/NO}
Opportunity cost (if wrong): ${amount}
Lesson: {one sentence}
```

## Scoring Passes Weekly

Run this analysis during `/learn` or `/report`:

```python
import os, re
from pathlib import Path

passes_dir = Path("output/passes")
correct = 0
wrong = 0
opportunity_cost = 0.0

for f in passes_dir.glob("*.md"):
    text = f.read_text()
    if "Was pass correct? YES" in text:
        correct += 1
    elif "Was pass correct? NO" in text:
        wrong += 1
        # Extract opportunity cost
        m = re.search(r"Opportunity cost.*\$(\d+\.?\d*)", text)
        if m:
            opportunity_cost += float(m.group(1))

print(f"Passes: {correct} correct, {wrong} wrong")
print(f"Total opportunity cost from wrong passes: ${opportunity_cost:,.2f}")
```

## What Good Pass Quality Looks Like

| Metric | Target | Concern |
|--------|--------|---------|
| Pass accuracy | ≥ 60% correct | Below 50% means you're passing too many good opportunities |
| Avg opportunity cost per wrong pass | < $100 | Higher means you need to trust your edge more |
| Pass rate among 4–8pp edge markets | 30–50% | Very high means excessive risk aversion |

## Learning Loop

If wrong-pass rate > 40%:
→ You're too conservative — trust your research more, or lower the edge threshold
If wrong-pass rate < 20%:
→ You're making good passes — this is fine, keep discipline

## Pass Reasons to Review

Passes filed as "insufficient research" should be prioritized for the next `/research` cycle
if the market is still open and the question is still live.
