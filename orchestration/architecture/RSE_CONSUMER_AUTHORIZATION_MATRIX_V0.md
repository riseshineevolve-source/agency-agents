# RSE Consumer Platform — Authorization Matrix v0

Status: SYNTHETIC SECURITY CONTRACT / NO DEPLOYMENT AUTHORIZATION
Updated: 2026-09-20

## Purpose

Define the minimum backend-neutral authorization behavior that any future RSE Consumer implementation must enforce before World 01, World 02, 24 Gentle Steps to Christmas, or another ordinary consumer app can share one identity/data platform.

This is not Supabase-specific SQL and does not authorize a live backend. It is the contract that later RLS/policy implementations must satisfy.

## Security principle

Authentication answers **who is this?**
Authorization answers **what may this identity do?**
Entitlement answers **which paid product/content may this identity access?**

A valid RSE login is never sufficient by itself to unlock a paid product.

## Subjects

- `guest_local`: no cloud account; local-only product state where the product permits guest mode.
- `account_owner`: authenticated account acting on its own profile/data.
- `other_account`: authenticated account attempting to access another account's data.
- `trusted_server`: backend-only purchase verification / entitlement administration path.

## Objects

- account/profile metadata
- product-scoped progress
- product-scoped sync state
- product entitlement
- privacy request
- public product/content metadata

## Decision matrix

| Subject | Action | Object | Same account? | Exact product entitlement required? | Decision |
|---|---|---|---|---|---|
| guest_local | read/write | local guest progress | n/a | No | ALLOW locally only |
| guest_local | read/write | cloud account/profile | n/a | n/a | DENY |
| guest_local | grant | entitlement | n/a | n/a | DENY |
| account_owner | read/write | own profile | Yes | No | ALLOW |
| account_owner | read/write | own free/local-sync progress | Yes | Product-scoped namespace required | ALLOW within exact product scope |
| account_owner | read protected content/cloud state | paid product | Yes | Yes, exact `product_id` | ALLOW only when valid |
| account_owner | read protected content/cloud state | different/unpurchased product | Yes | Missing | DENY |
| account_owner | grant/update authority | entitlement | Yes | n/a | DENY direct client mutation |
| other_account | read/write | another account profile/progress | No | any | DENY |
| trusted_server | verify/grant/revoke | entitlement | n/a | Server verification evidence | ALLOW |
| account_owner | create | own privacy request | Yes | No | ALLOW |
| other_account | read/write | another account privacy request | No | any | DENY |

## Required invariants

1. Cross-user isolation: Account A cannot read or mutate Account B profile, progress, sync state, privacy requests, or entitlements.
2. Cross-product isolation: Account A's World 01 progress cannot mutate World 02 progress.
3. Exact entitlement: a valid World 01 entitlement cannot unlock World 02.
4. Client cannot self-grant, extend, restore, or revoke authoritative entitlement rows.
5. Revoked or expired entitlement fails closed for protected cloud access.
6. Locale never widens authorization scope.
7. Linking local guest progress to an authenticated account does not create an entitlement.
8. Public product/content metadata may be readable without authentication only when explicitly designated public.
9. Access checks must exist at the trusted backend boundary, not only in UI visibility logic.
10. Missing/unknown subject, product, profile, or entitlement state fails closed.

## RLS translation requirements

When implemented on Supabase or another policy-capable backend, automated tests must demonstrate at minimum:

- own-row read/write for profile/progress;
- cross-user read denied;
- cross-user write denied;
- exact `product_id` filtering on product-scoped records;
- entitlement rows client read limited to own account where needed, but client insert/update/delete denied;
- trusted-server/service role is the only entitlement mutation path;
- account deletion/export enumeration cannot cross account boundaries;
- no policy uses email address as ownership key;
- no global `is_premium` account flag can authorize multiple unrelated products.

## Test identities

Use only synthetic IDs from the consumer fixture:

- Account A: `00000000-0000-4000-8000-000000000001`
- Account B: `00000000-0000-4000-8000-000000000002`

Expected baseline:

- Account A owns `world_01` only.
- Account B owns `world_02` only.
- Account A may authenticate in a World 02 client but protected World 02 access remains DENY.

## Definition of v0 DONE

This contract is green when deterministic synthetic tests prove:

- own-account allow paths;
- cross-account deny paths;
- cross-product deny paths;
- server-only entitlement mutation;
- revoked entitlement denial;
- guest-local behavior remains separate from cloud ownership.
