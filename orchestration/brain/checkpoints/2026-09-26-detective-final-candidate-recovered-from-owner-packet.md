# Detective Academy — final candidate recovery checkpoint

Date: 2026-09-26
Execution owner: central RSE Technical Orchestrator
English freeze: **FALSE**

## Material recovery

The previously local-only final English owner-review candidate is now recoverable from the owner packet `final-book-owner-review(1).zip`.

Verified packet SHA-256:

`55439b308d6d7a2db7b40485665bcc46aceeb9dffde528afffb276790378680c`

The packet contains the exact 146-page release candidate:

`01_FINAL_PDF/HMDA_Book1_EN_Interior_Release_Candidate.pdf`

Verified PDF SHA-256:

`313d9f4821f68da88fa51bcac03070594f9447e8ae9f99b7fbecceb045adeae0`

This exactly matches the SHA recorded in the earlier final-interior checkpoint.

The packet also contains the generated final source/runtime recovery material needed to avoid reconstructing from the stale remote PR head:

- `01_FINAL_PDF/book1_en_master_owner_review_v41.yml`
- `01_FINAL_PDF/book1_en_master_owner_review_v4.yml`
- `01_FINAL_PDF/hmda_spatial_runtime_v4.json`
- all 146 rendered page PNGs
- all four owner-locked visual PNGs plus their manifest/hashes
- approved all-15 map rasters and QA reports
- Case 03 exact-ten reconciliation/logic reports
- print/typography/full-PDF integrity reports
- artifact SHA manifest

Owner visual hashes recovered from the packet remain:

- `book2_archive_photo.png` — `44d46ec319b483e10bc6cc5b5b1742e29cf2a219deb9500d412433f1781283db`
- `case03_photo_A.png` — `1763fb5881da7ff144fa1d32bbf6b2fc711233d156bf5b50e7f38fe85e60a1cd`
- `case03_photo_B.png` — `7ad6f8d9773dc09819d36d5ac708db43144ff48f00251a2aa919dd9f17cd247a`
- `case03_solution.png` — `82d2348231013f34ceb712d68c5b101d72853d750c26ac1f63d967b9b1c67fad`

Case 03 recovery report is PASS with exact mechanic `FIND ALL 10 DIFFERENCES`, number card `017 / 071`, zero stale active terms, and neutral Room Zero record `INTAKE-03`.

## Remote state / collision safety

Remote PR #571 remains on `1fed50b7e969c60da1a1b9d743665473ceb15049`.

The recovery branch `rse/detective-final-polish-audit-20260926` also still points to that same stale head.

The local finalization commit recorded by the earlier checkpoint, `64b4c0787ea984efd3e155e00de2da2fab9e59d7`, is not present in GitHub.

Therefore:

- do **not** patch the stale remote branch directly;
- do **not** recreate Case 03, owner visuals, map geometry, or locked logic from chat/history;
- use the recovered owner packet as the byte-verified bridge back to the final candidate state;
- reconcile source before any future branch push so there is only one writer surface.

## Remaining bounded final-polish scope

The fresher independent audit remains authoritative. Before owner approval, apply only:

1. p.107 Room Zero climax: six badge hooks with 01–05 occupied and 06 resolving to Detective Six / OFFICIAL CALL SIGN; replace the equal-box-wall feel with a stronger payoff hierarchy.
2. p.003: replace the stale shield/torch/laurel Academy identity with the current question-mark/scanner identity without changing the locked squad.
3. Case 02 brief: align with the locked title that the trophy **never reached the shelf**.
4. Mechanical US-English normalization across active reader-facing copy.

Then rebuild the 146-page candidate and rerun targeted + full deterministic/visual QA.

## Gates preserved

No merge, English freeze, Polish scale-out, KDP upload, publication, price/cover change, ISBN decision, or owner-gated Book 2 archival interpretation decision is authorized by this recovery.
