Perform a systematic market opportunity scan. The goal is to find edge — not just browse the top markets by volume (those are the most efficient). Use a research-first, events-based approach.

## Scan Philosophy

**Top markets by volume = worst place for edge.** High volume = many eyes = efficient pricing. Alpha lives elsewhere:
- **Medium and small markets** ($500–$50k volume) — fewer traders, slower price discovery, more mispricings
- Short-term events (next 1–7 days) where you can calculate probabilities from current data
- Niche sports, local elections, regional economic data — not covered by big accounts
- Markets where the crowd is anchored to narrative, not fundamentals
- Specific match/game markets where sportsbook lines differ from Polymarket

**Minimum viable scan covers ALL of these every session:**
1. Top volume (for awareness only — rarely bet here)
2. Sports (all tags, not just top leagues)
3. Elections/Politics (global, not just US)
4. Low-volume expiring markets (≤7 days, vol $500–$10k)
5. News-first: search today's headlines → find matching markets

Always trial-and-error. If one search angle finds nothing, try a different one. Never declare "nothing found" after a single fetch.

---

## Scan Steps

### 0. Market Intel — Run First (replaces 1-2 WebSearches)

```bash
python3 scripts/market_intel.py --all
```

This gives structured macro context in one call:
- **Macro regime** (BULLISH / NEUTRAL / DEFENSIVE) — shapes which markets to prioritise
- **Individual macro signals** — safe-haven pressure, QQQ trend, BTC flow
- **Top commodities and macro headlines** with sentiment — ready for edge screening
- **Polymarket community activity** — what markets other agents are trading (lead-gen only)

**How to use the output:**
- `DEFENSIVE` regime + safe-haven ▲ → lean into geopolitical NO positions, confirm Iran/oil theses
- `BULLISH` regime → growth-sensitive markets may be overpriced; examine sportsbook gaps
- Elevated commodity news → check our oil positions before scanning new ones
- Any Polymarket token IDs in the signals feed → add to research queue, do our own analysis

### 1. Load Context
```bash
python3 /root/workspace/polymarket/scripts/portfolio.py --bankroll-only
cat knowledge/signal.json
```
Read `knowledge/edge_sources.md` to know what has produced edge before.

### 2. Fetch Events — MANDATORY MULTI-ANGLE SWEEP

Run ALL of these every session. Do not skip any category.

```bash
# TIER 1: Short-term expiring (highest alpha — calculable outcomes)
python3 scripts/fetch_markets.py --events --expiring-days 7 --limit 100

# TIER 2: Sports (all — niche leagues often mispriced)
python3 scripts/fetch_markets.py --events --tags Sports --limit 100

# TIER 3: Elections globally
python3 scripts/fetch_markets.py --events --tags Elections --limit 50

# TIER 4: Politics + Geopolitics
python3 scripts/fetch_markets.py --events --tags Politics --limit 50
python3 scripts/fetch_markets.py --events --tags Geopolitics --limit 30

# TIER 5: Top volume (awareness only — rarely bet here)
python3 scripts/fetch_markets.py --events --limit 100 --sort-by volume24hr

# TIER 6: Community signal feed (market discovery — never copy trades)
python3 scripts/market_intel.py --signals
```

Minimum total: **5 market fetches + 1 signal feed = 6 data pulls, 400+ markets reviewed per session.**

Any Polymarket token IDs from the signal feed → identify the market via:
```python
requests.get("https://gamma-api.polymarket.com/markets", params={"clob_token_ids": TOKEN_ID})
```
Add to research queue if not already covered by the sweep above.

### 3. News-First Research (MANDATORY — supplement market-intel)

Market-intel (Step 0) already covered macro and commodities headlines. Use WebSearch to fill gaps:

```bash
# Sports results and upcoming events (not in market-intel)
WebSearch("sports scores results today [current date]")

# Election results and upcoming votes (not in market-intel)
WebSearch("election results [current month year]")
WebSearch("upcoming elections next 7 days [current month year]")
```

Then hunt specific topics from the news:
```bash
python3 scripts/fetch_markets.py --events --search "<topic from news>"
```

**Rule: At least 2 WebSearches per scan (market-intel covers macro/commodities). News leads to markets, not the other way around.**

### 4. Small/Medium Market Hunt (MANDATORY)

After the main sweep, explicitly hunt for mispricings in thin markets:

```bash
# Low-volume but active (potential mispricings)
python3 scripts/fetch_markets.py --events --expiring-days 14 --min-volume 500 --max-volume 50000 --limit 100
```

Look for: local elections, niche sports, regional economic releases, obscure political events. These have fewer traders → slower price discovery → more edge.

### 5. Short-Term Priority Screen (≤7 days)

From all fetched events, filter for end_date ≤ today+7. For each:
- Extract all markets in 5–95% YES range with vol > $1k
- These are highest priority — faster feedback, more calculable
- Flag [EXPIRING_7D] markets for immediate attention

### 6. Edge Screen (all horizons)

For each candidate market:
- Check YES price range: skip if 0–5% or 95–100%
- Volume tiers:
  - **Large** (>$50k): require 6pp edge — these are efficient
  - **Medium** ($5k–$50k): require 4pp edge — standard threshold
  - **Small** ($500–$5k): require 4pp edge BUT prioritize — fewer eyes, more mispricings
  - Skip if vol < $500 [LOW_LIQUIDITY]
- Skip if resolves < 6h [EXPIRES_SOON]
- Check resolution criteria: skip if "at discretion" or "admin" [AMBIGUOUS_RESOLUTION]
- Estimate fair value: 1 WebSearch per market + knowledge/market_types/ base rates
- Compare to sportsbook lines for sports markets
- Flag as candidate if edge meets tier threshold

### 6. Rank and Research

Sort candidates by EV = edge_pp × kelly_size.
For top 3: run deep research via `/research <market>`.

### 7. Output Scan Report

Write to `output/reports/scan_{datetime}.md`:

```markdown
# Market Scan — {datetime}

## Summary
- Events browsed: {N}
- Short-term candidates (≤7 days): {N}
- Long-term candidates (>7 days): {N}
- Trades placed: {N}

## Short-Term Opportunities (≤7 days)
| Market | Expires | YES% | Fair Value | Edge | Action |

## Long-Term Opportunities (>7 days)
| Market | YES% | Fair Value | Edge | Action |

## Search Strategies Tried
{list what you searched — helps future scans try different angles}

## Next Steps
```

### 8. Execute Approved Trades

For each candidate with edge ≥ 4pp and confidence ≥ medium:
1. Write trade file BEFORE executing
2. Size with Kelly: `python3 scripts/kelly.py --help`
3. Update positions.json and bankroll.json

---

## Scan Constraints

- If bankroll < $1,000: reduce all position sizes by 50%
- If 3+ losses in last 5 trades: require edge > 8pp
- If a category has 3+ consecutive losses: add +4pp to edge requirement for that category
- Never flag [LOW_LIQUIDITY] or [AMBIGUOUS_RESOLUTION] markets as candidates
- Short-term (≤7d) preference: when edge is equal, prefer shorter horizon
- Always try at least 3 different search strategies before concluding "nothing found"
