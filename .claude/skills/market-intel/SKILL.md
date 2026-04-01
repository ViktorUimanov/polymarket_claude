---
name: market-intel
description: Pull structured macro context from AI-Trader before scanning — regime verdict, macro signals, and categorised news for commodities and macro. Replaces manual WebSearches for background context.
type: tool
performance:
  uses: 0
  wins_contributed: 0
  losses_contributed: 0
  status: ACTIVE
  last_reviewed: 2026-03-25
---

# Market Intel — AI-Trader Context Feed

Pull structured macro context from the AI-Trader market-intel API **at the start of every scan session**, before fetching Polymarket markets or running WebSearches. This replaces 1-2 manual WebSearches and gives a faster, structured macro picture.

## When to Use

- Start of every `/scan` — always run `--overview` first
- Before researching any commodities market — run `--news commodities`
- Before researching any political/macro market — run `--news macro`
- When assessing broad market risk — run `--macro` for the full regime signals

## Commands

```bash
# Full context dump (scan mode — run at start of each session)
python3 scripts/market_intel.py --all

# Compact overview only (fastest, always available)
python3 scripts/market_intel.py --overview

# Macro regime signals with individual indicators
python3 scripts/market_intel.py --macro

# News for a specific category
python3 scripts/market_intel.py --news macro
python3 scripts/market_intel.py --news commodities

# Polymarket community activity (market discovery)
python3 scripts/market_intel.py --signals
```

## Output Fields

**Overview:**
- `macro_verdict`: neutral / bullish / defensive — current regime
- `macro_bullish_count / macro_total_count`: signal breakdown
- `etf_direction`: BTC ETF flow direction (relevant for crypto-linked markets)
- `news_status`: normal / elevated / active — how busy news is today

**Macro Signals (--macro):**
- Individual signals: BTC trend, QQQ trend, QQQ vs XLP, safe-haven pressure, macro news tone
- Each has: status (bullish/neutral/defensive), value, explanation

**News (--news):**
- Top 5 headlines per category with sentiment labels (Bullish/Bearish/Neutral)
- Source, summary, ticker sentiment where applicable

## How to Read the Output for Trading

| Regime | Implication for Polymarket |
|--------|---------------------------|
| BULLISH | Risk-on; equity/growth markets may overprice positive outcomes |
| NEUTRAL | No macro tailwind/headwind; lean on fundamentals |
| DEFENSIVE | Risk-off; geopolitical NOs may become stronger bets |

**Safe-haven pressure ▲** → Watch Iran/geopolitical NO positions (strengthens thesis)
**QQQ trend ▼** → Growth slowdown; may affect tech-linked markets
**Macro news ELEVATED** → Higher edge opportunity from information asymmetry

## API Details

- Base URL: `https://ai4trade.ai/api`
- No authentication required (public endpoints)
- Data refreshed by backend jobs every ~15-30 min
- If unavailable: skip gracefully, proceed with manual WebSearch

## Common Gotchas

- News endpoint called with `?category=X` returns items array directly — not the same structure as overview's `categories` array
- Data is snapshots, not live — don't treat as real-time
- Polymarket signals feed skews heavily Chinese-language arbitrage agents; use for market discovery only, not for copying trades
