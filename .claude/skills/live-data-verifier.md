---
name: live-data-verifier
description: Mandates confirming a live data source URL before entering any count/activity-tracking market (tweets, posts, stats, etc.)
type: tool
performance:
  uses: 0
  wins_contributed: 0
  losses_contributed: 0
  status: ACTIVE
---

# Live Data Verifier

**Hard prerequisite for count/activity markets**: Before entering any market that resolves based on a count, rate, or cumulative activity metric, you MUST confirm a live data source is accessible.

## Required Checks

1. **Identify the live counter URL** — xtracker.polymarket.com, official stat page, or direct API
2. **Access it now** — verify the URL loads and shows current data
3. **Record current count and rate** — note: date, time, current value, daily rate
4. **Project to resolution** — use live rate, not historical average
5. **Apply day-of-week adjustment** — weekends are 40–55% lower activity than weekdays for social media

## Hard Rules (from Musk tweets -$150 loss)

- **Never enter without live counter access.** If xtracker or equivalent is down, PASS.
- **Never extrapolate weekday rate into weekend.** Weekend pace is 45–50% of weekday.
- **Required margin**: Only enter if current trajectory puts you 15%+ inside the target bucket with >24h remaining.
- **Time pressure cutoff**: Do not enter with <24h remaining unless count is already within the target bucket.

## Application

Triggers on any market with resolution criteria mentioning:
- "number of tweets / posts / shares"
- "total X by date Y"
- "at least N occurrences"
- "cumulative count"
- Any discrete event frequency
