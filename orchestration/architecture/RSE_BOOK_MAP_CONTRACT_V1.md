# RSE Book Map Contract v1

Status: CANONICAL
Date: 2026-10-04
Architecture parent: `orchestration/architecture/RSE_BOOK_AGENT_V3.md`

## Purpose

The Book Map is the machine-readable physical production plan for one edition of one book.
It is the only object the renderer is allowed to use to decide what belongs on each physical page.

It prevents a local change from silently altering unrelated pages.

## Required identity

- `schema_version`
- `book_id`
- `edition_id`
- `language`
- `trim`
- `source_lock`
- `renderer_lock`
- `design_lock`
- `templates`
- `assets`
- `pages`
- `dependency_graph`
- `release`

### Mandatory editorial source lock

For any manuscript that was not already owner-approved frozen input before RSE production, `source_lock` must include:
- exact premium content master path;
- premium content master SHA-256 / Git blob identity;
- `CONTENT_FREEZE_MANIFEST` path + hash;
- Content Map hash;
- language/edition identity;
- unresolved approved exceptions, if any.

The canonical pre-freeze editorial workflow is:
`orchestration/architecture/RSE_PREMIUM_BOOK_CONTENT_UPGRADE_PROTOCOL_V1.md`.

If the freeze manifest is missing, the Book Map generator must fail closed rather than select an informal "latest" manuscript or rewrite copy during rendering.

## Page record

Every physical page has a stable `page_id` that never changes because page content changes.

Required fields:
- `page_id`
- `physical_page`
- `role`
- `family`
- `render_mode`: FROZEN | FIXED_TEMPLATE | FLOW_SECTION
- `source_refs`
- `source_sha256`
- `template_id`
- `template_sha256`
- `asset_ids`
- `asset_sha256`
- `puzzle_sha256` when applicable
- `renderer_sha256`
- `page_input_sha256`
- `output_png_sha256`
- `output_pdf_sha256`
- `lock_state`
- `review_state`
- `dependencies`

## Input hash

`page_input_sha256` is computed over a canonical serialization of:
- canonical content hash;
- template hash;
- exact referenced asset hashes;
- puzzle/data hash;
- book/trim configuration relevant to the page;
- renderer version/hash.

No timestamp, filesystem path or nondeterministic value may enter the hash.

## Dependency graph

Nodes may include:
- content block;
- template;
- design token set;
- asset;
- puzzle/runtime;
- page;
- flow section;
- final assembly.

Edges are explicit `depends_on` relationships.

Changed scope is the reverse dependency closure of changed nodes.

A build must emit:
- `changed_nodes`
- `affected_pages`
- `unchanged_pages`
- `reason_by_page`

No page outside the affected set may be regenerated unless the renderer version or a global page dependency changed.

## Lock states

Content:
- DRAFT
- FROZEN_CONTENT

Assets:
- NEEDS_ART
- CANDIDATE
- APPROVED
- FROZEN_ASSET

Templates:
- DRAFT
- GOLDEN_CANDIDATE
- OWNER_APPROVED
- FROZEN_TEMPLATE

Pages:
- NEEDS_BUILD
- NEEDS_REVIEW
- APPROVED
- FROZEN_PAGE
- UNCHANGED

## Unlock record

Any mutation of a frozen object requires:
- `unlock_id`
- `target_id`
- `target_type`
- `old_sha256`
- `reason`
- `authorized_by`
- `authorized_at`
- `expected_scope`

After replacement:
- `new_sha256`
- actual affected pages are compared with expected scope.

If actual scope is broader, fail closed.

## Asset slot record

Required:
- `asset_id`
- `class`
- `semantic_id`
- `generation_mode`
- `style_anchor_ids`
- `character_reference_ids`
- `text_allowed`
- `background_contract`
- `geometry_contract`
- `approved_sha256`
- `status`

Generated art is never referenced by loose filename.

## Review manifest

Every proof run creates `REVIEW_MANIFEST.json` with:
- total page count;
- changed page count;
- unchanged page count;
- pages needing owner review;
- pages failing automated QA;
- new asset candidates;
- new template candidates;
- reason for every review item;
- paths to small review sheets.

Default owner-review set = exceptions only.

## Release manifest

A release candidate records:
- exact source lock;
- Book Map hash;
- template hashes;
- asset hashes;
- per-page input/output hashes;
- assembled PDF hash;
- automated QA results;
- unresolved exceptions;
- owner release decision.

A release cannot be claimed from chat prose.
