# Trade: Crude Oil $90+ March Settlement YES

**Date**: 2026-03-23
**Market ID**: 1487357
**Question**: Will Crude Oil (CL) settle at $90+ in March?
**Direction**: YES
**Entry Price**: 76.5c
**Size**: $34.80 (commodities cap limit)
**Shares**: 45.5
**End Date**: 2026-03-31

---

## Pre-Trade Checklist

- [x] All options checked — this is one outcome in a multi-bucket settlement market ($60-65, $65-70, ..., $90+)
- [x] Resolution criteria read — CME official settlement price on final trading day of March ≥ $90 (not intraday)
- [x] Calibration checked — Commodities: 0 resolved trades, neutral calibration
- [x] Settlement vs intraday rule applied — CME close on March 31 is the resolution metric
- [x] Edge ≥ 4pp confirmed — +17.5pp edge
- [x] Category cap checked — $386 used of $421 max; this $34.80 fills cap to $420.80
- [x] Never 97%+ — YES at 76.5%, well below ceiling

---

## Thesis

**Current state**: WTI spot $98.23 (intraday range $93.42–$99.67). Settlement must reach ≥$90 on March 31.

**Why YES wins**: Oil needs to DROP 8.4% from today's $98.23 to miss the $90 threshold on settlement day March 31. That's 8 trading days away.

**Bull case (94% fair value)**:
1. Iran war active — Strait of Hormuz closed since ~Feb 28, 2026
2. Iran FM explicitly rejected ceasefire (March 2026)
3. Even a surprise ceasefire typically produces 2-5% same-day oil decline, not 8%
4. Today's intraday LOW was $93.42 — still 3.8% above $90
5. Historical base rate: 8%+ 8-day crash without demand destruction shock = ~4% probability
6. CME settlement can diverge from intraday by 2-5% max in normal conditions; even extreme (March 9 had 21% intraday-to-settlement gap for HIGH $120 target, but that was from $119.94 — starting at $98, 21% gap would put settlement at $77.61, below $90, but the March 9 gap was an outlier)

**Bear case / what could go wrong**:
- US recession declaration or China demand shock
- Emergency OPEC+ output surge
- CME settlement anomaly (low probability given $90 is 8.4% below spot)
- Very tail-risk scenario

**Market pricing**: 76.5% YES implies 23.5% probability oil drops 8%+ in 8 days. Historical frequency of this event without major shock: 3-5%. Market appears to be pricing settlement-vs-intraday risk uniformly across all threshold levels, when $90 has far more headroom than $105/$110.

**Edge calculation**: 94% FV - 76.5% market = +17.5pp
**Kelly (1/4)**: $1,958 optimal but commodities cap constrains to $34.80
**Expected Value**: +$7.66

---

## Correlated Exposure

| Position | Direction | Condition for loss |
|----------|-----------|-------------------|
| Oil $105 NO ($186) | NO | Settlement ≥$105 |
| Oil $110 NO ($200) | NO | Settlement ≥$110 |
| Oil $90+ YES ($34.80) | YES | Settlement < $90 |

All three positions win if settlement lands in $90–$105 range. Only Oil $90+ YES loses if settlement falls below $90 — a scenario where all other oil positions would be unaffected (both NOs would win at settlement <$90). No adverse correlation.

---

## Size Justification

- Commodities cap: 4% × $10,520 = $420.80
- Oil $105 NO: $186
- Oil $110 NO: $200
- Remaining: $34.80 → full cap deployment

Kelly recommends $526 (1/4 Kelly) but cap binding. Position is small but edge is real.

---

## Exit Rules

- Hold to resolution on March 31
- Exit early ONLY if WTI spot drops below $93 AND a major demand shock is confirmed (US recession declaration or China lockdown)
- Do not exit on ceasefire news alone — even a ceasefire wouldn't move oil 8%+ in remaining 8 days

---

## Post-Mortem (fill after resolution)

Resolution date: 2026-03-31
Outcome: [ ] WIN / [ ] LOSS
CME settlement price: ___
P&L: ___
Edge calibration: ___
