#!/bin/bash
# wake_agent.sh — Invoked by OS cron every 37 minutes.
# Starts a non-interactive Claude session to run the trading loop cycle.
# Survives Claude session restarts, machine reboots, and context resets.

set -euo pipefail

# Ensure cron's minimal PATH includes local binaries and python
export PATH="/root/.local/bin:/usr/local/bin:/usr/bin:/bin:$PATH"

WORKDIR="/root/workspace/polymarket"
LOGFILE="$WORKDIR/output/reports/cron_wake.log"
LOCKFILE="$WORKDIR/.agent.lock"

# Update heartbeat first (pure Python, no LLM cost)
python3 "$WORKDIR/scripts/heartbeat.py" >> "$LOGFILE" 2>&1

# Prevent overlapping sessions — if a previous cycle is still running, skip this wake.
if [ -f "$LOCKFILE" ]; then
  LOCK_PID=$(cat "$LOCKFILE" 2>/dev/null)
  if kill -0 "$LOCK_PID" 2>/dev/null; then
    echo "=== Wake @ $(date -u '+%Y-%m-%d %H:%M UTC') — SKIPPED (PID $LOCK_PID still running) ===" >> "$LOGFILE"
    exit 0
  fi
  # Stale lock — previous run crashed without cleanup
  rm -f "$LOCKFILE"
fi

echo $$ > "$LOCKFILE"
trap 'rm -f "$LOCKFILE"' EXIT

TIMESTAMP=$(date -u '+%Y-%m-%d %H:%M UTC')
echo "" >> "$LOGFILE"
echo "=== Wake @ $TIMESTAMP ===" >> "$LOGFILE"

# Run the trading cycle non-interactively.
# All instructions are in CLAUDE.md and knowledge/README.md — no inline prompt needed.
cd "$WORKDIR" && claude \
  --print \
  --allowedTools "Bash,Read,Write,Edit,Glob,Grep,WebSearch,WebFetch,Agent" \
  --model sonnet \
  "Get to work." \
  >> "$LOGFILE" 2>&1

echo "=== Done @ $(date -u '+%Y-%m-%d %H:%M UTC') ===" >> "$LOGFILE"
echo "" >> "$LOGFILE"
