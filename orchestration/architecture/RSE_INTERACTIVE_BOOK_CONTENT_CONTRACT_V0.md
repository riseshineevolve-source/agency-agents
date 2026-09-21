# RSE Interactive Book Content Contract v0

Status: SPECIFICATION ONLY / SYNTHETIC FIXTURES / NO PRODUCT CONVERSION AUTHORIZATION
Updated: 2026-09-20

## Purpose

Define the smallest reusable, language-neutral contract needed by the future RSE Interactive Book App Factory. This is an AUTO architecture slice below publication/product gates. It does not authorize conversion, publication, pricing, backend creation, migration of existing users, or use of unpublished/private product copy.

## Design constraints

- One product/runtime architecture supports EN + pl-PL; do not fork application logic by language.
- English is the canonical source until a source is explicitly locked.
- IDs are language-neutral and stable across translations.
- Core installed content is offline-first where product behavior permits.
- Account/cloud sync is optional for ordinary content and must not be required merely to open a content pack unless a later product requirement says otherwise.
- Product ownership/paid entitlement may never be trusted solely from client state.
- Product-specific content remains isolated by `product_id` and `content_pack_id`.
- Child/family-sensitive products do not automatically join the shared consumer backend.

## Versioned pack envelope

```json
{
  "schema_version": "0.1.0",
  "product_id": "synthetic_world",
  "content_pack_id": "synthetic_world_core",
  "content_version": "1.0.0",
  "canonical_locale": "en",
  "supported_locales": ["en", "pl-PL"],
  "minimum_runtime_contract": "0.1.0",
  "activities": []
}
```

Required invariants:

1. `schema_version`, `product_id`, `content_pack_id`, `content_version`, and `canonical_locale` are non-empty.
2. `canonical_locale` must occur in `supported_locales`.
3. Every activity ID is unique inside the pack.
4. Every localization record refers to an existing language-neutral object ID.
5. No translated object may silently introduce a new activity semantic/configuration absent from the canonical object.
6. Unsupported schema/runtime versions fail closed rather than partially rendering.

## Language-neutral activity object

Minimum fields:

```json
{
  "activity_id": "mission_001",
  "activity_type": "reflection_choice",
  "sequence": 1,
  "required": true,
  "interaction": {
    "mode": "single_choice",
    "option_ids": ["option_a", "option_b"]
  },
  "progress": {
    "completion_rule": "submit_once",
    "unlock_ids": ["mission_002"]
  },
  "assets": [],
  "accessibility": {
    "requires_audio_alternative": false,
    "requires_motion_reduction_variant": false
  }
}
```

`activity_type` and `interaction.mode` must come from a runtime allow-list. Unknown types fail validation before packaging.

## Localized copy object

Localized copy is separate from behavior/configuration:

```json
{
  "locale": "en",
  "activity_id": "mission_001",
  "title": "Synthetic mission",
  "prompt": "Choose one synthetic option.",
  "options": {
    "option_a": "Synthetic A",
    "option_b": "Synthetic B"
  },
  "accessibility": {
    "screen_reader_prompt": "Choose one option."
  }
}
```

The equivalent `pl-PL` object must use the same `activity_id` and option IDs. Localized copy may reorder display text only where the runtime explicitly supports it; it may not change progression, entitlement, collection, privacy, or account behavior.

## Asset references

Content packs refer to assets by stable logical IDs rather than environment URLs:

```json
{
  "asset_id": "mission_001_hero",
  "kind": "image",
  "bundled_path": "assets/mission_001_hero.webp",
  "alt_copy_key": "mission_001.hero_alt",
  "required_offline": true
}
```

Remote asset delivery, if later used, must have an explicit offline/cache policy and integrity/version check. Private/user media is outside this content-pack contract.

## Progress contract

Local progress record direction:

```json
{
  "product_id": "synthetic_world",
  "content_pack_id": "synthetic_world_core",
  "content_version": "1.0.0",
  "profile_id": "local-profile-placeholder",
  "activity_id": "mission_001",
  "state": "completed",
  "completed_at": "client-generated-placeholder",
  "revision": 1
}
```

Rules:

- Local progress must work without network for offline-capable products.
- Sync identity is separate from display copy and locale.
- Sync conflict behavior must be deterministic and documented before implementation.
- A newer content version must not silently erase progress.
- Deletion/account lifecycle must define whether local-only progress is removed, retained, or exportable before public release.

## Entitlement boundary

Content-pack installation/visibility and paid entitlement are separate concepts.

A client may cache an entitlement for offline UX, but server-verified purchase/entitlement state is authoritative when monetization requires it. Synthetic schema/tests may be built before pricing or billing decisions; no pricing model is implied here.

Minimum future entitlement dimensions:

- `user_id` or account identity where accounts are used;
- `product_id`;
- `entitlement_id`;
- source/provider;
- verification state;
- verified timestamp;
- revocation/expiry state where applicable.

## Localization validation gates

Before a bilingual pack can be release-candidate quality:

1. 100% of required canonical IDs exist in `en`.
2. 100% of release-required IDs exist in `pl-PL`.
3. No orphan translation IDs.
4. Placeholder/token parity passes.
5. Option/action IDs are identical across locales.
6. Accessibility strings required by the activity are present in both release locales.
7. Polish copy has passed the RSE Polish Localization Engine/human quality gate appropriate to the product.
8. UI/layout fit is checked separately from linguistic correctness.

## Deterministic validator direction

The factory validator should fail a pack for at least:

- duplicate IDs;
- missing required locale;
- missing translation object;
- orphan translation object;
- unknown activity/interaction type;
- missing referenced asset;
- invalid unlock target;
- cyclic progression where cycles are not explicitly supported;
- behavior mismatch introduced through localization;
- unsupported schema version;
- malformed accessibility requirements.

Warnings, not automatic failures, may include unusually long localized copy or optional asset absence, but release gates decide whether warnings are acceptable.

## Synthetic acceptance fixture

The first implementation fixture must be invented content only, e.g. `synthetic_world`, with at least:

- 3 activities;
- EN + pl-PL copy;
- one branching/unlock relationship;
- one bundled image reference;
- one accessibility requirement;
- one intentionally broken pack for each fail-closed validator class.

Do not use World 01, World 02, Gentle Steps, Detective, Happy Me, unpublished book copy, or owner-private data merely to test the contract.

## Relationship to real products

- World 01 remains the intended first real pilot only after source/conversion approval.
- World 02 should reuse the proven contract/runtime.
- 24 Gentle Steps to Christmas should reuse it after its current canonical-source/localization gates are satisfied.
- Happy Me remains a separate family/child-sensitive backend domain and is not silently migrated by this factory.
- Mind Bloom remains private owner-only and outside the consumer factory.

## Definition of v0 spec DONE

This specification is ready for an implementation slice when:

- architecture authority points to it;
- synthetic fixtures can be created without product/private content;
- deterministic validation can be implemented without choosing pricing, publication, legal declarations, or a new paid backend;
- any future real-product pilot still requires its explicit source/conversion gate.
