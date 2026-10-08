# REPORT — RSE Print Finish Gate

Review date: 2026-10-09; commission/reference contract dated 2026-10-08  
Role: independent print-finish reviewer, 05_PRINT_FINISH_REVIEWER  
Scope: reference-led HOUSE H-01–H-10 recovery; 30 proposed treatments

**Disposition: CONCEPT_ONLY · IMAGE_NOT_GENERATED · PRINT_NOT_PROVEN · GOLD_NOT_AWARDED.** The written review is complete. No HOUSE candidate image, original Halloween board pixels, or physical print has been inspected in this task. Three of the 30 proposals are rejected below the required 9/10 optical-impact threshold; the other 27 remain conditional concepts. Neither a score nor a lead selection clears an image, geometry, anatomy, or print HOLD.

## 1. Evidence and authority

Read [ROLE_BRIEF.md](ROLE_BRIEF.md) and the parent [VISUAL_REFERENCE_CONTRACT.md](../VISUAL_REFERENCE_CONTRACT.md), then the canonical [HOUSE MASTER](../../HOUSE/MASTER.md), [HOUSE REVIEW](../../HOUSE/REVIEW.md), and [V01 batch prompts](../../HOUSE/BATCH_01_CREATIVE_GOLD_PROMPTS_V01.md). Reviewed the complete 20-scene causal arc to protect the first ten scenes' later payoffs.

Visually inspected all five explicitly named local Optical Animals PNGs using the image-viewing tool. Read their dimensions and sampled their pixels in memory; references were opened read-only. No other competitor report was consulted. This is one reviewer's assessment, with no invented jury votes or specialist approvals.

The HOUSE, CARNIVAL, and MUSEUM original boards are available here only through the contract's assistant-authored written observations. They are **described references, not inspected pixels**. The unavailable owner attachment pack was not opened. The HOUSE description supports monumental bowed domestic architecture, stair orientations, a black reflective floor, and a small cat; CARNIVAL's theatrical fabric/mask spectacle and MUSEUM's exhibition/vitrine language remain boundary references, not motifs to transplant into HOUSE.

The owner's criticism of previous basic Halloween art is accepted as direction. The inspected predecessor evidence is V01 text, not a local set of generated HOUSE illustrations. Consequently, this report diagnoses what those prompts leave unspecified; it does not claim to have measured or rejected unseen predecessor pixels.

## 2. Actual animal-image findings

### 2.1 Visual observations, transfer, and exclusions

| Inspected file | Actual visual observation | Transfer to HOUSE | Exclude or repair |
| --- | --- | --- | --- |
| 10_lion.png | A near-frontal face remains readable inside large cascading mane ribbons. A foreground paw is enlarged by proximity; the mane's broad curves continue the visual sweep into surrounding vortices. Tail and rear paws occupy quieter areas. White mane lobes are much wider than the small curls at several terminals. Gray modeling, fine fur, whiskers, and dark-to-light ribbon transitions are visible. | Protect a primary shape while thick black curves describe its actual volume; use near/far scale and generous white lobes to make architecture monumental. | No lion pose, mane identity, centered face composition, eye spiral, terminal vortex collection, fur, whisker hairlines, or gray relief shading. Translate ribbon volume into solid black edges and large white planes. |
| 09_peacock.png | A small, clearly readable profile head sits against an enormous sweeping fan. Nested long feather curves produce rising motion at several scales; pointed eye motifs punctuate them. Bird, perch, and fan feel integrated rather than pasted together. Tiny beads and parallel feather striations accompany broad shaded ribbons. | Make the structural environment much larger than its human cue; use directional fan-like expansion only where a real support, rail, or panel gives it a cause. | No feather eyes, bead chains, bird pose, ornamental fan wallpaper, or fine parallel striations. Keep hand/hinge contacts readable without repeated eye emblems. |
| kapibara 2.png | Landscape composition: one large seated animal before a ring of columns and nested arch tunnels. Patterned capybara heads appear repeatedly in circular floor/ceiling fields. A glossy horizontal floor carries architecture-like reflected bands. Central body stripes have broader intervals than many receding tunnel rings; facial fur and glossy floor modeling are tonal. The repeated medallion heads are plainly visible, but their physical nature is not established by this single image. | Borrow architectural scale, floor-plane depth, and continuity between subject volume and surrounding structure. Use a foreground mass against much larger repeating structural bays. | Do not certify the repeated heads as valid mirror counterparts. No duplicated animals, circular animal medallions, generic colonnade, tunnel wallpaper, or transfer of its landscape layout. Compress distant repetition before white gaps become filaments. |
| tucan.png | A very large diagonally projecting bill dominates an oblique bird portrait. The eye and pale cheek remain legible. Broad chest/bill curves meet densely repeated pointed loops around the head; the upper-left spiral and several plume-like fields tighten dramatically. Bill shading and fine feather lines are visible. | Use aggressive foreground foreshortening and a strong diagonal hero, with quiet white anatomy/contact zones beside a bold black volume. | No toucan bill silhouette, feather crown, plume loops, spiral eye field, jewelry-like details, or gray bill shine. One giant physical household element replaces the animal hero. |
| zyrafa 1.png | A full-body giraffe leans its long neck into the upper composition; its recognizable face survives irregular polygonal coat pattern. Several deep patterned tunnels and large surrounding waves contrast with a reflective/rippled floor showing inverted head/leg-like imagery. Broad peripheral whites coexist with thin coat gaps and fine floor ripples. | Contrast a legible primary object with deep structural recession; make contact with a reflective ground visually important. | Do not assert the rippled floor is a geometrically correct single plane mirror. No giraffe pose, polygonal skin network, repeated tunnel mouths, watery mirror distortion, or fine ripples in HOUSE's clean polished foyer. |

The strongest transferable property is **scale hierarchy**, not maximum line count: a few enormous curved black masses, broad white intervals, and smaller secondary rhythm. Adding more swirls would reproduce the references' least printable regions and violate the owner's requested large whites.

### 2.2 Read-only numerical observations

Pixel dimensions and a deterministic 100 × 100 center-of-cell sample grid were obtained from each original PNG with System.Drawing. Each grid contains 10,000 samples. “Intermediate” means RGB was neither exactly (0,0,0) nor exactly (255,255,255); it includes edge antialiasing, near-neutral values, and visible tonal modeling. This is a **sample**, not a full-image histogram or measured final black coverage. All sampled pixels were opaque.

| File | Native pixels W × H | Exact black samples | Exact white samples | Intermediate samples |
| --- | --- | ---: | ---: | ---: |
| 10_lion.png | 1103 × 1426 | 368 / 3.68% | 235 / 2.35% | 9397 / 93.97% |
| 09_peacock.png | 1055 × 1491 | 803 / 8.03% | 139 / 1.39% | 9058 / 90.58% |
| kapibara 2.png | 1536 × 1024 | 667 / 6.67% | 383 / 3.83% | 8950 / 89.50% |
| tucan.png | 1122 × 1402 | 1247 / 12.47% | 467 / 4.67% | 8286 / 82.86% |
| zyrafa 1.png | 1145 × 1374 | 1148 / 11.48% | 688 / 6.88% | 8164 / 81.64% |

Every inspected reference therefore contains sampled values disallowed in the strict HOUSE raster. Its visual authority does not make its pixels a print-finish master.

For band-scale evidence, selected horizontal intervals were scanned at native resolution using luminance Y = 0.2126R + 0.7152G + 0.0722B; Y ≥ 128 was classified white. Coordinates below are zero-based and inclusive. Only complete runs inside each interval are quoted, excluding clipped first/last runs.

| File | Scan y; x interval | Example white runs: pixels / % of full canvas width | Example black runs: pixels / % width |
| --- | --- | --- | --- |
| Lion | y=1254; x=0–418 | 55 / 4.99%; 125 / 11.33% | 73 / 6.62%; 77 / 6.98% |
| Peacock | y=223; x=0–442 | 30 / 2.84%; 105 / 9.95% | 30 / 2.84%; 41 / 3.89% |
| Capybara | y=409; x=0–290 | 11 / 0.72%; 17 / 1.11% | 19 / 1.24%; 26 / 1.69% |
| Toucan | y=1120; x=0–470 | 42 / 3.74%; 50 / 4.46% | 30 / 2.67%; 230 / 20.50% |
| Giraffe | y=302; x=801–1144 | 36 / 3.14%; 79 / 6.90% | 18 / 1.57%; 28 / 2.45% |

These are selected **thresholded horizontal runs**, not perpendicular line thicknesses, minimum widths, closed colorable-region measurements, or a statistically representative distribution. They quantify the visible difference between broad foreground fields and cramped repeated channels. For scale only, 0.72% of an 8.5-inch width is approximately 0.061 inch; 11.33% is approximately 0.963 inch. That normalization is not a proposed resize or crop of the references, whose aspect ratios differ.

## 3. What V01 must change

V01 is already conscientious about incidents, hand custody, mirror accountability, white-zone targets, and exclusions. Its main weakness is **under-specified optical construction**: “form-directed contours” plus an ink percentage can still yield an ordinary key, drawer, umbrella, stove, or piano with decoration around it. It seldom specifies the number, breadth, termination, and load-bearing attachment of the dominant black curves.

The recovery directions below replace that ambiguity with object-specific black architecture: jamb returns, cabinet carcasses, opaque canopy folds, slate laps, iron stove cheeks, piano side cheeks, headboard supports, stair edges, and the rook's carved profile. The visual target is roughly 70% of attention carried by optical geometry embodied in those physical forms. This is an attention/composition guide, not a false measured area fraction.

| Scene | V01 risk | Required recovery change |
| --- | --- | --- |
| H-01 | A key close-up plus a conventional black door | Make the jamb/return a sculptural black-and-white compression field; preserve a genuinely flat mirror and actual insertion. |
| H-02 | A small reflected picture on a featureless floor | Make real lintel/cabinet structure and its accountable inverted image occupy the portrait; enlarge the offered sleeve. |
| H-03 | A neat glove drawer with a minor negative-space trick | Let divider volume and white glove/recess occupancy build the entire image at unusually close scale. |
| H-04 | Familiar eight-spoke umbrella or a black canopy slab | Make opaque panel folds broad, asymmetrical, and dimensional; retain an exposed physical contour that can cast the roof clue. |
| H-05 | Normal roofing with one lifted tile | Make a few large slate laps generate deep rhythmic plane disruption; magnify the rod pinch without adding a roof monster. |
| H-06 | Kitchen still life beside a token glass jug | Use monumental iron enclosure and broad cylinder-bounded handle reversal while keeping the cup emotionally dominant. |
| H-07 | Ordinary piano with a doorway beside it | Show one explicit changed plane adjacency, framed by piano construction, not by flying keys or repeated room folds. |
| H-08 | Generic prepared bed with three little palm badges | Make three attached equal-scale supports dominate real architectural recession; leave the mattress exceptionally open. |
| H-09 | Giant black bar drawn onto a staircase | Build its projected contour from three separated structural edges and retain clear attachment evidence. |
| H-10 | Decorative checkerboard and oversized-looking chess prop | Construct near-rook/far-latch overlap with an ordinary piece, monumental carved profile, sparse cropped board, and reachable attic route. |

## 4. Premium 1-bit finish rules

All dimensions below are **proposed internal design targets at 8.5 × 11 inches**, not vendor specifications, measured HOUSE results, or physical-print guarantees. A 300-pixel-per-inch review raster would be 2550 × 3300 pixels; this report creates no raster or production document.

### 4.1 Pixel and edge discipline

1. Final evaluated pixels must be opaque #000000 or #FFFFFF only. No intermediate gray, colored RGB, translucent edges, graphite, stipple tone, hatching, soft highlights, or photographic texture. A final 1-bit lossless raster carrier must preserve those two values.
2. Establish structure before binary finishing. Blind thresholding or dithering a shaded generation can erase wrists, fill slit clearances, and turn white glass into noise. Rebuild the offending contours and regions; do not call a two-color conversion a quality pass.
3. Perform all scaling before the final two-color check. Later antialiased resizing can reintroduce gray. Crisp binary edges still need adequate native shape resolution; strict binary color does not excuse visibly jagged curves.
4. Model depth with overlap, interrupted edges, varying structural band breadth, white plane interiors, and selected solid-black occlusion masses. Do not imitate gray shading with many closely spaced lines.
5. White canopy fabric is still opaque. White glass is a graphic interior with a bounded optical transformation. Black lacquer uses a coherent reflected shape field, not gray shine streaks. Keep these material meanings distinct.

### 4.2 Width hierarchy and coloring space

| Feature | Proposed printed-width target | At 300 ppi | Reason / stop condition |
| --- | --- | --- | --- |
| Dominant curved black structural bands | Generally 0.12–0.35 inch; selected anchors 0.40–0.70 inch | 36–105 px; anchors 120–210 px | Establish sculptural weight at thumbnail. These are masses, not outline strokes; no constant-width wallpaper. |
| Primary bounded white coloring channels | At least 0.20 inch locally; prefer 0.25–0.50 inch across foreground curves | ≥60 px; preferred 75–150 px | A long white slit is not broad space. Check the narrowest useful section, measured approximately normal to its boundaries. |
| Hero white islands | At least three per image capable of containing a 0.50-inch-diameter circle; aim for several 0.75–1.50-inch fields | ≥150 px diameter | Protect pencil/marker usability inside actual hand, drawer, panel, tile, cup, or mattress forms. A large bounding box alone is insufficient. |
| Important object boundary | Usually 0.025–0.05 inch, adjusted to hierarchy | About 8–15 px after rounding | Protect clarity without turning fingers or glass rims into black tubes. Never promise survival from an unverified numerical minimum. |
| Critical non-coloring evidence gap | Prefer ≥0.08 inch; enlarge toward 0.12–0.20 inch where composition permits | ≥24 px; preferred 36–60 px | For cuff notch, slit clearance, attachment reveal, or rail separation. These can be smaller than coloring channels, but cannot disappear at intended size. |
| Secondary line/detail | Omit if it cannot remain clear without hairline dependence | No universal pass value | Reduce rib/hub minutiae, stitches, tile scoring, glare, board lines, and distant tunnel rings before shrinking the main whites. |

Where an actual object is too small to permit these depicted clue widths, enlarge its foreground projection or change the view. Do not enlarge the real lock, hand, or chess piece arbitrarily to satisfy the page. Rendering scale and real object scale must remain distinguishable.

Use about 40–55% black as the contract's flexible guide. Measure it later over the entire image, counting reflected white shapes correctly; no invented “50%” claim from visual impression. A page can miss the guide yet be superior after review, or fall inside it and still fail through local black congestion. No percentage overrides coherent anatomy, spacious whites, or the hero.

### 4.3 Three decisive viewing checks

- **Thumbnail:** at approximately 2 inches high, the page must immediately show an optical event, a legible hero, and a distinctive silhouette. Ordinary furniture with a patterned border fails. Black bands must still read as structure when minor details disappear.
- **Intended size:** at 8.5 × 11 inches, inspect local white-channel bottlenecks, closed versus escaping coloring contours, wrist/hinge/contact readability, and source-to-reflection registration. Optical depth must remain understandable without tiny labels.
- **Physical sheet, later:** inspect actual edge fill-in, white-gap survival, large black-field behavior, and pencil/marker use on intended material. Paper, reproduction, and marker behavior remain untested here; P-03 cannot be cleared in Markdown.

Optical impact below 9/10 is rejected regardless of weighted total. A route at or above 9 still stops on false optics, impossible anatomy, lost narrative causality, unusable whites, or nonbinary pixels.

## 5. Thirty candidate treatments

All route ink percentages and widths are future targets. The A/B/C identifiers below are **new recovery proposals**, not the predecessor's identically lettered alternatives. Each set changes camera position, silhouette, and structural band organization while retaining its scene's primary optical family. Alternatives must never be combined into one overloaded generation.

The source authorizes H-01's observation-dependent actual slit and H-07's single impossible adjacency. Other scenes here use ordinary optics/geometry; do not introduce fresh magic merely to intensify them. The smooth key never gains teeth, the floor is never a portal, and the water jug never alters a real handle.

### H-01 — The Key Without Teeth

**Incident lock:** one smooth key approaches the real latch under reflected observation; the door releases afterward. Keep the notched left cuff visible. Any chosen opening camera must be available for the intentional H-20 threshold bookend.

#### H-01-A — Jamb under compression — LEAD

**Camera and black architecture:** shoulder-height oblique view close to Mara's observing eye, with an enlarged foreground hand. Three thick curved jamb returns bow toward the real latch like nested compression ribs; each is attached to the same door surround. Their black widths grow toward the lens, while the door leaf remains ordinary and hinged. A straight rectangular plane mirror occupies the inward return, with its yaw chosen to show the same blade/latch contact visible outside it.

**White plan:** 46% black target. Reserve three 0.65–1.1-inch jamb fields, broad hand interior, and a ≥0.50-inch key-bow opening. White spaces between ribs stay ≥0.25 inch; depict essential insertion clearance at ≥0.08 inch through camera magnification.

**Optical payoff and veto:** the doorway seems compressed around an impossibly smooth key; close view proves the unchanged blade and real slit. HOLD O-01/O-07/P-01/P-02. Reject a mirror curved with its frame, ribs blocking Mara's reflected sightline, or broad stripes crossing her digits and hiding the grip.

#### H-01-B — Blade across a threshold canyon — RESERVE

**Camera and black architecture:** more lateral, near-hand shoulder view along the blade, retaining actual threshold depth and a sliver of the bell tray. The thick door edge and one returning jamb create two counter-sweeping black volumes rather than A's nested ribs. The existing inward-jamb plane mirror is shown as a broad angled facet, not a shiny hairline. Its virtual contact repeats the real contact without making the key look physically longer.

**White plan:** 49% black target. Keep a 1.0–1.4-inch doorway wedge, 0.70-inch hand field, and ≥0.50-inch bow interior. Principal white canyon intervals stay ≥0.30 inch; leave the cuff notch and latch body separate.

**Optical payoff and veto:** powerful near/far scale makes ordinary hardware feel architectural; the mirror exposes its cause. O-01 is harder than A because the blade can obscure the latch. Reject if either actual contact or reflected contact vanishes, if the observing eye cannot reach the mirror view, or if macro cropping loses the front-door place required for H-20.

#### H-01-C — Lintel fan over the lock — REJECT

**Camera and black architecture:** high shoulder position, looking obliquely down while retaining an upward-spreading crop of three broad curved lintel supports. The dominant black gesture opens toward the top; the straight mirror, key, and actual slit form a lower triangular cluster. All lintel supports are ordinary construction; no stair bridge or second fold is introduced.

**White plan:** 44% black target. Three 0.8–1.3-inch lintel/jamb regions and 0.30-inch channels offer ample coloring; preserve the hand and bow. Keep the working contact enlarged, with ≥0.08-inch depicted clearance.

**Optical payoff and veto:** architecture is bolder than V01, but its fan overpowers the observation-dependent contact. Optical estimate 8.8/10: reject despite good whites. To reconsider, lower the fan's prominence and rebuild the hand/mirror encounter; changing the story to a shadow-operated lock is prohibited. No score adjustment without a fresh composition.

### H-02 — A Minute Underfoot

**Incident lock:** actual lintel woodwork depicts the notched-cuff offer, one carved cup, and one empty carved chair. Its floor image is Mara's apparently backwards promise, not a different action. Clock remains stopped at 11:59; the cabinet cue leads to H-03. The real adult cat is small beside the cabinet.

#### H-02-A — Inverted lintel ravine — RESERVE

**Camera and black architecture:** heel-height view along a continuous horizontal black floor. The actual shallow relief is built into a wide lintel with three bowed structural shoulders. Its broad white sleeve and surrounding real lintel planes reappear below the floor in a single accountable reflection; virtual imagery and floor perspective make a deep inverted ravine. This is apparent depth, not an opening in the floor.

**White plan:** 51% black target. Reflected sleeve ≥0.75 inch locally, two 0.8-inch cabinet fronts, and a 1.0-inch door plane. Keep broad reflected bands ≥0.25 inch; omit distant repeats. Do not carve decorative white outlines around every cat limb.

**Optical payoff and veto:** the floor appears to hold the towering inverted house. O-01 must prove relief/floor/camera ray access, including unblocked actual source. Reject a floating inverted relief, reflected architecture not present above, or cat legs merged into the floor without readable ordinary contact.

#### H-02-B — Reflection across the portrait — LEAD

**Camera and black architecture:** heel-height lateral eye point, with a modest camera roll so the horizontal floor's projected seam cuts diagonally across the page. Roll changes the framing, not gravity. The cabinet's two broad curved side cheeks and the lintel shoulder generate opposing sweeps; their correct floor counterparts make the lower field feel as large as the real room. The reflected offering occupies the central diagonal instead of a small inset.

**White plan:** 50% black target. A 1.1-inch reflected sleeve field, two ≥0.75-inch cabinet interiors, and a broad doorway wedge. Use 0.30–0.45-inch main reflected intervals; keep the cuff/handle discontinuity ≥0.10 inch.

**Optical payoff and veto:** strong tilted framing makes the floor image climb the page while source and receiver remain one ordinary room. Cat stays beside the real cabinet, with its reflected contact rooted under its paws. Reject a tilted physical floor, wavy watery reflection, second light illusion, or clock/cat competing with the offer.

#### H-02-C — Cabinet shelf over black depth — RESERVE

**Camera and black architecture:** crouched view from nearer the cabinet, looking lengthwise along its projecting lower shelf. One thick bowed cabinet carcass sweeps across the near edge; the actual relief remains visible across the foyer. The clean floor image occupies the opening beneath that sweep. Unlike A's distant lintel ravine or B's diagonal field, this uses a single near structural overhang against deep reflected white woodwork.

**White plan:** 48% black target. Cabinet front ≥1.2 inches, reflected sleeve ≥0.65 inch, doorway ≥0.8 inch; channels ≥0.25 inch. Keep a broad uninterrupted reflective footprint below the relief.

**Optical payoff and veto:** an ordinary shelf seems to suspend a second house beneath it. Its real overhang must not occlude the very rays needed for the relief reflection. Reject if the reflected source could only be seen through opaque cabinet wood, if the cat becomes a giant foreground portrait, or if the mirror floor becomes a standalone decorative picture.

### H-03 — The Hand Kept Empty

**Incident lock:** Mara's bare right hand lifts one wearable left glove from a supported shallow drawer. A real empty hand-shaped receiving recess in the black divider supplies figure-ground reversal. The umbrella ferrule remains a quiet route cue; cup and cat are absent.

#### H-03-A — Drawer as a carved receiving canyon — LEAD

**Camera and black architecture:** steep downward diagonal from just over the near drawer corner. Three thick bowed divider faces flow toward the glove/recess encounter, attached to a common shallow carcass with visible runners. Their large black shoulders frame five broad white glove fingers and a connected negative receiving form. The geometric rhythm comes from actual divider depth; it does not add extra fingers.

**White plan:** 43% black target. Shelf fields 0.9–1.4 inches, glove palm ≥0.65 inch, primary finger interiors/channels ≥0.20 inch. The receiving recess keeps a ≥0.30-inch open neck.

**Optical payoff and veto:** black occupancy first closes around a hand, then white occupancy resolves as a vacant receiver beside a usable glove. Reject deep drawer tunnels inconsistent with its shallow depth, six-finger negative shapes, stitched microtexture, or a right glove masquerading as a left glove. O-07 and runner support remain open.

#### H-03-B — Across the lifted cuff — RESERVE

**Camera and black architecture:** shallow downward view just above the near drawer lip, looking along its diagonal. The glove's cuff rises into the foreground right-hand pinch; its empty finger shapes recede toward the shelf. One massive curved divider cheek occupies the opposite side, allowing the white recess to read against a different depth plane without becoming a shadow or reflection.

**White plan:** 45% black target. Near cuff interior ≥0.65 inch, two shelf planes ≥0.80 inch, receiving field ≥0.60 inch; finger channels ≥0.20 inch. Limit internal seams to a few necessary closed contour changes.

**Optical payoff and veto:** a near hollow cuff changes the scale of the ordinary drawer and makes absence dimensional. The lower camera makes finger occlusion harder: distinguish Mara's living right fingers from empty glove fingers. Reject if gravity makes the supple glove float horizontally, if the recess appears painted rather than cut into construction, or if optical force depends on a lacework slit.

#### H-03-C — Quarter-turn white palm field — RESERVE

**Camera and black architecture:** almost top-down, with the ordinary drawer diagonal rotated in framing. A broad S-shaped divider separates the left glove from its white receiving recess; two smaller attached divider returns set an off-center counter-rhythm. The drawer depth edge and runner attachment remain visible along one side. No kaleidoscope, multiple drawer, or mirror is added.

**White plan:** 41% black target. Large glove/recess palm fields ≥0.75 inch, shelf ≥1.2 inches, divider-to-finger intervals ≥0.25 inch. Preserve the cuff opening rather than filling it with linework.

**Optical payoff and veto:** the page alternates between one black enclosing contour and two plainly domestic white receiving spaces. Print geometry is strong; optical depth is less forceful than A. Reject a detached anatomical hand, a palm emblem centered like a logo, or bands that turn the cabinet into generic Op Art wallpaper. The ferrule must remain physically in the lower compartment.

### H-04 — The Umbrella That Holds the Storm

**Incident lock:** gloved left hand raises a damaged eight-rib umbrella; one exposed bent rib tip and actual opaque hem contour project the roof/slate clue from the single fixed left lamp onto the right plaster receiver. Service stair remains real. White panels are opaque fabric.

#### H-04-A — Broken hem, giant sail — RESERVE

**Camera and black architecture:** beneath the canopy but displaced sharply from the hub, looking across four foreground panel interiors toward the full supported eight-rib assembly. Thick black bands follow real rib sleeves and broad tension folds; white fabric lobes widen toward the lens. The displaced hem and exposed damaged tip occupy the far edge with their corresponding angular roof-profile projection beyond.

**White plan:** 52% black target. At least three panel fields ≥0.75 inch and a ≥1.0-inch plaster field; panel necks ≥0.25 inch. Keep hub/shaft separate with ≥0.10-inch visible interval where needed.

**Optical payoff and veto:** near curved fabric mass turns an ordinary umbrella into a huge domestic storm relic; a harder projected roofline gives the second reading. Reject carnival-tent stripes, hidden ribs projected through cloth, a black canopy slab, or unrelated shadows. O-08 needs source/edge/receiver construction, not merely a convincing silhouette.

#### H-04-B — Off-center hub bowl — LEAD

**Camera and black architecture:** low near the shaft, looking diagonally across the canopy's inner bowl with the hub well off-center. Broad S-shaped fold boundaries remain anchored between adjacent real ribs; they are tension folds within opaque panels, not extra spiral spokes. Near panels loom, far panels compress, and the actual hem points toward the interrupted roof shadow on the right return.

**White plan:** 50% black target. Three 0.9–1.3-inch panel islands, wall ≥1.0 inch, gloved palm ≥0.55 inch; primary white intervals ≥0.30 inch. Simplify struts around the hub before narrowing these spaces.

**Optical payoff and veto:** asymmetric concavity produces a powerful bowl-like depth without a circular mandala. The shaft grip and all eight rib connections must remain plausible; the receiver must show the actionable roof interruption, not a decorative swirl. Reject an impossible exposed tip, several light sources, extra floating struts, or a glove whose dark joins erase thumb opposition.

#### H-04-C — Canopy edge against a wall cliff — RESERVE

**Camera and black architecture:** lateral underside view nearer the open service-stair side. The canopy occupies one large oblique crescent, leaving nearly half the page to a plain receiver with the actual roof-profile shadow. Thick rib sleeves and two broad folded panel faces create depth inside the crescent. The shadow remains tied to the exposed hem and tip; no artificial cutaway makes cloth transparent.

**White plan:** 48% black target. Two large panels ≥0.8 inch, third ≥0.55 inch, wall ≥1.5 inches; channels ≥0.25 inch. Enlarge the projected lifted-slate interruption toward ≥0.20 inch.

**Optical payoff and veto:** source and shadow oppose curved depth and angular architecture. Its clearer projection may be safer than A/B, but avoid flattening everything into two logos. Reject if the silhouette demands a concealed rib to transmit through opaque fabric, if the damaged tip becomes a bat wing, or if the service stair is swallowed by the wall shadow.

### H-05 — The Roof's Unfinished Tooth

**Incident lock:** inspection from a supported hatch; one raised original slate pinches the bent weather terminal. The continuous sleeve/vent motivates H-06. Repair access is unavailable and no second active seam, roof-balancing person, or cat is shown. Reserve gutter-height repair framing for H-18.

#### H-05-A — Broad slate laps in a diagonal current — LEAD

**Camera and black architecture:** steep downward crop from the hatch over three broad courses. A few physically curved-cut slate edges form bowed lap contours on one coherent roof pitch; exposed dark underlaps make structural bands, not painted coat stripes. One raised black slate interrupts that flow with a large white wedge and a magnified rod contact.

**White plan:** 48% black target. Three tile-face fields 0.8–1.3 inches, hatch ≥0.9 inch, principal intervals ≥0.25 inch. Pinch evidence is enlarged enough to distinguish the terminal from support; no fake clearance is inserted where it is trapped.

**Optical payoff and veto:** the repeating structural current abruptly opens into the “unfinished tooth,” with no literal mouth. Reject too many little scales, laps facing uphill, slate edges bending independently of their pieces, or a rod drawn through stone. O-06/C-05 stay open on the inspection/repair distinction.

#### H-05-B — Roof zipper through the hatch — RESERVE

**Camera and black architecture:** more overhead from the supported hatch, modestly rolled so the actual pitched course runs diagonally. Three large staggered lap intervals form a stepped black zipper; broad slate faces remain planar and attached. The lifted tile breaks one tooth of this geometric rhythm while the sleeve and vent continue along the real roof edge.

**White plan:** 47% black target. Hatch opening ≥1.1 inches, three slate interiors ≥0.75 inch, sleeve/vent interval ≥0.25 inch. A supported left glove rests on the hatch rim, with no attempted repair reach.

**Optical payoff and veto:** a normally repetitive roof behaves as a monumental interlocking mechanism. It is distinct from A's flowing bows and H-18's later under-tile view. Reject an actual zipper prop, chevrons pasted onto unrelated surfaces, a giant staircase implied by mis-scaled tile thickness, or an extra fold demonstrating the inaccessible platform.

#### H-05-C — Vent wedge at the vanishing edge — REJECT

**Camera and black architecture:** steep oblique inspection along the roof pitch toward a broad vent cheek, using a few large bowed lap contours that converge behind the lifted tile. The raised edge and rod remain foreground evidence; the vent becomes a white vertical wedge against the roof's black sheet.

**White plan:** 46% black target. Vent ≥1.3 inches, slate interiors ≥0.8 inch, hatch ≥0.65 inch; main intervals ≥0.25 inch. No miniature distant tiling.

**Optical payoff and veto:** usable and more dimensional than V01, but the optical event remains ordinary recession dominated by a vent. Optical estimate 8.7/10: reject. More tiles or narrower rings would intensify noise rather than the incident. Reconsider only after making the single disruption reshape the dominant silhouette; preserve the H-18 repair camera and original trapped-terminal condition.

### H-06 — The Cold Cup

**Incident lock:** bare right hand begins lifting the one actual cup from the cold warming niche. A distant asymmetric pan handle is laterally inverted only through a real cylindrical water jug; unobstructed continuation and pan attachment remain normal. The actual service opening and vacant piano cradle provide the walking destination.

#### H-06-A — Iron collar, reversed handle — LEAD

**Camera and black architecture:** counter-height lateral close view. Two thick bowed cast-iron stove cheeks create a collar around the white cup and niche; real cast ribs terminate at their support plates rather than spreading over walls. A large upright cylinder sits to the side, cutting the thick asymmetric pan-handle contour into a bounded transmitted reversal. Cup retains the strongest local contrast.

**White plan:** 50% black target. Cup bowl ≥0.9 inch, jug interior ≥0.8 inch, counter ≥1.0 inch, handle aperture ≥0.25 inch. Main clear regions ≥0.30 inch; direct/transmitted handle branches must stay separately legible.

**Optical payoff and veto:** immense iron mass frames a quiet offer while the optical cylinder contradicts an ordinary object's apparent direction. HOLD O-04: water cross-section, object separation, and eye point must actually support inversion. Reject a jug-painted pattern, a reversed whole cup, dark glass hiding the handle, or stove curves forming a demon face.

#### H-06-B — Cylinder as a side-cut optical window — RESERVE

**Camera and black architecture:** slightly elevated lateral view from the opposite counter corner, sufficiently close to lateral for the cylinder's transmitted behavior to remain the same proposed mechanism. Three broad real stove casing returns sweep diagonally behind the cup. The jug's vertical axis is unambiguous; its side boundary visibly interrupts the handle, with the pan and both ordinary outside continuations available.

**White plan:** 49% black target. Cup ≥0.8 inch, two counter/niche fields ≥0.9 inch, jug ≥0.75 inch; white channels ≥0.25 inch. Give the cylinder boundary a firm contour, not a double gray glare.

**Optical payoff and veto:** the handle appears to travel against the enclosing iron current. This camera requires a fresh ray construction; a view that works for A cannot simply be rotated into B. Reject if the transmitted asymmetry is too small to read, if the jug eclipses the cup emotionally, or if the handle becomes a giant route arrow through the service opening.

#### H-06-C — Jug edge close, cup beyond — RESERVE

**Camera and black architecture:** low counter-level eye near one cylinder edge, looking past the jug toward the white cup in its niche. A single massive curved stove cheek fills one side; broad counter and niche planes fill the other. Only part of the asymmetric handle passes through the cylinder footprint, giving a sharp bounded optical cut rather than a second whole scene inside glass.

**White plan:** 48% black target. Cup ≥0.85 inch, niche plane ≥1.1 inches, jug field ≥0.65 inch; channels ≥0.25 inch. The transmitted segment must be thicker than fine glass scratches and stay distinguishable from the rim.

**Optical payoff and veto:** extreme near-glass/far-cup depth is original, but off-axis cylinder optics are the hardest of these routes. Coherence estimate is deliberately lower. Reject if a feasible layout cannot produce the specified lateral reversal or if the jug becomes the hero; do not replace the causal lesson with a prettier ordinary glass still life.

### H-07 — The Piano Opens a Corner

**Incident lock:** cup sits stably in its horizontal cradle at the retained-open instant. Its load released the fallboard; detent and stop retain it. Exactly one hinge continuation changes wall adjacency to the bedroom. Retrieval happens afterward. Keys retain ordinary two-and-three accidental groups.

#### H-07-A — Fallboard cliff over white keys — RESERVE

**Camera and black architecture:** beneath keyboard level, sharply upward from one end. Large curved piano side cheeks and their real supporting rails carry broad black sweeps; the fallboard remains one rigid ordinary plane. Enlarged white key tops provide a short grounded foreground rhythm. At the far end of the hinge, one wall continuation meets the wrong adjacency and exposes the normal bedroom frame.

**White plan:** 52% black target. Fallboard face ≥1.1 inches, door ≥0.9 inch, three key-top fields ≥0.5 inch; channels ≥0.25 inch. Keep cradle and stop readable instead of filling the underside with struts.

**Optical payoff and veto:** huge mass seems to open a corner of the house, while one sharply located seam explains it. Reject an all-black underside, curved/flying key staircase, floating board, or a second impossible doorway corner. O-03/O-06 remain open; gravity still governs the instrument.

#### H-07-B — End-cheek canyon at the hinge — RESERVE

**Camera and black architecture:** service-end view obliquely along the real hinge axis, near the cup cradle rather than below the keyboard's middle. Two broad attached side-cheek curves enclose a white canyon; they terminate at ordinary hinge/support joints. The singular changed wall adjacency lies beyond the near hinge barrel, with two plane continuations exposed instead of hidden behind a decorative ribbon.

**White plan:** 51% black target. Side-cheek/case field ≥0.85 inch, fallboard ≥0.9 inch, doorway ≥0.8 inch; channels ≥0.30 inch. Cup bowl ≥0.55 inch, with visible base contact.

**Optical payoff and veto:** a service mechanism gains gallery scale while revealing one impossible architectural connection. The hinge axis must not be confused with the wrong-side seam. Reject if the cup seems suspended, if the mechanical catch is buried in black, or if the room appears inside hollow piano wood rather than newly adjacent at the hinge continuation.

#### H-07-C — White fallboard, wrong corner — LEAD

**Camera and black architecture:** high service-side oblique view looking down across the raised fallboard and into the one changed corner. This breaks V01's low-camera sequence. The rigid board forms a huge white diagonal leaf between a black curved side cheek and a black keyboard/case mass; no multiple origami folds. Enough hinge length, barrel, retained stop, and ordinary doorframe remain visible to locate the single fantasy seam.

**White plan:** 49% black target. Fallboard ≥1.4 inches locally, doorway ≥1.0 inch, cup/case field ≥0.65 inch; primary intervals ≥0.30 inch. Crop the keyboard to a short coherent grouped run.

**Optical payoff and veto:** a broad ordinary plane seems to redirect a room at one specific corner. Reject if the elevated view hides that adjacency, if it becomes abstract origami, or if the fallboard intersects keys during its supposed retained opening. This new camera requires later continuity review; it is a proposal, not a silent change to MASTER.

### H-08 — The Bed Prepared for Nobody

**Incident lock:** exactly three real attached headboard supports of equal underlying scale show successive incomplete carved cup offers, each stopping one span short. Normal perspective reduces apparent size. Mara carries one physical cup; carved cup profiles are woodwork. Small adult cat rests on the floor at bed foot. The real stair opening leads to H-09; recognition of hospitality remains incomplete.

#### H-08-A — Three bowed receivers above an empty plane — LEAD

**Camera and black architecture:** elevated bed-foot quarter view, looking diagonally down across the broad white mattress toward three receding bays. Each attached support has a thick curved shoulder and an incomplete open terminal; their equal real size is clear from common headboard rails. This high camera replaces the predecessor's low viewpoint and makes empty white bed space as important as the ominous woodwork.

**White plan:** 44% black target. Mattress field ≥1.5 inches, pillow ≥0.9 inch, three bay fields ≥0.6 inch; terminal intervals ≥0.25 inch. Keep floor/cat contact separate from the bed rail.

**Optical payoff and veto:** three huge arrested approaches recede toward a normal stair opening while nobody occupies the bed. Reject body-shaped bedding, reliefs changing real scale to create false depth, detached hands, or a final completed offer. This resolves camera rhythm conceptually but does not clear C-02 without actual image comparison.

#### H-08-B — Side rail through three unfinished bays — RESERVE

**Camera and black architecture:** lateral view from bed-side seated height. One thick curved bed rail sweeps across the lower page and ends at real posts; above it, the three equal-size attached supports recede sharply across the headboard. Large white bay intervals, rather than spirals, create optical pulse. The mattress remains an ordinary unoccupied plane.

**White plan:** 43% black target. Mattress ≥1.3 inches, two bay interiors ≥0.8 inch, third ≥0.55 inch, pillow ≥0.75 inch; channels ≥0.25 inch. Retain enough bed length to prove adult scale.

**Optical payoff and veto:** a near sculptural rail makes the repeated stalled supports feel architectural without becoming a tunnel. Reject rail curves that detach from posts, a fourth support, a cup carried in the wrong hand, a cat placed on the mattress, or woodwork whose cup contours look like three extra physical cups.

#### H-08-C — Nested receiver frames — REJECT

**Camera and black architecture:** high room-corner view toward the three headboard bays. Thick curved supports overlap in projection as three enclosing frames, all still attached and equal-scale. One large white mattress wedge points toward the real stair opening, while the black bed perimeter counters it.

**White plan:** 42% black target. Mattress ≥1.5 inches, bay fields ≥0.65 inch, pillow ≥0.8 inch; primary channels ≥0.25 inch. Preserve floor space for a small naturally resting cat.

**Optical payoff and veto:** the route offers clean whites but looks too much like a familiar nested arch template; the offering incident risks becoming repeated badge decoration. Optical estimate 8.8/10: reject. More rings will not repair it. Reconsider through a new load-bearing support profile and view that makes the interrupted approach specific, without phantom bodies or a premature welcoming interpretation.

### H-09 — The Stair That Looks Locked

**Incident lock:** camera is one feasible crouched eye point over the real third tread. A foreground riser edge, middle landing edge, and upper balustrade edge join in projection into a false latch. They are physically separate. A later sideways lean breaks alignment and exposes the ordinary chess nook; depict only the alarming aligned instant.

#### H-09-A — Black latch across a white stair gorge — RESERVE

**Camera and black architecture:** centered low third-tread view looking upward. Three stout physical edges carry distinct broad curved contours, calibrated to join as one diagonal latch silhouette. Tread, landing, and rail attachments sit adjacent to the joined contour, providing close-view depth evidence without cutting the illusion into disconnected bits.

**White plan:** 49% black target. Wall ≥1.1 inches, tread fields ≥0.6 inch, nook opening ≥0.75 inch; channels ≥0.25 inch. Adjacent depth/contact evidence ≥0.10 inch where required.

**Optical payoff and veto:** the projected latch is frightening at thumbnail and dismantled by ordinary supports on close inspection. Do not draw a physically continuous bar. Reject stairs with inconsistent headroom, an ungrounded boot, a second impossible fold, or tiny gaps as the only proof of separate depths. O-09 requires construction from one eye point.

#### H-09-B — Latch canyon from the inside turn — LEAD

**Camera and black architecture:** crouched third-tread eye shifted toward the inside rail, with all three contour pieces recalibrated for that actual eye point. A near curving rail return looms overhead; the middle landing lip sweeps beneath it; the distant riser/edge contribution completes the same entrance-latch reading. One tall white wall blade separates their visible support zones. No camera position requires occupying a solid post.

**White plan:** 50% black target. Wall blade ≥1.0 inch, three tread/landing fields ≥0.6 inch, nook ≥0.8 inch; white channels ≥0.30 inch.

**Optical payoff and veto:** near structural foreshortening produces stronger depth than A without endless stairs. A slight sideways eye move must actually split the silhouette. Reject if any piece is moved into an impossible support position just to close the projected contour, if the apparent latch covers the reachable nook completely, or if a cast shadow performs the alignment.

#### H-09-C — Balustrade fork over the third tread — RESERVE

**Camera and black architecture:** feasible crouched eye at the outer side of the same third tread, looking upward through a wide interval between two real posts. Broad fork-like rail returns frame the near riser/landing/upper edge alignment; only those three separated edges create the false latch. The fork is ordinary support framing, not another illusion or a fourth latch component.

**White plan:** 47% black target. Post interval ≥0.75 inch, wall ≥1.2 inches, landing/treads ≥0.65 inch; channels ≥0.25 inch. Keep the boot and real supporting tread in view.

**Optical payoff and veto:** an enclosed near view opens into deep ordinary space behind the apparent obstruction. The nook must remain partly visible without a tiny pinhole. Reject if the camera sits beyond the usable tread, if balusters multiply into fine tracery, or if the fork becomes an unrelated hand motif. O-09 and real stair dimensions remain unresolved.

### H-10 — A Rook Larger Than the Door

**Incident lock:** one ordinary near rook occludes the actual far service-door latch. Gloved left hand is poised to slide it one square; bare right hand carries the single cup outside the crop. Board remains eight-by-eight, pieces sparse. The move later exposes reachable attic stairs and rod sleeve for H-11. No game solution is required.

#### H-10-A — Carved tower at board level — RESERVE

**Camera and black architecture:** just above the board, near an actual rook with broad turned shoulders and a few sturdy crown openings. Its real curved profile forms monumental black stacked masses without spiral engraving. Far latch overlap gives the false tower scale; large cropped white squares recede toward an adult-scale door.

**White plan:** 47% black target. Three board-square fields ≥0.75 inch, door ≥1.1 inches, rook crown openings ≥0.25 inch with adequate surrounding material. Keep base contact and left-hand grip visible.

**Optical payoff and veto:** proximity makes a small household occluder look like a lock architecture. Reject a literal giant rook, stretched carving, crown cutouts reduced to tiny crenels, or board perspective incompatible with the piece base. Do not invent a second rook as a moved copy.

#### H-10-B — White square wings around the rook — RESERVE

**Camera and black architecture:** tabletop eye near the board's front corner, looking diagonally between a near rook and one quiet distant piece. Two giant projected white squares open as wings around the rook's thick black stem; near turned shoulder and distant latch are specifically overlapped from this new eye point. Square edges remain straight on the ordinary plane.

**White plan:** 46% black target. Two near squares ≥1.1 inches, third ≥0.65 inch, door ≥0.9 inch; essential white intervals ≥0.25 inch. Glove separates from the rook through a broad genuine hand/background interval.

**Optical payoff and veto:** white board geometry amplifies false scale without decorative checker walls. Reject physically warped squares, insufficient eight-by-eight evidence, the far piece turning into a second hero, or an attic opening shrunk to match the rook. The intended move must unblock the same real latch/route rather than create a portal.

#### H-10-C — Rook crown across a tilted door canyon — LEAD

**Camera and black architecture:** very low board-level eye obliquely past the rook shoulder, with modest camera roll. The ordinary grounded rook appears to lean across the portrait only through framing; broad lathe curves and crown cutouts remain plausible solid carving. Its projected tower overlaps the far latch at a steep diagonal, leaving a wide real door plane and partial attic gap beside it.

**White plan:** 45% black target. Door field ≥1.2 inches, two foreground squares ≥0.9 inch, third ≥0.55 inch; crown/hand intervals ≥0.25 inch. Retain a readable rook base and its actual square.

**Optical payoff and veto:** tilted framing makes the near tower/far door relation cinematic while full-size contact restores ordinary scale. Reject a tilted physical board, unsupported rook, wrong-thumb glove, concealed base, or tiny distant sleeve serving as the only route clue. O-09 must show that moving the real piece one square exposes the normal passage.

## 6. Route scores and dispositions

These are **single-reviewer subjective concept forecasts**, assigned to the written compositions using the inspected references. They are not measurements of generated images or factual certification. Originality is an editorial estimate, not an exhaustive image-search result. The coherence score reflects construction plausibility and remaining risk; it does not clear optics or anatomy. Narrative scores assess preservation of the canonical written incident.

O = optical impact (30%); G = gallery originality (25%); W = usable coloring whites (20%); C = factual optical/anatomical coherence (15%); N = narrative continuity (10%).  
Weighted total = 0.30O + 0.25G + 0.20W + 0.15C + 0.10N. Values are on a 0–10 scale. LEAD means preferred concept within a scene; RESERVE means alternative concept. Neither is an image approval. Any O < 9 is REJECT even if its weighted total exceeds 9.

| Route | O | G | W | C | N | Weighted / 10 | Disposition |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| H-01-A | 9.5 | 9.3 | 9.2 | 8.8 | 10.0 | 9.335 | LEAD |
| H-01-B | 9.4 | 9.5 | 8.8 | 8.4 | 10.0 | 9.215 | RESERVE |
| H-01-C | 8.8 | 9.0 | 9.3 | 8.5 | 10.0 | 9.025 | REJECT |
| H-02-A | 9.4 | 9.1 | 9.0 | 8.5 | 10.0 | 9.170 | RESERVE |
| H-02-B | 9.6 | 9.4 | 9.0 | 8.7 | 10.0 | 9.335 | LEAD |
| H-02-C | 9.1 | 9.2 | 9.4 | 8.4 | 10.0 | 9.170 | RESERVE |
| H-03-A | 9.4 | 9.4 | 9.5 | 9.1 | 10.0 | 9.435 | LEAD |
| H-03-B | 9.2 | 9.2 | 9.1 | 8.8 | 10.0 | 9.200 | RESERVE |
| H-03-C | 9.1 | 9.3 | 9.5 | 9.0 | 10.0 | 9.305 | RESERVE |
| H-04-A | 9.4 | 9.2 | 9.1 | 8.2 | 10.0 | 9.170 | RESERVE |
| H-04-B | 9.6 | 9.5 | 9.2 | 8.4 | 10.0 | 9.355 | LEAD |
| H-04-C | 9.1 | 9.3 | 9.4 | 8.5 | 10.0 | 9.210 | RESERVE |
| H-05-A | 9.3 | 9.4 | 9.5 | 8.8 | 10.0 | 9.360 | LEAD |
| H-05-B | 9.2 | 9.2 | 9.4 | 8.9 | 10.0 | 9.275 | RESERVE |
| H-05-C | 8.7 | 8.9 | 9.5 | 8.5 | 10.0 | 9.010 | REJECT |
| H-06-A | 9.4 | 9.4 | 9.4 | 8.2 | 10.0 | 9.280 | LEAD |
| H-06-B | 9.3 | 9.5 | 9.0 | 7.9 | 10.0 | 9.150 | RESERVE |
| H-06-C | 9.1 | 9.4 | 9.2 | 7.7 | 10.0 | 9.075 | RESERVE |
| H-07-A | 9.5 | 9.2 | 8.9 | 8.4 | 10.0 | 9.190 | RESERVE |
| H-07-B | 9.4 | 9.4 | 9.1 | 8.5 | 10.0 | 9.265 | RESERVE |
| H-07-C | 9.5 | 9.6 | 9.4 | 8.7 | 10.0 | 9.435 | LEAD |
| H-08-A | 9.4 | 9.5 | 9.6 | 9.0 | 10.0 | 9.465 | LEAD |
| H-08-B | 9.2 | 9.3 | 9.5 | 8.9 | 10.0 | 9.320 | RESERVE |
| H-08-C | 8.8 | 8.6 | 9.4 | 8.8 | 10.0 | 8.990 | REJECT |
| H-09-A | 9.5 | 9.3 | 9.1 | 8.2 | 10.0 | 9.225 | RESERVE |
| H-09-B | 9.6 | 9.6 | 9.3 | 8.3 | 10.0 | 9.385 | LEAD |
| H-09-C | 9.2 | 9.4 | 9.4 | 8.1 | 10.0 | 9.205 | RESERVE |
| H-10-A | 9.3 | 9.2 | 9.2 | 8.6 | 10.0 | 9.220 | RESERVE |
| H-10-B | 9.4 | 9.4 | 9.3 | 8.5 | 10.0 | 9.305 | RESERVE |
| H-10-C | 9.5 | 9.6 | 9.5 | 8.7 | 10.0 | 9.455 | LEAD |

The three rejected routes are H-01-C, H-05-C, and H-08-C. Their repair notes are not extra candidates or automatic resubmissions. Each needs a new composition and reassessment.

## 7. Scene risk audit and required evidence

Likelihood/severity labels are qualitative forecasts of these concepts, not detected defects in nonexistent HOUSE pixels. All scenes retain P-01/P-02/P-03.

| Scene | Main print/construction risk | Likelihood / severity | Evidence needed before any finish clearance |
| --- | --- | --- | --- |
| H-01 | Black jamb/hand contact fills in; flat mirror wrongly curved or sightline blocked | High / critical | Actual and reflected same smooth blade, anatomical grip, mirror plane/eye construction, real aperture and clearance; intended-size cuff and bow visibility. O-01/O-07. |
| H-02 | Floor becomes a dark slab; inverted sleeve floats; cat merges with floor | High / critical | Source/floor/eye layout, correct virtual geometry and paw registration; actual broad sleeve/cabinet whites; measured black fraction. O-01/O-07. |
| H-03 | Finger channels become filaments; living hand, glove, and recess merge | Medium / high | Bare right versus wearable left glove, five plausible digits, real shallow drawer support and recess depth; local white-thickness measurements. O-07. |
| H-04 | Canopy eats white space; opaque fabric is wrongly treated as translucent | High / critical | Eight-rib attachment, exposed damaged tip, one lamp/occluder/receiver layout yielding the roof interruption; actual panel whites and shadow clue at size. O-08/O-07. |
| H-05 | Tiny tile rhythm replaces big planes; trapped terminal shown as free | Medium / high | Slate lap order, actual pinch/support contact, ordinary hatch support, continuity of sleeve/vent, unavailable maintenance reach without another active fold. O-06/O-07/C-05. |
| H-06 | Shaded/black jug loses reversal; arbitrary handle inversion masquerades as refraction | High / critical | Cylinder cross-section, water/glass and view/object distances, bounded transmitted segment, unchanged pan attachment, cup-first silhouette and right-hand grip. O-04/O-07/C-05. |
| H-07 | Dark underside slab; fake folding pile; no retained support after cup removal | High / critical | One changed adjacency with two visible continuations; ordinary hinge, stop, detent, stable cup base, correctly grouped keys; broad fallboard/door fields. O-03/O-06/C-05. |
| H-08 | Repeated palm badges, small unreadable far bay, cat anatomy lost | Medium / high | Exactly three attached equal-real-scale incomplete supports, accessible real third-tread opening, adult bed, small floor-resting cat, wide mattress/pillow. O-07/C-04. |
| H-09 | A real bar replaces anamorphosis; depth evidence depends on tiny cuts | High / critical | One eye-point construction plus a later ordinary shifted-view verification that separates the three real contours; coherent stairs and partly visible nook. O-09. |
| H-10 | Board noise, hidden base, wrong near/far scale, miniature attic gap | Medium / high | Common perspective, near-rook/far-latch overlap, ordinary piece and adult door scale; later displaced-piece check reveals the same route; gloved-left-hand contact. O-09/O-07. |

### Global immediate vetoes

- Any gray or transparent finished pixel; gray glass/floor shine or fur shading disguised as “black and white.”
- A generic hallway spiral, repeated tunnel wallpaper, centered eye vortex, mandala, border, text, or annotations inside art.
- Curves that cross material joints without a physical reason, become decorative skin on every object, or hide the causal clue.
- Mirror images that change objects, hands, actions, or time; reflected key teeth; shadow details transmitted through opaque fabric; whole-jug reflection substituted for cylindrical refraction.
- Extra living/carved/physical cups confused with the single carried cup, extra cats, a ghost host, or completed hospitality before its later reveal.
- Unusable narrow primary whites, buried contacts, or an ordinary domestic illustration whose optical event disappears at thumbnail.
- Unsupported anatomy, floating instruments, rods through slate, arbitrary scale changes, or more than one active impossible seam.

The contract forbids adding mirrors everywhere to restore “reflective” character. Reflection leads H-01/H-02 and returns later at canonical scenes; H-03–H-10 earn their impact through their assigned optical mechanisms. Optional gloss must remain incidental and must never become a second governing trick.

## 8. Proposed lead sequence for the jury

| Scene | Preferred route | Main silhouette / camera change | Dominant white reserve |
| --- | --- | --- | --- |
| H-01 | A | Shoulder-height sculptural jamb compression around an accountable plane mirror | Hand and broad jamb wings |
| H-02 | B | Rolled heel-height floor reflection across the portrait | Reflected sleeve and cabinet fronts |
| H-03 | A | Steep downward receiving canyon in a shallow drawer | Glove palm/fingers and shelf |
| H-04 | B | Off-center underside bowl with a real angular roof projection | Opaque canopy lobes and plaster |
| H-05 | A | Steep roof survey with broad flowing structural laps | Slate faces and lifted-edge wedge |
| H-06 | A | Lateral iron collar with bounded cylindrical inversion | Cup, clear jug field, and counter |
| H-07 | C | Elevated service-side white fallboard at one wrong corner | Fallboard and ordinary bedroom opening |
| H-08 | A | Elevated bed-foot quarter view of three real receivers | Very broad mattress, pillow, and bay fields |
| H-09 | B | Third-tread inside-turn alignment under looming rail return | Tall wall blade and supported tread fields |
| H-10 | C | Rolled board-level ordinary rook occluding the far latch | Large white squares and adult-scale door |

This sequence changes the original H-07/H-08 low-camera cluster through proposed high views, then preserves H-09's required low eye and H-10's board-level overlap. Those new cameras are deliberate recovery alternatives, not edits to canonical files. The jury must compare actual silhouettes later; C-02 remains open.

First later construction priorities within this batch: H-02-B for source-to-floor registration, H-04-B for opaque-canopy shadow feasibility, H-06-A for real cylinder inversion, H-07-C for the elevated single-seam construction, and H-09-B for a genuine view-dependent latch. Strong-looking geometry without those proofs is still on HOLD. Later canonical hero priorities H-16/H-12/H-19 remain acknowledged, outside this 30-route scope.

## 9. Remaining holds and completion record

- P-01 remains: no HOUSE raster exists here to measure black coverage or confirm optical silhouette.
- P-02 remains: all candidate white-zone dimensions are design targets, not measured candidate regions.
- P-03 remains: no physical sheet, edge behavior, or coloring-medium test was performed.
- Relevant O-01–O-09 and C-01–C-05 from HOUSE REVIEW remain open. A written continuity improvement does not clear future layout or geometry proof, including the single route/seam, motif restraint, reveal timing, and voluntary later acceptance.
- Only REPORT.md is produced in this role folder. No reference PNG, canonical Markdown, competitor output, generated art, production file, or assembly artifact is modified.

Completion checks: exactly 30 unique candidate headings (A/B/C for each H-01–H-10), 30 score rows, 10 leads, and three rejections; all weighted totals and optical-threshold dispositions checked with no discrepancies. SHA-256 checks before/after writing matched for all ten inputs: the role brief, contract, three HOUSE documents, and five reference PNGs. The role folder contains only its original ROLE_BRIEF.md and the completed REPORT.md.

**Written deliverable complete: five actually inspected visual references, quantified sample/scan evidence, strict finish targets, 30 distinct H-01–H-10 recovery candidates, weighted concept scores, three explicit optical-impact rejections, concrete route vetoes, a scene print-risk audit, and a proposed ten-scene lead sequence. No image is GOLD or print-approved.**