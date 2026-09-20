# RSE Consumer Platform — Identity + Entitlement Model v0

Status: TARGET SECURITY/ACCESS CONTRACT / SYNTHETIC ONLY / NO DEPLOYMENT AUTHORIZATION
Updated: 2026-09-20

## Core principle

**Authentication proves who the person is. Entitlement proves which product/content that authenticated account may access.**

A shared RSE account is intentionally NOT a shared all-products licence.

The same RSE credentials may authenticate in World 01, World 02 and Gentle Steps, while access remains product-scoped.

Example:
- account A signs in successfully with the same RSE identity in World 01 and World 02;
- account A owns only the verified entitlement for `world_01`;
- World 01 opens paid content;
- World 02 may recognize the account but MUST keep paid World 02 content locked until a valid `world_02` entitlement exists.

## Access decision

For protected product content, access requires BOTH:

1. a valid authenticated/account context when the product requires cloud/account features; and
2. a current server-authoritative entitlement matching the exact `product_id`.

Conceptually:

`can_access(account_id, product_id) = authenticated_if_required AND entitlement(account_id, product_id).is_valid`

There is no wildcard such as `account_exists -> all_products`.

## Google Play boundary

Google Play controls store acquisition and purchase state. RSE controls account identity and cloud product access.

A Google Play account and an RSE account are separate identity domains. Do not assume their email addresses are identical.

For monetized access:
- the Android client obtains purchase evidence from Google Play;
- purchase evidence is verified through a trusted server-side path before granting durable cloud entitlement;
- the resulting RSE entitlement is bound to the exact `account_id + product_id`;
- raw purchase tokens are never treated as ordinary profile data or committed to GitHub fixtures;
- revocation/refund/expiry state must be able to remove future protected access.

If World 01 and World 02 are separate paid Play applications, Play itself also restricts legitimate store installation by product/package purchase state. The RSE backend must still avoid treating successful RSE login as proof of ownership of another product.

## Shared-account UX

Shared identity is for convenience and continuity:
- one sign-in;
- optional shared profile basics/preferences;
- optional cross-device sync;
- future cross-product discovery where approved.

It does NOT imply:
- bundled ownership;
- cross-product progress mutation;
- cross-product storage access;
- access to another product's paid content;
- access to child/family-sensitive domains.

## Required authorization invariants

Before production:
1. `world_01` entitlement cannot unlock `world_02`.
2. A client cannot create or upgrade its own authoritative entitlement.
3. Missing entitlement fails closed.
4. Revoked/expired entitlement fails closed for protected cloud content.
5. One product cannot write another product's progress namespace.
6. Cross-user access fails regardless of matching product entitlement.
7. Locale choice never changes entitlement scope.
8. Guest/local progress does not become paid ownership.
9. Linking a guest session to an account does not auto-grant products.
10. Product access checks are enforced at trusted backend/RLS/function boundaries, not only by hiding UI buttons.

## Product-scoped key

The minimum durable entitlement key is:

`(account_id, product_id, entitlement_type)`

Optional dimensions may later include:
- content pack / edition,
- platform/source,
- expiry,
- family/household scope where explicitly approved,
- promotional/grant source.

No implementation may replace this with a single `is_premium` flag on the account.

## Failure mode to prevent

Bad design:

`user signed in -> premium=true -> every app opens`

Required design:

`user signed in -> query exact product entitlement -> allow/deny exact product`

## Relationship to shared Supabase

A single Supabase project can safely serve multiple ordinary RSE apps only if authorization is product-scoped and covered by deterministic + real RLS tests.

Shared infrastructure is a cost/operations decision. It is never permission to weaken data boundaries.

Happy Me remains a separate candidate security domain because its family/child-sensitive model has materially different risk and least-privilege requirements.

## Owner gates

This contract does not authorize:
- pricing;
- subscription/bundle decisions;
- live Play Billing configuration;
- backend deployment;
- Supabase project creation/restoration;
- migration of real users;
- combining Happy Me into the shared consumer project.
