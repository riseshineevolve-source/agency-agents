# RSE Consumer Platform — Privacy Lifecycle Contract v0

Status: SYNTHETIC CONTRACT / NO DEPLOYMENT OR LEGAL APPROVAL
Updated: 2026-09-20

## Purpose

Define the backend-neutral lifecycle behavior required for ordinary shared RSE Consumer accounts before live authentication or cloud sync is enabled. This is an engineering contract, not legal advice or a completed jurisdictional privacy review.

## Account creation

- Account creation is optional for products that support guest-first local use.
- The shared minimum account stores only data needed for identity, locale and lifecycle state.
- Product progress remains product-scoped; account creation does not create product ownership.
- No child email/password identity is introduced by this shared contract.

## Guest-to-account linking

Linking local guest state to an authenticated account must be:
- explicit;
- idempotent;
- scoped to the selected product/profile;
- independent from purchase entitlement;
- safe against accidental attachment of another person's local data.

A successful login by itself must not silently absorb all guest data found on a shared device.

## Export request

An authenticated account owner may request an export of their shared-consumer records.

The export enumerator must be account-scoped and capable of including, where applicable:
- account/profile data;
- product-scoped progress;
- sync metadata meaningful to the owner;
- entitlement status/history appropriate for export;
- privacy request history.

It must not include another account's records, backend secrets, raw provider purchase credentials/tokens, or internal security material.

## Delete request

Deletion is an explicit server-authoritative lifecycle state.

Minimum states:
- `requested`
- `in_progress`
- `completed`
- `failed_retriable`

Rules:
1. A stale offline client cannot cancel or overwrite a newer deletion request.
2. New cloud writes for an account in deletion processing must be blocked or routed through a documented safe policy.
3. Deletion must enumerate all shared-consumer records by stable account ownership, not by email string matching.
4. Product-scoped progress and sync records belonging to the account must be included in deletion planning.
5. Entitlement/audit records that must be retained for fraud, accounting or legal reasons, if any, require an explicit later retention decision; this engineering contract does not invent one.
6. Local-only guest data on a device is a separate local lifecycle and is not assumed deleted merely because a cloud account is deleted.

## Account email/credential changes

Ownership keys use stable opaque account IDs. Changing an email/login identifier must not orphan progress or transfer ownership.

No data model may use email as the primary ownership foreign key.

## Account linking and product ownership

- Linking guest progress does not grant an entitlement.
- Linking a Google Play purchase to an RSE account requires trusted verification and exact `product_id` binding.
- Replaying the same verified purchase/account linking operation must be idempotent.
- One purchase cannot be silently attached to multiple unrelated RSE accounts unless a future explicit family-sharing policy authorizes it.

## Cross-product lifecycle

Deleting the shared RSE Consumer account affects data in the shared consumer domain, including World 01 / World 02 / Gentle Steps data where present.

It does not silently delete or modify separate security domains:
- Happy Me separate backend;
- Senior / Hello Today Firebase domain;
- private Mind Bloom;
- local Opinie / Smart CV / Domowe Finanse.

Cross-domain account deletion orchestration, if ever desired, requires a separate explicitly reviewed contract.

## Required synthetic tests before deployment

1. Account A export cannot enumerate Account B records.
2. Account deletion enumeration is based on stable `account_id`, not email.
3. Email change preserves ownership of Account A records.
4. Stale offline sync cannot cancel `requested`/`in_progress` deletion.
5. Guest linking is idempotent.
6. Guest linking does not create entitlement.
7. Replayed purchase-account link does not duplicate entitlement.
8. Unknown product/account link fails closed.
9. Separate-domain data is never included by the shared-consumer deletion enumerator.
10. Raw purchase tokens/secrets are excluded from owner export fixtures.

## Owner/legal gates

Before production, the actual retention periods, privacy notice, lawful basis/consent needs, child/family requirements, Data Safety declarations and jurisdiction-specific deletion/export obligations require appropriate review. Passing this contract does not mark those human/legal gates complete.
