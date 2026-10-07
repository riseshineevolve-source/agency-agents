# RSE Graphic Gold Library v1

Status: CANONICAL ARCHITECTURE / IMPLEMENTATION ACTIVE
Date: 2026-10-07
Owner: RSE Production Control Plane

## Decision

The first Graphic Gold Library is extracted from the strongest owner-created Detective Academy first ~18 pages.

It is NOT derived from the rejected boxy frontmatter pilots.

The first 18 pages are the visual training/reference set. Their composition is recovered first, corrected for official Happy Makers identities, then encoded into reusable graphic families.

## Who creates a Gold Family

A Gold Family is created by a fixed production squad with clear authority:

### 1. Visual Storyteller — CREATIVE LEAD
Owns:
- visual grammar extraction from owner gold pages;
- pacing;
- composition;
- image/text balance;
- graphic-novel feel;
- identifying which visual motifs are structural rather than decorative.

Does not write canonical copy.

### 2. Brand Guardian — IDENTITY VETO
Owns:
- RSE / product visual identity;
- exact Happy Makers likeness compliance;
- logo/character consistency;
- preventing generic SaaS/corporate/worksheet drift.

May reject a technically correct candidate for identity/style drift.

### 3. UI Finish-Gate Reviewer — FAMILY QUALITY GATE
Owns:
- family-level visual QA at real print scale;
- hierarchy, balance, polish, consistency;
- visual regression target.

Technical PASS cannot override a visual FAIL.

### 4. Universal Document Compiler + Codex — IMPLEMENTATION
Owns:
- converting the approved visual grammar into deterministic React/CSS/SVG/Vivliostyle components;
- schemas;
- slot contracts;
- overflow variants;
- hashes;
- tests;
- page cache;
- visual regression fixtures.

Codex never invents the family visual grammar.

### 5. RSE Book Production Agent — REGISTRY/FREEZE OWNER
Owns:
- family manifest;
- reference page hashes;
- allowed variants;
- template SHA;
- dependency graph;
- freeze state;
- changed-page review routing.

## Creation lifecycle

OWNER GOLD PAGE
-> Visual Storyteller extraction
-> Brand Guardian review
-> family spec
-> deterministic implementation
-> actual print-scale candidate
-> UI Finish-Gate review
-> ONE owner family gate if genuinely new
-> FROZEN_GOLD_FAMILY
-> reusable across pages/books

## Initial Detective Gold Library

Expected first families from the recovered first ~18 pages:

- GOLD.CINEMATIC_INVITATION
- GOLD.ACADEMY_ORIENTATION
- GOLD.HAPPY_MAKERS_GROUP_INTRO
- GOLD.CHARACTER_DOSSIER
- GOLD.HM_COMMS
- GOLD.RECRUIT_CREDENTIAL
- GOLD.CASE_INTRO
- GOLD.WITNESS_EVIDENCE_BOARD
- GOLD.SPATIAL_MAP
- GOLD.VISUAL_COMPARE_AB
- GOLD.CASE_WALL_WORKSPACE
- GOLD.ACT_BREAKER

Hints/solutions/verdict families may be promoted from later strongest pages once their real references are inspected.

## Reuse law

New RSE book/page:
1. classify semantic page role;
2. find closest approved Gold Family;
3. populate structured slots;
4. create only missing atomic art;
5. deterministic render;
6. automated QA;
7. owner sees only true exceptions/new-family requests.

No existing Gold Family match -> NEW_FAMILY_REQUEST.
Never silently fall back to generic boxes.

## Family manifest minimum

- family_id
- semantic_roles
- owner_gold_reference_pages
- reference_artifact_sha256
- template_id
- template_sha256
- typography_contract
- composition_contract
- asset_slots
- canonical_copy_slots
- visual_motifs
- allowed_variants
- overflow_policy
- print_scale_rules
- automated_QA
- visual_regression_threshold
- status

## Throughput target

The first Gold Library costs time once.
The second and later books must reuse it.

Normal target:
- >=70% pages use existing frozen Gold Families;
- <=20% pages need a new visual-family decision;
- owner review = changed/new exceptions only.

If every page still needs bespoke art direction, the factory is not complete.
