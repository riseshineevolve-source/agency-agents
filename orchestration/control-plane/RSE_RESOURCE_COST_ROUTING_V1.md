# RSE Resource + Cost Routing v1

Status: CANONICAL OPERATING POLICY
Date: 2026-10-07

## Goal

Maximize published-product throughput while minimizing:
- owner relay work;
- paid API use;
- Desktop Commander consumption;
- duplicated AI reasoning;
- idle paid ChatGPT/Codex capacity.

## Routing principle

Use the cheapest reliable layer capable of the task.

### Tier 0 — deterministic local/repo work
Preferred whenever possible.

Use:
- scripts;
- Git;
- GitHub Actions;
- Playwright;
- Vivliostyle;
- tests;
- hash/diff/checkpoint logic.

Examples:
- PDF assembly;
- regression;
- asset hashing;
- page dependency closure;
- CI;
- content validation;
- screenshot comparison.

No LLM required.

### Tier 1 — GitHub Actions / self-hosted runner
Use for repeatable builds/tests triggered by commit/webhook/schedule.

Good for:
- book builds;
- app builds;
- visual regression;
- nightly QA;
- release packets;
- mailbox checks.

Do not use Desktop Commander merely to run a command that CI can run.

### Tier 2 — n8n Community Edition
Role: cheap orchestration/glue, not product logic.

Use for:
- scheduled control-plane poll;
- GitHub webhook routing;
- mailbox change detection;
- trigger CI;
- call an agent only when judgment is needed;
- notify owner only for true owner gate;
- approval routing;
- connector workflows.

Preferred deployment:
- self-hosted Community Edition first;
- local always-on host or low-cost VPS;
- n8n Cloud only if maintenance burden outweighs its monthly fee.

Do not store canonical book/app logic in n8n nodes.

### Tier 3 — Desktop Commander Remote
Role: exception bridge to the owner's authorized Windows machine.

Use only when task genuinely depends on:
- local-only asset/binary;
- local worktree;
- local build environment;
- physical/device tooling;
- confidential local-only data.

Do NOT make every chat poll the desktop.
One lane owner uses it only at checkpoints/exceptions.

### Tier 4 — ChatGPT Pro / Codex included usage
Role: high-value interactive engineering and difficult reasoning.

Use for:
- substantial Codex implementation;
- architecture;
- hard debugging;
- code review;
- source-aware refactors;
- substantial Work tasks.

Personal Pro usage is not the unattended automation backend.
Do not build a 24/7 scheduler around personal account credentials.

If owner has a second Pro account:
- assign it durable dedicated lane(s);
- it reads/writes through GitHub/Control Plane;
- do not duplicate work between accounts;
- do not share account credentials with automated services.

Recommended use of spare Pro capacity:
1. Detective / Book Factory heavy engineering
2. World App Factory or Gentle Steps heavy engineering
3. architecture/review when first two are at gates

### Tier 5 — OpenAI Agents API / API models
Role: unattended AI judgment.

Use only when a workflow truly needs AI while no human chat is active:
- Control Tower triage;
- document/visual family classification;
- exception summarization;
- agent handoffs;
- dependency resolution;
- automated review that cannot be deterministic.

API cost is explicit usage cost.
Keep deterministic steps outside the agent.

### Tier 6 — Temporal
Do NOT adopt into current critical path yet.

Pilot only when:
- workflows span hours/days;
- crash/restart recovery is a recurring real problem;
- n8n + GitHub checkpoints are insufficient.

Self-hosted Temporal is open source but operationally heavier than n8n.
Temporal Cloud is not justified for current RSE scale unless workload/reliability evidence changes.

## Desktop Commander budget law

Desktop Commander is shared scarce capacity.

Rules:
- no hourly polling from every lane;
- no reading huge files repeatedly;
- no process-status polling when GitHub/CI can report state;
- batch file inspections;
- use one command to retrieve structured facts;
- use local scripts for recursive analysis rather than many individual tool calls.

Control Tower may inspect usage weekly and adjust routing.

## Two-account ChatGPT policy

Treat each ChatGPT account as a separate human-supervised execution capacity.

Do:
- assign non-overlapping lanes;
- rely on GitHub/mailboxes for continuity;
- exploit included Codex/Work capacity for meaningful jobs;
- let each account stop at durable checkpoints.

Do not:
- make the accounts edit the same branch/worktree;
- copy secrets between accounts unnecessarily;
- attempt credential-sharing automation;
- treat personal ChatGPT subscriptions as API credits.

## Cost-control dashboard metrics

Track monthly:
- products published;
- owner touches/product;
- Codex/agent turns by lane;
- API spend;
- Desktop Commander usage %;
- GitHub Actions minutes;
- n8n workflow executions;
- number of new vs reused Gold Families;
- average changed pages/screens per release;
- cycle time from source lock to release candidate.

Success metric:
published throughput, not number of agent runs.
