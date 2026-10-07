# RSE Automation Stack Decision — 2026-10-07

Status: FINAL CURRENT DECISION

## Adopt now

1. GitHub + GitHub Actions as durable event/evidence backbone.
2. RSE Control Plane + lane mailboxes.
3. Graphic Gold Library from the first 18 Detective gold pages.
4. Desktop Commander as exception-only local bridge.
5. ChatGPT/Codex Pro capacity as interactive heavy worker.
6. n8n Community Edition as the next orchestration layer.

## Do next

### n8n MVP workflows

A. CONTROL-TOWER-HOURLY
- schedule trigger
- read mailbox/checkpoint changes from GitHub
- identify lanes with new milestone/blocker/gate
- run deterministic routing
- notify owner only for true owner gate

B. LANE-CHECKPOINT
- GitHub webhook
- run lane CI/status extractor
- update central summary
- no LLM unless exception classification is ambiguous

C. RELEASE-CANDIDATE
- release manifest created
- trigger final CI/preflight
- create review packet
- notify owner once

D. ASSET-INGEST
- new owner-approved asset manifest
- verify hash/registry
- notify consuming lanes

### Agents/API pilot

After n8n deterministic routing works:
- add one Agents API Control Tower triage worker;
- max 1–2 agent calls per changed event;
- subagents only for independent specialist judgment;
- trace every run.

Do not convert all chat workflows to API agents at once.

## Defer

Temporal until n8n/GitHub checkpoint recovery proves insufficient.

## Why

Current RSE bottleneck is not durable distributed-workflow failure.
It is:
- manual routing;
- duplicated visual interpretation;
- missing reusable Gold Families;
- owner used as message bus;
- expensive tools used for deterministic tasks.

Solve these first.
