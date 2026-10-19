# Gentle Steps PL V03 R5 — exact-source fit guards integrated into CI

Date: 2026-10-08
Lane: Polish Localization Engine
Status: R5_FIT_GUARDS_IN_CI__EXACT_TEMPLATE_EVIDENCE_STILL_PENDING

## Authority
- Started from `orchestration/bootstrap/POLISH_LOCALIZATION_EXECUTION_BOOTSTRAP.md`.
- GitHub/durable state is authoritative over chat memory.
- Central RSE priorities changed: NO.
- CONTENT_FROZEN / PRINT_READY / publication authorized: NO.

## Source preservation
- PL R4 final content blob: `6a0fbafa1b0fdc1f102c456cd45301d4eef275c2`.
- PL R5 packaging blob: `04b4afcc438789d648ed34fa594f86ee97b02472`.
- Gentle Steps PL body copy changed in this slice: NO.
- Exact real-template render evidence returned by consumer lane: NO.

## Freshness
Pre-slice implementation HEAD: `6a037ddf29881684928251883edd0e3d09b0c248`.
Before the CI integration write:
- branch was 521 commits ahead / 20 behind `main`;
- no localization-owned overlap requiring reconciliation was identified;
- no blind merge was performed.

## CI integration
Commit:
`91e876d5739519886a7cfdb7eae17222d3f84ade`

Updated:
`.github/workflows/polish-localization-regression.yml`

Changes:
1. trigger the localization workflow when the R5 evidence producer changes;
2. trigger it when the R5 evidence validator CLI changes;
3. execute `python scripts/test-localization-gentle-steps-r5-fit.py` as a required regression step.

## Exact implementation-head verification
GitHub Actions:
- Polish Localization Regression run #401: SUCCESS.
- The new step `Test Gentle Steps PL R5 exact-source fit evidence guards`: SUCCESS.
- Existing terminology, Detective source guard, localization engine, bilingual backcheck, native re-authoring, fixture QA and artifact upload steps: SUCCESS.

At checkpoint creation time the other repository-wide workflows on the same implementation HEAD were either SUCCESS or still completing; no failure was observed.

## Remaining production dependency
The consumer Gentle Steps repository still contains no exact-source-bound real-template evidence for R5 blob:
`04b4afcc438789d648ed34fa594f86ee97b02472`.

Therefore the next safe action remains:
1. consume the exact R5 final-template PDF + required print-scale surfaces;
2. run `V03_R5_FINAL_EDITORIAL_SAFETY_PROOF_CONTRACT_2026-10-07.json`;
3. if PASS with zero unresolved BLOCK/FIX, stop for owner visual approval and explicit content-freeze authorization.

## Detective Academy PL
Status remains PRE-FREEZE INFRASTRUCTURE ONLY.
Full production translation started: NO.
Required gate: explicit Detective EN freeze.

## Stop boundary
Do not authorize:
- CONTENT_FROZEN
- PRINT_READY
- KDP publication
- release
