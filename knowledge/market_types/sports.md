# Sports Markets — Knowledge Base

## Category Profile

| Attribute | Value |
|-----------|-------|
| Variance level | MEDIUM (season-long) to HIGH (single game) |
| Calibration status | No data yet |
| Max position size | 4% bankroll (season-long) / 3% (single game) |
| Min edge required | 4pp standard |
| Active positions | 1 (Arsenal EPL) |

---

## Rules (Apply Before Every Sports Bet)

### Rule 1 — Distinguish Season-Long vs Single-Game Risk
**Rule**: Season-long markets (EPL winner, NBA champion) have much lower variance than single-game markets. Apply different max position sizes accordingly.
- Season-long with large lead: up to 4% bankroll
- Single playoff game: max 2–3% bankroll (anything can happen in 90 minutes)
- Championship match: max 2% (neutral venue, motivation even)

### Rule 2 — Calculate Mathematical Elimination Probability
**Rule**: Before betting on a team to win a league, do the full math:
- What points does the leader need from remaining games?
- What perfect record would the chaser need?
- Is there a scenario where the chaser can win?
- Weight that scenario by its probability.

**Template**:
```
Leader: {X} pts from {N} games ({M} remaining)
Expected: {base rate} pts from {M} games → final {total}
Chaser: {Y} pts from {N} games ({M+1} remaining)
Maximum possible: {Y + 3*(M+1)} pts
For chaser to win: needs {A} pts AND leader needs ≤ {B} pts
Probability of both: {calc}%
```

### Rule 3 — Champions League / Cup Competition Distraction Risk
**Rule**: When a team is deep in cup/CL competition alongside a league title race, factor in fatigue and squad rotation risk. Adjust probability -2 to -5pp depending on schedule congestion.
**Apply when**: Team has CL knockout rounds or domestic cup final within 2 weeks.

### Rule 4 — Form Window for Single-Game Markets
**Rule**: For single-game markets, use last 5 games (not season average) as primary form indicator. Recent form matters more than season-long stats for one-off games.

### Rule 5 — Injury News Before Betting
**Rule**: Always check injury news within 24 hours of any single-game bet. A key player absence can shift probability by 5–10pp.
**Sources**: Official club injury reports, reputable football journalists (Sky Sports, BBC Sport, L'Équipe)

### Rule 6 — Golf Tournament Winner Markets: Use Sportsbook Consensus as Primary Reference
**Date learned**: 2026-03-17 (from Scheffler Masters YES trade — trade file: `output/trades/2026-03-17_scheffler-masters-yes.md`)
**Rule**: For golf tournament winner markets, Polymarket prices are frequently stale relative to sportsbook consensus. Use 3+ major sportsbooks (BetMGM, FanDuel, DraftKings) as the primary reference for fair value. If Polymarket is below the lowest sportsbook implied probability, the edge is on YES.
**Why**: Golf tournament markets are high-field (80+ players), high-variance events where casual bettors on Polymarket anchor on round numbers or known brand names. Sportsbooks with dedicated golf quant teams converge faster on updated player odds.
**Apply when**: Any golf major or PGA Tour event. Cap size at 2% (single-event high-variance rule). Fair value = midpoint of the 3-book sportsbook range. Edge threshold: 5pp minimum for high-variance single-event markets.
**Specific rule**: World #1 with 4+ consecutive top-10 finishes at a specific major venue is a material signal (track-specific consistency). Model separately from pure world ranking.

### Rule 7 — Individual Award Markets: Sportsbook Gap Applies to Thin-Market Player Awards
**Date learned**: 2026-03-17 (from Kucherov Hart Trophy YES trade — trade file: `output/trades/2026-03-17_kucherov-hart-trophy-yes.md`)
**Rule**: The sportsbook vs Polymarket pricing gap applies not only to team futures but also to individual player award markets (Hart Trophy, Norris Trophy, MVP races). Polymarket prices on thin award markets (<$10k volume) can be 3–4× below sportsbook consensus.
**Why**: Award markets with low Polymarket volume attract fewer sharp bettors. Sportsbooks have dedicated staff tracking player performance and voter sentiment. The gap is larger on thin markets than high-volume futures.
**Caution**: Thin market liquidity ($5k–$15k pool) means:
  - Size to ≤ 1% of total pool to avoid material price impact
  - Entry/exit slippage 1–3pp more than stated market price
  - Fair value = midpoint of 3+ sportsbook consensus, not just one book
**Entry signal**: Sportsbook consensus ≥ 3 books at X%, Polymarket ≤ (X - 10pp), total pool < $15k — size ≤ $100 regardless of Kelly calc
**Apply when**: Any NHL/NBA individual award market where sportsbook consensus exceeds Polymarket by 10pp+ with 3+ months remaining.
**Confirmed in**: Kucherov Hart Trophy YES — sportsbooks 20–28% implied (BET99 +255, DraftKings +500), Polymarket 5.6% — 3.5× gap.

**EXIT SIGNAL (added Mar 22)**: When Polymarket price EXCEEDS sportsbook consensus by >10pp, the gap has inverted — EXIT immediately. The edge source was "PM underpriced vs books." Once PM is OVERPRICED vs books, there is no remaining edge and you are holding a directional bet you didn't intend to make.
**Kucherov exit result**: Entered 5.6¢ (Mar 17). Exited ~38¢ (Mar 22) when PM reached 41.6% vs sportsbooks 27% (+578.57 on $100). The gap closed AND inverted, signaling exit.
**Rule**: For gap trades, monitor the gap DIRECTION, not just price level. Closing = reassess. Inverted = EXIT.

### Rule 8 — Large-Volume NBA/NHL Futures: Sportsbook Gap Still Present but Smaller (4-6pp)
**Date learned**: 2026-03-18 (from OKC Thunder NBA YES trade — trade file: `output/trades/2026-03-18_okc-thunder-nba-yes.md`)
**Rule**: The sportsbook vs Polymarket gap exists even on high-volume team futures markets ($5M+ volume). For large markets, the gap is structurally smaller (4-6pp vs 10-20pp for thin markets), but the gap is reliable because sharp sportsbook consensus consistently outpaces Polymarket's crowd.
**Why**: For OKC Thunder ($5.17M Polymarket volume), sportsbook consensus was +135 (43.3%) vs Polymarket 37.5% — a 5.8pp gap. Large markets are more efficient than thin ones, but sportsbook quants with full lineup/analytics data still have an informational edge over Polymarket's casual crowd.
**Entry threshold for large markets**: Require ≥ 5pp gap (vs 10pp for thin markets) AND sportsbook consensus across 3+ major books. Single-book outlier does NOT qualify.
**Sizing**: 1/6 Kelly for medium confidence, capped at 1.5% bankroll. Do not size aggressively — the edge is real but thin ($5M market).
**Apply when**: Reigning champion with best current record trades at 5pp+ below 3-book sportsbook consensus. Reigning champions especially underpriced by Polymarket crowd (regression-to-mean anchoring).
**Standing trigger**: If Polymarket price ≤38%, bet YES up to $120-150. If Polymarket price rises to 50%+, exit to lock gain.

### Rule 9 — National Team Markets: Use Injury-Adjusted Squad Probability, Not Brand Probability
**Date learned**: 2026-03-18 (from Italy WC NO trade — trade file: `output/trades/2026-03-18_italy-wc-no.md`)
**Rule**: Before any national team short-window tournament market (qualifying knockout, single-elimination, World Cup path), compute injury-adjusted squad probability rather than relying on FIFA ranking or the team's historical brand. Markets price the "normal" version of strong national teams and adjust only partially for injury crises.
**Method**:
1. Identify all confirmed absences (injured players, withdrawn from squad)
2. Assess positional impact: losing a key playmaker vs depth player matters differently
3. Estimate P(win each required game) with the depleted squad
4. For multi-game paths: compound probabilities (P(qualify) = P(win game 1) × P(win game 2))
5. Compare to market-implied probability
**Entry signal**: 5+ confirmed starters absent including at least 1 key playmaker + two-game-or-more knockout format + market YES > (injury-adjusted probability + 8pp) — bet the underdog side.
**Why market misprices this**: Polymarket crowd anchors on the team's brand and ranking. They see "Italy" or "Germany" and apply a historical strength prior without rebuilding probability from the actual available squad. The brand premium is real but partially unjustified when the squad is significantly depleted.
**What happened (Italy)**: 7 confirmed injuries (Verratti, Di Lorenzo, Calafiori, Udogie, Rovella, Leoni, Gabbia). Two-game knockout path required (March 26 semi-final + March 31 final). Injury-adjusted: P(qualify) = 0.80 × 0.55 = 44%. Market priced Italy at 61% YES — a 17pp brand premium. Bet NO at 39c with +11pp edge.
**Historical precedent**: Italy missed 2018 WC (Sweden) and 2022 WC (North Macedonia) — the brand premium has repeatedly failed to materialize when squads are weakened.
**Apply when**: Any national team in a knockout qualifier or tournament path where the squad is visibly weakened relative to their FIFA ranking.

### Rule 10 — Formula 1 Season-Long Championship: Early-Season Dominant-Team Markets
**Date learned**: 2026-03-22 (F1 Russell NO trade — trade file: `output/trades/2026-03-22_f1-russell-no.md`)
**Rule**: When a single team is dominant in F1 and runs two co-equal drivers, Polymarket over-weights the current championship points leader. The true probability of each driver must share the team's total championship probability (~65-70% for a fully dominant team), meaning no individual driver should exceed ~40% early in the season.
**Why Polymarket misprices this**:
1. Crowd anchors on standings (who's currently leading?) rather than on the season-length horizon
2. Post-race price updates lag sportsbook repricing by 1-2 days
3. In dominant 2-car teams, race-to-race leadership swaps make the early points leader only marginally better than their teammate
**Key base rate**: After 2 of 24 races, the current points leader wins the championship ~50-55% of the time. If their team is dominant (~65-70% championship share) but runs two co-equal drivers, the leader's expected share is ~32-38%.
**Entry signal**: When PM prices a championship points leader ABOVE the sum of (a) sportsbook de-vigged consensus + (b) 4pp buffer, enter NO on that driver. Minimum gap: 10pp. Confirmed sportsbooks: 3+ books.
**Sizing**: Up to 4% bankroll for season-long F1 futures (treat same as other season-long sports).
**Exit triggers**:
- Gap closes to within 5pp of PM vs SB consensus → exit
- Driver extends lead to 30+ points (3+ race advantage) → re-evaluate FV
- Monitor after every race (every 2 weeks)
**Applied**: Russell NO at 44.5¢ (PM 55.5% YES vs SB ~30-38% de-vigged post-Australia, further widened post-China). Edge +18.5pp. Size $260.

---

## EPL — 2025–26 Season Context

### Standings as of 2026-03-15
- **Arsenal**: ~67 pts from ~29 games, 9 remaining
- **Manchester City**: ~58 pts from ~28 games, 10 remaining
- **Lead**: 9 points (with 1 game in hand)

### Arsenal Mathematical Analysis
For Man City to overturn:
- City needs maximum 30 pts from 10 remaining (win every game)
- Arsenal needs to collapse to ≤19 pts from 9 remaining (huge drop in form)
- Combined probability of both: ~1–3%
- Historical precedent: Teams with 9+ point lead with 9 games left win EPL 97–99% of time

### Arsenal Risk Factors
- CL vs Leverkusen second leg (March 17) — rotation risk
- Direct Etihad match in April — single game could close gap
- Viktor Gyokeres injury risk
- New signing Max Downman (16 years old) has performed well — positive sign

### Arsenal Position
- Direction: YES (89.5¢ entry, fair value 93–97%)
- Size: $300
- Resolves: 2026-05-27 (end of EPL season)

---

## Upcoming Sports Markets to Watch

| Event | Date | Note |
|-------|------|------|
| Arsenal vs Leverkusen CL | 2026-03-17 | Will affect squad fatigue |
| Man City fixture | ongoing | Monitor for slip-ups |
| Arsenal vs Man City at Etihad | ~April 2026 | Key title race moment |

---

## Sports Base Rates (Reference)

| Scenario | Win Probability |
|----------|----------------|
| EPL lead of 9+ pts with 9 games left | 97–99% |
| EPL lead of 5–8 pts with 9 games left | 85–90% |
| EPL lead of 1–4 pts with 9 games left | 55–70% |
| Home team in EPL (average) | 45% |
| Favorite in Champions League knockout | 60–65% |

---

## Calibration History

| Date | Market | Stated % | Outcome | Error |
|------|--------|----------|---------|-------|
| 2026-03-15 | Arsenal EPL YES | 95% | OPEN | — |
| 2026-03-17 | Scheffler Masters YES | 22% | OPEN | — |
| 2026-03-16 | Colorado Avalanche Cup YES | 27% | OPEN | — |
| 2026-03-22 | Kucherov Hart Trophy YES | 16% | EARLY EXIT at ~38¢ (+578.57) | N/A (gap trade, not held to resolution) |
| 2026-03-18 | OKC Thunder NBA YES | 43.3% | OPEN | — |
| 2026-03-18 | Tampa Bay Lightning Cup YES | 20% | OPEN — resolves 2026-06-30 | — |
| 2026-03-18 | Italy 2026 WC qualifying NO | 50% | OPEN — resolves 2026-04-12 (effectively Mar 26) | — |

*Calibration history table current as of 2026-03-22 session1. 6 open sports trades (Kucherov exited).*

No resolved-to-outcome trades yet. First data points expected: Italy WC NO (March 26 semi-final), Scheffler (April 13, 2026), Arsenal (May 2026), Avalanche/OKC/Lightning (June–July 2026).
