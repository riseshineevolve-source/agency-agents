# Exact English candidate: integration supplement, 21 October 2026

This supplement supersedes the *status and integration assumptions* in historical
writer notes. It does not alter their bytes, the manuscript, review receipts, or
source authority. Candidate wording remains KEEP.

## Current authority

- Original illustrated source PDF: `9db84d4f138cbbde8eb1f4a0f783f4d126c639120a11cabb65fc00711b9f05a0`.
- Exact candidate: `9ebae1eabafe2f5ed92c38c2ad7b858a9c85d573b5a7e92c4fb08f1c5810a978`.
- Intake V5: `89b2ec319b5510c664c2932ac6895d185e53fd4b36fc0cf3afa468b79de15003`.
- 3,067 units, 225 source folios, 93 changes on 46 source folios; 2,365 protected
  units unchanged. Four actual stage delta reviews accepted this exact hash; unchanged3065texts retain acceptedV4whole-book baseline evidence. Final deterministic check is PASS with the inherited caption
  OWNER_GATE. Earlier `DIAGNOSTIC_REQUIRED` prose is historical.

Data files and reproducibility scripts are included in `INTEGRATION_EVIDENCE_20261021.zip`. Unzip it into this integration directory.

Use `EDITORIAL_IMPORT_PACKET.json`: every changed ID has original/replacement
bytes and hashes, source folio/bbox, and a defect reason. Every source ID has a
target text hash. The packet is an import contract, not an existing Studio API.
`SOURCE_PAGE_ART_LEDGER.json` inventories all 225 original leaves and image
instances. Reproduce them with the exact builder order and pinned PyMuPDF version: extraction/cache order can change MuPDF pixels without changing source bytes. These fingerprints do not assert all-page semantic visual approval,
rendered candidate fit, independent map uniqueness, or print readiness.

## Actual Studio capabilities and identity

Read-only recovery of the registered Studio item succeeded. Observed archive
SHA256 is `cc6d4381cfa867b28db4dd858a260640b5e8aefbae3c344738daaf9494ae40cb`.
It differs from the historical delivery checkpoint's `820b4430...` archive hash.
Pin the observed archive and per-module hashes in `STUDIO_CAPABILITY_SNAPSHOT.json`;
do not silently claim it is the historical byte-identical ZIP or its test run.
The observed bundle has newer release notes/tests. No full Studio build/test was
claimed in this pass, and no production module was changed.

The inspected `parse_v12` requires the immutable V12 hash
`b39215cb5e26cfb53e624b01fe7e5913654645774fccde8c7ef46b12d5c4001e`.
It cannot directly import the editorial JSON or a modified V12 file. Studio's
page controls adjust type/layout, not copy. Several families import original
PDF bodies or raster artwork unchanged. A successful old-V12 build would
therefore not prove that any new wording was integrated.

Only Book Factory's existing writer can add/consume a versioned source adapter
and issue real per-unit destination receipts. This lane supplies the exact
candidate, evidence, and constraints. No renderer fork is introduced here.

## Source folios are not destination folios

The owner PDF is **before** the newer Studio's physical-layout migration:

| Stable source role | Source folio | Post-migration destination |
| --- | ---: | ---: |
| Case 01 story and Comms | 16 | 15 |
| Case 01 board | 17 | 16 |
| Case 01 map | 18 | 17 |
| Something Is Off transition | 15 | 18 |
| Case 04 story | 27, narrative portion | 26 |
| Case 04 Comms | 27, dialogue portion | 27 |
| Case 30 story and Comms | 137 source story plus canonical dialogue | 137 |
| Case 30 final-check board | 138 | 138 |

These destination hints come from the recovered `spread_layout.py` and
`production.py`, not an illustrated candidate render. Preserve stable source
IDs and resolve actual product slots explicitly. In particular,
`page016.block04` is **Comms**, not witness-board prose. It must not be applied
to destination page 16. Eight changed raster-front units have no native bbox;
all eight need explicit asset/page-family bindings. Never cover an entire
source illustration merely to replace lettering.

## New visual backcheck and documentary corrections

The independent figure reviewer inspected 20 actual original leaves, including
opening pp15–18, Case03 photos, p80, pp122–123, pp130–131, finale pp141–147, and
p158. Original intake folios are correct. Finale speaker mapping, RULE 0 FIRST
repair and rule-recording instruction are supported. No new prose defect was
found within that scope.

**Page 122:** the fourteen-case list is visible inside the raster WITNESS BOARD
on p122 **and** on p123. The previous assertion that the original `this page`
was factually wrong is superseded. The accepted `next page` locator remains
accurate and is retained; classify it as an explicit duplicate-list navigation
choice, not repair of an absent list. Future reviewers must inspect figure
lettering as well as extracted PDF text.

Historical `qa/story-graph.json` and `qa/evidence-payoff-map.json` have
`source_sha256=5fa5a54685165a346f622a1d0518a737602da3e14ba673d5563f1246bfeccc21`.
That is exactly `source/detective-225.txt` (the extraction), **not** the PDF.
Interpret it as `source_text_extraction_sha256`; current PDF/intake bindings
remain as above. Historical diagnostics are retained byte-for-byte.

## Required product return evidence

1. Bind the exact source, candidate, chosen Studio code revision and actual
   output PDF hash. Supply every source ID's final slot, destination folio and
   actual consumed text/hash; preserve verified reader-order attribution.
2. Render the complete illustrated product through its sole writer. Check new
   opening lettering, changed Comms, p80 note, p130 objective and finale fit.
   Reflow split PDF extraction blocks as one semantic passage, without silently
   changing wording. Keep all protected clues, maps, 107 placements and four
   plain-zero records.
3. Compare protected art/geometry and unchanged leaves against the exact chosen
   base, allowing only explicit physical-layout migration. A raw whole-page
   equality test cannot approve a genuinely reflowed page.
4. Resolve the inherited Case03 `ARCHIVED 017 / LATER 071` chronology caption
   before release. Do not invent a photo date or change protected captions here.
5. Preserve separate owner reading, real print proof, artwork-resolution and
   release gates. The existing 225-folio text proof has no original illustrations.

No main merge, freeze, publication, PL R8 translation, or production write is
made by this supplement. Mailbox delivery is durable and does not establish
consumer acknowledgment.

## V5 separator repairs and source geometry closure

CurrentV5 adds only6NUL→ASCIIhyphen substitutions in page207.block05 and
page212.block05. Both are proven visible source glyph defects. Letter orders
A-B-C-D andB-D-A-C unchanged. Import actual V5text; never reintroduce NULs
from canonical V12 or old PDF font mapping. geometry-audit contains two actual
delta reviews and independent Case12/18/21/26/27source checks. CorrectCase13
empty-room auxiliary name is HideRoom; Hinitial unchanged. Source107placements
and allmaps/figures unchanged. Current fullpackage V5supersedes initial archive;
old reports boundec93... are baseline evidence, not new currenthash reviews.
