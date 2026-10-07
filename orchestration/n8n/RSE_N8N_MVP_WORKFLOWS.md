# RSE n8n MVP — Workflow Contracts

Status: READY FOR CONNECTION / IMPLEMENTATION
Date: 2026-10-07
Parent: RSE Universe Factory v1.0

## Principle

n8n is orchestration glue, not product truth.

GitHub remains source of truth.
n8n may trigger/read/report, but must not become the only place where a product rule exists.

## WF-01 CONTROL-TOWER-HOURLY

Trigger:
- hourly schedule.

Steps:
1. fetch the latest successful `RSE Control Plane v1` GitHub artifact or run the deterministic status script through GitHub Actions;
2. read owner_attention_lanes and dependency_requests;
3. if none -> finish silently;
4. if present -> route:
   - owner gate -> concise owner notification;
   - cross-lane dependency -> notify producing lane / create durable GitHub issue/comment only if the lane contract requires it;
   - deterministic blocker -> trigger relevant CI/workflow, not an AI agent;
   - ambiguous blocker -> optional Agents API triage after W6.
5. record workflow outcome.

Never poll Desktop Commander.

## WF-02 LANE-CHECKPOINT

Trigger:
- GitHub webhook / workflow completion / push affecting a registered lane.

Steps:
1. map repo/branch/path to lane using `RSE_CHAT_REGISTRY_V1.yml`;
2. run lane status extractor / project CI;
3. if PASS -> update central status artifact / notify no one;
4. if FAIL deterministic -> trigger bounded retry if policy allows;
5. if owner gate -> notify once with exact checkpoint reference.

Do not edit product source.

## WF-03 RELEASE-CANDIDATE

Trigger:
- lane emits a release-candidate manifest/checkpoint.

Steps:
1. trigger final lane-specific CI/preflight;
2. require PASS evidence;
3. collect review/release artifact refs;
4. send one owner release packet;
5. wait for owner decision;
6. on approval, hand off to the explicit publication/deployment process.

No automatic publication.

## WF-04 ASSET-INGEST

Trigger:
- new Asset Vault manifest commit.

Steps:
1. validate manifest schema and SHA metadata;
2. identify consuming lanes;
3. notify those lane mailboxes/workflows;
4. trigger dependency-closure calculation where supported;
5. build changed-page/screen packet only.

Do not regenerate owner-approved assets.

## Secrets

Use n8n credential store/environment secrets.
Never commit:
- GitHub tokens;
- OpenAI API keys;
- Gmail/Metricool/Supabase credentials;
- Desktop Commander auth;
- store credentials.

## First deployment target

Use n8n Cloud trial for proof.
After proof choose:
- Cloud for lower maintenance; or
- self-hosted Community Edition on a small always-on VPS.

Do not make the owner's Windows machine the permanent scheduler.
