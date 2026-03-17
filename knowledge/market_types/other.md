# Other / Miscellaneous Markets — Knowledge Base

## Category Profile

| Attribute | Value |
|-----------|-------|
| Variance level | VARIABLE (market-specific) |
| Calibration status | OVERCONFIDENT (−37.5pp error, 1 trade) |
| Max position size | 2% bankroll (until calibration established) |
| Min edge required | 8pp (calibration probation — fewer than 5 trades) |
| Current ban | None — caution required |

---

## Rules

### Rule 1 — Count/Activity Markets Require Live Data Source
**Date learned**: 2026-03-17
**Rule**: Never enter a tweet-count, post-count, or any activity-tracking multi-bucket market without access to a live running counter at time of entry. Do not rely on historical daily-average extrapolations.
**Why**: Elon Musk 300-319 tweets market (March 10-17, 2026): entered at 28.5% based on 5-day weekday extrapolation projecting 318 total. By March 16 the live count showed ~248 with 18h remaining — physically impossible to reach 300. The market had correctly repriced to 7-25% based on live tracker data. We did not have access to the live count when making the decision.
**Apply when**: Any multi-bucket count market (tweets, posts, statements, votes, etc.).
**Specific sub-rule**: If live count shows running total below the lower bound of the target bucket with less than 24h remaining, do not enter or exit immediately.

### Rule 2 — Weekend Slowdown is Real for Social Media Activity
**Date learned**: 2026-03-17
**Rule**: For social media posting-rate markets, do not assume weekday pace continues through weekends. Weekend posting rates for high-volume public figures can drop 30-50% from weekday rates.
**Why**: The market was pricing a weekend slowdown (~28.5%) that proved accurate. Our counterargument ("Musk posts heavily on weekends") was qualitative and not data-backed. The 5-day pace of 45.4/day was based on March 10-15 (Mon-Fri). Weekend pace was ~20-25/day.
**Apply when**: Any tweet-count or social media activity market spanning a weekend.
**Required**: Obtain historical weekend vs. weekday posting breakdown before entering.

### Rule 3 — Prior Week's Bucket Does Not Predict This Week
**Date learned**: 2026-03-17
**Rule**: The prior week resolving at 340-359 (high bucket) is weak evidence for this week. Each weekly window is independent. Do not anchor on recent high-resolution weeks.
**Why**: Prior week 340-359 influenced our view that pace was elevated. But the tracking window for this week started midweek, capturing more weekday volume in the first 5 days, making the total structurally different from a Mon-Sun window.
**Apply when**: Any recurring weekly/daily count market.

### Rule 4 — Exit Count Markets When Live Data Crosses Below Target Floor
**Date learned**: 2026-03-17 (Musk tweets post-mortem refinement)
**Rule**: For any open count/activity market, define a live-data exit trigger at entry: "If live count falls below [lower bound of target bucket] with less than 24h remaining, exit immediately at market price regardless of remaining time value." Do not hold hoping for a late surge unless the live pace still supports reaching the floor.
**Why**: In the Musk tweets trade, the live count of ~248 with 18h remaining made reaching 300 essentially impossible — pace would need to accelerate from ~25/day (weekend rate) to ~52/day with no structural reason. The position had residual time value but no realistic path to YES.
**Apply when**: Any count/activity market where the live running total diverges from the projection at the mid-to-late stage.
**Specific sub-rule**: If live pace × remaining hours < lower bound of target bucket × 1.2 buffer, exit. Do not hold.

---

## Calibration History

| Date | Market | Stated % | Outcome | Error |
|------|--------|----------|---------|-------|
| 2026-03-15 | Elon Musk 300-319 tweets (Mar 10-17) | 37.5% | LOSS (resolved NO) | −37.5pp |

Current: 0/1 (0% win rate vs 37.5% stated avg) = −37.5pp calibration error
→ **Probation**: Require +8pp edge on all "other" category bets. Max 2% bankroll.
