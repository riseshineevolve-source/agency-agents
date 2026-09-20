# RSE Consumer Platform + Bilingual App Factory

Status: TARGET ARCHITECTURE / NO DEPLOYMENT AUTHORIZATION
Updated: 2026-09-20

## Purpose

Define the intended systems architecture for bringing RSE public apps online in English and Polish without creating one backend per app. This is an architecture constraint for future implementation, not authorization to create projects, restore paid services, publish apps, change pricing, or move private data.

## Product boundary

### Shared public consumer platform candidates
- RSE website/account surfaces where a customer account is actually needed
- World 01
- World 02
- 24 Gentle Steps to Christmas app
- future ordinary RSE interactive-book/content-pack apps after explicit portfolio approval

### Separate security/data domains
- Happy Me: retain a separate family/child-sensitive backend unless a later privacy/security review explicitly approves consolidation.
- Senior / Hello Today: retain its existing Firebase/Google-oriented architecture unless a later technical decision explicitly changes it.
- Mind Bloom: private owner-only application; not a commercial RSE consumer product and must not share consumer user data/backend by default.
- Opinie: real production data stays local/offline.
- Smart CV Tailor and Domowe Finanse: LOCAL_PRIVATE; no consumer cloud backend.

## Target topology

1. **RSE Consumer Platform**
   - shared authentication where account functionality is justified;
   - shared user/profile identity;
   - product-scoped progress and preferences;
   - entitlements/purchase state;
   - optional cloud sync;
   - strict RLS/least-privilege boundaries by user/profile/product.

2. **RSE Interactive Book App Factory**
   - one reusable application/runtime architecture;
   - products are structured content packs rather than independent codebases where feasible;
   - World 01 is the intended first factory pilot once its source is approved for app conversion;
   - World 02 and 24 Gentle Steps should reuse the proven engine rather than fork it.
   - versioned content contract: `orchestration/architecture/RSE_INTERACTIVE_BOOK_CONTENT_CONTRACT_V0.md`.

3. **Localization**
   - one app binary/product listing architecture per product, not separate PL and EN apps by default;
   - English remains canonical source until locked;
   - Polish Localization Engine produces approved pl-PL content from stable English source;
   - content IDs remain language-neutral and translations map to the same semantic object;
   - app UI strings and book/activity content are versioned separately but validated together before release.

4. **Offline-first**
   - core purchased/installed content should work without network where product behavior allows;
   - local progress is authoritative while offline and syncs safely when connectivity returns;
   - account creation should not be required merely to start ordinary content where business/privacy requirements permit guest-first UX.

## Systems responsibility map

- GitHub: source, CI, durable technical state.
- Google Play: Android distribution, test tracks, Play Billing, store declarations.
- Supabase Auth/Postgres: candidate shared consumer identity/data platform, subject to implementation review.
- Supabase RLS: user/profile/product data isolation.
- Firebase services: retain where already architecturally required, including Senior; app analytics/crash/push choices are product-specific and must pass privacy review.
- Cloudflare: website/DNS/CDN/edge/public delivery; not the default consumer password authority.
- RSE Polish Localization Engine: EN -> pl-PL transcreation/QA pipeline.
- RSE Interactive Book App Factory: structured content -> bilingual app experience.

## Cost-control rule

**No agent may create a new Supabase/Firebase/backend project merely because a new app exists.**

Before creating any new backend, the implementation packet must document:
1. why the RSE Consumer Platform cannot safely serve the product;
2. whether legal/privacy/security isolation requires a separate project;
3. expected active-user/storage/egress/auth requirements;
4. free-tier impact and likely paid-tier trigger;
5. migration/exit implications.

Project creation/restoration that can incur cost remains an OWNER GATE.

## Current Supabase planning assumption

Free-tier active-project capacity is scarce and should be treated as shared infrastructure, not per-app allocation. Current durable orchestration already records Happy Me backend restoration as owner-gated due to possible billing impact. Do not restore it silently.

The desired long-term logical allocation is:
- shared RSE Consumer Platform for ordinary public consumer apps;
- Happy Me separate where family/child sensitivity warrants isolation;
- Mind Bloom separate and private while it remains the owner's personal Chief of Staff.

This is a logical target, not authorization to migrate existing live data or merge current projects.

## Consumer data model direction

Minimum product-scoped primitives:
- account/user identity;
- household or profile only where genuinely needed;
- product catalog ID;
- content pack/version ID;
- progress/checkpoint;
- language/locale preference;
- entitlement/purchase verification state;
- sync metadata and deletion/audit state.

Never rely on client-provided product ownership without server-side verification for paid entitlements.

Authentication and entitlement are separate security decisions. A successful shared RSE login identifies the account but does not unlock another product. Protected access must be evaluated against the exact product-scoped entitlement. See `RSE_CONSUMER_ENTITLEMENT_MODEL_V0.md`.

## Factory content contract direction

The current synthetic-only v0 contract is `RSE_INTERACTIVE_BOOK_CONTENT_CONTRACT_V0.md`. It defines the language-neutral envelope, localized-copy separation, asset references, progress direction, entitlement boundary, localization gates, deterministic validator requirements and synthetic acceptance fixtures.

A reusable content pack separates:
- language-neutral IDs and activity semantics;
- EN canonical copy;
- pl-PL approved copy;
- assets/media references;
- interaction type/config;
- progression/unlock rules;
- accessibility metadata;
- content schema version.

Do not duplicate application business logic merely to localize content.

## Candidate rollout sequence

1. Preserve/finish current Wave 1 apps and external gates.
2. Specify RSE Consumer identity/progress/entitlement schema using synthetic fixtures only. **Synthetic data contract and product-scoped entitlement model are now specified; deterministic contract tests are being added before any live backend work.**
3. Specify Interactive Book Factory content schema and renderer contract. **Content contract v0 plus deterministic synthetic validator/fixture are implemented and CI-verified; no real product conversion is authorized yet.**
4. Select/approve World 01 as first conversion pilot.
5. Build and verify EN pilot offline-first.
6. Pass stable EN source through Polish Localization Engine and bilingual QA.
7. Validate store/privacy/billing requirements before release.
8. Reuse the proven factory for World 02.
9. Reuse the same factory for 24 Gentle Steps to Christmas, respecting its existing canonical source/localization gates.
10. Add future content-pack apps only through the same architecture/change filter.

## Explicit non-goals / owner gates

This document does NOT authorize:
- a new product line;
- a new paid Supabase/Firebase project;
- restoring Happy Me backend;
- migrating existing users;
- combining child/family data with ordinary consumer data;
- publishing World 01/02/Gentle Steps;
- pricing/subscription decisions;
- paid marketing;
- legal/privacy declarations;
- turning private Mind Bloom into a commercial product.

## Definition of architectural DONE

Before the first factory-based public app ships, evidence must show:
- one versioned content schema;
- one EN/pl-PL localization mapping strategy;
- deterministic content validation;
- offline progress behavior and conflict strategy;
- authenticated sync only where needed;
- product-scoped RLS/authorization tests;
- verified Play purchase/entitlement flow if monetized;
- account deletion/data export behavior where applicable;
- privacy/Data Safety review for the actual data collected;
- accessibility and real-device QA;
- no unnecessary backend project proliferation.