# Detective Academy — All-15 Hybrid Final PASS

Date: 2026-09-25
Status: MAP VISUAL SYSTEM CLOSED / READY FOR FINAL BOOK INTEGRATION
Authority: Central RSE Technical Orchestrator

Owner supplied Codex final gate result from local worktree:

- local branch: `codex/modern-props-pilot`
- local HEAD / commit: `4c46f75117b4d27cac7b3849cdd060c55bcd6f40`
- tracked worktree: clean

Final gate:
- All-15 render: **15/15 PASS**
- Structural fingerprints: **15/15 PASS**
- Locked-field differences: **0**
- Puzzle/solution consistency: **PASS**
- Unique solutions: **15/15 exhaustively proven; canonical answers match**
- Room Zero meta: **PASS**
- CHECK THE OLD MAP: **PASS**
- Approved modern placements: **106**
- Retained locked-source placements: **154**
- Hydration HMDA_29:D9: **PASS** with approved asset + WATER REFILL label
- Print QA: **PASS**
- Grayscale: **PASS**
- 30 production maps: 8.5 x 11 in / 300 dpi
- Targeted visual blockers: **0**
- No new prop art generated
- No approved art changed
- No geometry / clue / answer / story / cover change
- No merge / publication / English freeze

Owner review packet reported:
`dist/modern-props/all15-hybrid-final-owner-review.zip`

QA summary reported:
`dist/modern-props/all15-hybrid-final-owner-review/06_QA/final_gate.json`

## Decision

The Detective Academy map visual system is now CLOSED for Book 1.

Do not reopen:
- hydration station,
- the 23 approved modern prop families,
- hybrid retained-source policy,
- all-15 geometry,
- object bindings,
- map logic,
- Room Zero meta,
- CHECK THE OLD MAP,
unless a later final-book render proves a concrete production regression.

## Next bounded execution

Proceed to FINAL BOOK INTEGRATION of the English interior:
1. reconcile current final English content source with the current production Book Factory;
2. verify the four owner-controlled visual inputs expected by the finalizer:
   - case03_photo_A.png
   - case03_photo_B.png
   - case03_solution.png
   - book2_archive_photo.png
3. SHA-lock exact supplied owner assets if present;
4. use the just-passed all-15 map production outputs as the spatial layer;
5. render the canonical full interior artifact;
6. run full-page human-readable visual QA + deterministic QA + reverse support/back-entry simulation;
7. create final owner review packet;
8. do not merge, freeze English, publish, or touch the final cover without explicit owner approval.

Modern-props scope is complete.
