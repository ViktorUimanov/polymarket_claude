Synthesize learnings from recent trade outcomes. Runs automatically at 02:17 via cron.

Delegate to the **synthesizer** agent defined in `.claude/agents/synthesizer.md`.

## What the Synthesizer Does

1. Analyzes resolved trades from the past 7 days
2. Computes calibration stats by category
3. Reviews strategy performance ratings
4. Updates edge source success rates
5. Audits skill contributions
6. Extracts specific actionable learnings from losses
7. Proposes skill additions or retirements

## After Synthesis Completes

Review the synthesis report at `output/learnings/synthesis_{date}.md`:

- **Proposed new skills**: If any are proposed and make sense, create them in `.claude/skills/`
  with a performance header. Template:
  ```markdown
  ---
  name: {skill-name}
  description: {one-line description}
  performance:
    uses: 0
    wins_contributed: 0
    losses_contributed: 0
    status: ACTIVE
  ---
  {skill content}
  ```

- **Skills flagged for pruning**: Run `/prune-skills` to review them

- **Calibration problems identified**: Update `knowledge/market_types/<category>.md` immediately

- **Key Question for next session**: Note it — address it in the next scan or research session

## When to Run Manually

- After any session with 2+ resolved trades
- After any loss (run immediately to capture lessons while context is fresh)
- Weekly even if no new trades (calibration stats update is valuable)
