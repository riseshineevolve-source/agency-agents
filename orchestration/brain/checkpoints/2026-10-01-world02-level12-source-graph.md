# World 02 — Level 12 source-proven graph checkpoint

Date: 2026-10-01
Status: **LEVEL 12 SOURCE-PROVEN CANDIDATE / CI PENDING**

## Authority

Canonical source:
`paperback 10 STORIES WORLD 02 FINAL standard(1).pdf`

- ISBN: `9798249971823`
- pages: 104
- bytes: 66,576,954
- SHA-256: `e94d2937cc459a5c7c3c5968c64ba39f2a03702f929488e42b00b5db3f9f7f76`

Historical Lovable World 02 content remains comparison-only.

## Bounded slice

Level 12:
- number: 12
- title: **The Nightly Reboot**
- key: **REST**
- source pages: 22–29
- source blocks: 27

Preserved semantic blocks:
- opener: 1
- dialogue: 13
- system log: 6
- Neuro-Coaching Console: 3
- Quest: 2
- Brain Hack science block: 1
- Secret Family Code: 1

The printed `XP REWARD` label remains source copy only; no XP engine, score,
reward calculation or entitlement behavior is added.

The Level 12 GLITCH uses the source-derived `Correction:` field already proven
by Level 11 and rendered by the shared Interactive Book runtime.

## Source-fidelity notes

The canonical paperback visibly contains the Talk About It sentence:

`Alio was bouncing on the bed beacuse hig brain was pumping out emergency adrenaline.`

The misspellings are preserved verbatim in this source graph. They are not
silently corrected during extraction.

The printed Rocket Launch correction is preserved as:

`Use the Rocket Launch. In the morning, don't think. Just count 5-4-3-2-1 and BLAST OFF out of bed!`

Any later editorial/factual/copy correction must be an explicit reviewed change
against this source layer.

## Files

- `orchestration/content-sources/world02-level12-page-evidence.json`
- `orchestration/content-packs/world02/level12.en.candidate.json`
- `scripts/build-world02-graph.py`
- `scripts/validate-world02-graph.py`
- `scripts/test-world02-graph.py`

Interactive Book CI now rebuilds and validates World 02 Levels 11–12.

## Boundaries

- World 02 numbering remains 11–20.
- English is canonical/supported.
- Polish remains planned only.
- No legacy Lovable prose is promoted.
- No science/wellbeing claim is silently rewritten.
- No auth/paywall/backend requirement is introduced.
- No publication/signing/Play action is authorized.

## Next slice after green source CI

Import this exact Level 12 pack into the shared `spark-joy-fam` runtime, add
runtime integrity/render tests, keep the user-facing app entry on World 01 while
World 02 is incomplete, and require full Android CI before merge.
