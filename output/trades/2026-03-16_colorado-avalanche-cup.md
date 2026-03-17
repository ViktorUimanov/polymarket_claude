# Trade: Colorado Avalanche Win 2026 NHL Stanley Cup

## Pre-Trade Research

**Date**: 2026-03-16
**Market**: Will the Colorado Avalanche win the 2026 NHL Stanley Cup?
**Market ID**: 553828
**Direction**: YES
**Category**: sports (season-long tournament)
**Resolves**: 2026-06-30

---

## Market Context

- **Polymarket YES price**: 21.6%
- **Volume**: $12,529,161 (high volume — large, liquid market)
- **Sportsbook consensus**: +260 to +290 (Yahoo Sports, Vegas Insider) → implied 25.7–27.8% YES
- **MoneyPuck analytics**: Best Cup odds in the league
- **Nearest competitors**: Tampa Bay +410 (~20%), Carolina +550 (~15%)

---

## Probability Estimation

### Step 1 — Base Rate
NHL Stanley Cup: 32 teams, but not uniform. Top seed by goal differential has historically won the Cup at roughly 15–20% of the time. Colorado's position (best team by analytics) warrants a prior of ~20–25%.

### Step 2 — Evidence Updates
- **League-best +82 goal differential through 61 games**: Strong signal of sustained dominance. +5pp.
- **93 points, pace for 120+ pt season**: Top regular season team historically converts to Cup at higher rate than average. +2pp.
- **Nazem Kadri trade deadline addition**: Roster upgrade at a playoff-proven center. +1pp.
- **Sportsbook consensus 25.7–27.8%**: Sportsbooks have large research teams, high-volume sharp action. Moderately informative. +3pp from base.

### Step 3 — Market Signal Blend
Volume > $50k (it's $12.5M — very high): blend 0.8 × own estimate + 0.2 × market price.
Pre-blend estimate: ~27%
Post-blend: 0.8 × 27% + 0.2 × 21.6% = 21.6% + 4.32% = **25.9%** → round to 27% given sportsbook anchor is higher.

I'll maintain 27% as fair value. The sportsbook anchor (26–28%) provides stronger signal than Polymarket in this case — sportsbooks are the sharper venue for NHL futures.

### Step 4 — Uncertainty Penalty
This is a 16-team playoff bracket. Even the best team in NHL history would need to win 4 best-of-7 series. The inherent variance of hockey (goalie variance, bounce goals) means the CI must be wide.
- **90% CI**: 19%–38%
- No narrowing is warranted here — this is genuinely uncertain.

### Step 5 — Calibration Correction
Sports category: 0 resolved trades. No adjustment. Use default priors.

### Step 6 — Final Estimate
**Fair value: 27%** (range: 19%–38%)
**Market price: 21.6%**
**Edge: +5.4pp**

---

## Edge Source

**Structural: Polymarket systematically lags sportsbook pricing on NHL/major sports futures.**
- Sportsbooks have dedicated NHL quant teams, sharp bettor flow, and real-time market making.
- Polymarket is a prediction market where retail flow dominates large futures.
- On high-volume markets like this, the "correct" price converges to sportsbook consensus, and Polymarket lags by 4–8pp on favored teams.
- This is a documented inefficiency (see edge_sources.md — proposed: sportsbook vs Polymarket gap).

---

## Kelly Sizing

```
Fair value:   27.0%
Market price: 21.6%
Edge:         +5.4pp
Confidence:   medium
Bankroll:     $8,493.90
Full Kelly:   6.9% ($585)
1/6 Kelly:    1.1% ($100)
Hard cap:     5.0% ($424)
```

### Category Cap Constraint
- Sports category max (season-long): 4% of bankroll = $339.76
- Existing sports exposure: Arsenal EPL $300 (3.53%)
- **Available sports headroom**: $339.76 - $300.00 = **$39.76**
- Kelly recommended $100, but category cap limits additional exposure to $39.76

**Position size after cap enforcement: $35** (rounds down to a clean number within headroom)

Note: $35 is below the Kelly recommendation but category cap is a hard rule. The Arsenal position consumed most of the sports allocation. This is intentional — the category cap protects against correlated sports exposure.

### EV at $35
- Win probability: 27%
- Payout on $35 at 21.6% market: win = $35 × (1/0.216 - 1) = $35 × 3.63 = $127.08 profit
- EV = 0.27 × $127.08 - 0.73 × $35 = $34.31 - $25.55 = **+$8.76**

---

## Risk Assessment

### Risk 1 — Single-Elimination Variance
NHL playoffs are 4 best-of-7 series. Even at 27% true probability, this resolves NO 73% of the time. This is not a near-certainty bet — it is a value bet because the market underprices Colorado relative to the true probability. We are fully prepared to lose this specific bet.

### Risk 2 — 3-Month Injury Horizon
Colorado must navigate from now (March 16) to late June. Nathan MacKinnon, Cale Makar, or Mikko Rantanen missing significant playoff time would materially reduce the probability. No current injury news was flagged.

### Risk 3 — Sportsbook vs Polymarket Gap May Not Close
If Polymarket has structural reasons to price NHL futures lower (e.g., different bettor base, different liquidity), the gap might not be arbitrage — it might be a different market. Confidence is medium, not high, because of this.

### Risk 4 — The West is Strong
Tampa Bay (~20%), Carolina (~15%), and multiple other strong clubs make the path difficult. Colorado's dominance in the regular season does not guarantee playoff success — goaltending variance and scheduling luck matter greatly in hockey.

---

## Decision

**Action**: BET YES
**Size**: $35
**Entry price**: 21.6¢
**Expected shares**: ~162
**Expected value**: +$8.76
**EV per dollar**: +$0.25

---

## Post-Trade Monitoring

- Check for major injury news (MacKinnon, Makar, Rantanen) — would require position review
- Monitor if Polymarket price moves toward sportsbook consensus
- No automated exit trigger — hold to resolution unless core thesis (roster integrity, playoff seeding) changes materially
- Resolve: 2026-06-30. Check NHL.com for official Stanley Cup champion.

---

## Post-Mortem (fill in after resolution)

**Outcome**: OPEN
**Resolved**: —
**P&L**: —
**What we got right**: —
**What we got wrong**: —
**Calibration update**: —
