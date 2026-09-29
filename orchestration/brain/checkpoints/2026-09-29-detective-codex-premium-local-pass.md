# Detective Academy — Codex Premium Interior Durable PASS

Date: 2026-09-29
Authority: owner-reported Codex result, reconciled by Central RSE Technical Orchestrator
Status: PREMIUM SOURCE PUSHED / CURRENT-HEAD CI GREEN / OWNER REVIEW GATE / EN NOT FROZEN

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

Central verified the pushed implementation on GitHub.

PR #571:
- state: OPEN
- draft: YES
- mergeable: YES
- mergeable_state: CLEAN
- current head: `5a911d48f4b1268d97d93ad0694fb3abb9b40796`

Current-head CI:
- **Build Detective Academy PDF #192: SUCCESS**
- **SEO Validation #756: SUCCESS**

The pushed source contains the non-private renderer, input-preparation, audit, QA, dependency and checkpoint changes required for the 180-page premium build.

The durable branch checkpoint:
`tools/detective-book-factory/HMDA_BOOK1_V3_PREMIUM_INTERIOR_CHECKPOINT_2026-09-29.md`

records:
- current canonical reader text commit `3c0caedbcc313658767cb4251b2c1741c4a7edcf`;
- V3 text blob `8370026a811ad3354aaa8e422ebe2edf58464845`;
- 180-page local premium PDF SHA-256 `2a2fffebfe43ddc4d3e50c22e27b1e9bb68225d01a6a786ca9e0c118996af858`;
- all 15 Witness Board/map pairs on even-left / following odd-right pages;
- Case 03 Photo A/B on pages 20/21 with exactly ten tracker marks;
- STOP page 121 and 59 reverse support pages with true 180-degree content transform;
- 714 substantive reader-text fragments checked with zero missing;
- all 15 spatial cases exhaustively unique on the audited packet runtime;
- Case 05 six-symbol answer verified;
- exact owner visual/map hash checks;
- print geometry, grayscale, font and visual QA PASS.

Important provenance limitation remains:
the premium PDF itself depends on private hash-pinned production inputs and is not independently reproduced by normal CI. Current-head CI validates the pushed public/non-private code path, not the exact private-input premium artifact.

## Next gate

1. Owner uploads/shares the exact 180-page premium PDF for page-by-page review.
2. Review the owner-review artifact with special attention to physical map/axis readability, handwriting, Evidence Grid, section boxes, Case 03 spread, Room Zero pacing, reverse-entry usability and accidental clipping/blank pages.
3. Apply only bounded fixes found in that review; do not reopen solved story/mechanics.
4. Run KDP Previewer.
5. Order/review representative physical proof.
6. Recalculate cover spine from the final frozen page count.
7. Only then may the owner explicitly freeze English and later control KDP upload/publication.

## Ownership

Detective is now at an **OWNER REVIEW GATE**. Central must not perform additional creative/layout rewriting before the owner reviews the 180-page artifact. Codex source work is durably pushed, but further Detective changes should be bounded review fixes only. No merge, EN freeze or KDP publication is authorized.
