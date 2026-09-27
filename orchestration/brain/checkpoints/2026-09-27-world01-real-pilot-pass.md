# Interactive Book App Factory — World 01 bounded real pilot PASS

Date: 2026-09-27
Authority: Central RSE Technical Orchestrator
Status: BOUNDED REAL-PILOT PASS / EXPAND SOURCE COVERAGE NEXT

## Branch

`codex/interactive-book-world01-pilot`

Remote HEAD:
`7795e6933c39f4f126666ad712c690ccd418f048`

Working tree reported clean.

## Canonical source

Published World 01 paperback was hashed and checked against candidate evidence.
Published book remains canonical over divergent app copy.

## Candidate pack

`orchestration/content-packs/world01/mission-openers.en.candidate.json`

Current coverage:
- 3/10 mission openers = 30%
- 3/108 pages direct pack evidence = 2.78%
- 0/10 complete missions

The pilot contains only source-supported title/key/objective content for missions 1–3.

## Provenance / custody / comparison

Durable reports:
- `orchestration/content-sources/WORLD01_PAPERBACK_CUSTODY_2026-09-26.md`
- `orchestration/content-sources/WORLD01_APP_COMPARISON_2026-09-26.md`
- `orchestration/content-sources/world01-paperback-opener-evidence.json`
- `orchestration/checkpoints/INTERACTIVE_BOOK_WORLD01_PILOT_2026-09-26.md`

Existing derivative comparison confirms speaker and scene divergences in `spark-joy-fam`; divergent app copy is not promoted to canonical truth.

## Changed implementation

- source registry updated
- program registry updated
- interactive-book content contract extended for provenance handling
- comparison script added
- provenance validator added
- provenance tests added
- CI workflow updated

## Verification

PASS:
- both historical synthetic fixtures
- candidate contract validation
- PDF provenance check
- 24 fail-closed provenance/contract tests
- Interactive Book Contract CI

No deployment, backend, pricing, billing, Play listing, or merge occurred.

## Remaining source gaps

- mission openers 4–10
- full mission story text
- speaker/order verification
- Neuro-Coaching Console content
- quests
- secret codes
- artwork
- front/end matter
- equivalence with older print master
- approved Polish copy

## Next safe slice

Audit Level 1 pages 16–22 next and expand only source-supported coverage.
Prefer a small complete mission slice over broad unverified conversion.
