# Existing Detective Book Factory -> RSE Book Factory v2 migration map
Date: 2026-10-03
Status: VERIFIED AGAINST LIVE PR #571 HEAD

## Existing factory found

Repo: `riseshineevolve-source/RISE.SHINE.EVOLVE`
Branch: `feature/detective-book-factory`
PR: #571 — Build reusable Happy Makers Detective Academy Book Factory

This is a substantial implementation, not a prototype.

## Reuse as-is or adapt

### KEEP / PORT
- `content/DETECTIVE_ACADEMY_BOOK1_TEXT_GOLD_MASTER_V3.md`
- `scripts/verify_v3_final_text_source.py`
- `scripts/validate_book1_v3_logic.py`
- `scripts/validate_spatial_map_pilot.py`
- `scripts/validate_spatial_source_manifest.py`
- `content/v3_locked_spatial_evidence_contract.json`
- `content/v3_witness_board_copy.json`
- `content/spatial_source_manifest_final.yml`
- `content/spatial_room_skin.yml`
- `content/modern_prop_catalog.source-locked.yml`
- owner visual contracts / hash gates
- preview/contact-sheet tooling
- KDP/preflight logic

### MIGRATE / REPLACE
- `render_book.py` page layout -> React/CSS/SVG components
- `scripts/build_v3_premium_interior.py` layout drawing -> normalized-model adapter + v2 templates
- versioned owner-review builders `build_owner_review_v*.py` -> retire after parity proof
- legacy phase/production YAML direct rendering -> normalize then render
- raster/hybrid map presentation -> SVG visual layer using existing topology

### ARCHIVE / DO NOT FEED DIRECTLY TO RENDERER
- stale `book1_en_production.yml` reader copy;
- phase YAMLs as renderer truth;
- V4/V4.1 reader prose when it conflicts with V3;
- local-only hydrated masters as independent text authorities;
- any script that rewrites/crops/guesses final owner visuals.

## Existing weakness demonstrated

`book1_en_production.yml` still contains stale reader-facing Case 01 aliases ARI / BEA / COLE / DANI even though current V3 and current owner work use QUILL / MORSE / PIP / KNOX.

This is the exact class of problem v2 normalizer must make impossible.

## Current dependency stack

Existing factory:
- ReportLab
- PyYAML
- Pillow
- PyMuPDF
- pypdf
- pdfplumber

These remain useful for validation/migration, but ReportLab must no longer be the primary visual-template layer.

## Migration rule

No feature parity rewrite from memory.

For every capability:
1. identify existing source/validator;
2. port it or wrap it;
3. add test;
4. compare old/new evidence;
5. only then retire legacy code.

## First parity target

Case 02 is the factory acceptance test.

The v2 Case 02 proof must pass:
- canonical text source checks;
- witness count/name checks;
- puzzle geometry/solution checks;
- character/logo asset locks;
- print-safe margins;
- visual style review;
- output manifest/checksums.

Only then can batch rendering begin.
