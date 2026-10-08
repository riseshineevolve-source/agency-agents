# Optical Halloween / Batch 01 / Native image run QA checkpoint
Date: 2026-10-08. Source of truth remains existing `BATCH_01_CREATIVE_GOLD_PROMPTS_V01.md`, `world-bibles/HOUSE_MASTER_V01.md`, `OPTICAL_HALLOWEEN_VISUAL_DNA_V1.md`, and `BATCH_01_QA_STATUS_V01.md`. Existing source documents unchanged.

## Status
Four actual standalone native ChatGPT image generations occurred: H-01 v01, v02, v03; H-02 v01. Each was a distinct single full-page portrait image; no contact sheet. **None passes creative/canonical QA; no GOLD.** Intended aspect 17:22, actual raster near 1103 x 1426 px, **not print-ready 2550 x 3300 / 300 dpi**.

## Candidate inventory (generated in ChatGPT; original PNGs held in conversation sandbox, NOT uploaded to GitHub)
- `OH_H01_v01_REJECTED.png`: ornate key lying horizontally on tabletop, no Mara hand, no real key-to-latch insertion, no jamb plane-mirror contact. Candle/books/staircase/cat and fine hatching intrude. Image generator gen_id `2e2ed04d-eb2b-4e09-8778-4ea329697c6a`.
- `OH_H01_v02_REJECTED.png`: visible hand and mirror, but the key contains a pictorial house, has ornate skeleton-key ornament; no real receiving slit or insertion. Cat, baroque mirror, hallway dominate. **Relative strongest composition (BEST_CANDIDATE_FOR_REVISION only, NOT ACCEPTED)**. gen_id `3cd453c1-541d-4abd-8663-cf68ed743889`.
- `OH_H01_v03_REJECTED.png`: returned to ornate key on tabletop; no hand/latch/insertion; clutter and hatching. gen_id `2b37bd6e-6a9a-4e7d-91b9-619c39e0dfac`.
- `OH_H02_v01_REJECTED.png`: repeats large H-01 key/candle imagery, giant eye-emphasis cat; required lintel-relief cup-offering gesture and correct floor reflection/glove cabinet/clock absent. gen_id `399d7091-6901-40ad-956e-a06ba8a81a37`.

## QA perspectives (editorial lenses, no independently launched agents)
Visual Storyteller: neither H-01's observed-contact event nor H-02's reflected offer is depicted. Brand Guardian: fantasy-key/chandelier/generic haunted-house motifs violate premium DNA. Image Prompt Engineer: source A/B selections correct; output ignores primary constraints even after narrowing. Reality Checker: no H-01 slit-contact/mirror validation; no H-02 floor/source reflection ray validation. Print Finish-Gate: high-frequency strokes and thin white gaps; actual pixel count insufficient for intended 8.5x11 inch 300-dpi output. All retain HOLD/REJECT and NO GOLD.

## Operational caution
Repeated native generation calls in the same turn reproduced the ornate key/haunted foyer motif despite H-02 being a different source prompt. Further uncontrolled calls risk filling the batch with non-canonical material. Start H-02 and later images only when independent scene-specific control works; don't count rejects as production output. Do not modify Optical Animals.

## Asset storage truth
All four actual originals exported in the current ChatGPT conversation under `/mnt/data/optical-halloween/BATCH_01/` and in an archive `BATCH_01_REJECTED_CANDIDATES_2026-10-08.zip`. Those sandbox files are **not yet in GitHub** and should not be treated as durable repository assets. Any later transfer requires a verified upload/commit.