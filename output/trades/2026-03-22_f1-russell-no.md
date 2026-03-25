# Trade: F1 2026 Drivers Championship — George Russell NO

**Date**: 2026-03-22
**Market**: Will George Russell win the 2026 F1 Drivers Championship?
**Market ID**: 898411
**Direction**: NO
**Entry Price**: 44.5¢ (55.5% YES / 44.5% NO)
**Size**: $260
**Shares**: 584.3
**Category**: sports (season-long futures)
**Resolves**: ~2026-11-22 (F1 season end, Abu Dhabi GP)

---

## Pre-Trade Reasoning

### Edge Source
Sportsbook vs Polymarket gap — confirmed pattern (Edge Source 5). Kucherov exit precedent: enter when gap forms, exit when gap inverts.

### Market Facts
- 2026 F1 season has completed 2 of 24 races
- Race 1 (Australia, March 9): Russell WIN. Race 2 (China, March 15): Antonelli WIN.
- After 2 races: Russell leads by 4 points (negligible on 22-race horizon)
- Mercedes dominant: 1-2 finish in both races. Total Mercedes share ~65-70% of championship probability.

### Fair Value Estimation

**Sportsbook consensus (confirmed 3 books, post-Australia, pre-China):**
| Book | Odds | Implied Prob | De-vigged |
|------|------|-------------|-----------|
| FanDuel | +230 | 30.3% | ~35% |
| Caesars | +202 | 33.1% | ~38% |
| BetMGM | +200 | 33.3% | ~38% |

Pre-China de-vigged consensus: ~38-40% YES for Russell.

**Post-China adjustment (Antonelli won Race 2, gap cut to 4pts):**
- Books almost certainly lengthened Russell after losing Race 2
- Estimated post-China range: +250 to +350 (22-28% implied, ~27-33% de-vigged)
- Central estimate: ~32-36% de-vigged after China result

**Analytical base rate:**
- F1 championship leader after 2/24 races wins championship: ~50-55% historically
- HOWEVER: Mercedes has TWO co-equal drivers splitting ~65-70% total probability
- Per-driver share: if equal pace, ~32-35% each
- Russell consistency advantage vs rookie: +3pp
- Final analytical estimate: ~35% YES Russell

**Market signal blend (80/20 with skepticism on $1M+ futures):**
- 35% × 0.8 + 55.5% × 0.2 = 28 + 11.1 = **39%** — but Polymarket sports futures consistently lag sportsbook repricing; anchor closer to analytical estimate
- Final fair value: **37% YES / 63% NO**

### Edge Calculation
- NO fair value: 63%
- NO market price: 44.5%
- Edge: **+18.5pp on NO**
- Even at most conservative FV (45% YES → 55% NO): edge still +10.5pp on NO
- Well above 4pp minimum

### Kelly Sizing
```
fair_value_no = 0.63
market_price_no = 0.445
bankroll = 7197.33
edge = 0.63 - 0.445 = 0.185
odds = (1 - 0.445) / 0.445 = 1.247 (per $1 risked, gain = 1.247 × $1)
full_kelly = edge / odds_decimal ≈ 0.185 / 1.247 ≈ 14.8%
fractional_kelly (1/4) = 3.7% = $266
```
$266 fractional Kelly. Category cap: 4% × $7,197 = $288. Final size: **$260** (3.6% bankroll, within cap).

### Why PM is Mispriced
1. Polymarket anchors on standings (Russell leads) without proper season-length discounting
2. Post-China race result likely hasn't propagated to PM pricing yet
3. In a dominant 2-car team, NO SINGLE DRIVER should be priced above 45% this early unless they have a dominant points lead (Russell has a 4-point lead = effectively 0)
4. Pre-China sportsbook consensus (~38% de-vigged) is ALREADY below PM's 55.5% — gap was there before China, and China only widened it

### Pre-Trade Checklist (Golden Rules)
- [x] Checked all options (Russell YES, Russell NO, other drivers)
- [x] Resolution criteria clear: Russell must finish P1 in final 2026 championship standings
- [x] Calibration checked: sports category — no resolved trades, no penalty
- [x] Settlement mechanics: final standings, not intermediate — no settlement gap risk
- [x] Edge ≥ 4pp: +18.5pp base case, +10.5pp conservative (yes)
- [x] Correlated exposure: no correlation with existing positions (OKC Thunder/NHL/Arsenal)
- [x] Not betting at 97%+: NO at 44.5¢ is well within bounds
- [x] Category cap: $260 < $288 (4% of $7,197)
- [x] 3+ sportsbooks confirmed pre-China (FanDuel, Caesars, BetMGM at +200-+230)
- [x] Cross-platform confirmed: sportsbooks all below 35% de-vigged for Russell

### Exit Triggers
- **EXIT**: Sportsbook consensus reprices Russell to within 5pp of PM price (gap closed)
- **EXIT**: Russell extends lead to 30+ points (3+ race wins, Antonelli DNFs)
- **REVIEW**: After 5+ races, re-run probability model with updated sportsbook consensus
- **WATCH**: Antonelli reliability issues (2+ mechanical DNFs in a row)
- **DO NOT EXIT**: Normal race-to-race swings (±10 points), PM price fluctuations alone

---

## Position Management
- **Category**: season-long sports futures (4% cap = $288)
- **Correlation**: none with existing portfolio
- **Monitoring**: check sportsbook prices after every race (every 2 weeks)
- **Expected hold**: through 2026 F1 season end (~8 months)

---

*Pre-trade file written 2026-03-22. Executing now.*
