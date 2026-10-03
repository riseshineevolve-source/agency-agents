# World 02 — Level 11 source-proven graph checkpoint

Date: 2026-10-01
Status: **LEVEL 11 SOURCE-PROVEN CANDIDATE / CI PENDING**

## Authority

Canonical source:
`paperback 10 STORIES WORLD 02 FINAL standard(1).pdf`

- ISBN: `9798249971823`
- pages: 104
- bytes: 66,576,954
- SHA-256: `e94d2937cc459a5c7c3c5968c64ba39f2a03702f929488e42b00b5db3f9f7f76`

Historical `spark-joy-fam/src/data/storyContent.ts` remains comparison-only.

## Bounded slice

Level 11:
- number: 11
- title: **The Daily Habit Loop**
- key: **DISCIPLINE & AUTOMATION**
- source pages: 13–21
- source blocks: 27

Preserved semantic blocks:
- opener: 1
- dialogue: 14
- system log: 5
- Neuro-Coaching Console: 3
- Quest: 2
- Brain Hack science block: 1
- Secret Family Code: 1

The printed `XP REWARD` label on the Family Mission is preserved as source
copy only. No XP calculation, score or reward engine was added.

The Level 11 GLITCH block contains a printed `Correction:` field rather than
an `In The Story:` field. The source graph preserves this as
`correction_label` + `correction`; the reusable runtime must render these
fields rather than silently dropping them.

## Files

- `orchestration/content-sources/world02-level11-page-evidence.json`
- `orchestration/content-packs/world02/level11.en.candidate.json`
- `scripts/build-world02-graph.py`
- `scripts/validate-world02-graph.py`
- `scripts/test-world02-graph.py`

Interactive Book CI has been extended for this bounded World 02 slice.

## Boundaries

- Level numbering remains 11.
- English is canonical and supported.
- Polish remains planned only.
- No legacy Lovable prose is promoted.
- No source science/wellbeing claim is silently rewritten.
- No auth/paywall/backend/entitlement requirement is introduced.
- No publication, signing or Play deployment is authorized.

## Next slice after green source CI

Import this exact Level 11 pack into the shared `spark-joy-fam` runtime and
prove rendering through the World 01 source-aware renderer with the minimum
runtime extension required for the source-derived `Correction:` field.
