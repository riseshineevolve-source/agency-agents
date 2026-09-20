# RSE Consumer Platform — Synthetic Data Contract v0

Status: DESIGN CONTRACT / SYNTHETIC ONLY / NO DEPLOYMENT AUTHORIZATION
Updated: 2026-09-20

## Purpose

Define the smallest reusable, product-scoped data contract needed to validate the future RSE Consumer Platform and Interactive Book App Factory without creating/restoring any backend, moving real users, or committing to a paid service.

This contract is deliberately backend-neutral at the domain level. Supabase is the current candidate implementation platform, but the semantic model must remain portable.

## Scope

Candidate shared products:
- World 01
- World 02
- 24 Gentle Steps to Christmas
- ordinary future RSE content-pack apps explicitly approved for the shared consumer platform

Excluded domains:
- Happy Me family/child-sensitive backend
- Senior / Hello Today existing Firebase domain
- Mind Bloom private owner-only domain
- Opinie real data
- Smart CV Tailor private data
- Domowe Finanse private data

## Design rules

1. Guest-first is permitted where product/privacy requirements allow it.
2. No child email/password identity is required by this contract.
3. Language-neutral IDs bind EN and pl-PL versions of the same semantic content.
4. Progress is always product + content-pack scoped.
5. Paid ownership is never trusted from a client-only flag.
6. Cloud sync is optional; offline progress must remain usable without it.
7. Deletion/export state must be representable before production auth is enabled.
8. RLS/authorization tests must prove cross-user and cross-product isolation before deployment.

## Logical entities

### account
Only exists after explicit account creation.

Fields:
- account_id: opaque UUID
- locale: `en` or `pl-PL`
- created_at
- deletion_requested_at: nullable

Do not put product progress directly on the account row.

### profile
Optional experience profile owned by an account. A product that does not need multiple profiles should not invent them.

Fields:
- profile_id
- account_id
- display_label: optional, non-unique
- locale
- created_at

No birth date, child email, school, address, or other sensitive field belongs in the shared minimum schema.

### product
Language-neutral product identity.

Example synthetic IDs:
- `world_01`
- `world_02`
- `gentle_steps_christmas`

Fields:
- product_id
- status
- current_content_pack_id

### content_pack
Versioned installable content contract.

Fields:
- content_pack_id
- product_id
- schema_version
- content_version
- canonical_locale: `en`
- supported_locales
- manifest_hash

### content_item
Language-neutral activity/mission/day identity.

Fields:
- content_item_id
- content_pack_id
- interaction_type
- sequence
- unlock_rule
- accessibility_metadata_ref

Localized copy is mapped by `(content_item_id, locale)` and never creates a second semantic activity ID.

### progress
Fields:
- profile_id or local_guest_id
- product_id
- content_pack_id
- content_item_id
- state: `not_started | in_progress | completed`
- checkpoint_version
- client_updated_at
- server_updated_at: nullable offline
- sync_revision

A later implementation must define deterministic conflict handling. Last-write-wins is not accepted implicitly.

### entitlement
Server-verified access state for monetized content.

Fields:
- account_id
- product_id
- entitlement_type
- source: e.g. `google_play`
- external_purchase_ref_hash
- verified_at
- valid_until: nullable
- revoked_at: nullable

Raw purchase credentials/tokens must not be exposed to clients after verification or committed to GitHub fixtures.

### sync_state
Fields:
- profile_id
- product_id
- device_instance_id: pseudonymous
- last_pushed_revision
- last_pulled_revision
- last_sync_at

### privacy_request
Fields:
- account_id
- request_type: `export | delete`
- requested_at
- completed_at: nullable
- status

## Synthetic fixtures

The first implementation/test packet should use only invented identities such as:

- account A: `00000000-0000-4000-8000-000000000001`
- account B: `00000000-0000-4000-8000-000000000002`
- profile A1 / profile B1
- products `world_01`, `world_02`, `gentle_steps_christmas`
- fake Google Play purchase references represented only by non-secret placeholder hashes

No fixture may contain a real email, name, transaction, child detail, CV datum, or private project content.

## Required authorization tests before deployment

1. Account A cannot read/write Account B profile or progress.
2. Account A progress for World 01 cannot mutate World 02 progress accidentally.
3. Guest progress can function locally without creating an auth user.
4. Linking guest progress to an account is explicit and idempotent.
5. Client cannot self-grant an entitlement.
6. Revoked entitlement blocks protected cloud access without destroying legitimate local data unexpectedly.
7. Deletion request can enumerate all shared-consumer records owned by the account.
8. Unsupported locale fails safely to canonical EN rather than binding the wrong content ID.
9. EN and pl-PL variants resolve to the same language-neutral content item.
10. Stale/offline sync revisions cannot silently overwrite a newer incompatible revision.

## Offline conflict contract to resolve before implementation

The implementation packet must choose and test conflict semantics per data class:
- completion/progress state: monotonic merge where feasible;
- free-form user data, if ever introduced: explicit version conflict policy;
- preferences: deterministic latest valid revision;
- entitlements: server authority only.

Do not apply one generic merge rule to all data.

## Backend creation gate

This document does not authorize a Supabase project, migration, Firebase resource, live auth configuration, SMTP configuration, billing activation, or user migration.

Before a new backend is created, the architecture packet must still demonstrate why the existing RSE Consumer candidate cannot safely serve the product and document free-tier/cost impact.

## Exit criteria for v0 contract

The contract is ready for implementation planning when:
- World 01 source is approved as the first pilot;
- product/account requirements are confirmed;
- monetization model is known enough to select entitlement behavior;
- privacy review confirms the actual minimum collected data;
- offline conflict rules are selected;
- synthetic authorization tests can be translated into executable tests without real user data.
