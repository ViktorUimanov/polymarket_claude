---
name: size-position
description: Kelly criterion position sizing for binary Polymarket bets with practical adjustments for model uncertainty
type: tool
performance:
  uses: 0
  wins_contributed: 0
  losses_contributed: 0
  status: ACTIVE
  last_reviewed: 2026-03-16
---

# Position Sizing Skill

## Quick: Use the Script

```bash
python3 /root/workspace/polymarket/scripts/kelly.py \
  --fair-value 55 \
  --market-price 40 \
  --confidence medium \
  --bankroll $(python3 /root/workspace/polymarket/scripts/portfolio.py --bankroll-only)
```

## Kelly Formula (Reference)

For a binary YES bet at market price `p_market`:

```
b = (1 / p_market) - 1         # net profit per dollar risked
f* = (b × p_fair - (1 - p_fair)) / b    # full Kelly fraction
```

**Always use fractional Kelly** — never bet full Kelly with model uncertainty:

| Confidence Level | Kelly Fraction |
|----------------|---------------|
| High | 1/4 Kelly |
| Medium | 1/6 Kelly |
| Low | 1/10 Kelly |

## Hard Caps

- **Max single bet**: 5% of bankroll (regardless of Kelly)
- **Max category exposure**: 15% of bankroll (all open positions in one category combined)
- **Bankroll < $5,000**: max single bet 3%
- **Losing streak** (3+ consecutive losses): max single bet 2% until streak ends

## Worked Example

Market price: 40% YES | Your estimate: 55% YES | Confidence: medium | Bankroll: $9,500

```
b = (1/0.40) - 1 = 1.5
f* = (1.5 × 0.55 - 0.45) / 1.5 = 0.375 / 1.5 = 25% (full Kelly)
1/6 Kelly = 25% / 6 = 4.2% = $399
Cap at 5% = $475
Recommended: $400 (round to nearest $50)
EV = 0.55 × (1.5 × $400) - 0.45 × $400 = $330 - $180 = +$150
```

## Mental Shortcuts

| Scenario | Typical Size |
|----------|-------------|
| Edge < 4pp | PASS (Kelly ≈ 0) |
| Edge 5–7pp, medium confidence | 0.5–1% ($50–$100 on $10k) |
| Edge 8–12pp, medium confidence | 1–2% ($100–$200) |
| Edge 12–20pp, high confidence | 2–4% ($200–$400) |
| Edge > 20pp, high confidence | 4–5% ($400–$500) |

## Category Exposure Check

Before placing any bet:
```bash
python3 /root/workspace/polymarket/scripts/portfolio.py --full
```

Sum current open positions in the same category. If adding this bet would exceed 15% total exposure in that category: reduce size or skip.

## After Sizing: Sanity Check

1. If recommended size > $300: re-read the research one more time
2. If recommended size > $400: explicitly list the 3 scenarios where you lose and their probability
3. If Kelly recommends > 5%: something is wrong with your edge estimate — double-check
