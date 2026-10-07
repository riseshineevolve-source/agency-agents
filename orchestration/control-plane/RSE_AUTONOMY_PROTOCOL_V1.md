# RSE Autonomy Protocol v1

Status: CANONICAL
Date: 2026-10-07
Parent: orchestration/control-plane/RSE_UNIVERSE_MAP_V1.md

## Meaning of 95% autonomous

95% autonomous means:
- once a lane chat is active, it reconstructs state itself;
- it selects the next safe task itself;
- it uses deterministic tools / agents / Codex itself;
- it self-repairs bounded failures;
- it checkpoints and continues;
- it asks the owner only for genuine judgment, external, legal, spending, freeze or publication gates.

A normal closed ChatGPT chat does NOT literally execute forever in the background.
Unattended 24/7 execution is a separate runtime layer (n8n / Agents API / Temporal / scheduled Work). This protocol is intentionally compatible with that later layer.

## Mandatory opening sequence for every execution chat

1. Read:
   - `orchestration/control-plane/RSE_UNIVERSE_MAP_V1.md`
   - `orchestration/control-plane/RSE_CHAT_REGISTRY_V1.yml`
   - this file.
2. Read its own bootstrap from the registry.
3. Read its own mailbox and relevant dependency mailboxes.
4. Read project repo truth:
   - PROJECT_BRIEF.md
   - AGENTS.md
   - CHECKPOINT.yml
   - current branch/head/status
   - current CI
   when present.
5. If local state matters, use Desktop Commander instead of asking the owner to paste terminal output.
6. Reconcile stale chat claims against current GitHub/local evidence.
7. Continue the highest-priority safe AUTO/AUTO_VERIFY task.

## One-writer rule

Each lane has:
- one project/source writer;
- one mailbox writer;
- explicit read dependencies.

Never run two Codex/agent writers against the same branch/worktree/surface.

Before pull/reset/rebase/checkout on a local worktree:
- inspect git status;
- inspect git diff;
- preserve legitimate uncommitted work;
- do not blind-clean/reset.

## Task classes

AUTO:
execute directly.

AUTO_VERIFY:
execute -> targeted tests/evidence -> bounded self-repair -> checkpoint.

OWNER_GATE:
stop only when owner judgment or explicit authorization is required.

EXTERNAL_GATE:
park the lane and take the next safe task; do not manufacture work.

## Agent routing

Default:
CORE first + maximum about 4 active specialist roles.

Use specialists only where they provide unique expertise or independent risk reduction.

Typical routing:
- cross-system architecture -> Multi-Agent Systems Architect
- workflow tree/failure paths -> Workflow Architect
- visual storytelling/new family -> Visual Storyteller
- visual identity -> Brand Guardian
- image slot prompt -> Image Prompt Engineer
- document/page compiler -> Universal Document Compiler
- PDF geometry -> PDF Engine Architect
- bounded repair -> Minimal Change Engineer
- automated regression -> Test Automation Engineer
- final reality gate -> Reality Checker
- cost/latency optimization -> Autonomous Optimization Architect only after stable baseline
- app build -> Mobile App Builder
- app release -> Mobile Release Engineer

Do not invoke specialists just to appear "agentic".

## Tool routing

Ask in this order:

1. Can deterministic code/check answer it?
2. Is fresh evidence already available?
3. Does Desktop Commander give the local fact directly?
4. Does a connected provider own the data?
5. Does Codex need to implement something?
6. Does an agent need judgment?
7. Does image generation/editing add value for an atomic asset?

Codex:
- code;
- adapters;
- tests;
- deterministic renderers;
- integration;
- build repair.

Codex is NOT:
- art director;
- source-of-truth editor by default;
- freeform puzzle inventor.

Desktop Commander:
- local-only assets/binaries;
- real local build/test;
- local Git/worktree inspection;
- device/runtime evidence;
- confidential local workflows when permitted.

Image generation/editing:
- isolated art asset;
- character/prop/hero/decorative asset;
- owner-authorized edits.

Never final canonical text/map/table/puzzle geometry as an AI-generated full-page image.

## Cross-chat mailbox contract

Path:
`orchestration/control-plane/mailboxes/<lane>.yml`

Only the registered lane owner writes that file.

Schema fields:
- lane
- updated
- status
- branch_or_repo_state
- milestone
- blocker
- owner_gate
- dependencies_needed
- reusable_outputs
- next_safe_task
- checkpoint_reference

When a dependency is required from another lane:
- add it under `dependencies_needed`;
- continue independent safe work if possible;
- do not ask the owner to relay the message.

The producing lane reads dependency mailboxes on startup and at checkpoints.

## Checkpoint contract

Every meaningful milestone writes:
- exact branch/head when meaningful;
- source/input lock;
- changed scope;
- tests/evidence;
- output hashes where applicable;
- unresolved exceptions;
- next safe task;
- next real owner gate.

Do not write status-only commits repeatedly.

## Stop conditions

Do NOT stop for:
- ordinary implementation errors;
- a retryable test failure;
- stale chat uncertainty resolvable from repo/local evidence;
- needing another agent;
- needing Codex;
- needing local terminal access when Desktop Commander is available.

STOP for:
- true source contradiction;
- missing owner-only source/asset;
- destructive decision;
- privacy/security/legal decision;
- paid service/spend;
- final visual family choice where no lock exists;
- source freeze;
- publication/deployment/store submission;
- irreversible production mutation.

## Review minimization

Owner sees:
- new visual/template family candidates;
- changed/flagged pages/screens;
- unresolved editorial/brand decisions;
- release packet.

Owner does NOT re-review unchanged pages/screens.

## Continuous improvement

At lane completion:
- record reusable template/component;
- record failed patterns;
- update deterministic tests;
- expose reusable output in mailbox.

The goal is that the second product is materially cheaper/faster than the first.
