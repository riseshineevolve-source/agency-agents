# Optical Animals — RSE pure black/white Canva and KDP handoff

Date: 2026-10-21
Writer: Optical Animals ONE writer
Status: COMPLETE_DIGITAL_VARIANT_DELIVERED__OWNER_VISUAL_AND_PHYSICAL_PROOF_GATE

## Owner scope and decisions

Owner requested a global pure black/white visual variant, consistent intro typography, retention of single-sided wording, a restrained RSE identity, consideration of text on blank reverses, and complete Canva-to-KDP files. Earlier approved originals and grayscale final remain byte-for-byte unchanged.

The team chose RSE Optical Art Series. Ordinary reverse pages remain white; copy appears on collection entry, before the butterfly and at the end. No clinical claims or coaching slogans were introduced.

- Page 5: Familiar animals. Unexpected patterns. / Follow a line and see where it leads. / Add a color. Notice what changes. / There is no need to finish today.
- Page 45: One last flight.
- Page 48: A good place to pause.
- Before: The 18 single-page designs / are printed single-sided. / The opening and closing artworks / span two facing pages each.
- Marker warning: Alcohol markers can bleed through paper, / so always place a protective sheet / behind the page.
- Publishing identifies RSE Optical Art Series, retains exact legal text/contact URL, has no empty ISBN placeholder, and wraps the AI note across two smaller lines.

## Delivered durable files

| File | Library identity / version | Bytes | SHA256 |
|---|---|---:|---|
| WILD_ILLUSIONS_RSE_PURE_BW_KDP.pdf | libfile_aed6ac5d16d08191bed955fc490808df / 0; file_00000000976c81f590381fb663dab962 | 6588081 | 20481cc911c8970b356cc8846a2519dc4885ae296f5549719269d57e1b04d0d0 |
| WILD_ILLUSIONS_RSE_PURE_BW_CANVA.pdf | libfile_a8703b24693c8191a29f163073eb2d9e / 0; file_00000000e90481f5ada91ed301baf778 | 4974454 | ed9e1887d62569c4038ab1bea3614fb7aae833f8b9d7fcc76e50831489ebb567 |
| WILD_ILLUSIONS_RSE_PURE_BW_CANVA_PACK.zip | libfile_8882efb1921c8191bb606d8e0f2c25bb / 0; file_000000003afc81f588ab4c046c6e6fe9 | 11299101 | 14fefb0e9ad70f96b137ec426f365d2d24997e2f506c0fd83e11fbc332630f06 |
| WILD_ILLUSIONS_BW_COMPARISON.png | libfile_ac9e0caf2568819197f5031f580e70ec / 0; file_00000000d10081f5a87fb4d32629d491 | 3421044 | b3c7999a01f553d9d6fb9f11a11803b3cfe6703d963dac4d26f7957fc7386a27 |

ZIP: 58 files including import PDF, 48 numbered 300ppi bitonal PNGs, 5 intro backgrounds without utility copy, text/position manifest, Polish instructions, font license and SHA256 manifest.

## Production implementation

- Separate deterministic derivative. All 22 body images retain native 2588×3375 source grids: gray below80 becomes black, otherwise white; no dithering, resampling, despeckling or generated lookalikes.
- Measured black coverage39.17–53.40%. Soft gray modeling and metallic depth are reduced deliberately; principal contours, eyes, nostrils and optical pattern geometry remain.
- Intro utility copy EB Garamond16pt; shared headings54pt; AI note11pt. Approved Wild Illusions decorative logotype retained as artwork. No horizontal compression.
- Font sourced from official google/fonts EBGaramond variable font, instanced400; SIL OFL license included. Utility words/headings re-authored after precise glyph masks; surrounding approved art retained in derivatives.
- KDP text outlined; intro background contours vector. Body image XObjects lossless Flate, DeviceGray, BitsPerComponent1, no soft masks.
- Canva PDF has one opaque bitonal image background per content page plus genuine embedded text, avoiding thousands of imported vector elements.
- 48 pages, Media/Crop/Bleed621×810pt. Alternating TrimBoxes [0,9,612,801] and [9,9,621,801]; trim8.5×11in. Two spreads6–7 and46–47.19 fully white pages8,10,...44.45 and48 have quiet text.
- No cover included. KDP interior settings:8.5×11in, Bleed, black ink/white paper. Canva canvas8.625×11.25in already includes bleed; export PDF Print with additional Crop marks and bleed OFF. Re-preflight after Canva edits.

## Independent QA and scope

Art, editorial, typography and print-handoff agents reviewed independently. Final actual-file delta QA confirms both48-page strict parses, warning-free MuPDF/Poppler rendering of revised pages, all22 embedded body pixel streams exactly equal authorized BW80 assets, consistent embedded live Canva type, and resolved p2/p3 border collisions. Earlier complete48-page render pass retained. Root exported and checked all48 final pages; all expected live text extracted. KDP has zero fonts, metadata, annotations and soft masks. Pure black/white paint/image resources checked; normal viewer edge antialiasing is expected.

Four-file save completed successfully. Post-save hashes unchanged; both PDFs strict-parse48 pages, all pages render, Poppler text extraction zero warnings. ZIP CRC passes.

No actual Canva account import was performed: font substitution/reflow remains an import check. No physical paper/ink/gutter proof, KDP upload, paid order or release occurred. No subjective10/10 guarantee.

## Custody and continuation

Original V4 SHA256:2dbe312fe0b8df5cecac2c1bf2c90e20d7ab69a30996eee05d444e98a9174e13.
Earlier grayscale premium final SHA256:bf12439907c4481d91926bc34ef86ed51d7667a17fc712a5e8261fa33963a6ef, Library libfile_507fe3cae5088191be459397753617d0 version1. Retained as alternative, not replaced.
All five approved intro source hashes checked unchanged. No seek-and-find token was fabricated; no source hero overwritten.
Product branch riseshineevolve-source/riseshineevolve feat/optical-animals-book-creator unchanged. Large art/PDF files remain outside Git.

Reproducible workspace producer: /workspace/scratch/b288b564abb1/tmp/bw-rse/build_bw_book.py; finalizer finalize_pack.py; source manifest body-assets/manifest.json; preflight.json; final-contact.jpg. Workspace paths are session-local; durable delivered PDFs/ZIP are the handoff of record.

Next safe task: owner compare pure B/W vs retained grayscale version, inspect actual Canva import if editing, and review a physical proof. Apply only concrete authorized corrections; do not publish automatically or reprocess approved hero originals.

model_policy_ack: rse-weekly-usage-2026-10-21-v1
recommended_profile: production
runtime_model_observed: UNKNOWN
runtime_reasoning_observed: UNKNOWN
runtime_speed_observed: UNKNOWN
application_status: RECOMMENDATION_ONLY
