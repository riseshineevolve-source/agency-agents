# RSE Book Agent v3 — Universal Deterministic Book Production System

Status: CANONICAL ARCHITECTURE CANDIDATE / IMPLEMENTATION AUTHORIZED
Date: 2026-10-04
Owner: Central RSE Technical Orchestrator
Primary goal: produce repeatable KDP-ready books with minimal owner action and no silent drift.

## 1. Executive decision

Do NOT build another renderer from zero.

Keep the working deterministic core already implemented in:
- repo: `riseshineevolve-source/RISE.SHINE.EVOLVE`
- branch: `feature/rse-book-factory-v2`
- engine: React + TypeScript + CSS/SVG + Vivliostyle + Playwright + Python/PyMuPDF
- legacy validation source: `tools/detective-book-factory/`

Add one missing layer above it:

**RSE Book Agent**

The Book Agent is a stateful production orchestrator. It owns the Book Map, lock graph,
asset plan, incremental build, QA routing and owner-review surface. Codex is one worker
inside this system, not the art director and not the source of product truth.

Architecture:

`NEW-CHAT INTAKE -> ROUTE A/B -> SOURCE CONVERGENCE -> PREMIUM CONTENT UPGRADE -> FROZEN_CONTENT -> BOOK MAP -> LOCK GRAPH -> ASSET SLOTS -> DETERMINISTIC PAGE BUILD -> PAGE CACHE -> PDF ASSEMBLY -> QA -> PRINT_READY -> OWNER RELEASE AUTHORIZATION`

The same inputs must always produce the same page outputs.

## 2. Why v2 did not yet solve the operating problem

The v2 engine solved important mechanical problems:
- source convergence;
- exact puzzle/runtime adapters;
- checksum asset registry;
- fixed Letter rendering;
- PDF/PNG proof generation;
- overflow, source and puzzle QA;
- visual snapshots.

The remaining failure is control-plane architecture:
- Codex was still allowed to interpret prose as visual design;
- full-page generative images were used for geometry-critical maps;
- "visual regression" sometimes meant only repeated output equals itself;
- approved inputs were not represented by one dependency graph with lock scope;
- owner review still operated on pages rather than exceptions;
- a one-item change could trigger broad re-render/review anxiety.

v3 changes these rules without discarding the engine.

## 2A. Mandatory premium-content gate before Book Map

If a manuscript is not already explicitly owner-approved and hash-locked as FROZEN_CONTENT, it MUST start from:

`orchestration/bootstrap/PREMIUM_BOOK_CONTENT_UPGRADE_BOOTSTRAP.md`

and then pass:

`orchestration/architecture/RSE_PREMIUM_BOOK_CONTENT_UPGRADE_PROTOCOL_V1.md`

before Book Map generation.

That protocol owns the editorial stage:

`INITIAL MANUSCRIPT -> SOURCE SNAPSHOT -> CONTENT MAP -> MULTI-AGENT DIAGNOSTIC -> BOUNDED SURGICAL EDITS -> REGRESSION QA -> OWNER-READ CANDIDATE -> REAL-SURFACE FIT -> CONTENT_FREEZE_MANIFEST -> FROZEN_CONTENT`

Permanent rules:
- stable segment IDs are the unit of editorial change;
- KEEP beats rewrite when copy is already excellent;
- many agents may review, but only one controlled writer applies a bounded patch;
- every edit starts from a durable base snapshot and explicit allowlist;
- changes outside the declared scope fail closed;
- mechanics, facts, safety, consent and approved voice are protected;
- full-book rereads occur at milestone gates, not after every local patch;
- layout/rendering may never rewrite frozen copy;
- the Book Map consumes exact frozen content hashes, not chat memory or an informal "latest version".

Required editorial handoff into Book Agent v3:
- selected route (same-language upgrade or cross-language native re-authoring);
- target-language/style profile;
- premium content master path + hash;
- CONTENT_MAP hash;
- GOLDEN_KEEP/source-convergence evidence when applicable;
- CONTENT_FREEZE_MANIFEST;
- unresolved approved exceptions;
- owner-gated decisions;
- QA receipts.

If these are absent, the content is not frozen and production must treat it as an upstream gate rather than silently rewriting it.

## 3. Core operating law

### AI decides only where judgment is genuinely required

AI may:
- normalize content into a schema before it is locked;
- plan asset requirements;
- compile visual prompts from a locked art bible;
- create or edit isolated decorative/illustrative assets;
- inspect contact sheets and flag anomalies;
- recommend corrections.

AI may NOT:
- place canonical text by eye;
- invent page geometry;
- invent puzzle geometry;
- generate final maps as one image;
- choose "close enough" characters or logos;
- alter a frozen page while changing another page;
- rewrite locked copy during render;
- decide that technical PASS equals owner visual approval.

### Code owns deterministic work

Code must own:
- page numbers;
- text;
- coordinates;
- tables;
- diagrams containing labels;
- map walls, doors, cells and markers;
- blocked/occupiable semantics;
- page geometry;
- asset placement;
- hashing and dependency tracking;
- PDF assembly;
- DPI, dimensions, font and grayscale checks;
- incremental rebuild scope.

Rule: **anything with text, numbers, coordinates, puzzle truth or repeatable geometry is rendered by code, not generated as an image.**

## 4. The Book Map — the one source of production truth

Every book must have one machine-readable `BOOK_MAP.json` produced before volume rendering.

It records the complete physical book.

Minimum top-level fields:

```json
{
  "schema_version": "1.0",
  "book_id": "detective-academy-book1-en",
  "edition": "en",
  "trim": {"width_in": 8.5, "height_in": 11, "bleed": false},
  "source_lock": {},
  "design_lock": {},
  "templates": {},
  "assets": {},
  "pages": [],
  "release": {}
}
```

Every physical page record contains at least:

```json
{
  "page_id": "da-en-p019",
  "physical_page": 19,
  "family": "case_intro",
  "render_mode": "template",
  "source_refs": ["case:02:canonical"],
  "template_id": "detective.case-intro.v1",
  "template_sha256": "...",
  "asset_ids": ["hm.alio.portrait.v1"],
  "asset_sha256": {"hm.alio.portrait.v1": "..."},
  "content_sha256": "...",
  "puzzle_sha256": null,
  "page_input_sha256": "...",
  "output_png_sha256": "...",
  "output_pdf_sha256": "...",
  "lock_state": "APPROVED",
  "review_state": "UNCHANGED"
}
```

The Book Map is not generated from chat memory.
It is generated from canonical source files + explicit owner locks.

## 5. Lock graph

Four independent locks exist.

### FROZEN_CONTENT
Canonical text/data may not change.
Layout may reflow only inside an approved template.

### FROZEN_ASSET
Exact visual file + SHA-256.
No regeneration or nearest match.

### FROZEN_TEMPLATE
Component geometry/styles + hash.
Normal content changes do not authorize CSS/template changes.

### FROZEN_PAGE
Entire page output is immutable.
Used for approved raster/vector pages that should be inserted 1:1.

Changing one lock requires an explicit unlock event with:
- target ID;
- reason;
- old hash;
- new hash;
- affected dependent page IDs.

No global "unlock book".

## 6. Content-addressed incremental build

For every page compute:

`page_input_sha256 = SHA256(canonical content + template hash + referenced asset hashes + puzzle hash + book config + renderer version)`

Build rule:
- if `page_input_sha256` is unchanged and cached output exists -> REUSE page artifact;
- if changed -> render only this page and its declared dependents;
- final PDF assembly may change, but unchanged individual page PDF/PNG artifacts remain byte-identical.

The dependency graph therefore answers:
- what changed;
- why;
- which physical pages are affected;
- which pages are guaranteed untouched.

Owner-facing result example:
`3 pages changed / 197 pages unchanged / 0 unexpected dependency changes`.

This is mandatory. A build may not ask the owner to re-review unchanged pages.

## 7. Three page rendering modes

### A. FROZEN
Input is an approved full-page asset.
Renderer verifies hash/aspect/DPI and places it 1:1.

### B. FIXED_TEMPLATE
React/CSS/SVG component populated only from structured data.
Used for Detective case pages, profiles, hints, solutions, puzzle pages and most RSE fixed-layout workbooks.

### C. FLOW_SECTION
For prose-heavy books/sections.
Vivliostyle paginates a locked section/chapter, but that section is one dependency unit.
A change in Chapter 4 cannot invalidate Chapter 1–3 art or source locks.

One Book Agent supports all three modes in one Book Map.

## 8. Universal page-family contract

Every page family has:
- schema;
- template version;
- accepted content slots;
- asset slots;
- overflow variants;
- golden references;
- QA rules.

Template lifecycle:
`DRAFT -> GOLDEN_CANDIDATE -> OWNER_APPROVED -> FROZEN_TEMPLATE`.

An ordinary production page may never create new layout rules.
If content does not fit:
1. standard approved template;
2. approved compact variant;
3. approved split variant;
4. exception gate.

No ad-hoc font shrinking or creative redesign.

## 9. Visual Asset Engine

Generative art is a separate subsystem.

Every required image is an **asset slot**, never an informal prompt.

Example:

```json
{
  "asset_id": "detective.prop.costume_cart.v1",
  "class": "prop_sprite",
  "generation_mode": "ai_new",
  "semantic_id": "costume_cart",
  "style_anchor_ids": ["detective.visual.anchor.v1"],
  "character_reference_ids": [],
  "background": "transparent",
  "text_allowed": false,
  "max_box": "cell_center_safe",
  "status": "NEEDS_ART",
  "approved_sha256": null
}
```

Allowed generation modes:
- `locked_existing`
- `code_svg`
- `ai_new`
- `ai_edit`
- `external_owner_asset`

### Art generation sequence

`ASSET SLOT -> COMPILED PROMPT -> GENERATE/EDIT -> VISION QA -> DETERMINISTIC FINISH -> CONTACT SHEET -> AUTO ACCEPT OR OWNER LOOK GATE -> HASH LOCK`

The prompt is compiled from:
- asset semantic meaning;
- book art bible;
- palette/style tokens;
- style anchor image;
- character identity refs where relevant;
- slot dimensions;
- explicit NOT list.

Prompts are data artifacts with their own hashes.

## 10. What generative image models are allowed to make

Good AI-image tasks:
- character master art;
- hero illustrations;
- decorative scenes;
- spot illustrations;
- isolated props;
- textures/background art;
- surgical edits of existing approved art.

Bad AI-image tasks:
- final maps;
- final diagrams with labels;
- grids;
- witness boards;
- page numbers;
- tables;
- clue text;
- final full book pages with canonical text;
- anything where one changed pixel can change puzzle semantics.

No baked-in page text by default.
Text is overlaid by the deterministic renderer.

## 11. Map engine — reset and permanent rule

The current five hand-generated premium whole-map images are reclassified as:
`STYLE_REFERENCE_ONLY`.

They are NOT production puzzle truth, even when they look good.

Production spatial maps are built as:

`LOCKED RUNTIME GEOMETRY -> SVG GRID/WALLS/DOORS/ROOM LABELS/MARKERS -> APPROVED PROP SPRITES -> VERDICT/UI OVERLAY`

Source/runtime owns:
- grid dimensions;
- cells;
- walls;
- doorways;
- room membership;
- room/zone kind;
- prop cell;
- prop source type;
- variant;
- blocked/occupiable state;
- witness placement;
- answer.

Art layer owns only:
- sprite pixels for a semantic prop ID.

A prop image has no authority to decide whether a cell is blocked or usable.
The renderer always draws the marker from runtime data.

### Map art workflow

For each of the 70 locked source prop types:
1. map to stable semantic presentation ID;
2. generate one transparent sprite outside Codex, using a style anchor;
3. validate alpha/dimensions/no text/allowed footprint;
4. make a prop contact sheet;
5. approve the prop family once;
6. SHA-lock sprite;
7. reuse on every map.

This turns "15 AI-generated maps" into "one deterministic map renderer + a reusable prop library".

Existing legacy validators remain authoritative:
- `validate_modern_prop_contract.py`
- `validate_modern_prop_footprint.py`
- `validate_modern_prop_structure.py`
- `validate_spatial_object_art.py`
- `validate_spatial_source_manifest.py`

Case02/04/06/07/10 premium whole-map outputs may be used as visual inspiration for the prop library only.

## 12. Character engine

One character = one stable identity record.

```text
HM_MIMI
HM_LULI
HM_DILO
HM_ALIO
HM_NINI
HM_BIBI
```

Each ID points to approved:
- face master;
- portrait;
- full-body;
- optional pose family.

All are SHA-locked.

A page asks for `HM_DILO.portrait`.
It never searches a folder and never chooses a similar boy.

If exact asset is absent, build fails.

## 13. Art backend adapters

The Book Agent exposes one interface:

`generateAsset(slot, references, promptSpec) -> candidate asset + sidecar metadata`

Initial recommended backend:
- OpenAI Image API for new isolated art and reference-guided edits.

Optional later adapters:
- ComfyUI/local diffusion for high-volume low-cost variants;
- external owner art;
- other image services only behind the same slot/lock contract.

Backends are interchangeable.
The Book Map and renderer never depend on a model name.

## 14. Deterministic finishing

After generation, code performs:
- crop/alpha cleanup where authorized;
- target canvas padding;
- color/grayscale conversion;
- DPI metadata;
- file naming;
- checksum;
- duplicate detection;
- contact-sheet generation.

AI does not perform these steps.

## 15. PDF pipeline

Keep the current v2 rendering stack.

Fixed pages:
`React/TypeScript + CSS/SVG -> Vivliostyle -> single-page PDF + proof PNG`

Flow sections:
`HTML/Markdown -> Vivliostyle -> section PDF`

Final assembly:
`immutable page/section PDFs -> qpdf merge -> final interior PDF`

Why page/section assembly matters:
a page change does not require recomputing every approved page visual.

Existing PyMuPDF/preflight stays.
Add qpdf structural check/merge.
veraPDF may be an optional additional standards validator; it is not required to ship KDP.

## 16. Automated QA stack

### Source gate
- canonical source IDs;
- content hashes;
- no stale aliases;
- no unauthorized copy mutation.

### Schema gate
- Book Map;
- pages;
- templates;
- asset slots;
- localization contracts.

### Asset gate
- exact ID;
- hash;
- dimensions;
- alpha/background requirement;
- no missing asset;
- no unapproved substitution.

### Puzzle gate
- topology;
- cells;
- walls/doors;
- prop semantics;
- solution uniqueness;
- live/solution parity;
- meta puzzle.

### Layout gate
- overflow;
- clipping;
- overlap;
- minimum font;
- safe margins;
- declared variant only.

### Visual gate
For unchanged input:
- output must be pixel-identical.

For a frozen page:
- exact asset hash / exact placement.

For a locked template with new content:
- structural geometry/mask invariants;
- declared slot positions;
- expected component count;
- black-density/rule checks where useful.

AI visual review is anomaly detection only, not the sole gate.

### PDF/KDP gate
- page count;
- Letter/trim geometry;
- fonts embedded;
- image DPI;
- grayscale/color contract;
- no encryption;
- rotations;
- print-safe line widths;
- final release manifest.

## 17. Exception-only owner review

Owner is NOT a QA worker.

Normal build report:
- total pages;
- changed pages;
- unchanged pages;
- failed automatic gates;
- new assets;
- new template families;
- exceptions.

Owner sees:
- only pages/assets needing a new visual decision;
- one contact sheet per decision;
- before/after/diff;
- exact reason the item needs review.

Review packet limits:
- ordinary local change: changed pages + at most one page of context on each side;
- new template family: 1–3 representative pages;
- new asset family: one contact sheet;
- full-book milestone: flagged pages + representative sample, not 200 individual pages.

A complete 200-page contact sheet can be generated for archive/AI audit, but is not an owner task.

## 18. Owner action budget

Target for an ordinary new RSE book:

1. SOURCE/PRODUCT gate — only if source ambiguity exists.
2. LOOK LOCK — one visual contact sheet.
3. TEMPLATE FAMILY gate — only once per genuinely new family.
4. EXCEPTION gate — only if automatic checks cannot resolve an anomaly.
5. FINAL RELEASE gate — cover, final report, representative physical proof.

Everything else is autonomous.

For a sequel using already-approved templates/assets, actions 2–3 should usually disappear.

## 19. Agent routing

### RSE Book Agent
Single operational owner.
Maintains state and decides the next deterministic step.

### Codex
Use only for:
- implementation;
- schemas;
- adapters;
- deterministic renderers;
- validators;
- test repair;
- incremental build logic.

Codex must NOT:
- art direct;
- generate page visuals by taste;
- choose character identities;
- approve owner-visible design;
- regenerate a whole approved page to fix one local defect.

### PDF Engine Architect
Used when page/PDF geometry or export engine changes.

### Image Prompt Engineer
Used to compile reusable asset prompts from the art bible/slot spec.

### Brand Guardian / Visual Storyteller
Used for the initial look lock or a new visual family, not every image.

### Test Automation Engineer
Owns regression harnesses and changed-page verification.

### UI Finish-Gate Reviewer
Used at template-family milestone.

### Reality Checker
Used once at final release gate.

### Minimal Change Engineer
Used for a bounded correction where "change only X" is the requirement.

Do not use an agent swarm for ordinary builds.

## 20. Workflow state machine

```text
INGEST
  -> NORMALIZE
  -> BOOK_MAP_LOCK
  -> LOOK_LOCK
  -> TEMPLATE_LOCK
  -> ASSET_PLAN
  -> ASSET_BUILD
  -> ASSET_LOCK
  -> BUILD_CHANGED
  -> AUTO_QA
  -> EXCEPTION_REVIEW (only if needed)
  -> FULL_ASSEMBLY
  -> RELEASE_QA
  -> OWNER_RELEASE_GATE
  -> RELEASED
```

Every transition has a durable checkpoint.
A failed run resumes from the last completed state.

## 21. CLI contract

Target commands:

```text
book-agent status --book <id>
book-agent plan --book <id>
book-agent build --book <id> --changed
book-agent proof --book <id> --changed
book-agent assets --book <id> --needed
book-agent qa --book <id> --changed
book-agent release-candidate --book <id>
```

One normal command for daily work:

```text
book-agent run --book <id>
```

It detects current state and executes until:
- a real owner decision;
- a missing external asset/source;
- release gate.

## 22. User-facing dashboard

Generate a static `BOOK_STATUS.html` and JSON, not a new complex web app.

Must show:
- current phase;
- book completion;
- page count;
- changed / unchanged / failed pages;
- locked templates;
- locked assets;
- missing assets;
- automatic QA;
- owner decisions required;
- direct links to small review packets.

No owner should need to inspect Git logs to understand the book.

## 23. Detective Academy migration

Immediate Detective rules:

1. Preserve current v2 source convergence and Case01 template work.
2. Do not scale the rejected generic Case02 template.
3. Treat current Pages 1–18 as manifest slots; freeze each only after its exact production asset decision.
4. Final spatial maps are reconstructed from locked runtime + vector geometry + approved atomic prop sprites.
5. Whole AI-generated premium map pages become style references, not puzzle truth.
6. Case01 page-family visual approval locks the three spatial-family templates.
7. Case02 then becomes a data substitution test, not a design task.
8. When Case02 passes all automatic gates, batch other spatial cases mechanically.
9. Owner gets only the changed/exception packet.
10. Full English build occurs only after page families and required art assets are locked.

## 24. Reuse across RSE

### Detective Academy PL
Same Book Map structure, templates, assets and puzzle hashes.
Only language copy and declared typography/overflow variants differ.

### Gentle Steps
Reuse engine, Book Map, incremental build, asset slots, PDF assembly and QA.
Add Gentle Steps page families and art bible.

### Optical Animals
Mostly FROZEN/ASSET pages.
Reuse Book Map, exact image locks, page assembly, DPI/preflight and release pipeline.

No separate factory per title.

## 25. External patterns adopted

Adopted concepts:
- checkpointed workflow state after each successful stage;
- art bible + look lock;
- visual style anchors/reference images;
- atomic image asset pipeline;
- deterministic post-processing;
- contact-sheet review;
- "code for anything with text or data";
- model/backend routing behind an adapter.

Do not copy external repos wholesale.
Implement the useful patterns inside current RSE source/asset contracts.

## 26. Definition of done

RSE Book Agent is done when:

- one command resumes from current book state;
- a source change invalidates only dependent pages;
- unchanged page artifacts remain immutable;
- ordinary pages need no manual placement;
- generative art is isolated from canonical geometry/text;
- a map cannot change logic because of image generation;
- missing/changed character or logo fails closed;
- owner sees only exceptions/new visual decisions;
- same locked inputs yield same pages;
- full PDF assembles deterministically from locked page/section artifacts;
- one release report proves source, assets, puzzle truth, visual locks and print preflight;
- Detective EN can be built without reviewing hundreds of unchanged pages;
- PL and future books reuse the same engine.
