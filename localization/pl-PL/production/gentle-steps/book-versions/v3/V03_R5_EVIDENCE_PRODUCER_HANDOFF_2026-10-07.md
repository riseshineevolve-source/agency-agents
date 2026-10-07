# Gentle Steps PL V03 R5 — exact-template evidence producer handoff

Date: 2026-10-07
Owner of this handoff: Polish Localization Engine
Consumer/renderer lane: Gentle Steps
Status: READY_FOR_REAL_TEMPLATE_RENDER; this document is **not** evidence of render completion.

## Source to render
Use the exact contents (not retyped or proxy text) of
`localization/pl-PL/production/gentle-steps/book-versions/v3/GENTLE_STEPS_PL_BOOK_VERSION_03_PACKAGING_CANDIDATE_R5_2026-10-07.md`
from `riseshineevolve-source/agency-agents`, branch `codex/polish-engine-main-reconcile`.

Git blob: `04b4afcc438789d648ed34fa594f86ee97b02472`.

The entire book body from `## DZIEŃ 1` to end must remain identical to approved R4 content blob `6a0fbafa1b0fdc1f102c456cd45301d4eef275c2`.

## Consumer lane: minimal return package

The renderer returns an artifact directory with:
- the actual final-template snapshot;
- the complete rendered book PDF;
- 12 exact page/surface reviews saved as PNG or PDF: `front_title_subtitle`, `front_happy_makers`, `front_how_book_works`, `day_24`, `day_18`, `day_09`, `day_01`, `day_23`, `day_07`, `day_21`, `day_22`, `day_10`;
- a JSON evidence manifest with SHA-256 hashes of every artifact and the R5 source, renderer version, reviewer identity and time, actual final-template declaration, explicit no-shrink-to-fit confirmation and each surface's print-scale review flags.

JSON shape is defined by `scripts/localization/gentle_steps_r5_fit.py`, and the preconditions/acceptance rule are specified in `V03_R5_FINAL_EDITORIAL_SAFETY_PROOF_CONTRACT_2026-10-07.json`.

Each surface review must explicitly mark `no_clipping`, `no_collisions`, `diacritics_correct`, `print_scale_reviewed`, `readable` and `copy_complete` as true, and bind `review.render_sha256` to the reviewed file.

The consumer may place artifacts in its own repository, but should return immutable paths and hashes. Do not copy binary evidence into the localization source tree without a defined storage contract.

## Validation

On the localization repository, with canonical R5 file checked out:

```sh
python scripts/validate-gentle-steps-r5-fit-evidence.py --evidence <evidence.json> --artifact-root <artifacts-directory> --output <proof.json>
```

A PASS validates the declared evidence package and source/artifact integrity; it does **not** prove visual quality by itself. The specialist print-scale and editorial/safety checks must still inspect the actual rendered pages.

## Fail-closed rule

No evidence, proxy template, mismatched R5 source, unreadable print-scale rendering, skipped high-density page, or typography shrink-to-fit => no fit PASS. Layout-only issues route back to the Gentle Steps renderer; localization body edits require surgical change control.

Even after PASS, `CONTENT_FROZEN`, `PRINT_READY`, KDP publication and release are **NOT** authorized. Final visual approval and freeze remain explicit owner decisions.

## Detective Academy PL

Remain at pre-freeze infrastructure/readiness only until explicit Detective EN source freeze. No full Detective PL translation work is authorized by this handoff.
