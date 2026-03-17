# Cron Loop Log

## 2026-03-16 18:23 UTC — Loop Started

Jobs created:
| Job | ID | Schedule | Purpose |
|-----|----|----------|---------|
| Scan | a6c10116 | `*/37 * * * *` | Market opportunity sweep every 37 min |
| Resolve | 93101ba7 | `7 * * * *` | Open position resolution check every hour |
| Learn | 6e859dfc | `17 2 * * *` | Daily learning synthesis at 02:17 |
| Report | 0570a280 | `47 2 * * *` | Daily report generation at 02:47 |
| Restart reminder | c368489d | one-shot `2026-03-19 17:00` | Alert before expiry |

**Auto-expires**: 2026-03-19 ~18:23 UTC (3-day limit)
**Next manual restart needed by**: 2026-03-19 17:00 UTC

## To Restart
Run `/restart-loop` in a Claude Code session before the expiry time.
Crons are session-only — they do NOT persist if Claude exits.

---

## 2026-03-17 17:38 UTC — Migrated to OS-level crontab (PERSISTENT)

Session-based crons replaced with OS crontab (`crontab -e`). These survive session restarts and reboots.

| Job | Schedule | Command |
|-----|----------|---------|
| Heartbeat | `*/13 * * * *` | `python3 scripts/heartbeat.py` |
| Wake agent (scan/resolve/learn) | `*/37 * * * *` | `scripts/wake_agent.sh` |
| Daily learn | `17 2 * * *` | `scripts/wake_agent.sh` |
| Daily report | `47 2 * * *` | `scripts/wake_agent.sh` |

**Logs**: `output/reports/cron_wake.log`
**No expiry. No manual restart needed.**
**Max budget per wake: $3.00 (hardcoded in wake_agent.sh)**
