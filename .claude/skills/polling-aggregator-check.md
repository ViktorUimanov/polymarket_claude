---
name: polling-aggregator-check
description: Mandates consulting 3+ independent polling houses before any election market entry to avoid single-poll entry errors
type: tool
performance:
  uses: 0
  wins_contributed: 0
  losses_contributed: 0
  status: ACTIVE
---

# Polling Aggregator Check

**Hard prerequisite for election markets**: Before entering any market that depends on polling data (election outcomes, approval ratings, etc.), you MUST verify the thesis across at least 3 independent polling sources.

## Required Checks

1. **Collect 3+ polls from 3+ different polling houses** (not 3 reports citing the same poll)
2. **Check recency** — all polls must be within the last 30 days (14 days preferred for fast-moving races)
3. **Check consistency** — if polls disagree by >5pp, treat as uncertain; do not enter based on the favorable outlier
4. **Note ecosystem size** — European elections often have only 3–6 active pollsters; single-poll signals are especially unreliable

## Entry Rules (from Slovenia exit $0)

- **Minimum 3 consistent polls** showing the same directional thesis before entry
- **"Tightening race" thesis** (betting against the leader): requires 3+ polls all showing frontrunner lead ≤5pp from 3 different houses
- **Single outlier poll = PASS** — one poll showing a surprise result is noise until confirmed by a second
- **Conflicting polls**: if 2+ polls contradict your thesis, do not enter regardless of single supportive data point
- **Aggregate sources**: prioritize polling aggregators (e.g., Politico, 538-equivalent, national news aggregators) over individual poll press releases

## Application

Triggers on any market with resolution criteria involving:
- Election outcomes (parliamentary seats, executive winners)
- Approval ratings or poll-dependent thresholds
- Any market where your fair value estimate rests on polling data
