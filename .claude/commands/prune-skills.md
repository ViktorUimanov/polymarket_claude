Review all skills and retire underperforming ones. Propose new skills based on recent edge sources.

Run this weekly or when the synthesizer flags skills for review.

## Step 1 — Audit Current Skills

List all files in `.claude/skills/` (not `retired/`). For each skill:

1. Read the skill file — note its `performance` header (uses, wins_contributed, losses_contributed, status)
2. Search trade files for references:
```bash
skill_name="fetch-markets"
grep -rl "$skill_name" /root/workspace/polymarket/output/trades/ /root/workspace/polymarket/output/learnings/ | wc -l
```
3. Check if trades that referenced it were wins or losses
4. Rate: `CONTRIBUTING` / `NEUTRAL` / `UNDERPERFORMING` / `UNKNOWN`

## Step 2 — Retirement Decisions

For each skill rated `UNDERPERFORMING` with ≥ 10 opportunities to have contributed:
- Was it ever useful in any trade?
- Is the category it covers still active in our portfolio?
- Would retiring it cause us to miss something?

**Decision threshold**: Retire if net contribution (wins - losses) is negative with ≥ 5 data points.

**To retire a skill**: Move to `.claude/skills/retired/<name>.md` (never delete).
Add retirement note at top:
```markdown
<!-- RETIRED: {date} — Reason: {specific reason} -->
<!-- Can be un-retired if conditions change -->
```

## Step 3 — Propose New Skills

Read `knowledge/edge_sources.md` and latest `output/learnings/synthesis_*.md`.

For each active edge source that lacks a corresponding skill:
- What systematic process would this skill encode?
- Create `.claude/skills/<name>.md` with performance header and content

For each pattern identified in winning trades that isn't yet a skill:
- Same — create a skill to systematize it

## Step 4 — Update Performance Headers

For all skills you've just reviewed, update their performance headers with current stats:
```markdown
performance:
  uses: {N}
  wins_contributed: {N}
  losses_contributed: {N}
  status: CONTRIBUTING / NEUTRAL / UNDERPERFORMING / RETIRED
  last_reviewed: {date}
```

## Step 5 — Output Report

```markdown
# Skills Review — {date}

## Current Skills
| Skill | Uses | Wins | Losses | Net | Status | Action |
|-------|------|------|--------|-----|--------|--------|
| fetch-markets | N | N | N | +N | CONTRIBUTING | KEEP |

## Retired Today
- {skill}: {specific reason}

## New Skills Created
- {skill}: {rationale — which edge source does it systematize?}

## Skills to Monitor
- {skill}: {concern — will review again in N trades}

## Portfolio Assessment
{Overall: are our skills coherent? Any gaps? Any redundancies?}
```
