# RSE Technical Orchestrator — Resume From Zero

Use this protocol whenever a new ChatGPT thread, Work session, Codex session or human collaborator takes over RSE technical work.

## Goal
Resume accurately without relying on prior chat memory.

## 2026-10-07 Control Plane override

Before the legacy Step 1 read order, every fresh RSE execution chat must read:

1. `orchestration/control-plane/RSE_UNIVERSE_MAP_V1.md`
2. `orchestration/control-plane/RSE_AUTONOMY_PROTOCOL_V1.md`
3. `orchestration/control-plane/RSE_CHAT_REGISTRY_V1.yml`
4. its registered lane mailbox under `orchestration/control-plane/mailboxes/`

Execution ownership is now one-writer-per-lane. The Central Control Tower is read/sync-only on delegated product/marketing lanes and must not duplicate their source work.

When current Control Plane ownership conflicts with older central/delegated wording in this file or older checkpoints, the Control Plane ownership model wins unless the owner explicitly changes it.

## Step 1 — Load RSE Brain and portfolio truth
Read, in order:
1. `orchestration/brain/RSE_BRAIN_MASTER.md`
2. `orchestration/brain/DECISION_LEDGER.md`
3. `orchestration/brain/PROGRAM_REGISTRY.yml`
4. `orchestration/brain/SOURCE_REGISTRY.yml`
5. `orchestration/brain/OWNER_GATES.md`
6. `orchestration/brain/CONFLICT_LOG.md`
7. `orchestration/brain/RSE_BRAIN_CHECKPOINT.yml`
8. `orchestration/brain/PORTFOLIO_COMPLETION_SNAPSHOT.md` (working management estimate; never overrides live repo facts)
9. newest dated delta under `orchestration/brain/checkpoints/` if present
10. `orchestration/rse-business-projects.yml`
11. `orchestration/RSE_BUSINESS_PORTFOLIO.md`
12. `orchestration/RSE_TECHNICAL_ORCHESTRATOR.md`
13. `orchestration/RSE_INTEGRATION_MAP.md`
14. `orchestration/WAVE1_AUTOPILOT_QUEUE.md` if present
15. current project-specific bootstrap/plan files under `orchestration/projects/` and `orchestration/bootstrap/`

If an old chat or older prose control document conflicts with RSE Brain, a fresher repository checkpoint, or current repository state, do not follow the stale source. Log the contradiction in `orchestration/brain/CONFLICT_LOG.md`.

## Step 2 — Select one project
Do not work on all Wave 1 projects at once. Pick the highest-priority project whose next task is AUTO/AUTO+VERIFY and not blocked by an owner gate.

## Step 3 — Load project truth
For the selected project, read:
- repo `PROJECT_BRIEF.md`,
- repo `AGENTS.md`,
- repo `CHECKPOINT.yml`,
- current branch/PR/issue state,
- relevant CI/checks,
- only the implementation files needed for the next task.

If any of the three durable project files are missing, creating them from templates is the first safe task.

## Step 4 — Reconcile freshness
Treat GitHub/repository state as fresher than conversational summaries. If the registry and repository disagree, do not guess. Update the registry/checkpoint after verifying current repo facts.

## Step 5 — Apply work class
- `AUTO`: execute directly.
- `AUTO_VERIFY`: execute, run targeted verification, self-repair bounded failures, checkpoint.
- `OWNER_GATE`: stop implementation and surface one concise decision packet.

## Step 6 — Protect budget
Before calling Codex or specialists, ask:
1. Can a deterministic script/API/check answer this?
2. Is there already fresh evidence?
3. Can related edits be bundled?
4. Does a specialist add unique expertise or independent risk reduction?

If not, do not spend the extra agent call.

## Step 7 — Finish with durable state
Every meaningful milestone ends with:
- updated `CHECKPOINT.yml` or equivalent issue/PR checkpoint,
- evidence for PASS/NEEDS WORK/BLOCKED,
- next autonomous task,
- next owner gate if any,
- central RSE Brain sync when phase/blocker/source/decision/gate changed.

## New-chat handoff prompt
A user should be able to start a fresh technical conversation with:

`Take over RSE Technical Orchestrator. Reconstruct current state from the connected GitHub durable sources using RESUME_FROM_ZERO.md. Do not re-audit completed work. Continue the highest-priority safe Wave 1 task and stop only at an owner gate or real blocker.`

No old conversation URL should be required for normal continuation.


## Current Detective handoff — 2026-09-30

Before any Detective Academy production work, read:
`orchestration/brain/checkpoints/2026-09-30-detective-owner-frontmatter-source-lock.md`

Canonical reader copy remains the same V3 file:
`orchestration/detective/DETECTIVE_ACADEMY_BOOK1_TEXT_GOLD_MASTER_V3.md`

Current canonical blob:
`8685f8e561d0bfb3837445b72b4d6f799a9a48f2`

Important regression rule:
the Sep 29 180-page owner-review PDF mixed physical Page 3 because the renderer, not the canonical text, hardcoded `YOUR SQUAD` + squad art on top of the black-envelope page.

Locked physical opening order is now:
Title -> Publication -> Black Envelope ONLY -> Your Squad -> Credential -> Book Promise -> Case Rhythm -> Map Rules -> Case Wall/Hint Vault -> Case Index.

Do not:
- put squad art or `YOUR SQUAD` on the black-envelope page;
- restore the global upper-left micro-grid/ruler;
- place Happy Makers dialogue directly on a full evidence-grid field;
- advance to final Previewer/physical-proof status from a pre-fix artifact.

Current state:
**FRONT-MATTER SOURCE-FIXED / FRESH REBUILD + FULL AUDIT REQUIRED / EN NOT FROZEN.**
