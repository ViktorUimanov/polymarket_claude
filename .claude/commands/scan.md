Perform a systematic market opportunity scan. The goal is to find edge — not just browse the top markets by volume (those are the most efficient). Use a research-first, events-based approach.

## Scan Philosophy

**Top markets by volume = worst place for edge.** The best opportunities are in:
- Short-term events (next 1–7 days) where you can calculate probabilities from current data
- Events with less volume but clear information advantage
- Markets where the crowd is anchored to narrative, not fundamentals
- Specific match/game markets where sportsbook lines differ from Polymarket

Always trial-and-error. Try new search strategies. If one approach finds nothing, try a different angle.

---

## Scan Steps

### 1. Load Context
```bash
python3 /root/workspace/polymarket/scripts/portfolio.py --bankroll-only
cat knowledge/signal.json
```
Read `knowledge/edge_sources.md` to know what has produced edge before.

### 2. Fetch Events (PRIMARY — do this first)

The **events endpoint** groups related markets and shows 24h volume, which is far more informative than total volume.

```bash
# Most active events right now (24h volume)
python3 scripts/fetch_markets.py --events --limit 100 --sort-by volume24hr

# Events expiring in next 7 days (short-term focus)
python3 scripts/fetch_markets.py --events --expiring-days 7 --limit 50

# Sports events (upcoming games)
python3 scripts/fetch_markets.py --events --tags Sports --limit 50

# Politics/geopolitics
python3 scripts/fetch_markets.py --events --tags Politics --limit 30
python3 scripts/fetch_markets.py --events --tags Geopolitics --limit 30

# Elections (upcoming)
python3 scripts/fetch_markets.py --events --tags Elections --limit 30
```

### 3. News-First Research

Search for current events, THEN find matching Polymarket markets:

```bash
# Search for today's big stories
WebSearch("major news events today March 2026 prediction markets")
WebSearch("upcoming elections March April 2026")
WebSearch("sports results today March 2026 upcoming games")
```

Then search for specific topics:
```bash
python3 scripts/fetch_markets.py --events --search "election"
python3 scripts/fetch_markets.py --events --search "Iran"
python3 scripts/fetch_markets.py --events --search "bitcoin"
```

### 4. Short-Term Priority Screen (≤7 days)

From all fetched events, filter for end_date ≤ today+7. For each:
- Extract all markets in 5–95% YES range with vol > $1k
- These are highest priority — faster feedback, more calculable
- Flag [EXPIRING_7D] markets for immediate attention

### 5. Edge Screen (all horizons)

For each candidate market:
- Check YES price range: skip if 0–5% or 95–100%
- Skip if vol < $2,000 [LOW_LIQUIDITY]
- Skip if resolves < 6h [EXPIRES_SOON]
- Check resolution criteria: skip if "at discretion" or "admin" [AMBIGUOUS_RESOLUTION]
- Estimate fair value: 1 WebSearch per market + knowledge/market_types/ base rates
- Compare to sportsbook lines for sports markets
- Flag as candidate if edge ≥ 4pp

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
