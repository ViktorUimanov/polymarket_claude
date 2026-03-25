# TRADE: Greenland Sovereignty NO (Market 997488)

**Date**: 2026-03-18
**Action**: BET NO
**Market**: Will the US acquire Greenland before 2027?
**Market ID**: 997488
**Resolves**: 2026-12-31

---

## Position Details

| | |
|--|--|
| **Direction** | NO |
| **Market price (YES)** | 9.7% |
| **Market price (NO)** | 90.3¢ per share |
| **Fair value (NO)** | 96% (range: 93–98%) |
| **Edge** | +5.7pp |
| **Size** | $193 |
| **Shares** | 213.7 NO shares |
| **Expected value** | +$12.18 |
| **Category** | politics |
| **Kelly mode** | 1/6 Kelly, capped by 3% politics cap |

---

## Research

### Resolution Criteria (Exact)
The market resolves YES only if the US **officially announces Greenland will come under US sovereignty** before December 31, 2026. Sovereignty = transfer of **actual governmental authority** — not military base agreements, not framework deals, not diplomatic frameworks.

**Critical distinction**: Trump's Davos "framework" (January 2026) is explicitly about military base expansion, NOT sovereignty transfer. This does NOT resolve YES.

### Why YES is overpriced at 9.7%

**Legal barrier**: Greenland sovereignty requires THREE separate ratification steps:
1. Greenlandic referendum
2. Greenlandic parliament approval
3. Danish parliament approval

The independence commission has not yet reported (expected late 2026). No step has been initiated.

**Political barriers**:
- Denmark's position: explicit "not for sale" on sovereignty (structural, not rhetorical)
- No Greenlandic main party has launched independence process
- Trump ruled out use of force at Davos January 2026
- The "framework" signed at Davos = military base expansion agreement, explicitly NOT sovereignty transfer

**Historical base rate**: Peaceful territorial annexation of a NATO member state within 12 months = <1%. Market prices 9.7% — 10x the historical base rate.

**Why market is inefficient**:
- Trump's bombastic rhetoric about "buying Greenland" gets conflated with actual sovereign transfer probability
- Media coverage of the Davos "framework" was ambiguous — many outlets reported it as a sovereignty deal
- Long resolution horizon (Dec 31) creates "anything can happen" premium that overstates the legal/political realities

### Key sources
- Wikipedia "Proposed United States acquisition of Greenland" — independence commission timeline
- Chatham House January 2026 — Danish/Greenlandic position reaffirmed
- CNBC Davos reporting — confirmed framework ≠ sovereignty transfer
- Trump January 21: "We will not use force" + Danish PM: "not for sale"

---

## Probability Estimate

**Method**: Base rate + structural analysis
- Base rate (NATO sovereign annexation, 12 months): <1%
- Legal timeline impossibility (3-step ratification, none started): <2% conditional
- Political consensus (Denmark + Greenland both blocking): adds modest probability of surprise political realignment

**Bayesian update**: Could a surprise deal emerge? Only if: (a) Denmark reverses position + new election + pro-transfer majority, (b) Greenlandic parliament initiates process, (c) all three bodies ratify in 9 months. Probability of all three: <3%.

**Fair value**: YES 4% (conservative) / NO 96%
Range: NO 93–98%

---

## Sizing

```
Bankroll: $9,664
Politics cap: 3% = $290 max per trade
Kelly formula: (edge / odds) × bankroll = (0.057 / 0.097) × 9664 = $5,677 full Kelly
1/6 Kelly = $946 → exceeds 3% politics cap
Cap constraint: $290
Conservative sizing at 2% for 12-month horizon with tail risk: $193
```

**Final size: $193**

---

## Position Limits Check

| Check | Result |
|---|---|
| Single-market cap (5% = $483) | $193 — within cap |
| Politics per-trade cap (3% = $290) | $193 — within cap |
| Correlated macro exposure (10% cap) | No direct correlation with open positions |
| Category: awards/other probation? | Politics — no probation, 0 resolved |
| 4pp minimum edge | +5.7pp — passes |
| Never at 97%+ | NO at 90.3% — passes |

---

## Thesis Monitor

**Thesis breaks if ANY of the following occur:**
- Denmark reverses its "not for sale" position publicly at ministerial/PM level
- Greenlandic parliament votes to initiate independence referendum
- US-Denmark bilateral treaty framework explicitly includes sovereignty transfer (not base expansion)
- Emergency fast-track legislation introduced in all three bodies simultaneously

**Monitoring frequency**: Monthly (long-horizon trade)
**Next check**: Mid-April 2026

---

## Skills Used

- resolution-parser: Read exact resolution criteria (sovereignty ≠ base agreement)
- evaluate-edge: +5.7pp edge confirmed
- size-position: 1/6 Kelly capped at politics 3% limit
- correlated-position-check: No direct correlation with existing positions
