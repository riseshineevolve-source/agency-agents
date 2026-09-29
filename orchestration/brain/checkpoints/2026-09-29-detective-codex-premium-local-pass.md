# Detective Academy — Codex Premium Interior Local PASS

Date: 2026-09-29
Authority: owner-reported Codex result, reconciled by Central RSE Technical Orchestrator
Status: LOCAL CODEX PASS REPORTED / GITHUB NOT YET UPDATED / EN NOT FROZEN

## Owner-reported local Codex result

Codex reports a premium Book 1 owner-review PDF:

`C:/Users/danie/GitHub/detective-academy/tools/detective-book-factory/dist/HMDA_Book1_EN_PREMIUM_ALMOST_KDP_READY_V3.pdf`

Reported pagination:
**180 pages**

Reported QA:
- 714 V3 text fragments verified;
- 15 Witness Board -> map pairs on the intended facing-page structure;
- one valid solution for each of 15 spatial cases;
- exactly 10 Case 03 tracker marks;
- Hint Vault / Solution section rotation verified;
- page format, margins, fonts and grayscale checks passed;
- all 180 page previews visually reviewed by Codex;
- Page 3 uses the scanner-mark variant;
- original squad art unchanged.

Reported local supporting artifacts:
- `dist/HMDA_Book1_EN_PREMIUM_ALMOST_KDP_READY_V3_final_QA.json`
- `dist/HMDA_Book1_EN_PREMIUM_ALMOST_KDP_READY_V3_page_index.json`
- `dist/v3_premium_review/final`
- `HMDA_BOOK1_V3_PREMIUM_INTERIOR_CHECKPOINT_2026-09-29.md`

Codex explicitly reports:
- EN not frozen;
- nothing published;
- nothing merged;
- renderer/audit changes and private production assets remain local;
- PR not updated;
- CI reproduction requires an approved path for private production assets.

## Live GitHub reconciliation

At central verification time, PR #571 remains open/draft/clean but its head is still:

`989bce1fc1846fcb2480517d1b4965f3add204aa`

Therefore the 180-page local Codex build is **not yet durable GitHub truth** and has not been independently reproduced by Central from repository state.

## Required next step before owner review can become durable

1. Codex should commit/push all non-private renderer, audit, test and checkpoint changes to `feature/detective-book-factory`.
2. Do NOT commit private production assets if their current boundary requires local-only storage.
3. Do NOT commit generated `dist/` binaries unless the repository contract explicitly calls for them.
4. Keep the 180-page PDF + QA JSON + page index available for owner review and central audit.
5. After the non-private source push, rerun current-head CI where supported.
6. Owner uploads/shares the exact 180-page PDF for page-by-page review.
7. Only after bounded fixes + KDP Previewer + physical proof may owner explicitly freeze English.

## Ownership

Detective remains delegated/read-only for Central until:
- the Codex source changes are durably pushed and checkpointed, and
- owner/Codex explicitly hands the lane back.

No central writer should overwrite the local premium-layout work in the meantime.
