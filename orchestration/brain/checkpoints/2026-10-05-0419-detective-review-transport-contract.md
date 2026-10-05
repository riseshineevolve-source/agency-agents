# Detective Case01 minimum owner-review transport contract — 2026-10-05

Status: VERIFIED / CENTRAL RELEASE-PACKAGE TRUTH
Authority: Central RSE Technical Orchestrator
Product writer: delegated Book Production / Detective lane (Central remains read-only on product surface)

## Live state

Repository: `riseshineevolve-source/RISE.SHINE.EVOLVE`
Branch: `feature/rse-book-factory-v2`
Head: `bbe4941ea190d8ef3d2617fe18c1b26c8a562864`

Case01 physical Pages 16–18 remain `READY_FOR_OWNER_VISUAL_REVIEW`.
G1/G2/G3 PASS; G4 remains candidate-only and requires explicit owner visual approval.
Case02 remains `TECHNICAL_PASS_VISUAL_REJECTED_DO_NOT_SCALE`.
English remains NOT FROZEN.

## Verified transport gap

GitHub contains the durable proof metadata and artifact hashes in:
`tools/rse-book-factory-v2/docs/CASE01_GOLDEN_PARITY_RESULTS.json`.

The actual visual artifacts remain local under:
`tools/rse-book-factory-v2/build/case01-golden-parity/`.

Live remote checks confirm there is currently no usable remote packet path:
- the build directory is not tracked on the active branch;
- there is no open PR whose head is `feature/rse-book-factory-v2`;
- the relevant Case01/M1/current-head commits have no Actions workflow artifacts;
- the repository currently has no GitHub Releases, so there are no release assets containing the packet.

Do not rerender merely to create transport.

## Minimum owner-review packet

The delegated Detective writer can make the existing owner gate executable with only these five exact artifacts, losslessly exported and SHA-256 verified:

1. `case01-reconstructed.pdf`
   SHA-256: `5d0efa1fe779263d7f7ad45da607d70119de1fed704ba2070ced24b3ad8c1e62`
2. `case01-golden-contact-sheet.png`
   SHA-256: `c39757eef7bb58cb59efd4d3c8ad588add7a7c01fb24df837e42be61eb23d9c6`
3. `page-16-side-by-side.png`
   SHA-256: `a7bad91c80ef522ed71bd7cc6d7556f6882f379164fa3f59eabffa6dbda6e2ed`
4. `page-17-side-by-side.png`
   SHA-256: `7c36eb051e7cd4f2b14ed2aee40480484ddcb69419b877cc60fec1f55cb6881a`
5. `page-18-side-by-side.png`
   SHA-256: `a84657d9fad3606085de5d611c9e93d80a3c2d895fdaf03eec439570ea786012`

Overlays, diagnostic diffs and QA JSON remain supporting evidence but are not required for the first owner visual decision.

## Exact next gate

Lossless five-file export + hash verification -> owner reviews physical Pages 16–18 -> approve or bounded-correct -> G4 freeze -> Case02 regeneration on locked template -> Case02 exception review.

The 24 half-inch safe-zone flags remain a separate print-master blocker after template approval.

No Cases03–30 batch, EN freeze, main merge or KDP publication is authorized.
