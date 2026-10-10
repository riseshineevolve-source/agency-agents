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


## Executable evidence draft producer (2026-10-08)

For the real Gentle Steps renderer, assemble this **actual** final-template artifact
directory (file names are fixed for the helper; use `--template`, `--book` and
`--surface-dir` if your output names differ):

```text
fit-artifacts/
  template/final_template.html
  book/full_book.pdf
  reviews/front_title_subtitle.png
  reviews/front_happy_makers.png
  reviews/front_how_book_works.png
  reviews/day_24.png
  reviews/day_18.png
  reviews/day_09.png
  reviews/day_01.png
  reviews/day_23.png
  reviews/day_07.png
  reviews/day_21.png
  reviews/day_22.png
  reviews/day_10.png
```

From a checkout of this localization branch, with the exact R5 source file
present and unchanged:

```sh
python scripts/create-gentle-steps-r5-evidence-draft.py \
  --artifact-root /path/to/fit-artifacts \
  --renderer-name "ACTUAL_RENDERER_NAME" \
  --renderer-revision "ACTUAL_RENDERER_COMMIT" \
  --output /path/to/fit-artifacts/evidence.draft.json
```

The script verifies the canonical R5 Git blob, verifies that files exist inside
the artifact root, captures each SHA-256, checks basic PNG/PDF signatures and
rejects duplicated review bytes. It **does not render pages** or certify
their quality.

**Safety by construction:** the generated manifest is deliberately blocked:
`surface_kind` remains PENDING, `body_font_reduced_to_force_fit` remains
null, reviewer identity/time are blank and all twelve print-scale review
flags are false. The real reviewer must check the complete PDF and the
twelve exact surfaces, then explicitly attest the actual final template,
legible typography and every review flag. No script may auto-set these flags.

After authentic review, save the completed manifest separately and run:

```sh
python scripts/validate-gentle-steps-r5-fit-evidence.py \
  --evidence /path/to/fit-artifacts/evidence.reviewed.json \
  --artifact-root /path/to/fit-artifacts \
  --output /path/to/fit-artifacts/validation-proof.json
```

Do not mistake this deterministic intake result for the independent editorial,
safety or owner visual gates. No content freeze, print-ready or publication
decision is delegated to the evidence producer.

New focused test additions live in
`scripts/test-localization-gentle-steps-r5-fit.py`. To test the producer
locally (independent of the existing general CI workflow), run:

```sh
python scripts/test-localization-gentle-steps-r5-fit.py
```

The general Polish Localization Regression workflow currently does not call
this focused test script explicitly; a green general workflow must not be
misreported as proof that this suite ran.
