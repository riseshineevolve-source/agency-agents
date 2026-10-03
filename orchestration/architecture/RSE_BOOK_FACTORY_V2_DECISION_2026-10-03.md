# RSE Book Factory v2 — consolidation decision
Date: 2026-10-03
Status: CANONICAL / IMPLEMENTATION PRIORITY #1 FOR BOOK PRODUCTION

## Executive decision

Do NOT start a second unrelated book factory from zero.

RSE already has a substantial Detective Book Factory on:
- repo: `riseshineevolve-source/RISE.SHINE.EVOLVE`
- branch: `feature/detective-book-factory`
- PR: #571
- current head inspected: `e6a531bc6f26b7cafc4fa73b1af5ee549d1c4283`

That factory already contains:
- 30-case source structure;
- V3 canonical text snapshot + source verifier;
- puzzle and spatial validators;
- map-runtime extraction;
- Witness Board source;
- modern-prop contracts;
- KDP preflight;
- 180-page build scripts;
- preview/contact-sheet utilities;
- owner visual hash gates.

The failure was NOT “we have no factory”.
The failure was architectural: content truth, visual rendering and private asset hydration were split across too many layers and renderer versions.

## Diagnosis of the existing factory

### What is valuable and MUST be kept
1. V3 source verifier and locked source invariants.
2. Case matrix / logic ledger / spatial runtime.
3. Map topology and solution validators.
4. Character/source asset contracts.
5. Modern prop footprint validation.
6. KDP/preflight scripts.
7. Owner-visual hash locking.
8. Existing 30-case production knowledge.
9. Existing contact-sheet / preview generation.
10. Existing branch/PR history as provenance.

### What caused repeated regressions
1. ReportLab drawing code mixes layout logic with content decisions.
2. Multiple partially overlapping sources exist:
   - phase YAMLs;
   - production YAML;
   - V3 text master;
   - V3/V4 overrides;
   - local/private hydration masters.
3. Some historical YAML contains obsolete reader text and stale names even when V3 is correct.
4. Build scripts evolved by version (`v3`, `v4`, `v41`, premium/final/finale/audit), creating renderer drift.
5. Visual geometry is hardcoded in Python and difficult to compare to a live 1:1 page editor.
6. Art is a mixture of source rasters, reconstructed/hybrid maps and private local inputs.
7. CI can be green without reproducing the exact private-input premium PDF.
8. Technical PDF/preflight PASS did not guarantee owner visual quality.
9. Approved PNG pages were repeatedly regenerated instead of treated as immutable assets.
10. English and future Polish layouts had no single language-aware overflow contract.

## V2 architecture

### Principle
Separate:
A. CONTENT TRUTH
B. PUZZLE TRUTH
C. DESIGN SYSTEM
D. ASSET TRUTH
E. RENDERER
F. QA

No layer may silently rewrite another.

### Rendering stack
Primary fixed-layout renderer:
- React + TypeScript page components;
- CSS/SVG design system;
- Vivliostyle CLI as the publication/PDF compiler;
- Playwright for browser preview, screenshot tests and visual-regression capture;
- Python/PyMuPDF + existing validators for PDF/puzzle/source preflight.

Do NOT use ReportLab for ordinary page layout in v2.
Keep ReportLab scripts only as legacy reference and for migration comparison until v2 output is accepted.

### Why Vivliostyle
- dedicated book/publication typesetting;
- HTML/CSS source;
- browser preview;
- high-quality PDF;
- supports publication-focused page handling;
- supports print-ready PDF workflows;
- compatible with a React-generated HTML layer;
- easier to tune visually than low-level drawing coordinates.

### Why not Typst as primary
Typst is excellent for deterministic, vector-first documents and remains an evaluation/fallback option, but current Detective pages behave like a graphic UI/graphic-novel layout. React/CSS/SVG maps more directly to the already-approved page visual grammar and allows WYSIWYG browser preview.

### Why not raw Playwright PDF as the only compiler
Playwright remains valuable for snapshots/tests and can output PDF, but v2 should use a publication-oriented paged-media layer rather than relying only on Chromium print behavior.

### PrinceXML
Keep as optional commercial validation/production fallback if Vivliostyle exposes a real blocker. Do not pay for or adopt it before a bounded proof shows need.

## Migration target

Fastest implementation location:
`riseshineevolve-source/RISE.SHINE.EVOLVE/tools/rse-book-factory-v2`

Do not create a new repository yet.
Stabilize the factory beside the existing Detective source first; split into a dedicated repo only after the engine proves reusable.

## Source adapters

### Detective adapter
Canonical reader copy:
`agency-agents/orchestration/detective/DETECTIVE_ACADEMY_BOOK1_TEXT_GOLD_MASTER_V3.md`

Canonical production map:
`agency-agents/orchestration/detective/DETECTIVE_CASES_02_30_PRODUCTION_MAP.md`

Existing old-factory logic/geometry sources are imported only where they do not conflict with current owner locks.

### Frozen pages
Approved opening pages are not re-created immediately.
They enter the v2 manifest as immutable/frozen raster pages with checksum + DPI validation.

This lets publication move while the reusable case engine is built.

## One normalized book model

Create ONE generated normalized JSON model:
`build/content/detective-en.normalized.json`

It is the sole renderer input.

It is produced from:
1. canonical V3 reader copy;
2. explicit owner overrides/locks;
3. puzzle-geometry contracts;
4. asset manifest.

Legacy YAMLs NEVER feed the renderer directly.

Normalizer fails closed if two sources disagree.

## Page manifest

Every physical page has:
- page ID;
- page family;
- source IDs;
- language;
- asset checksums;
- layout template version;
- content checksum;
- puzzle checksum;
- review state.

States:
- FROZEN_RASTER
- TEMPLATE_RENDERED
- OWNER_APPROVED
- NEEDS_REVIEW

## Design system

One versioned theme controls:
- trim / bleed / safe zones;
- typography;
- spacing;
- borders;
- frame geometry;
- icons;
- speech bubbles;
- cool-gray palette;
- map visual grammar;
- Witness Board visual grammar.

No case may invent its own font, header or icon geometry.

## Page component families

1. FrozenPage
2. Publication
3. Recruitment / Intro
4. CharacterProfiles
5. CaseIntro
6. HMComms
7. WitnessBoard
8. LiveMap
9. VisualCompare
10. CodePuzzle
11. TimelinePuzzle
12. ReconstructionPuzzle
13. CaseWall
14. Hint
15. Solution
16. Divider
17. Index
18. Certification / Finale

## Non-negotiable page overflow policy

Never solve overflow by unrestricted font shrink.

Order:
1. normal template;
2. approved compact variant;
3. move HM Comms to dedicated page;
4. split evidence over a second page when source warrants;
5. owner gate.

This is the EN/PL localization safety mechanism.

## Character system

Characters are stable asset IDs, not images selected ad hoc.

Example:
`hm.mimi.portrait.v1`
`hm.dilo.portrait.v1`
`hm.alio.portrait.v1`

Each ID maps to a checksum-locked file.

If Dilo is requested and Dilo asset is missing, build FAILS.
No nearest-match or generation fallback.

## Map system

Keep existing spatial validation and topology.
Replace final visual map drawing with SVG components.

Source geometry owns:
- cells;
- room membership;
- walls;
- doorways;
- blocked/usable states;
- prop footprints;
- answer.

Theme owns:
- wall stroke;
- cool-gray fill;
- room-label rail;
- prop render style;
- map key;
- verdict box.

The same normalized map model renders both live and solution views.

## Golden-page strategy

Case 01 and the approved First20 become the first golden references.

After owner approves one v2-generated Case 02:
- Case Intro golden;
- HM Comms golden;
- Witness Board golden;
- Live Map golden;
- Verdict golden.

Batch rollout may start only after that.

## Visual QA

For every changed template:
- exact-size PNG snapshot;
- contact sheet;
- pixel diff against golden where applicable;
- browser overlay mode;
- text overflow report.

AI reviewer may flag visual concerns, but cannot mutate locked copy/assets automatically.

## Release pipeline

One command must create:
- interior PDF;
- per-page PNG proofs;
- contact sheet;
- manifest;
- source-lock report;
- puzzle-truth report;
- visual-regression report;
- PDF/KDP preflight report.

## Language pipeline

English and Polish share:
- page components;
- design tokens;
- maps;
- asset IDs;
- puzzle geometry.

Different:
- normalized language copy;
- language typography overrides;
- layout variant selection.

Never maintain a separate PL renderer.

## First proof milestone

DO NOT attempt all 180 pages first.

Milestone:
1. ingest owner-approved frozen pages 1–20;
2. normalize Case 02 from current canonical truth;
3. render Case 02:
   - Intro;
   - Witness Board;
   - Map + Verdict;
4. build a PDF containing frozen pages + generated Case 02 proof;
5. produce contact sheet + QA;
6. owner reviews ONE case.

If approved, batch spatial cases.
If not approved, fix template once.

## Implementation order

P0 — source convergence:
- normalizer;
- asset registry;
- page manifest;
- content/puzzle checksums.

P1 — visual engine:
- React fixed pages;
- CSS/SVG theme;
- Vivliostyle build;
- browser preview.

P2 — Detective template proof:
- Case Intro;
- HM Comms;
- Witness Board;
- Map + Verdict;
- Case 02 proof.

P3 — batch spatial cases.

P4 — special case families.

P5 — Hint/Solution/front/backmatter + full EN.

P6 — PL same engine.

P7 — Gentle Steps adapter.

P8 — Optical assembly adapter.

## Kill criteria

Do not continue a renderer approach if:
- it requires hand-editing every case;
- it cannot visually preview 1:1 before PDF;
- it uses a second reader-copy source;
- it silently shrinks text;
- it accepts missing assets;
- it cannot reproduce output from Git commit + asset manifest;
- it requires AI to re-create a final page.

## Definition of success

RSE Book Factory v2 succeeds when:
- one owner-approved template can produce the remaining case family;
- same inputs produce byte-stable or visually stable deterministic outputs;
- English and Polish reuse the same page system;
- a content change requires editing data, not page geometry;
- source truth cannot be lost through renderer fallbacks;
- the owner reviews exceptions, not 180 manually reassembled pages.
