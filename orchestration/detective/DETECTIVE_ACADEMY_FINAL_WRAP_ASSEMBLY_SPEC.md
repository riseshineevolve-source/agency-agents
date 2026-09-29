# Detective Academy — Final KDP Wrap Assembly Specification

Status: **CANONICAL ASSEMBLY CONTRACT / OWNER COVER GATE OPEN**
Date: 2026-09-27
Authority: Central RSE Technical Orchestrator
Product: **Happy Makers Detective Academy — The Mystery of Room Zero — Book 1**

This specification exists to stop repeated AI regeneration of the approved front cover and to make the final paperback wrap a deterministic compositing task.

It does **not** authorize publication, English freeze, price changes, or any interior redesign.

## 1. Immutable inputs

### Final front-cover source

Filename:
`OSTATECZNA OKLADKA ROOM ZERO.png`

Exact dimensions:
`1086 × 1448 px`

Exact SHA-256:
`2570df512f3883663aca1c4e5359ba12aa0489276f484b86ac5623ab037429a9`

Rule:
**the approved front is an immutable raster layer.**

Do not:
- regenerate it;
- redraw it;
- face-swap it;
- restyle Bibi or any Happy Maker;
- recolor characters;
- replace the squad;
- change title/subtitle/BOOK 1 typography;
- crop away any existing front-cover content;
- stretch the source non-proportionally.

All future full-wrap work must composite this exact file into the front panel and build only the surrounding bleed/edge extension, spine and back cover.

### Final interior reference

Page count:
**146**

Trim:
**8.5 × 11 in**

Print:
**black ink / white paper**

Final interior candidate SHA-256:
`cb1038dcc9086501b86527227550584da7f38fc051bc70442803f82ebddeab7f`

Local source commit reported for that artifact:
`6579ac896c477461fe1c384993315d7455b3f7c5`

The local commit is not yet durable remotely. The wrap may be prepared from the confirmed 146-page geometry, but final EN freeze still requires remote persistence of the exact source/artifact.

## 2. KDP geometry for the current 146-page artifact

KDP paperback / black ink / white paper spine formula:

`spine = page_count × 0.002252 in`

For 146 pages:

`146 × 0.002252 = 0.328792 in`

Therefore the working wrap geometry is:

- back trim width: **8.5 in**
- spine width: **0.328792 in**
- front trim width: **8.5 in**
- cover bleed: **0.125 in on each outside edge**
- full wrap width: **17.578792 in**
- full wrap height: **11.25 in**

At 300 ppi this is approximately:
- **5274 × 3375 px**

The KDP Cover Calculator/template generated from the exact live book settings remains the final geometric authority. If the downloaded KDP template differs, stop and reconcile instead of forcing this working calculation.

### Horizontal construction coordinates, inches

Using full-wrap origin at the top-left:

- left bleed: `x 0.000000 → 0.125000`
- back trim: `x 0.125000 → 8.625000`
- spine: `x 8.625000 → 8.953792`
- front trim: `x 8.953792 → 17.453792`
- right bleed: `x 17.453792 → 17.578792`

Vertical:
- top bleed: `y 0.000000 → 0.125000`
- trim: `y 0.125000 → 11.125000`
- bottom bleed: `y 11.125000 → 11.250000`

## 3. Exact-front placement without crop or distortion

The approved front source is 1086:1448 = **3:4**.

The KDP trim panel is 8.5:11, which is slightly wider.

To preserve the full approved front with **zero destructive crop**:

1. scale the exact front source proportionally to **11.0 in high**;
2. its proportional width becomes **8.25 in**;
3. center it inside the 8.5 × 11 front trim panel;
4. this leaves **0.125 in** of background extension on each vertical side inside the trim;
5. extend only background/architecture into those narrow side strips;
6. extend background outward into the required front bleed.

Working front-source placement inside the full wrap:

- image left: **x 9.078792 in**
- image right: **x 17.328792 in**
- image top: **y 0.125000 in**
- image bottom: **y 11.125000 in**

The 0.125 in strips immediately left and right of the locked image are **edge-extension zones**, not regeneration zones.

If an editor/outpainting tool is used, the locked front raster must remain a separate top layer and stay pixel-identical after compositing.

Do not scale the source to 8.5 in wide and crop top/bottom. That would violate the owner front lock.

## 4. Spine contract

Use the current approved modern Academy / scanner-question-mark identity.

Spine copy:

**HAPPY MAKERS DETECTIVE ACADEMY**

**THE MYSTERY OF ROOM ZERO**

**BOOK 1**

The 146-page spine is wide enough for text under KDP rules.

Keep spine text and logo within the KDP template spine safe area. KDP requires at least **0.0625 in** clearance between spine text and the spine edges.

Do not use:
- shield;
- torch;
- laurel/wreath crest;
- Victorian detective iconography.

## 5. Back-cover layout contract

The back must stay visually continuous with the approved front:
- midnight / deep navy Academy interior;
- restrained warm-gold architectural lighting;
- black/gold structural elements;
- contemporary detective-academy atmosphere;
- clearly **less festive / less Christmas-like** than rejected drafts.

### Central navy box

Use the successful centered composition, but:

- enlarge the navy copy box so it occupies the back panel confidently;
- keep it optically centered;
- preserve generous margins and breathing room;
- do not distort it into a narrow/tall shape;
- keep body copy readable at print size.

### Gold ALL-CAPS callouts

The emphasized gold capital-letter statements must form **one typography system**.

Use the same:
- font family;
- visual cap height / size;
- weight;
- gold treatment;
- box/border construction;
- vertical padding;
- spacing logic.

The callouts that must be visually normalized include:

- `OR AN INVITATION MEANT FOR YOU?`
- `WILL YOU CLAIM IT?`
- `THE MYSTERY GETS HARDER. SO DO THE CASES.`
- `WHAT IS ROOM ZERO?`
- `YOUR FIRST CASE IS WAITING.`

No one callout should look like it came from a different cover draft.

Hierarchy may be expressed through placement and spacing, not random font-size changes.

## 6. QR tablet + envelope placement

Owner direction:
**tablet with QR and black envelope belong at the very bottom of the back cover, not floating high.**

Placement rules:

- QR tablet remains lower-left;
- black envelope remains lower-center;
- both sit as low as KDP safe margins allow;
- do not move either into bleed;
- do not place either under the barcode area;
- keep both fully visible after trim;
- keep the tablet large enough for a real overlaid QR code to remain scannable.

For outer-edge safety, important content should remain at least **0.25 in** inside the outside trim edge.

The final QR code must be a real exact asset overlaid after visual generation/compositing. Never use an AI-generated QR pattern as the live code.

## 7. Barcode reservation

Preferred production choice:
**use the Amazon/KDP-placed ISBN barcode** rather than baking a custom barcode into the generated artwork.

Reason:
KDP recommends the Amazon-placed barcode because it is guaranteed to satisfy manufacturing requirements.

Reserve the **lower-right back-cover area** for the KDP barcode.

Do not place:
- important copy;
- QR tablet;
- envelope;
- logo;
- evidence objects;
- decorative focal points

inside the barcode reservation shown by the downloaded KDP template.

The KDP template / Previewer barcode zone is authoritative.

## 8. Safe-area and bleed rules

From current KDP paperback guidance:

- cover bleed: **0.125 in**;
- important content: minimum **0.25 in** from the outside cover edge;
- spine text: minimum **0.0625 in** from spine edges;
- final cover should be one continuous wrap;
- fonts must be embedded in the print PDF;
- no surrounding white space or crop marks.

Treat KDP Previewer warnings as blocking until resolved.

## 9. Required production method

The final wrap is a **composite**, not a fresh image generation.

Recommended layer order:

1. KDP template guide layer — non-printing.
2. continuous back/spine/front background extensions.
3. back-cover navy box and exact approved copy.
4. back-cover typography / icons / evidence details.
5. QR tablet body.
6. black envelope.
7. spine branding.
8. **exact locked front raster, unchanged**.
9. exact functional QR overlay.
10. optional production marks only if required by the KDP workflow.

Then:
- hide/remove template guide;
- export print-ready PDF;
- verify exact page geometry;
- launch KDP Previewer;
- inspect barcode placement;
- order representative proof.

## 10. Acceptance checks before owner review

The wrap candidate is not review-ready unless all are true:

- [ ] final canvas = exact current KDP template geometry;
- [ ] canonical front SHA source is used as the locked front layer;
- [ ] no front character, face, title, logo or composition was regenerated;
- [ ] front is not stretched;
- [ ] front source is not destructively cropped;
- [ ] spine is centered to the 146-page template;
- [ ] navy back box is larger and centered;
- [ ] all gold all-caps callouts use one consistent size/style system;
- [ ] back environment is modern and not Christmas-like;
- [ ] QR tablet is at the bottom-left safe area;
- [ ] envelope is at the bottom-center safe area;
- [ ] lower-right barcode reservation is empty;
- [ ] live QR is overlaid as a real asset and test-scanned;
- [ ] all important content remains inside safe areas;
- [ ] bleed reaches every outside edge;
- [ ] KDP Previewer has no unresolved blocking warning.

## 11. Owner gate

A successful compositing/preflight pass still does not authorize publication.

Sequence remains:

**safe remote persistence of final interior → final wrap → KDP Previewer/preflight → representative physical proof → owner proof approval → explicit FREEZE EN → final publication decision**

No Detective PL full-book production begins before explicit **FREEZE EN**.

## References

Current official KDP paperback cover guidance:
- https://kdp.amazon.com/en_US/help/topic/G201857950
- https://kdp.amazon.com/en_US/help/topic/G201953020
- https://kdp.amazon.com/en_US/help/topic/G5HDYGP4BXLX4RUW
- https://kdp.amazon.com/cover-calculator
