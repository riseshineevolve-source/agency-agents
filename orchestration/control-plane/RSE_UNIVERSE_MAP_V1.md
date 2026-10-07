# RSE Universe Map v1 — Final Operating Model

Status: CANONICAL CONTROL-PLANE MAP
Date: 2026-10-07
Owner: RSE Central Control Tower
Primary durable repo: riseshineevolve-source/agency-agents

## North star

RSE is operated as one portfolio factory, not a set of independent chats.

Target after stabilization:
- 1–2 production-ready books/week;
- 1 app/content-pack release/week;
- marketing and localization consume the same locked product truth;
- owner intervention only for meaningful creative/commercial/legal/release gates.

Core laws:
- GitHub/current durable repository state > chat memory.
- ONE WRITER PER SURFACE.
- REUSE > GENERATE.
- DIFF > REBUILD.
- TEMPLATE > REDESIGN.
- EXCEPTION REVIEW > FULL REVIEW.
- deterministic checks before agent judgment.
- agents add expertise; they do not become new sources of truth.

## Control-plane topology

```
OWNER
  |
RSE CENTRAL CONTROL TOWER
  |-- priorities / strategy / dependency routing / shared truth / owner gates
  |-- reads every lane
  |-- writes central Brain + Control Plane only
  |
  +-- BOOK FACTORY / DETECTIVE ACADEMY
  +-- OPTICAL ANIMALS
  +-- GENTLE STEPS / BEFORE CHRISTMAS SLIPS BY
  +-- POLISH LOCALIZATION ENGINE
  +-- WORLD 01 + WORLD 02 / INTERACTIVE APP FACTORY
  +-- HAPPY ME 24/7
  +-- SENIOR / HELLO TODAY + MIND BLOOM bounded lane
  +-- UNSTOPPABLE / BOOK-FIRST
  +-- OPINIE
  +-- MARKETING AUTOPILOT
```

RSE Quick Desk remains an optional read-only/front-door chat. It may answer status and prepare owner decisions, but it is not a parallel writer.

## Shared cross-chat communication

Chats do not rely on one another's conversation history.

They communicate through:
1. project repository checkpoint;
2. project branch/head/CI;
3. one lane-owned mailbox under `orchestration/control-plane/mailboxes/`;
4. central Control Tower reconciliation.

Every mailbox has exactly ONE writer: the chat that owns that lane.
All other chats may read it.

A lane writes its mailbox only when one of these changes:
- milestone;
- blocker;
- owner gate;
- dependency needed from another lane;
- reusable component produced;
- source/freeze/release state.

No chat edits another lane's mailbox.

## Portfolio lanes

### 1. RSE Central Control Tower
Owns:
- company/brand/business strategy;
- commercial sequencing;
- shared architecture;
- cross-project dependencies;
- owner gates;
- central Brain / Control Plane;
- AI Discovery/website coordination where no dedicated writer owns the surface.

Does NOT write product lane source while a delegated writer is active.

Default specialist squad:
- RSE Production Orchestrator
- Multi-Agent Systems Architect
- Workflow Architect
- Automation Governance Architect
- Business Strategist when strategic decision is genuinely needed

### 2. Detective Academy / Book Factory
Commercial priority: highest current finish lane.

Owns:
- Detective EN production;
- reusable Book Factory v3 implementation currently co-located with Detective;
- official Happy Makers identity pack;
- deterministic page families / scene specs;
- puzzle/page QA;
- KDP interior packaging below owner gates.

Current branch family:
`feature/rse-book-factory-v2`

Current operating rule:
Book Factory chat is the writer. Central is read/sync-only.

Agent squad:
- RSE Book Production Agent
- RSE Visual Scene Compiler
- Brand Guardian
- Visual Storyteller
- Image Prompt Engineer
- Test Automation Engineer
- UI Finish-Gate Reviewer
- Minimal Change Engineer
- PDF Engine Architect only for PDF-engine changes

Tools:
GitHub, Desktop Commander, Codex, Playwright, Vivliostyle, image generation/editing for atomic assets only.

### 3. Optical Animals
Owns:
- Final 20 exact source set;
- premium optical-animal art production where still owner-authorized;
- exact-identity masks/tokens;
- seek-and-find pages;
- answers/proof/KDP packaging.

Branch:
`feat/optical-animals-book-creator`

Rules:
- approved final hero art stays byte-for-byte unless a concrete blocker is proven;
- exact tokens come from exact source pixels;
- image agents may improve art only when that slot is explicitly open;
- no AI lookalikes as final seek-and-find identity tokens.

Useful agents:
Image Prompt Engineer, Visual Storyteller, Brand Guardian, Reality Checker, Test Automation Engineer.

### 4. Gentle Steps / Before Christmas Slips By
Owns:
- current EN/PL 24-day product source;
- EN+PL Advent app;
- PL KDP production fit where active;
- product visual runtime and release readiness.

Branch family:
`gentle-steps/app-en-full24-purple-gold`

Polish language truth is consumed from Polish Localization Engine outputs; this chat does not independently rewrite PL after a localization lock.

Tools:
GitHub, Desktop Commander, Codex, Playwright/device QA; image generation for product assets only.

### 5. Polish Localization Engine
Owns:
- localization framework;
- project voice profiles;
- terminology;
- linguistic QA;
- source-to-PL transformation artifacts.

Current rule:
- Gentle Steps PL may consume it now;
- Detective PL full-book production waits for explicit Detective EN freeze;
- no literal translation where transcreation profile says otherwise.

It may READ product lane sources and WRITE only localization-owned surfaces.

### 6. World 01 + World 02 / Interactive App Factory
Owns:
- source-proven content graphs;
- reusable interactive book runtime;
- World 01/02 product packs;
- reusable content-pack/app-factory improvements required by real slices.

World 02 canonical published source overrides legacy app copy.

Does not block Gentle Steps seasonal lane.

Tools:
GitHub, Codex, Playwright, app/runtime test stack, Desktop Commander when local/device evidence is required.

### 7. Happy Me 24/7
Owns:
- Happy Me Adventures source hardening;
- UI/UX/device readiness;
- Play/internal-test preparation.

Production Supabase restoration remains owner/cost gated.
Central does not write Happy Me branch while this lane is active.

### 8. Senior / Hello Today + Mind Bloom
One dedicated chat may own both with strict split-project rules and separate worktrees.

Senior:
- active app/product completion and release hardening;
- production/device/legal gates preserved.

Mind Bloom:
- private single-owner deployment/privacy completion only;
- ordinary feature development frozen unless explicitly reopened;
- provider/OAuth Phase 2B remains owner-gated.

No shared source between the two repos.

### 9. Unstoppable / Book-First
Owns:
- Project Unstoppable book-first safer-copy / KDP revival;
- bounded content and production sync on its dedicated branch.

Central and Marketing read product truth; they do not rewrite its source.

When reusable Book Factory components are needed, consume frozen Book Factory interfaces rather than forking new renderer code.

### 10. Opinie
Owns:
- sanitized/synthetic code and deterministic tooling in remote repos;
- confidential real case data remains LOCAL/OFFLINE.

Desktop Commander may be used for local-only real-data work.
No real case content, embeddings, evidence or outputs are uploaded to GitHub/Drive/remote agents unless explicitly sanitized and authorized.

### 11. Marketing Autopilot
Owns:
- content engine;
- channel adaptation;
- organic scheduling operations;
- performance memory;
- campaign drafts;
- product launch coordination from VERIFIED product truth.

Product repos are READ-ONLY to Marketing.

Tools:
Metricool, Creative Claw, GitHub, Drive, Gmail where useful, native analytics/connectors when verified.
No paid activation without owner authorization.

## Shared factories

### Book Factory
Current implementation lives with Detective until stable generic extraction.

Contract:
source lock -> Book Map -> lock graph -> scene specs -> asset slots -> deterministic render -> page cache -> QA -> exception review -> release.

Future books reuse family libraries before creating new templates.

### App Factory
Contract:
canonical source/content pack -> language-neutral IDs -> shared runtime -> localization -> offline-first QA -> release packet.

A weekly "new app" should usually be a new content pack/config on a proven shell, not a brand-new codebase.

### Localization Factory
English/master source lock -> project-specific transcreation profile -> deterministic terminology/invariant checks -> human/owner exception gate -> PL lock.

### Asset Factory
asset request -> exact identity/style references -> generation/editing -> QA -> SHA lock -> registry -> consuming pages/screens.

AI may create isolated visual assets.
AI must not create final text-heavy book pages, semantic maps, puzzle coordinates, final tables or canonical copy as pixels.

## Tool stack

### Active now
- GitHub / GitHub Actions — durable technical truth.
- Desktop Commander Remote — verified local Windows bridge for filesystem/terminal/local builds.
- Codex — bounded implementation worker.
- Playwright — browser/screenshots/visual regression.
- Vivliostyle — book HTML/CSS -> PDF.
- image generation/editing — atomic art assets and approved visual edits.
- Metricool — marketing operations.
- Creative Claw — video/media production when it adds value.
- Google Drive / Library — heavy masters when manifests point there.
- Supabase — project-specific backend when authorized.
- Gmail — communication workflows when needed.

### Next control-plane integrations
- n8n: operations glue, triggers, notifications, approval routing, scheduled syncs.
- OpenAI Agents SDK / Agents API: programmatic agent definitions, handoffs, guardrails and tracing.
- Temporal: durable long-running workflow execution after stable lane E2E exists.

Do not migrate working critical-path renderers merely to adopt orchestration technology.

## Owner intervention target

Normal lane:
1. source/final creative lock only when genuinely needed;
2. one new family/look gate when a reusable family is introduced;
3. final release gate.

Everything else should be AUTO or AUTO+VERIFY.
