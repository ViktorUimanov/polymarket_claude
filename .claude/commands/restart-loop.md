Restart the continuous 24/7 cron loop. Run this every 72 hours (crons auto-expire after 3 days).

## What This Does

Sets up 5 recurring cron jobs (2 layers):

**Layer 1 — Lightweight heartbeat (no LLM cost):**
1. **Heartbeat** every 13 minutes — updates signal.json flags

**Layer 2 — LLM operations (triggered by signal):**
2. **Market scan** every 37 minutes
3. **Resolution check** every 67 minutes
4. **Daily learning synthesis** at 02:17
5. **Daily report** at 02:47

Also sets a one-shot 71-hour reminder to run `/restart-loop` before crons expire.

## Steps

Use the `CronCreate` tool to create these 5 jobs:

**Job 1 — Heartbeat (every 13 min, lightweight)**
```
cron: "*/13 * * * *"
recurring: true
prompt: "Run: python3 /root/workspace/polymarket/scripts/heartbeat.py — this writes knowledge/signal.json with scan_needed, resolve_needed, learn_needed flags. No LLM analysis needed, just run the script and output the result."
```

**Job 2 — Market Scan (every 37 min)**
```
cron: "*/37 * * * *"
recurring: true
prompt: "Run /scan — automated market opportunity sweep. Fetch top markets by volume across all categories. Screen for edge ≥ 4pp. If any candidate found with edge ≥ 4pp and volume ≥ $5,000: run /research on the top candidate and log to output/reports/scan_{datetime}.md. Keep the scan concise — this is automated, not a full session."
```

**Job 3 — Resolution Check (every 67 min)**
```
cron: "7 * * * *"
recurring: true
prompt: "Run /resolve — check all positions in output/positions.json for resolution. Update outcomes, P&L, calibration. Write post-mortem for any losses. Output brief summary."
```

**Job 4 — Daily Learning Synthesis (02:17)**
```
cron: "17 2 * * *"
recurring: true
prompt: "Run /learn — daily learning synthesis. Analyze resolved trades from past 7 days. Update calibration database, review strategy performance, update edge sources. Write synthesis to output/learnings/synthesis_{date}.md (human audit log — agent reads knowledge/market_types/ not this file)."
```

**Job 5 — Daily Report (02:47)**
```
cron: "47 2 * * *"
recurring: true
prompt: "Run /report — generate daily report to output/reports/daily_{date}.md. Include P&L, trades, passes, calibration snapshot, open positions."
```

**Job 6 — Restart Reminder (one-shot, 71 hours from now)**
Calculate the timestamp 71 hours from now and create a one-shot cron:
```
cron: "{min} {hour} {day} {month} *"
recurring: false
prompt: "SYSTEM ALERT: Cron loop is expiring in ~1 hour. Run /restart-loop to keep the 24/7 system alive."
```

## After Creating Jobs

Log to `output/reports/cron_log.md`:
```markdown
# Cron Log

## {datetime} — Loop Restarted

Jobs created:
- Heartbeat (ID: {id}): */13 * * * *
- Scan (ID: {id}): */37 * * * *
- Resolve (ID: {id}): 7 * * * *
- Learn (ID: {id}): 17 2 * * *
- Report (ID: {id}): 47 2 * * *
- Restart reminder (ID: {id}): one-shot at {datetime}

Auto-expires: {datetime + 3 days}
Next manual restart needed by: {datetime + 71 hours}
```

## Notes

- Crons only fire while Claude is idle (not mid-conversation)
- Jobs add up to 10% jitter on top of schedule — this is expected
- If Claude session ends, all crons are lost — they must be recreated on next session start
- The heartbeat (Job 1) is cheap — just a Python script, no LLM thinking required
- The one-shot reminder will alert before expiry so you can run `/restart-loop` in time
