---
name: rules-compliance-checker
description: Pre-trade checklist that cites specific Golden Rules for every bet decision, preventing entry when rules are violated
type: tool
performance:
  uses: 0
  wins_contributed: 0
  losses_contributed: 0
  status: ACTIVE
---

# Rules Compliance Checker

**Hard prerequisite before any trade entry**: Explicitly cite and verify each applicable Golden Rule. A trade that cannot pass this checklist is a PASS, not a BET.

## Required Pre-Trade Checklist

Run through every item. State explicitly: PASS or FAIL.

1. **Rule 1 — All options enumerated?**
   - List every possible outcome for this market before forming a view
   - FAIL = entering without checking if there's a better-priced alternative outcome

2. **Rule 2 — Resolution criteria read?**
   - Quote the exact resolution text, not just the title
   - FAIL = any ambiguity in how the market resolves

3. **Rule 3 — Calibration checked?**
   - Run `python3 scripts/calibration.py --category <cat>`
   - FAIL = category on probation (oscars, other) and edge < 8pp

4. **Rule 4 — Settlement vs intraday confirmed?** (commodities/price markets only)
   - Confirm whether market uses settlement price, closing price, or intraday high/low
   - FAIL = uncertainty about price mechanism

5. **Rule 5 — Edge ≥ 4pp?** (8pp if category on probation or 3+ consecutive losses)
   - State fair value, market price, and edge explicitly
   - FAIL = edge below threshold

6. **Rule 6 — Correlated exposure checked?**
   - Check total bankroll exposure to same macro scenario
   - FAIL = adding to same macro scenario when already at 10%+ exposure

7. **Rule 7 — Price ≤ 97%?**
   - FAIL = market price 97%+ in either direction

8. **Rule 8 — Category cap respected?**
   - politics 3% | awards 2% | single-game sports 2% | commodities 4%
   - Check current category exposure in positions.json
   - FAIL = would exceed cap

9. **Rule 9 — Kelly sizing applied?**
   - High confidence → 1/4K | Medium → 1/6K | Low → 1/10K
   - State Kelly calculation explicitly
   - FAIL = sizing above Kelly output

10. **Rule 11 — Status quo bias applied?** (for "will X change?" markets)
    - Default prior: 70% probability status quo holds
    - FAIL = not accounting for status quo bias in fair value estimate

## Output Format

```
RULES COMPLIANCE CHECK — [Market Name]
=====================================
Rule 1 (All options): PASS — checked [N] outcomes: [list]
Rule 2 (Resolution text): PASS — resolves if: "[exact text]"
Rule 3 (Calibration): PASS — [category] unrestricted / FAIL — 8pp min required
Rule 4 (Settlement): N/A or PASS/FAIL
Rule 5 (Edge): PASS — fair value [X]%, market [Y]%, edge [Z]pp ✓
Rule 6 (Correlation): PASS — [macro scenario] at [%]% total exposure
Rule 7 (Price cap): PASS — market at [X]%, well below 97%
Rule 8 (Category cap): PASS — [category] at [current $] / [cap $], adding [$] = [new %]%
Rule 9 (Kelly size): PASS — Kelly = [$X], sizing at [$Y] ([1/N]K)
Rule 11 (Status quo): PASS/N/A — [reasoning]

VERDICT: BET $[amount] / PASS
```

## Application

This checker must run on every trade, even when confidence is high. The root cause of both confirmed losses (Oscars −$200, Musk tweets −$150) was that existing rules were not cited at the decision point. The rules existed — they just weren't applied.

**Never skip this checklist because a trade "feels obvious."** Obvious trades are where overconfidence lives.
