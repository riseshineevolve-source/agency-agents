# Interactive Book Factory v0 checkpoint — 2026-09-20

Status: **PASS / SYNTHETIC CONTRACT ONLY**

## Durable result

The first safe implementation slice below all product/publication gates is complete on `main`:

- deterministic validator: `scripts/validate-interactive-book-pack.py`;
- invented bilingual EN + pl-PL `synthetic_world` fixture only;
- fail-closed validator tests covering the v0 contract error classes;
- GitHub Actions workflow: `Interactive Book Contract`;
- live CI run `35522302101` on head `ed04e55b3752ebb117eba92be0617dbec12cbe37`: **SUCCESS**.

The validator enforces the bounded v0 contract including stable activity IDs, locale coverage, copy-only localization, option/action parity, allow-listed activity/interaction types, valid unlock targets, unsupported progression-cycle rejection, accessibility requirements, and supported schema/runtime versions.

## Boundaries preserved

- No World 01, World 02, Gentle Steps, Detective, Happy Me, unpublished product copy, or owner-private data was used as a fixture.
- No real-product conversion is authorized by this checkpoint.
- No backend was created or restored.
- No paid service, pricing, publication, store action, legal/compliance decision, or user migration was performed.
- Mind Bloom remains private and outside the consumer factory.
- Happy Me remains a separate family/child-sensitive backend domain.

## Next gate

Do **not** convert a real product merely to create activity. The intended first real pilot remains World 01 only after explicit source/conversion approval. Until then, safe work is limited to correcting verified contract/CI regressions or architecture dependencies that are independently required.
