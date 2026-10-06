# 2026-10-06 — RSE Production Stack v1 activation

Status: CANONICAL CURRENT DIRECTION / IMPLEMENTATION ACTIVE
Owner: Central RSE Technical Orchestrator

## Owner objective

Move RSE from manual repeated creation into a throughput factory targeting, after stabilization:
- 1–2 production-ready books/week;
- 1 app/content-pack release/week.

This is achieved by reuse and deterministic production, not by spawning more freeform agents.

## Canonical architecture

- `orchestration/architecture/RSE_PRODUCTION_STACK_V1.md`
- `orchestration/architecture/RSE_VISUAL_PAGE_FACTORY_V1.md`
- `orchestration/architecture/RSE_PRODUCTION_AGENT_ROUTING_V1.yml`
- `orchestration/architecture/RSE_BOOK_AGENT_V3.md`
- `orchestration/architecture/RSE_BOOK_MAP_CONTRACT_V1.md`
- `orchestration/architecture/RSE_CONSUMER_PLATFORM_APP_FACTORY.md`

## New operational roles

- `specialized/rse-production-orchestrator.md`
- `specialized/rse-visual-scene-compiler.md`

Existing agents reused:
- Multi-Agent Systems Architect;
- Autonomous Optimization Architect;
- Universal Document Compiler;
- PDF Engine Architect;
- Minimal Change Engineer;
- Mobile App Builder;
- Mobile Release Engineer;
- Image Prompt Engineer;
- Brand Guardian;
- Visual Storyteller;
- UI Finish-Gate Reviewer;
- Test Automation Engineer;
- Reality Checker;
- Workflow Optimizer;
- RSE Book Production Agent.

Do not duplicate these roles.

## Tool stack decision

Use now:
- GitHub / GitHub Actions;
- Playwright;
- Vivliostyle;
- current Book Agent runner/cache/Book Map.

Agent layer target:
- OpenAI Agents SDK / Agents API — handoffs, guardrails, tracing, MCP/tool integration.

Operations glue:
- n8n — notifications, schedules, approvals, external sync; never canonical product logic.

Durable orchestration pilot:
- Temporal, after current Book Agent E2E is stable. Do not block Detective on Temporal migration.

Useful local-execution bridge available to owner:
- Remote Desktop Commander ChatGPT integration can remove repeated manual local terminal/Codex handoffs if owner connects it.

## Active Detective state

Active repo/branch:
`riseshineevolve-source/RISE.SHINE.EVOLVE / feature/rse-book-factory-v2`

Real 180-page baseline no-op: PASS.
Exact V12 hydration: PASS.
Book Agent incremental infrastructure: PASS.

Visual Frontmatter Factory is now queued/authorized:
- `tools/rse-book-factory-v2/schema/visual-scene.schema.json`
- `tools/rse-book-factory-v2/control/frontmatter-page-family-registry.json`
- `tools/rse-book-factory-v2/control/RSE_VISUAL_FRONTMATTER_FACTORY_2026-10-06.md`

Current Pages01–15 taxonomy is frozen as a production input registry, not as final template approval.

## Owner pagination resolution

V12 is current logical page/content authority.
The old 180-page PDF is semantic-role guarded visual/artifact baseline, not physical-number authority where roles differ.

Current logical opening:
- Pages01–15 frontmatter;
- Page16 Case01 Intro;
- Page17 Case01 Witness Board;
- Page18 Case01 Map/Verdict.

No guessed offsets.

Page16 copy-preserving compact variant is authorized; deterministic split/repagination is the fallback if exact copy still cannot fit safely.

Durable active control:
`tools/rse-book-factory-v2/control/V12_PAGINATION_BASELINE_OWNER_RESOLUTION_2026-10-06.md`

## Visual factory owner-gate policy

Do not ask owner to approve all 15 pages separately.

F1:
source → exact scene specs / dependency hashes, no visual gate.

F2:
representative template families only:
- Page03 cinematic invitation;
- Pages07–08 character dossier trio;
- Page04 or Page10 process/menu family.

One contact sheet → one owner family-look decision.

After approval:
scale affected Pages01–15 automatically and review only changed/flagged pages.

## Next implementation sequence

1. Codex completes current V12/Book Map resolution + Page16 fit.
2. Codex executes Visual Frontmatter F1.
3. Build 3 representative template families.
4. Owner gives one visual-family gate.
5. Scale Pages01–15.
6. Extend reusable page families to case pages.
7. Stabilize Book Agent one-command release path.
8. Reuse the factory for the next book.
9. In parallel, wrap existing Consumer/Interactive Book contracts into the shared App Production lane.
10. Add n8n operational glue and then durable Temporal/Agents integration only after stable E2E baselines.

## Anti-regression rules

- no new renderer from zero;
- no whole-page AI final pages;
- no whole-map AI final maps;
- no mass owner review after local change;
- no new app codebase per content pack where shared runtime fits;
- no source fallback to stale versions;
- no agent swarm without contracts/traces;
- no unbounded retries.
