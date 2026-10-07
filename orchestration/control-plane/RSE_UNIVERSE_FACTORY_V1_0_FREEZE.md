# RSE Universe Factory v1.0 — Architecture Freeze

Status: FINAL CURRENT ARCHITECTURE / FROZEN
Date: 2026-10-07
Owner: RSE Technical Orchestrator

## Decision

RSE Universe Factory v1.0 is now the final operating architecture for the current publication/app scale.

Do not redesign the factory in response to a single project defect, agent failure, visual miss, CLI issue or temporary blocker.

Future architecture changes require an ADR with:
- measured problem;
- why v1.0 cannot solve it by configuration/process;
- expected throughput/cost/reliability benefit;
- migration cost/risk;
- rollback plan.

No ADR = no architecture change.

## Final topology

1. Central Control Tower
2. Parallel dedicated product lanes
3. Shared factories:
   - Graphic Gold Library / Book Factory
   - App Factory
   - Localization Engine
   - Asset Vault
4. Deterministic execution backbone:
   - GitHub / GitHub Actions
   - project tests/renderers
5. Interactive heavy worker:
   - ChatGPT Pro / Codex
6. Local exception bridge:
   - Desktop Commander
7. Operations orchestration:
   - n8n
8. Unattended AI exception judgment:
   - Agents API only where deterministic routing is insufficient
9. Temporal:
   - DEFERRED until measured need proves n8n + GitHub checkpoints insufficient

## Parallelism — FINAL RULE

ONE WRITER PER SURFACE does NOT mean one project at a time.

Allowed:
- multiple project lanes active in parallel;
- each lane has its own branch/worktree/source ownership;
- independent subtasks inside one lane may fan out to up to ~4 specialist roles;
- deterministic CI/build tasks may run in parallel;
- if one lane is waiting at an owner/external gate, other safe lanes continue.

Forbidden:
- two writers editing the same branch/worktree/surface;
- two agents independently deciding the same canonical source;
- parallel visual redesign of the same family without a merge authority;
- duplicate full audits/builds that provide no new evidence.

Default portfolio WIP:
- 3 primary finish lanes;
- support/infrastructure lanes may continue when they do not compete for the same writer/worktree or block releases.

Current primary finish lanes:
1. Detective Academy EN / Book Factory
2. Optical Animals KDP
3. Gentle Steps seasonal app/KDP

Support lanes:
- Polish Localization
- World App Factory
- Marketing
- other delegated apps below their gates

## Graphic production — FINAL RULE

The factory is graphic-first.

First Graphic Gold Library is extracted from the strongest owner-created Detective first ~18 pages.

Creative authority:
- Visual Storyteller = visual grammar lead
- Brand Guardian = identity/style veto
- UI Finish-Gate Reviewer = premium family gate
- Universal Document Compiler + Codex = deterministic implementation
- Book Production Agent = family registry/freeze/dependency owner

Codex never invents visual grammar from scratch when an owner Gold reference exists.

Current boxy pilot families are technical evidence only and are not Gold Library visual authority.

## Book pipeline

OWNER/CANONICAL SOURCE
-> source lock
-> semantic page roles
-> Gold Family match
-> scene spec
-> exact Asset Vault references
-> deterministic layout/render
-> automated structural + visual QA
-> bounded specialist review
-> changed/new exception packet
-> freeze
-> assemble
-> release QA

No matching Gold Family -> NEW_FAMILY_REQUEST, not generic-box fallback.

## App pipeline

CANONICAL CONTENT
-> content graph/pack
-> existing shared runtime
-> product config/assets
-> localization
-> deterministic validation
-> Playwright/device QA
-> release packet

New app should usually reuse the runtime rather than create a new codebase.

## Resource routing

1. deterministic script/check
2. GitHub Actions
3. n8n routing
4. Codex/Pro for substantial engineering
5. specialist agents for judgment
6. Desktop Commander only for local-only dependencies
7. Agents API for unattended judgment
8. Temporal only after measured need

## Owner role

Owner should not:
- relay prompts;
- choose which technical agent runs;
- paste routine terminal output;
- re-review unchanged pages;
- manually trigger ordinary deterministic pipelines.

Owner gates remain for:
- new visual family/look;
- material source/editorial choice;
- source freeze;
- pricing/spend;
- privacy/legal/security;
- destructive production mutation;
- publication/store submission.

## Freeze horizon

Keep v1.0 architecture unchanged until BOTH:
- at least one book reaches publication/release candidate through this system; and
- at least one app reaches release candidate through this system;

OR a severity-1 architecture defect proves continuation impossible.

Before that point, fix implementations/configuration, not the architecture.
