# RSE Book Agent — 8-hour execution plan — 2026-10-04

Status: ACTIVE ORCHESTRATOR PLAN
Owner: RSE Technical Orchestrator
Timebox: next 8 hours
Primary objective: move from "working pieces" to a reliable one-command Book Agent without creating another renderer or another competing architecture.

## Working rule

Prefer integration over invention.

Before adding code, ask:
1. does v2 already implement this?
2. does legacy Detective Factory already implement this?
3. can the existing validator/renderer be wrapped instead of rewritten?
4. does this reduce future owner actions?

Do not create a second implementation when an existing one can be adapted.

## Milestone order

### M1 — Incremental Book Map foundation
Codex current slice.

Required:
- Book Map schema;
- Detective Book Map generator;
- stable page input hashes;
- dependency graph + reverse closure;
- page artifact cache;
- changed-page-only build/proof;
- review manifest;
- freeze/unlock records;
- cached unchanged-page assembly;
- isolation regression tests.

Acceptance:
a one-page input change demonstrably leaves unrelated page hashes/artifacts untouched.

### M2 — One-command Book Agent runner
Only after M1 proof.

Add the thinnest possible state-machine wrapper around existing commands:

`book-agent run --book detective-academy --lang en`

The runner must:
- load checkpoint + Book Map;
- compute next required state;
- call existing normalizer/render/QA/cache functions;
- stop only at real source/asset/owner gate;
- write BOOK_STATUS.json.

Do not duplicate renderer or validator logic inside the runner.

### M3 — Owner-light status surface
Generate:
- `BOOK_STATUS.json`
- static `BOOK_STATUS.html`

Show only:
- phase;
- completion;
- total/changed/unchanged/failed pages;
- missing assets;
- failed gates;
- real owner decisions;
- small review packet links.

No application/dashboard framework.

### M4 — Asset-slot inventory
Use current Detective content/runtime/asset registry to emit:
- reusable asset slots;
- missing assets;
- locked assets;
- style-anchor requirements;
- no image generation yet unless an approved backend/credential already exists.

Output:
`ASSET_PLAN.json`

Do not use loose filenames or generate whole pages/maps.

### M5 — Spatial-map deterministic integration plan
Reuse legacy locked runtime and validators.

Machine-only proof:
- runtime geometry -> SVG grid/walls/doors/labels/markers;
- prop slots reference stable semantic asset IDs;
- marker state always comes from runtime;
- no whole-map generative image path.

Do not scale all 15 or create final art before the representative pilot gate.

### M6 — Reliability gate
Run a bounded end-to-end dry run on Detective using currently available locked data.

Required evidence:
- resume after checkpoint;
- cache hit for unchanged pages;
- changed page rebuild only;
- missing locked asset fails closed;
- unrelated frozen page cannot mutate;
- repeated run with no changes is a no-op except status metadata;
- review manifest contains only exceptions.

## Explicit non-goals during this timebox

- no new renderer;
- no broad refactor for cleanliness;
- no Cases03–30 page production;
- no owner-visible redesign;
- no whole-map AI generation;
- no new content writing;
- no EN freeze;
- no PR571 merge;
- no KDP publication.

## Orchestrator behavior

Hourly:
- inspect live branch and new commits;
- verify milestone evidence;
- resolve only source/control blockers deterministically;
- prevent duplicated implementations;
- checkpoint meaningful state;
- if Codex is active, do not race overlapping files.

If M1 completes early, advance to M2 then M3.
M4/M5 are allowed only if they reuse current source contracts and do not create an owner visual gate.
M6 is the preferred endpoint for the 8-hour window.

## Owner action budget

Target during this 8-hour window: ZERO owner actions unless:
- a required external credential is truly necessary;
- canonical source is contradictory;
- an irreversible visual/product decision is reached.

Otherwise continue autonomously.
