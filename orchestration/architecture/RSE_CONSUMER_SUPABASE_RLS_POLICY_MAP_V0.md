# RSE Consumer Platform — Supabase RLS Policy Map v0

Status: SYNTHETIC IMPLEMENTATION CONTRACT / NO DEPLOYMENT AUTHORIZATION
Updated: 2026-09-20

## Purpose

Translate the backend-neutral consumer authorization contract into a concrete Supabase/Postgres Row Level Security policy map without creating, restoring, or modifying any live backend.

This document is a design/test contract only. It does **not** authorize a Supabase project, migration, production auth configuration, billing, user migration, Play Billing integration, or real product rollout.

Canonical inputs:
- `RSE_CONSUMER_SYNTHETIC_DATA_CONTRACT_V0.md`
- `RSE_CONSUMER_AUTHORIZATION_MATRIX_V0.md`
- `RSE_CONSUMER_ENTITLEMENT_MODEL_V0.md`
- `RSE_OFFLINE_SYNC_CONFLICT_POLICY_V0.md`
- `RSE_CONSUMER_PRIVACY_LIFECYCLE_V0.md`

## Locked security rule

Authentication identifies the account. It does not grant product ownership.

A valid `auth.uid()` may authenticate in more than one RSE app while having access only to products with a matching valid product-scoped entitlement. No account-level `is_premium` or similar wildcard may unlock unrelated products.

## Role model

- `anon`: unauthenticated browser/app session. May read only explicitly public catalog/content metadata.
- `authenticated`: signed-in account. May access only its own rows and only within the exact product scope allowed by the policy.
- `trusted_server`: server-only purchase verification, privacy lifecycle, and other privileged workflows. Never exposed to browser/mobile clients.

`service_role` or equivalent privileged credentials must never appear in client code, app bundles, local storage, analytics, or fixtures.

## Ownership keys

Use opaque immutable IDs, never email addresses, display labels, device labels, or locale as authorization keys.

- account ownership key: `account_id = auth.uid()` or an equivalent server-bound immutable account UUID.
- profile ownership: profile row must resolve to the authenticated account through `profile.account_id`.
- product-scoped state: authorization must include the exact `product_id` on the row being accessed.
- entitlement identity: exact tuple `(account_id, product_id)`.

Changing email or locale must not change row ownership or product access.

## Proposed table/policy classes

The exact physical schema may change before implementation. Any replacement must preserve these semantics and pass the SQL test plan.

| Logical table | anon SELECT | authenticated SELECT | authenticated INSERT | authenticated UPDATE | authenticated DELETE | privileged/server mutation |
| --- | --- | --- | --- | --- | --- | --- |
| `accounts` | DENY | own row only | DENY direct client bootstrap | own safe preference fields only | DENY; deletion uses privacy workflow | ALLOW reviewed lifecycle operations |
| `profiles` | DENY | own account profiles only | own account only | own account only | own account only if product design explicitly supports profile deletion | ALLOW administrative lifecycle only |
| `progress` | DENY | own profile + exact product scope; valid exact entitlement when the product state is protected | same predicate | same predicate + revision/conflict rules | DENY by default; no destructive sync shortcut | ALLOW only for reviewed repair/migration paths |
| `sync_state` | DENY | own profile/account + exact product scope | own scope only through the approved sync contract | own scope only through revision-safe sync contract | DENY by default | ALLOW repair/cleanup workflows |
| `entitlements` | DENY | own account rows only where UI needs status | DENY | DENY | DENY | ALLOW verified grant/revoke/expiry only |
| `privacy_requests` | DENY | own account requests only | own account only | DENY client completion/status mutation | DENY | ALLOW server completion/export/delete workflow |
| `products` | explicitly public rows only | explicitly public rows | DENY | DENY | DENY | catalog administration only |
| `content_packs` / content metadata | explicitly public/installable metadata only | same or narrower | DENY | DENY | DENY | release pipeline only |

No policy should grant an operation merely because the actor is authenticated.

## Profiles

A profile policy must bind profile ownership to the account. Cross-account profile IDs fail closed.

Required behavior:
- Account A can read/write profile A1.
- Account A cannot read/write profile B1 even if it knows the UUID.
- profile ownership cannot be reassigned by changing `account_id` from the client.
- if profile deletion is later supported, deletion must still be same-account only and must not cascade into unrelated products/accounts.

## Product-scoped progress

Every cloud progress row must carry enough immutable scope to prove:
- owner/profile;
- exact `product_id`;
- content pack/item identity;
- revision/version state.

Policy checks must never infer product scope from the calling app binary, route, locale, or client-provided `is_owned` flag.

For protected paid cloud state, access must additionally prove a valid entitlement for the exact `(account_id, product_id)` pair. A World 01 entitlement cannot satisfy a World 02 predicate.

Revoked or expired entitlement must fail closed for protected cloud access. Legitimate local/offline data is handled by the offline contract and is not silently destroyed by RLS denial.

## Entitlements

Entitlement rows are server-authoritative.

Browser/mobile clients:
- may read their own entitlement status only if needed for UX;
- may never insert, update, delete, extend, restore, revoke, or change authority/source;
- may never convert a client purchase claim directly into an authoritative row.

Only the trusted server purchase-verification path may create or mutate authoritative entitlement state.

The policy/test contract must reject:
- client-created `server_verified` rows;
- product substitution (`world_01` claim written as `world_02`);
- revoked/expired row reuse;
- any global premium flag as a substitute for exact product entitlement.

## Sync state

RLS protects ownership and exact product scope. Conflict semantics are enforced in the sync transaction/function or equivalent server boundary, not by a permissive generic UPDATE policy.

Required properties:
- Account A cannot push/pull Account B sync state.
- a World 01 sync packet cannot mutate World 02 rows;
- stale revisions cannot overwrite newer incompatible revisions;
- completion progress follows the locked monotonic merge rule;
- preferences follow explicit revision conflict handling;
- entitlement data is never merged from client state.

A later implementation may use RPC/functions for compare-and-swap or atomic batch sync, but no privileged function is allowed merely to bypass RLS. Any `SECURITY DEFINER` use requires a separate threat review, explicit fixed `search_path`, narrow grants, and proof that caller-controlled ownership fields cannot escape authorization. v0 assumes ordinary RLS/`SECURITY INVOKER` behavior unless such a review exists.

## Privacy requests

Authenticated users may create an export/delete request for their own account only.

Clients cannot mark a request completed, change its owner, or enumerate another account's request. The server-side lifecycle performs the authoritative export/delete enumeration.

Shared-consumer deletion must not implicitly delete data from separate domains:
- Happy Me;
- Senior / Hello Today;
- Mind Bloom;
- Opinie;
- LOCAL_PRIVATE Smart CV Tailor / Domowe Finanse.

## Public catalog/content metadata

Public read access must be explicit per table/view and limited to non-sensitive release metadata. Public access to a product/content catalog does not grant cloud progress access or a paid entitlement.

No user/profile/progress/sync/privacy/entitlement row is public.

## Required indexes / integrity support

Before live deployment, schema review must verify indexes that support policy predicates and foreign-key integrity, at minimum around:
- `profiles(account_id)`;
- product-scoped progress ownership lookup;
- `entitlements(account_id, product_id)` with uniqueness appropriate to entitlement history/current-state design;
- sync-state ownership/product lookup;
- `privacy_requests(account_id)`.

Composite foreign keys or constraints should encode same-owner/same-product provenance where feasible so application bugs cannot easily create cross-scope rows.

## Fail-closed rules

DENY when any of these is missing or unknown:
- authenticated account for private cloud rows;
- owner binding;
- product scope;
- required exact entitlement for protected product state;
- supported operation;
- compatible revision/version evidence.

Locale, email, device ID, app route, product display name, or client feature flags never widen authorization.

## SQL implementation constraints

Future migrations must:
1. enable RLS on every private table;
2. avoid broad `USING (true)` / `WITH CHECK (true)` for authenticated private tables;
3. avoid PUBLIC/anon write grants;
4. deny direct client entitlement mutation;
5. keep server-only mutation paths outside client credentials;
6. make ownership predicates explicit;
7. include exact product predicates on product-scoped state;
8. preserve account deletion/export isolation;
9. add tests before remote activation;
10. remain unapplied until the backend/cost/product gates are explicitly passed.

## Definition of DONE for this mapping

The mapping is ready for a future implementation only when deterministic synthetic tests and the companion SQL test plan cover:
- own-row allow paths;
- cross-user deny paths;
- cross-product deny paths;
- exact entitlement allow/deny/revoked/expired cases;
- client entitlement mutation denial;
- privacy request ownership;
- public metadata read-only behavior;
- locale/email non-authority;
- no wildcard premium authorization;
- no implicit access to separate security domains.
