# RSE Production Stack v1 — Book + App Throughput Architecture

Status: CANONICAL TARGET / IMPLEMENTATION AUTHORIZED
Date: 2026-10-06
Owner: Central RSE Technical Orchestrator

## 1. Business objective

Build a production system capable of a sustainable target of:

- **1–2 production-ready books per week**
- **1 production-ready app/content-pack release per week**

without requiring the owner to manually rebuild, re-review, or re-explain unchanged work.

This is a throughput architecture, not a promise that every new title/app can ship in one week regardless of source readiness, art volume, legal/store gates, or owner decisions.

Primary law:

`REUSE > GENERATE`
`DIFF > REBUILD`
`TEMPLATE > REDESIGN`
`EXCEPTION REVIEW > FULL REVIEW`
`DURABLE STATE > CHAT MEMORY`

## 2. One production control plane

RSE production is governed by one hierarchical orchestration layer:

```
RSE Production Orchestrator
├── BOOK lane
│   └── RSE Book Production Agent
├── APP lane
│   └── RSE App Production Lane
├── ART lane
│   └── isolated asset generation only
├── QA lane
│   └── deterministic + specialist finish gates
└── RELEASE lane
    └── channel-specific release controller
```

The Production Orchestrator does not write book copy, draw pages, implement app features, or publish products itself. It owns:

- durable job state;
- routing;
- dependency/impact graph;
- retries and circuit breakers;
- owner-gate budget;
- trace IDs;
- status packets;
- completion criteria.

Default topology is hierarchical orchestrator → specialized workers. No mesh agent swarm.

## 3. Shared production state machine

Every product follows:

```
INTAKE
→ SOURCE_LOCK
→ IMPACT_ANALYSIS
→ TEMPLATE/CONTENT PLAN
→ ASSET_PLAN
→ BUILD
→ AUTOMATED_QA
→ EXCEPTION_REPAIR
→ OWNER_GATE_ONLY_IF_NEEDED
→ FREEZE
→ RELEASE_QA
→ RELEASE_PACKET
→ PUBLISH_EXTERNAL_GATE
```

Every state transition writes durable state to GitHub/project checkpoint.

No workflow is allowed to exist only in chat.

## 4. Shared artifacts across Book and App lanes

Every product gets:

- `PRODUCT_MANIFEST.json`
- `SOURCE_LOCK.json`
- `IMPACT_GRAPH.json`
- `ASSET_PLAN.json`
- `BUILD_STATUS.json`
- `QA_MANIFEST.json`
- `REVIEW_MANIFEST.json`
- `RELEASE_MANIFEST.json`

Book-specific:
- `BOOK_MAP.json`
- page cache
- page/template/freeze records

App-specific:
- `CONTENT_PACK.json`
- runtime contract
- test/build artifacts
- store/release manifest

## 5. Production agent roster

Use existing agents first.

### Always-on control roles

**RSE Production Orchestrator** — NEW
- job routing;
- lane selection;
- progress/state;
- trace IDs;
- retry/fallback logic;
- owner gate minimization.

**RSE Book Production Agent** — EXISTING
- Book Map;
- locks;
- incremental pages;
- book review packets.

### Judgment workers, invoked only when needed

**Visual Scene Compiler** — NEW
- canonical text → structured visual scene spec;
- chooses an approved page family/variant;
- never invents final geometry.

**Visual Storyteller** — EXISTING
- look/visual storytelling critique for new template families only.

**Brand Guardian** — EXISTING
- validates RSE/product visual identity.

**Image Prompt Engineer** — EXISTING
- compiles prompts for atomic asset slots.

**UI Finish-Gate Reviewer** — EXISTING
- approves a new template family after deterministic render.

**Universal Document Compiler** — EXISTING
- schema/layout architecture when a genuinely new document family is introduced.

### Deterministic engineering workers

**Codex**
- adapters;
- schemas;
- renderers;
- caches;
- validators;
- CI;
- integration.

**Minimal Change Engineer** — EXISTING
- bounded correction of one defect without collateral change.

**PDF Engine Architect** — EXISTING
- only when PDF/page-engine geometry itself changes.

**Mobile App Builder** — EXISTING
- implementation in shared app runtime.

**Mobile Release Engineer** — EXISTING
- store/release automation.

### QA / reliability

**Test Automation Engineer** — EXISTING
- deterministic regression suites.

**Reality Checker** — EXISTING
- final product/release reality gate.

**Workflow Optimizer** — EXISTING
- measures bottlenecks and cycle time.

**Multi-Agent Systems Architect** — EXISTING
- changes to orchestration topology, trust boundaries, context and failure recovery.

**Autonomous Optimization Architect** — EXISTING
- cost/latency routing after stable baselines exist; never before.

## 6. What must be code, not an agent

Do not assign agent judgment to deterministic work.

Code owns:
- diffing hashes;
- dependency closure;
- page numbers;
- layout coordinates;
- map geometry;
- text placement inside approved templates;
- schema validation;
- cache reuse;
- image dimensions/DPI;
- PDF assembly;
- app build;
- regression comparisons;
- release checklist state.

Agents may recommend; code proves.

## 7. Book throughput model

Books are produced from reusable families.

### Book type A — baseline-first edition

Use when an approved full-book interior already exists.

`APPROVED BASELINE → SOURCE DIFF → AFFECTED PAGES → APPROVED DELTAS → REASSEMBLE`

Unchanged pages are immutable.

### Book type B — template-first new book

`SOURCE → PAGE TAXONOMY → SCENE SPECS → APPROVED TEMPLATE FAMILIES → ASSET SLOTS → BUILD`

A new title should mostly instantiate existing page families rather than create new design systems.

### Target reuse threshold

For a high-throughput RSE book:
- ≥70% pages use already-approved template families;
- ≥80% recurring assets come from the approved registry;
- ≤20% pages need new owner-visible art decisions;
- owner review packet contains only changed/new/flagged pages.

If a title violates these thresholds, it is a bespoke design project and does not count toward normal weekly factory throughput.

## 8. App throughput model

Do not create a new app codebase for each content product where a reusable runtime can serve it.

Preferred:

`RSE APP SHELL + VERSIONED CONTENT PACK + ASSETS + CONFIG + LOCALIZATION + QA`

Shared runtime capabilities:
- language-neutral content IDs;
- EN + pl-PL;
- offline-first content;
- progress;
- asset bundle;
- accessibility;
- optional identity/sync;
- product-scoped entitlement;
- analytics hooks;
- store metadata/release config.

A weekly app target means **a new content/product configuration on a proven shell**, not a completely new bespoke application architecture every week.

## 9. Tooling decision

### Adopt now

**GitHub + GitHub Actions**
- source of truth;
- checkpoints;
- CI;
- release artifacts;
- immutable evidence.

**Playwright**
- browser/UI automation;
- screenshot capture;
- visual regression;
- app flow testing;
- trace viewer;
- agent/browser automation surface.

**Vivliostyle**
- deterministic HTML/CSS fixed/flow book rendering to PDF.

**OpenAI Agents SDK / Agents API architecture**
- reusable agent definitions;
- handoffs;
- guardrails;
- tracing;
- tool/MCP integration.

Do not migrate working production logic merely to use the SDK. Wrap current Book/App controllers incrementally.

### Adopt as operations glue

**n8n**
Use for:
- notifications;
- scheduled operational workflows;
- handoff alerts;
- publishing checklists;
- external service synchronization;
- owner approval messages.

Do NOT put canonical book layout/puzzle truth or app business logic inside an n8n canvas.

### Pilot after current Book Agent local end-to-end PASS

**Temporal**
Use when RSE has long-running multi-hour/multi-day pipelines that must resume after machine/process failure.

Good candidates:
- full book release workflow;
- app release workflow;
- localization + QA + store release;
- multi-stage asset production.

Do not introduce Temporal into the current Detective critical path before the existing runner proves full local E2E. It is an orchestration reliability upgrade, not a renderer replacement.

## 10. Observability contract

Every production run has:
- `trace_id`;
- `product_id`;
- `lane`;
- `source_sha`;
- start/end timestamps;
- current state;
- agent/tool;
- input artifact hashes;
- output artifact hashes;
- cost/usage where available;
- retry_count;
- final outcome.

No agent call without traceability in production.

## 11. Owner interaction budget

Default weekly production owner interactions:

- source approval/freeze when needed;
- one new template-family look gate only if introduced;
- one new high-value asset-family look gate only if introduced;
- final release packet.

No recurring whole-book review.
No repeated approval of identical character/prop families.
No full app walkthrough after a one-screen copy correction.

## 12. Throughput metrics

Track per product:
- cycle time;
- owner touch count;
- new template count;
- new asset count;
- changed pages/screens;
- unchanged reused pages/screens;
- automated QA pass rate;
- retry count;
- production cost;
- release blockers.

Targets after stabilization:
- owner touches ≤4/product;
- unchanged rebuild rate ≈0%;
- template reuse ≥70% for books;
- app shell reuse ≥80%;
- CI deterministic gate pass before owner packet = 100%;
- unresolved failure never silently converted to PASS.

## 13. 30-day implementation sequence

### Wave A — now
1. Detective Book Agent real local E2E.
2. Visual Page Factory for Detective pages 1–15.
3. Asset registry + atomic asset pipeline.
4. exception-only review packet.
5. stabilize one-command Book Agent.

### Wave B
1. Convert the next suitable RSE book using the same factory.
2. Measure cycle time and eliminate manual steps.
3. Freeze reusable page families.

### Wave C
1. Finish shared App Factory runtime around the existing Consumer/Interactive Book architecture.
2. Convert one real approved content pack.
3. automate Playwright/device QA and release packet.

### Wave D
1. Add n8n operational glue.
2. Pilot OpenAI Agents SDK wrapper around durable agent definitions.
3. Pilot Temporal only if current workflow interruption/recovery remains a material bottleneck.

## 14. Definition of success

RSE Production Stack v1 is successful when:

- a one-line product run resumes from durable state;
- source changes compute exact dependency closure;
- unchanged artifacts are reused;
- only new/changed exceptions reach owner review;
- approved assets/templates never silently drift;
- failed agents/tools retry within bounded policy or degrade/escalate;
- a new book or app mostly selects/feeds existing production components;
- status is visible without reading raw GitHub history or chat.
