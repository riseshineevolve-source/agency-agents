# RSE Autopilot Policy

Status: ACTIVE DESIGN CONTRACT
Purpose: maximize autonomous progress while preserving owner control over irreversible or strategic decisions.

## Core principle

The system should keep moving without waiting for the owner when the next action is safe, reversible, testable and already consistent with an approved project brief.

The owner should be interrupted only for a meaningful decision, a true blocker, or an irreversible external action.

## Execution classes

### AUTO

Proceed without asking when all conditions are true:
- task is inside an already-approved milestone,
- change is reversible,
- no pricing/legal/product-scope/brand/final-art/publication decision is introduced,
- no confidential data crosses its permitted boundary,
- no destructive migration is required,
- no production/store release is triggered.

Examples:
- repository/context inspection,
- status reconciliation,
- test execution,
- lint/build repair,
- documentation sync,
- creating or updating implementation checkpoints,
- generating comparison artifacts,
- low-risk bug fixes backed by tests,
- updating non-production orchestration metadata,
- preparing drafts for later owner approval.

### AUTO + VERIFY

Proceed without asking, but completion requires an independent verification pass.

Use for:
- code changes,
- parser/generator changes,
- book-factory logic,
- layout-generation logic,
- localization-engine rule changes,
- deterministic content transformations,
- migration preparation that does not execute destructive production changes,
- dependency upgrades needed to fix an identified blocker.

Required loop:
1. minimal implementation,
2. automated test/build/preflight,
3. targeted specialist review when needed,
4. correction,
5. independent Reality Checker or equivalent final gate,
6. checkpoint.

If verification fails, repair automatically while the fix remains within the approved milestone. Escalate only when the repair would cross an OWNER GATE.

### OWNER GATE

Stop and ask the owner only for decisions such as:
- final visual/art selection,
- product scope expansion or removal,
- pricing, subscriptions, payment model or paid/free strategy,
- legal/compliance policy choices,
- material privacy/data-sharing changes,
- brand identity or major UX redesign,
- publication, Google Play/App Store/KDP submission,
- public production deployment not already covered by an explicitly approved release policy,
- destructive data migration,
- deletion of substantial source material,
- crawler/indexing policy changes with material external consequences,
- activating Wave 2 Lovable apps,
- activating Gifts work,
- any action that would expose confidential Opinie data outside the local environment.

An OWNER GATE message must be compact and decision-ready: recommended options, consequences, evidence, and the exact decision required. Do not send a vague status dump.

## Budget-aware routing

Default mode: SMART EFFICIENT.

Rules:
- 1 CORE owner for the task.
- Add specialists only when the task actually requires their domain.
- Default maximum active roles per milestone: 4.
- Do not ask multiple agents to independently reread the full repository.
- Reuse `PROJECT_BRIEF.md`, checkpoints, manifests, test reports and prior accepted decisions.
- Prefer deterministic scripts/tests over repeated LLM review.
- Prefer one strong generation pass plus targeted critique over parallel speculative generations.
- Do not use Codex for work that GitHub Actions, scripts, tests, static checks or the central ChatGPT Orchestrator can do deterministically.

## Codex conservation mode

When Codex usage is constrained:

1. GitHub Actions/tests handle deterministic validation.
2. Central Orchestrator handles portfolio/status/routing/reconciliation.
3. Codex is reserved for repository changes requiring code reasoning or local execution.
4. Bundle related repository work into one coherent task instead of many tiny Codex sessions.
5. Give Codex narrow context pointers rather than the full history.
6. Do not start a Codex task when the next step is waiting on an OWNER GATE.
7. Avoid speculative refactors.
8. Prefer fixing the smallest verified blocker.

## Automatic retry policy

A failing task may self-repair for up to 2 targeted correction loops when:
- the failure is understood,
- the repair stays inside the approved milestone,
- no OWNER GATE is crossed.

After two unsuccessful targeted correction loops, mark BLOCKED with:
- observed failure,
- evidence/log/test,
- attempted fixes,
- smallest decision or missing dependency needed.

Do not burn usage on endless retry loops.

## Project-specific autonomy

### RSE Core / AI Discovery
AUTO: measurement, parity checks, schema/fact consistency checks, recrawl evidence gathering, benchmark reruns.
OWNER GATE: new public content families, material brand/business changes, crawler-policy changes, production strategy changes.

### Polish Engine
AUTO + VERIFY: golden-test runs, QA classification, rule patches, anti-AIism additions, regression reruns.
OWNER GATE: accepted final Polish voice when a genuine style preference cannot be resolved from existing accepted examples; full publication.

### Detective Academy
AUTO + VERIFY: Book Factory code, puzzle regression, geometry/solution validation, comparison renders, print-preflight preparation.
OWNER GATE: visual map standard, major art direction, final book approval/publication.

### Happy Me
AUTO + VERIFY: custody audit, build/lint/test repair, release-blocker fixes, state/navigation regression, release preparation.
OWNER GATE: commercial model, major UX/product redesign, store publication.

### Optical Animals
AUTO: inventory, manifest maintenance, duplicate/gap detection, assembly automation.
AUTO + VERIFY: technical Book Creator changes, preflight tooling, image-file bookkeeping.
OWNER GATE: which illustrations/species are final, artistic replacement acceptance, KDP publication.

### Senior / Mind Bloom
Dedicated execution chats remain primary. Central autopilot may reconcile status, dependencies and shared infrastructure but must not seize their active implementation files without an explicit cross-project need.

### Opinie
AUTO is allowed only for non-confidential orchestration metadata remotely. Case work and local pipeline execution remain local/offline. Human expert review is always required before opinion-ready output.

## Daily portfolio loop

Each daily orchestration pass should:
1. read the Wave 1 registry,
2. inspect active PRs/issues/checkpoints available through connected systems,
3. identify stale/blocking states,
4. advance safe AUTO work where tools allow,
5. verify completed changes,
6. update project checkpoint/status,
7. create at most one concise owner escalation if an OWNER GATE is reached,
8. leave Wave 2 and Gifts untouched.

Do not manufacture work merely to make every project appear active. A project waiting at an owner gate or external dependency may legitimately remain unchanged.

## Notification policy

Notify the owner when:
- an OWNER GATE is reached,
- an important milestone is complete,
- a blocker cannot be self-repaired,
- a material regression is detected,
- a budget/usage constraint would change execution strategy.

Do not notify for routine green checks, documentation sync or successful low-risk maintenance.
