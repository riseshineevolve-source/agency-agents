# Optical Animals — FINAL GRAY15 Amazon interior and Canva handoff

Date: 2026-10-21
ONE writer: Optical Animals
Status: FINAL_GRAY15_INTERIOR_DELIVERED__DIGITAL_QA_PASS__COVER_AND_PHYSICAL_RELEASE_GATE

## Owner authorization and resulting book

Owner approved applying the selected15% lighter-gray treatment to the whole book and completing all accepted agent improvements for Amazon readiness. This supersedes the one-image tonal-choice gate. The selected publication treatment is soft grayscale with lighter shading, not the earlier pure B/W alternative.

Final48-page interior combines all20 grayscale artworks (22 image pages) with the latest RSE Optical Art Series intro/copy/typography. The selected lion matches the approved15% trial pixel-for-pixel. No generated colored examples were inserted into the book.

## Canonical deliverables

| File | Durable identity / version | Bytes | SHA256 |
|---|---|---:|---|
| WILD_ILLUSIONS_RSE_FINAL_GRAY15_KDP.pdf | libfile_507fe3cae5088191be459397753617d0 v2; file_00000000bc0081f587e6201bee2f9eb9; /AI AGENTS/WILD_ILLUSIONS_RSE_FINAL_GRAY15_KDP.pdf | 66633025 | 20442ed44576f27b92d59bde138285d7529e978bfd196948ac1f29a6be16821f |
| WILD_ILLUSIONS_RSE_FINAL_GRAY15_CANVA.pdf | libfile_4b6440500a0c81918a1f0315513d5ab3 v0; file_00000000efc081f5a1b79d3b38889c75 | 65019398 | b5853b0f8ce66dadee5d20071e5e9d08a89598ac17c586e87256ec9de225d8e0 |
| WILD_ILLUSIONS_RSE_FINAL_GRAY15_CANVA_PACK.zip | libfile_2ae552e0151881919c6a1c49b01aef5a v0; file_000000009998820d80dd0047ed878771 | 133719479 | ff3bc147ea90757f417a81eb7b8b98812f120fca8b05d239b1ae98a5cd4003db |

KDP replaced the canonical grayscale book identity with expected_current_version1, preserving its history. Prior grayscale v1 (SHA256bf12439907c4481d91926bc34ef86ed51d7667a17fc712a5e8261fa33963a6ef) remains historical source, not the current final. Local original/source files remain byte-identical. Existing B/W variant identities remain as alternatives.

ZIP contains58files: live-text import PDF,48 numbered300ppi grayscale PNGs,5 intro backgrounds, exact copy/layout manifest, Polish instructions, font license and SHA256 manifest. ZIP CRC verified.

## Applied art treatment

Pointwise monotone gray-mask transformation on original2588×3375 image grids. Black and near-black0–24 plus white255 locked exactly; smooth weighting24–72; no spatial edits, resampling, dithering, despeckling or new anatomy/pattern generation. Each artwork calibrated to approximately15% lower digital density sum(255-value) for nonprotected gray. Actual14.9937–15.0111%. This metric is digital tone, not measured physical ink consumption.

Opening6–7 and butterfly46–47 each use one shared LUT across both halves, preserving tonal continuity. All20 artworks retain many gray levels and3D modeling. Approved hero originals unchanged; no seek-and-find tokens fabricated.

Only22 body image streams changed relative to the approved RSE B/W layout. All paint commands, text, transforms, trim boxes and26 non-art-page appearances are unchanged. Lossless8-bit DeviceGray images with Flate/PNG predictor15, no soft masks.

## Agent improvements retained

- RSE Optical Art Series identity, not Happy Makers.
- EB Garamond16pt utility copy,54pt headings,11pt AI note; no horizontal compression. Decorative Wild Illusions logotype retained as art.
- Publishing has accurate legal/contact text, no empty ISBN label, two-line smaller AI note.
- Before truthfully describes18 single-page designs printed single-sided and opening/closing two-page spreads. Three-line marker warning fits its border.
- Color Your Way instructions and test fields intact.
- Collection entry: Familiar animals. Unexpected patterns. / Follow a line and see where it leads. / Add a color. Notice what changes. / There is no need to finish today.
- Ordinary reverse pages white; page44 remains the horse reverse. Page45: One last flight. Page48: A good place to pause.
- No long dashes or repeated motivational slogans.

## Digital QA

Root full preflight and independent art/print-handoff agents PASS:
- Both PDFs strict-parse48pages; all48pages render in MuPDF and Poppler without warnings.
-621×810pt Media/Crop/Bleed; alternating612×792pt trim,8.5×11in finished format.
- All22 embedded image pixel payloads exactly match intended native tonal derivatives; at least300ppi.
- All protected black/white pixels and geometry retained; both spread LUTs common; lion trial exact.
- KDP zero fonts, metadata, annotations and masks. Canva EB Garamond embedded at16/54/11pt; all live text unchanged.
- All26 non-art pages unchanged. Independent Canva check compared unchanged intro image/font bytes and Poppler renders to avoid a MuPDF extraction side effect.
-19 fully blank pages8,10,...44. No missing artwork or accidental blank art.
- PNG48 exports2588×3375,8-bit L gray,300ppi. All three saved deliverable hashes unchanged after writeback.

Workspace evidence: /workspace/scratch/b288b564abb1/tmp/final-gray15/build.py, final-preflight.json, art-manifest.json, independent-art-qa.json, all20-contact.jpg, intro-ending-contact.jpg. Durable final files above are the handoff of record. Product repository branch feat/optical-animals-book-creator unchanged; large art/PDF assets outside Git.

## Remaining real gates

This is the completed upload-ready INTERIOR. No separate approved full-wrap cover was included or prepared. Actual Canva account import, KDP Print Previewer/account upload, physical paper/ink/gutter proof and publication were not performed. No paid order or release.

Next: use FINAL_GRAY15_KDP directly for the interior upload if no edits; provide/check separate approved cover matched to48pages/paper, inspect KDP preview and physical proof, obtain owner release authorization. Re-preflight any Canva round-trip export. Do not return to old gray typography or publish B/W alternative by mistake.

model_policy_ack: rse-weekly-usage-2026-10-21-v1
recommended_profile: production
runtime_model_observed: UNKNOWN
runtime_reasoning_observed: UNKNOWN
runtime_speed_observed: UNKNOWN
application_status: RECOMMENDATION_ONLY
