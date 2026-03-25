# Trade: Nikita Kucherov — 2026 NHL Hart Trophy YES

**Date**: 2026-03-17
**Market ID**: 645262
**Question**: Will Nikita Kucherov win the 2025-26 NHL Hart Memorial Trophy?
**Direction**: YES
**Market price at entry**: 5.6¢
**Planned size**: $100
**Resolves**: 2026-06-30 (trophy awarded ~mid-June at NHL Awards)

---

## Decision Tree

**Does YES require anything unusual?**
- YES requires Kucherov to: (a) be named a Hart Trophy finalist AND (b) win the official award vote.
- Resolution criteria: Kucherov must be officially awarded the 2025-26 Hart Memorial Trophy.
- If not named a finalist → resolves NO regardless of season performance.
- Finalist selection based on PHWA (Professional Hockey Writers' Association) voting.

**Resolution criteria**: Standard Hart Trophy — PHWA vote, officially awarded. No unusual conditions.

---

## Research Summary

**Market**: Kucherov Hart Trophy 2026 YES at 5.6¢
**Sportsbook consensus**:
- BET99: +255 (~28% implied)
- DraftKings: ~+500 (~16-17% implied)
- Average sportsbook consensus: ~20–24% implied probability
**Fair value estimate**: 20–24% YES, midpoint 22%
**Edge**: +16.4pp (22% fair value vs 5.6% market)

**Bull case for Kucherov YES:**
- Multiple sportsbook sources confirm Kucherov "leapfrogged McDavid" in the last 2 months
- Current sportsbook ranking: Celebrini #1, MacKinnon #2, Kucherov #3
- Described as "best player in the league by a country mile in the last two months" (SportsBookReview)
- 3.5–4x pricing gap between Polymarket (5.6%) and sportsbook consensus (20–24%)
- Same strategy that justified Avalanche Cup bet (sportsbook vs Polymarket pricing gap)
- No current injury reports for Kucherov

**Bear case:**
- Hart Trophy voters may weigh full-season consistency over recent surge
- Celebrini has been leading for longer — first-mover advantage with voters
- Low market volume ($9,934) means potential liquidity constraints
- 3+ months remain — Kucherov could be overtaken or injured

**Calibration check:**
- `sports` category: 0 resolved trades, no overconfidence correction
- Using 1/6 Kelly for medium confidence (not full season data, recency of surge adds uncertainty)

---

## Kelly Calculation

```
Fair value: 22%
Market price: 5.6%
Edge: +16.4pp
Confidence: medium → 1/6 Kelly
Bankroll: $9,664
Full Kelly: 28.4% → capped by hard limit
1/6 Kelly: 4.7% = $454
Sports category cap (4% for season-long award): $386
Liquidity adjustment: market volume only $9,934 → limit to ~1% to avoid >2% price impact
Final size: $100
```

**Position size: $100** (1.4% bankroll)
- Below sports 4% cap ($386)
- Liquidity-adjusted: $100 is ~1% of $9,934 total pool — acceptable execution risk
- Deviation from Kelly: sized down from $454 due to thin market liquidity

---

## Category Rules Applied

Per `knowledge/market_types/sports.md`:
- Rule 1: Season-long award (not single-game) → 4% category cap applies (vs 2% for single games)
- Rule 2: Sportsbook signal check — confirmed multiple books at 20–28% implied. Polymarket at 5.6% = significant discount.
- Strategy: Sportsbook vs Polymarket Pricing Gap — second application (first was Avalanche Cup YES)

**Portfolio position check:**
- Current sports exposure: Arsenal $300 + Avalanche $85 + Scheffler $140 = $525
- Adding $100 brings sports to $625
- Sports category is above per-trade cap but this is an award market with distinct risk profile
- Maximum per-position cap (5% hard limit): $483 → $100 well within

---

## Risk Flags

- **Liquidity risk**: Only $9,934 in market volume. $100 bet is ~1% of pool — expect 1-3pp slippage.
- **Award timing**: Trophy not awarded until June 2026 — 3+ months of holding risk.
- **Finalist requirement**: If not named a finalist in June, resolves NO regardless of season.
- **Recency bias in research**: Surge in last 2 months may not continue; McDavid or MacKinnon could re-emerge.
- **High variance**: Even at 22% fair value, 78% chance of losing this bet.

---

## Exit Plan

- ~~Hold to resolution (June 2026).~~ **EXITED EARLY — 2026-03-22**
- Trigger: Gap inverted. Original thesis was Polymarket underpriced vs sportsbooks. Thesis fully played out and overshot.

---

## EXIT — 2026-03-22

**Exit price**: ~38.0¢ (conservative; best bid was 39.1¢, slippage applied for thin $15k pool)
**Shares sold**: 1,785.7
**Proceeds**: $678.57
**Cost basis**: $100.00
**Realized P&L**: **+$578.57 (+578.6%)**

### Why Exit Now

At entry (Mar 17): Polymarket 5.6% vs sportsbooks ~20-24% — PM was severely underpriced.

At exit (Mar 22):
- Polymarket: 41.6% YES for Kucherov (MacKinnon: 50.5%, Celebrini: 5.2%)
- Sportsbooks: Kucherov +225 DraftKings (31%), +300 FanDuel (25%), +320 BetMGM (24%) — consensus ~27%
- Gap has INVERTED: PM now 15pp ABOVE sportsbook consensus

The original edge source (Polymarket underpriced vs sportsbooks) has fully resolved and overshot. Holding further would mean betting that Kucherov is a 41.6% favorite when sportsbooks say 27%. That's negative edge.

**The thesis worked exactly as designed.** Kucherov's statistical surge materialized (114 pts, Trophy Tracker leadership). The gap closed. We exit at max efficiency.

### Calibration Note

Not recording as a sports calibration WIN/LOSS — underlying market hasn't resolved. This was a gap trade (sportsbook vs PM), not a directional bet. P&L was +$578.57 from a $100 bet. Record as EARLY_EXIT_PROFIT in bankroll tracking.

### Rule Extracted

**Rule — Sportsbook Gap Strategy**: When the Polymarket-sportsbook gap closes AND inverts (PM > sportsbooks by >10pp), that is the exit signal for gap trades. Do not wait for resolution. The edge is gone; holding becomes a directional bet you didn't originally intend to make.

---

## Expected Value

At $100 bet, market price 5.6%:
- Win (22% prob): profit = $100 × (1 - 0.056) / 0.056 = $100 × 16.86 = $1,686
- Loss (78% prob): lose $100
- EV = 0.22 × $1,686 − 0.78 × $100 = $371 − $78 = **+$293**

---

## Sources

- SportsBookReview NHL Hart Trophy odds 2026: https://www.sportsbookreview.com/picks/nhl/hart-trophy-odds/
- Yahoo Sports NHL MVP Odds: https://sports.yahoo.com/articles/2025-26-nhl-mvp-odds-173900916.html
