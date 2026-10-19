# RSE Book Factory v2 — Execution Bootstrap

Date: 2026-10-03
Status: ACTIVE

You are the dedicated implementation owner for RSE Book Factory v2.

## Read first

1. `orchestration/brain/RSE_BRAIN_MASTER.md`
2. `orchestration/RESUME_FROM_ZERO.md`
3. `orchestration/architecture/RSE_BOOK_FACTORY_V2_DECISION_2026-10-03.md`
4. `orchestration/architecture/RSE_BOOK_FACTORY_EXISTING_ASSET_MIGRATION_2026-10-03.md`
5. `orchestration/bootstrap/DETECTIVE_FIRST18_EXECUTION_BOOTSTRAP.md`
6. `orchestration/detective/DETECTIVE_CASES_02_30_PRODUCTION_MAP.md`
7. `orchestration/detective/DETECTIVE_KDP_REGRESSION_GATE.md`

Then switch to:
repo `riseshineevolve-source/RISE.SHINE.EVOLVE`
branch `feature/rse-book-factory-v2`

Read:
- `tools/rse-book-factory-v2/PROJECT_BRIEF.md`
- `tools/rse-book-factory-v2/AGENTS.md`
- `tools/rse-book-factory-v2/CHECKPOINT.yml`

Inspect the existing migration source:
`tools/detective-book-factory/`

## Mandatory editorial preflight

Before any new book/edition enters page production, verify whether its content is already explicitly owner-approved and hash-locked as `FROZEN_CONTENT`.

If NOT, do not start layout/rendering. Route upstream to:

1. `orchestration/bootstrap/PREMIUM_BOOK_CONTENT_UPGRADE_BOOTSTRAP.md`
2. `orchestration/architecture/RSE_PREMIUM_BOOK_CONTENT_UPGRADE_PROTOCOL_V1.md`

Book Factory must receive an exact `CONTENT_FREEZE_MANIFEST` + premium master hash. It may not select an informal "latest" draft or improve copy during rendering.

Keep `CONTENT_APPROVED`, `FROZEN_CONTENT`, `PRINT_READY` and `RELEASE_AUTHORIZED` as separate states.

## Mission

Do NOT create another unrelated factory.
Migrate the validated source/logic/QA capabilities of the existing Detective Book Factory into a clean generalized v2 engine.

## Technology decision

Primary:
- React + TypeScript
- CSS + SVG
- Vivliostyle CLI publication build
- Playwright visual-regression screenshots
- existing Python validators + PyMuPDF/preflight

Legacy ReportLab renderer is comparison/reference only after v2 visual components exist.

## Phase 0 — source convergence

Implement before page styling:
1. exact V3 source adapter;
2. owner-lock adapter;
3. puzzle/spatial contract adapter;
4. asset registry with checksum locks;
5. normalized JSON model;
6. conflict detector: fail if legacy and canonical reader copy disagree;
7. page manifest.

No renderer component may read legacy phase/production YAML directly.

## Phase 1 — fixed-page engine

Build:
- exact 8.5x11 page shell;
- safe margin overlay;
- theme tokens;
- typography tokens;
- asset ID resolver;
- FrozenPage component;
- HTML preview;
- Vivliostyle PDF output;
- per-page PNG proof;
- contact sheet.

## Phase 2 — Detective master family

Build:
- CaseIntro;
- HMComms;
- WitnessBoard;
- LiveMap;
- VerdictBox.

Rules:
- use Case 01/First18 owner-approved grammar;
- no AI-generated page copy;
- no invented visual props;
- characters by exact locked ID;
- maps from exact topology;
- no font shrink below minimum;
- overflow => approved variant/split.

## First proof

Render ONLY Case 02 plus any frozen owner-approved opening pages available.

Deliver:
- PDF proof;
- individual page PNGs;
- contact sheet;
- normalized Case 02 JSON;
- page manifest;
- source-lock report;
- puzzle-truth report;
- visual-regression report;
- PDF preflight.

## Stop gate

STOP for owner visual review when Case 02 proof is ready.

Do not batch Case 03–30 until Case 02 page family is explicitly accepted.

## Important

Do not mutate active FIRST18 source/output.
Do not merge legacy PR #571.
Do not label Detective EN frozen or KDP-ready.
