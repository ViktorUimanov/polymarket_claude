# output/learnings/ — Human Audit Log

**This directory is for the human operator to read, not for the agent.**

## What goes here

- Synthesis reports written by `/learn` after each resolved batch
- Narrative explanations of what changed and why
- Files like `synthesis_2026-03-16.md`, `oscars-prediction-markets.md`, etc.

## What does NOT go here

Structured machine-readable learnings go in **`knowledge/market_types/`** instead:
- `knowledge/market_types/oscars.md`
- `knowledge/market_types/sports.md`
- `knowledge/market_types/commodities.md`
- `knowledge/market_types/politics.md`
- `knowledge/market_types/crypto.md`

The agent reads `knowledge/market_types/` at the start of every session.
It does NOT read `output/learnings/` — that's purely for human review and audit.

## Why the separation?

- `output/learnings/` can grow large with narrative text — not efficient to load every session
- `knowledge/market_types/` stays concise and structured — specific rules, base rates, patterns
- The human can audit `output/learnings/` to verify the agent is extracting the right lessons
