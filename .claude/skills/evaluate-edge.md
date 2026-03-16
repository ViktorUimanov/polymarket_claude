---
name: evaluate-edge
description: Framework for estimating fair probability and calculating edge vs market price on Polymarket markets
type: tool
performance:
  uses: 0
  wins_contributed: 0
  losses_contributed: 0
  status: ACTIVE
  last_reviewed: 2026-03-16
---

# Evaluate Edge Skill

## The Core Discipline

Form your probability estimate BEFORE looking at the market price.
Then compare. The gap is your edge (or your error).

## Step-by-Step Estimation

### 1. Base Rate
What is the historical frequency of this type of outcome?

| Category | Where to Find Base Rates |
|----------|------------------------|
| Sports | Head-to-head records, ELO ratings, current form, injuries |
| Elections | Historical incumbency rates, polling aggregators (538, Metaculus) |
| Commodities | Price history, analyst forecasts, seasonal patterns |
| Awards (Oscars) | Guild awards track record by category |
| Crypto | Historical price patterns, on-chain data |

### 2. Evidence Updates (Bayesian)

Apply incremental updates to base rate:

| Signal Strength | Update |
|----------------|--------|
| Very strong (direct data, high reliability) | ±15–25pp |
| Strong (expert consensus, multiple sources) | ±8–15pp |
| Moderate (single credible source) | ±3–8pp |
| Weak / ambiguous | ±1–3pp |
| Noise (unverifiable, contradictory) | 0pp |

### 3. Market Signal Blend

For liquid markets (volume > $50k):
```
adjusted_estimate = your_estimate × 0.75 + market_price × 0.25
```

For thin markets (volume < $10k):
```
adjusted_estimate = your_estimate × 0.95 + market_price × 0.05
```

Rationale: Liquid markets aggregate many informed opinions. Thin markets may be mispriced.

### 4. Category Uncertainty Penalty

Widen your confidence interval based on category volatility:

| Category | CI Width | Max Position |
|----------|----------|-------------|
| Awards (Oscars, BAFTAs) | +15pp wider | 2% bankroll max |
| Single-game sports | +10pp wider | 3% bankroll max |
| Politics / elections | +12pp wider | 3% bankroll max |
| Multi-game standings | +5pp wider | 4% bankroll max |
| Commodities (settlement) | +8pp wider | 4% bankroll max |
| Near-certainty (>95%) | irrelevant — skip | N/A |

### 5. Calibration Correction

```bash
python3 /root/workspace/polymarket/scripts/calibration.py --category <category>
```

Apply correction based on calibration error:
- Overconfident (negative error): shift estimates toward 50%
- Underconfident (positive error): slight confidence increase OK

### 6. Final Output

```
Base rate: X%
Evidence adjustments: +Ypp (source) / -Zpp (source)
Market blend: adjusted to X%
Uncertainty range: [low%, high%]
Calibration correction: ±Npp
Final estimate: X% (90% CI: low–high%)
Edge vs market: +/-Npp on YES/NO
```

## Edge Decision Table

| Edge (pp) | Confidence | Action |
|-----------|-----------|--------|
| < 4 | any | PASS |
| 4–7 | low | PASS |
| 4–7 | medium | BET small (0.5–1%) |
| 4–7 | high | BET medium (1–2%) |
| 8–15 | medium | BET medium (1.5–3%) |
| 8–15 | high | BET large (3–5%) |
| > 15 | any | SANITY CHECK then BET |

## Red Flags — PASS Regardless of Edge

- Cannot explain edge in one sentence
- Resolution criteria ambiguous
- Category has 3+ consecutive losses (require +8pp minimum)
- Market resolves within 6 hours and full research not done
- "It just feels right" — no systematic basis
- Haven't checked `knowledge/market_types/<category>.md` yet
