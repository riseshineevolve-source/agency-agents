# Detective Case01 owner-review packet durability gap — 2026-10-05

Status: VERIFIED RELEASE-GATE HANDOFF GAP
Authority: Central RSE Technical Orchestrator
Product writer: delegated Book Production / Detective lane (Central remains read-only on product surface)

## Verified live product state

Repository: `riseshineevolve-source/RISE.SHINE.EVOLVE`
Branch: `feature/rse-book-factory-v2`
Head: `bbe4941ea190d8ef3d2617fe18c1b26c8a562864`

Case01 Pages 16–18 remain `READY_FOR_OWNER_VISUAL_REVIEW`.
G1/G2/G3 PASS; G4 is candidate-only and requires explicit owner visual approval.
Case02 remains `TECHNICAL_PASS_VISUAL_REJECTED_DO_NOT_SCALE`.
English remains NOT FROZEN.

## New durability finding

The durable results file
`tools/rse-book-factory-v2/docs/CASE01_GOLDEN_PARITY_RESULTS.json`
registers the owner-review artifacts and SHA-256 hashes, including:
- `build/case01-golden-parity/case01-reconstructed.pdf`
- `build/case01-golden-parity/case01-golden-contact-sheet.png`
- `page-16/17/18-side-by-side.png`
- overlays/diffs and QA reports.

However the referenced `build/case01-golden-parity/` artifacts are not tracked on the live GitHub branch, and no pull-request workflow artifacts are attached to the relevant Case01/M1 commits.

Therefore GitHub contains proof metadata + hashes but not the actual visual packet needed for remote owner review.

## Release consequence

This is now the shortest concrete blocker before the existing owner gate can be exercised from the canonical remote workflow.

Do not rerender or redesign. The delegated Detective writer should export the already-generated exact review packet losslessly to a durable review surface (tracked owner-review packet or CI artifact), verify every exported file against the registered SHA-256 values, and then stop for owner review.

The existing 24 half-inch safe-zone flags remain a separate print-master blocker after template visual approval; the current parity proof must not be promoted as a publication master.

## Exact next gate

Durable exact-hash review packet available -> owner reviews physical Pages 16–18 -> approve or bounded-correct -> G4 template freeze -> regenerate Case02 on locked template -> Case02 exception review.

No Cases03–30 batch, EN freeze, main merge, or KDP publication is authorized.
