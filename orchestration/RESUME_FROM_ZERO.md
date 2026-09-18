# RSE Technical Orchestrator — Resume From Zero

Use this protocol whenever a new ChatGPT thread, Work session, Codex session or human collaborator takes over RSE technical work.

## Goal
Resume accurately without relying on prior chat memory.

## Step 1 — Load portfolio truth
Read, in order:
1. `orchestration/rse-business-projects.yml`
2. `orchestration/RSE_BUSINESS_PORTFOLIO.md`
3. `orchestration/RSE_TECHNICAL_ORCHESTRATOR.md`
4. `orchestration/RSE_INTEGRATION_MAP.md`
5. `orchestration/WAVE1_AUTOPILOT_QUEUE.md` if present
6. current project-specific bootstrap/plan files under `orchestration/projects/` and `orchestration/bootstrap/`

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
- next owner gate if any.

## New-chat handoff prompt
A user should be able to start a fresh technical conversation with:

`Take over RSE Technical Orchestrator. Reconstruct current state from the connected GitHub durable sources using RESUME_FROM_ZERO.md. Do not re-audit completed work. Continue the highest-priority safe Wave 1 task and stop only at an owner gate or real blocker.`

No old conversation URL should be required for normal continuation.
