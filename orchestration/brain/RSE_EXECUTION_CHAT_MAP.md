# RSE Execution Chat Map

Status: CANONICAL
Date: 2026-09-30
Owner intent: reduce central-chat blocking and maximize parallel execution without creating competing sources of truth.

## Roles

| Chat / stream | Role | May execute | May mutate central Brain |
|---|---|---:|---:|
| RSE Quick Desk | fast conversation/status/decision support | only on explicit command | no |
| RSE Technical Orchestrator | portfolio sequencing, cross-project integration, owner gates, canonical reconciliation | yes | yes |
| Detective Academy execution | bounded KDP interior/print/proof work | yes | no |
| Optical Animals execution | masks/tokens/seek-find/assembly/KDP proof | yes | no |
| Gentle Steps execution | PL book production + EN/PL app conversion | yes | no |
| World 01 / Interactive Book execution | source graph/factory reusable implementation | yes | no |
| Polish Localization Engine execution | localization engine + project profiles/tests | yes | no |
| Marketing Autopilot | launch/content/performance execution | yes | no |

## Project-chat rule

Each project chat:
1. starts from its bootstrap file in `orchestration/bootstrap/`;
2. treats current repo/checkpoint as source of truth;
3. does not re-audit already closed work;
4. executes until a real owner gate/blocker;
5. writes durable project checkpoint;
6. reports to central Orchestrator only milestone/blocker/gate/next action;
7. never edits `RSE_BRAIN_MASTER.md`, `COMMERCIAL_PRIORITY_STACK.md` or cross-project sequencing.

## Central-Orchestrator rule

Central Orchestrator does not perform every project task itself.
It should:
- keep at most three central finish lanes active;
- delegate deep project execution;
- reconcile durable outputs;
- resolve shared dependencies;
- protect owner gates;
- update canonical Brain only after verification.

## Owner interaction

Use Quick Desk for rapid conversation.
Use project chats for long execution.
Use Technical Orchestrator for:
- changing priorities,
- resolving cross-project conflicts,
- accepting project milestones,
- authorizing gates,
- central checkpoint/Brain updates.
