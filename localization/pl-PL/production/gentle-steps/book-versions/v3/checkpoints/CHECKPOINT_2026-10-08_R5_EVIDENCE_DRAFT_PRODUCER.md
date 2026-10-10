# Polish Localization — Gentle Steps PL R5 evidence producer checkpoint

Date: 2026-10-08
Lane: Polish Localization Engine
Status: R5_EVIDENCE_DRAFT_PRODUCER_IMPLEMENTED__ACTUAL_TEMPLATE_RENDER_PENDING

## Authority and boundaries
- Started from `orchestration/bootstrap/POLISH_LOCALIZATION_EXECUTION_BOOTSTRAP.md`.
- Reconstructed current RSE Control Plane, lane registration, dependency mailboxes, branch, PR #13 and CI from GitHub.
- One writer for localization-owned surfaces only. Main/central priorities unchanged.
- No authorization of CONTENT_FROZEN, PRINT_READY, KDP publication, or release.
- Detective Academy PL remains PRE-FREEZE INFRASTRUCTURE ONLY.

## Exact Gentle Steps content integrity
Read both current GitHub blobs directly:
- R4: `6a0fbafa1b0fdc1f102c456cd45301d4eef275c2`
- R5: `04b4afcc438789d648ed34fa594f86ee97b02472`

From the first `## DZIEŃ 1` marker to the end, R4 and R5 are identical:
59,207 characters / 1,306 lines, 24 daily sections, 24 each ZWOLNIJ,
GRAMY, MIĘDZY NAMI and NA JUTRO. No manuscript copy changed.

## New reusable producer artifact
Added `scripts/create-gentle-steps-r5-evidence-draft.py`.
It produces a content-hash-bound evidence JSON from actual renderer files,
verifies source and artifact paths, basic PNG/PDF signatures and uniqueness,
and requires explicit renderer identification.

Critical safety: all generated review flags remain FALSE, reviewer name/time
remain blank, final-template status remains PENDING and the typography
no-shrink assertion remains NULL. The draft is deliberately unable to PASS the
existing evidence intake validator until independent real print-scale review.

Added three focused tests to
`scripts/test-localization-gentle-steps-r5-fit.py`:
1. exact source/hash draft is unapproved;
2. duplicate render bytes are rejected;
3. path escape and non-PDF full-book output are rejected.

Expanded the consumer-facing executable handoff:
`localization/pl-PL/production/gentle-steps/book-versions/v3/V03_R5_EVIDENCE_PRODUCER_HANDOFF_2026-10-07.md`
with real artifact-directory structure and exact draft/validation commands.

Source blobs at this checkpoint:
- producer script: `c3f4bc05535401df1105f4c5cd98a2e8331f597f`;
- focused test script: `9af5ac51fafa2c813bad4b0bf41306c6b91f28a1`;
- handoff document: `72ac4c67ef238c0a32fa21948b75c61f97edbde4`.

## Freshness, PR and CI
- PR #13 remains OPEN/DRAFT and targets `main`.
- Before this checkpoint: `main` was 18 commits ahead of the branch's
  merge base; localization branch was 516 commits ahead and 18 behind.
- Main-side changed paths were 15; localization-owned overlap was zero.
  No blind merge, rebase or reset performed.
- Pre-slice exact-head `e2454c289aba04692166da3705b191fb554f09c8`:
  all 11 GitHub workflows SUCCESS.
- Post-implementation exact-head `59d1025377b30ed25d03d73386b34eca90b4f992`:
  Polish Localization Regression SUCCESS, other workflows were still settling
  at observation time.
- The focused R5 validator tests are NOT explicitly executed by the current
  general CI workflow. Workflow-wiring edit was attempted but blocked by tool
  safety checks; do not misreport these 13 focused tests as CI PASS.
- Remote Desktop Commander and local Python runner were unavailable during
  this run; the new producer/tests were not locally executed.

## Consumer evidence and real gate
Inspected the live Gentle Steps app branch file tree on GitHub:
`riseshineevolve-source/RISE.SHINE.EVOLVE`,
`gentle-steps/app-en-full24-purple-gold`. No exact R5 final-template
render evidence files were present.

Required next:
1. consumer renders exact R5 blob in actual final book template;
2. consumer uses new helper to build a draft manifest from real artifacts;
3. independent print-scale review explicitly attests all twelve surfaces;
4. localization runs strict evidence validator plus final editorial/safety proof.

Only then is the owner gate: final visual approval + explicit content freeze.
Detective PL full translation remains prohibited pending explicit EN freeze.
