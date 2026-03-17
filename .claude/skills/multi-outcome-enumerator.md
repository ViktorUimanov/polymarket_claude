---
name: multi-outcome-enumerator
description: Forces enumeration of all market outcomes in multi-outcome markets with independent fair-value assignment before comparing to prices. Prevents anchoring on favorites and missing dark horses.
performance:
  uses: 0
  wins_contributed: 0
  losses_contributed: 0
  status: ACTIVE
  type: tool
---

# Multi-Outcome Enumerator

Use this skill BEFORE researching any multi-outcome market (awards, elections with 3+ candidates, tournament winner markets, etc.).

## The Problem It Solves

The Oscars 2026 loss occurred because we anchored on "Sinners" as the favorite and never ran a complete enumeration of nominees. Bugonia (a Lanthimos auteur film) was available at 2% and won. We never looked.

This skill FORCES you to build a probability table for every outcome before doing deep research on any one of them.

## When to Use

- **Awards markets**: Best Picture, Best Actor/Actress, Grammy Album of Year, etc.
- **Tournament winner markets**: Stanley Cup, EPL title, March Madness champion, etc.
- **Election markets with 3+ candidates**
- **Any market where there are more than 2 mutually exclusive outcomes**

## How to Run

### Step 1: List ALL outcomes

For an awards market, fetch the market data and find the complete list of nominees/candidates:
```bash
python3 scripts/fetch_markets.py --search "<market question>" --limit 1
# Check the 'outcomes' field for all options
```

If the market data doesn't list all candidates, do a web search:
```
WebSearch("<award year> nominees complete list")
```

### Step 2: Build the probability table

For EACH candidate, assign a fair value probability INDEPENDENTLY before looking at market prices:

| Candidate | Base Rate | Guild Signals | Recent Momentum | My Fair Value | Market Price | Edge |
|-----------|-----------|---------------|-----------------|---------------|--------------|------|

**Rules for the table:**
- The sum of all fair values must be ≤ 100% (market prices might sum to more due to bid/ask spread)
- No candidate gets 0% — use a floor based on category rules:
  - Awards: minimum 1% for any official nominee (Oscars lesson: dark horses have real probability)
  - Auteur director films: minimum 5% floor regardless of market price
  - Leading candidates: do NOT cap at 80% even if strong favorite (lock risk is real)
- Assign "other/field" as a catch-all if some candidates are unlisted

### Step 3: Compare to market prices

After completing the table, check where YOUR fair value diverges from market price by more than 4pp. Those divergences are your candidates for research.

### Step 4: RED FLAGS

Stop and re-examine if:
- Any candidate is priced below 5% in the market but you assigned > 8% fair value (dark horse)
- Any candidate is priced above 70% (favorite lock risk — has this winner swept ALL predictors?)
- Your probability table doesn't sum to ~100% (you're missing something)

## Example Output (Oscars Best Picture)

Before the 2026 Oscars, we SHOULD have run:

| Film | Director Type | Guild Signals | My Fair Value | Market | Edge |
|------|--------------|---------------|---------------|--------|------|
| Sinners | Commercial | SAG Ensemble | 45-55% | 65% | -10 to -20pp (OVERPRICED) |
| Bugonia | Lanthimos auteur | No guild sweep | 8-12% | 2% | +6 to +10pp (BET NO on Sinners, maybe YES on Bugonia) |
| [Others] | Various | — | 35-45% shared | — | — |

Had we run this table, we would have:
1. Identified that Sinners at 65% was likely overpriced (SAG Ensemble → 45-55%)
2. Assigned Bugonia a 8-12% floor as a Lanthimos auteur film
3. Avoided the $200 loss

## Integration with Other Skills

- Run this BEFORE `/research` on any specific candidate
- After enumeration, use `/research` for deep-dive on the 1-2 best candidates
- Reference `knowledge/market_types/oscars.md` for awards-specific base rates and floors

## Tracking

After each use, note:
- Did enumeration find a dark horse we would have missed? (add to wins_contributed)
- Did we skip enumeration and later discover a dark horse? (add to losses_contributed)
