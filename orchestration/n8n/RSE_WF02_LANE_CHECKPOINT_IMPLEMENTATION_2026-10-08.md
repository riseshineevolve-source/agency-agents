# WF-02 LANE CHECKPOINT — deterministic implementation contract

Date: 2026-10-08  
Status: **CODE / CONTRACT READY FOR CI; N8N UI TEST + PUBLISH NOT YET VERIFIED**  
Authority: RSE Universe Factory v1.0 FROZEN and RSE_CHAT_REGISTRY_V1.yml.

## Zero-credential routing

WF-02 runs hourly at **minute 37** (Europe/Warsaw) and reads only the existing GitHub read-only credential already proven by WF-01. No permission widening, webhook registration, secrets in GitHub, new vendor or additional AI service.

1. Read `orchestration/control-plane/RSE_CHAT_REGISTRY_V1.yml` from `agency-agents/main`.
2. Extract the `mailbox` field under each of the 11 `chats` entries; require **exactly 11 unique** paths under `orchestration/control-plane/mailboxes/`. Fail closed on missing/duplicate/out-of-root paths.
3. Read **all 11** mailbox files from `agency-agents/main` **read-only**. Never infer inactive writers merely from bootstrap-stale mailboxes; current branch/head/CI remains authoritative for source operations.
4. Feed the registered sources through the existing deterministic snapshot contract `scripts/rse-control-plane-status.py`. The snapshot now emits `attention_class`, `attention_dedupe_key`, and compact `attention_events`.
5. Classify **BLOCKED > OWNER_GATE > DEPENDENCY > NORMAL**, no independent AI judgment. Store last delivered fingerprint **per lane** in n8n persistent workflow data; suppress unchanged keys on subsequent hourly runs. The fingerprint includes only the highest-priority active signal; unrelated lower-priority field edits cannot create duplicate alerts. When a lane returns to NORMAL, clear its stored fingerprint; a later recurrence must be a new event.
6. Action rules: NORMAL silent, DEPENDENCY route internally only, BLOCKED flag deterministic repair/external gate according to lane contract, OWNER_GATE notify only on a genuinely actionable owner decision. Stale bootstrap placeholders without a true field signal are NORMAL. Do not change any lane mailbox.
7. Run four sample cases **BLOCKED / OWNER_GATE / DEPENDENCY / NORMAL** plus unchanged/revised fingerprint tests, then one real full 11-mailbox GitHub read and compare the resulting classifications to the published deterministic snapshot. **Publish only after these pass in n8n.**

## Existing reusable implementation

- Parser and current registry/mailbox validation: `scripts/rse-control-plane-status.py`.
- Snapshot workflow and artifact: `.github/workflows/rse-control-plane.yml`, `rse-control-plane-status`.
- Deterministic unit/fixture test: `scripts/test-rse-control-plane-status.py`.

The primary validation/test already reads every registered mailbox from GitHub's checked-out canonical tree. WF-02 may consume the artifact for preflight, but its required 11 direct read-only mailbox checks must remain in the n8n activation test.

## Current release boundary

This branch contains no n8n Cloud credential IDs or published workflow mutation. Cloud activation requires a real authenticated n8n execution test and must not be reported as PASSED on the strength of Python CI alone.

No product source, owner gate, art, paid service, token scope, publication or production deployment is changed by this packet.
