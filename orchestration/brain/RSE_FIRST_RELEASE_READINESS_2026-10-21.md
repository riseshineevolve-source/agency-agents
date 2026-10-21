# First release readiness — 2026-10-21

Status: PREMIUM_INTERIOR_DELIVERED__MATCHING_COVER_METADATA_PHYSICAL_PROOF_PRICE_OPEN
Scope: central receipt reconciliation only; no product files changed.
Evidence snapshot: agency-agents @ adb2fa30c57a1d45c17aa74b12f7227de821ff60; Optical mailbox blob b86bebcf61cc47cd778fa0f10c758c1a5abb79db; premium checkpoint blob b83711fcf792882ba748128c38ac0dfd2bfce2a0.
Primary remains Optical Animals / Wild Illusions. Gentle Steps remains the existing fallback.

## Optical Animals: current exact artifact

| Field | Producer receipt |
|---|---|
| Current full interior | `WILD_ILLUSIONS_PREMIUM_FINAL_48P.pdf` |
| SHA256 | `bf12439907c4481d91926bc34ef86ed51d7667a17fc712a5e8261fa33963a6ef` |
| Location | Library `libfile_507fe3cae5088191be459397753617d0`, version 1; `/AI AGENTS/WILD_ILLUSIONS_PREMIUM_FINAL_48P.pdf` |
| Size / format | 104,838,751 bytes; 48 single pages; PDF 1.7 |
| Bleed page | 621 × 810 pt (8.625 × 11.25 in) |
| Trim | 612 × 792 pt (8.5 × 11 in); alternating outer bleed |
| Illustration custody | All 22 encoded body image streams byte-identical to original V4; body image placements minimum 300 ppi |
| Retained body pages | 41 retained body pages, excluding new 45/48: normalized painting content and rendered pixels identical |
| Original V4 | SHA256 `2dbe312fe0b8df5cecac2c1bf2c90e20d7ab69a30996eee05d444e98a9174e13` unchanged |
| Full-wrap cover | Exact matching filename/hash/specification receipt still UNKNOWN |

Source: [premium producer receipt](../projects/optical-animals/checkpoints/2026-10-21-premium-revision-final.md) and [producer mailbox](../control-plane/mailboxes/optical_animals.yml).
Hashes and checks above are producer-reported and verified against durable Git receipts. Central has not downloaded/rehashed private PDF bytes or rerendered the book. Digital delivery is not owner acceptance or release approval.

## Audit response and superseded evidence

The premium revision supersedes `WILD_ILLUSIONS_KDP_INTERIOR_FINAL_48P_PRINT.pdf` (hash `42befffa23a295d0e05c7020fba66f765158c2714000a71af735fab366513516`), earlier intro-only v5 and malformed v4. Do not use older print-master recommendations.

The producer records owner authorization to implement audit improvements. Main “Wild Illusions / A Premium Op Art Coloring Book” retained; secondary line is now “20 Animal Designs to Color.” Before accurately distinguishes 18 single-page designs with blank backs and two facing-page artworks. Publishing has no empty ISBN label; this does not finalize the ISBN choice. Publishing/Before body type uses native EB Garamond outlines; approved intro art/source originals remain unchanged.

Page 44 remains blank to protect horse43. Page45 says “Let your imagination take flight.” Original butterfly46–47 retained; page48 says “Stay curious. See differently.” There are now19 blank pages, not21. The two spread exceptions are disclosed. The previous central “blank44–45/closing48/title audit pending” item is fulfilled by a concrete response; owner visual acceptance and paper/ink/gutter proof remain open.

Producer reports independent visual/copy and technical PASS against the final hash: strict parsing, all48 MuPDF and Poppler renders, pdftotext zero stderr, correct alternating trim, no live fonts/soft masks/metadata/annotations. Intro consists of faithful vector contours; a300ppi render does not establish native300ppi source detail.

Validation nuance: unused nonpainting default font blocks were removed after a real warning. Whole decoded body streams are therefore NOT byte-identical to V4. All22 encoded illustration streams are unchanged;41 retained body pages have identical normalized painting content and rendered pixels. The former blanket “43 whole content streams unchanged” assertion must not carry forward to this premium artifact.

## Actual remaining gates

| Requirement | Current evidence / next remedy | Existing owner |
|---|---|---|
| Digital interior/audit response | Producer PASS on current premium hash; no central rerender/rebuild needed | optical_animals |
| Owner visual acceptance | Revised exact interior delivered; acceptance not observed | optical_animals / owner |
| Matching full wrap | Expose existing filename/location/SHA256 and48-page trim, bleed, binding, paper, ink match. Resolve existing source before any cover recreation | optical_animals |
| Final metadata | Producer title/subtitle direction is recorded; confirm exact author/language/ISBN choice and agreement across cover/interior/listing | optical_animals; marketing consumes accepted facts |
| Previewer / physical proof | No actual KDP Previewer or physical paper/ink/gutter proof receipt supplied. Producer still requires physical proof. Digital PASS does not replace it | optical_animals / authorized owner |
| Rights / AI declaration / account | Exact legal/AI copy preserved by producer; final rights/declaration and required account status still unverified. Private details stay outside public Git | optical_animals / authorized owner |
| Price and royalty | Need marketplace/currency, confirmed paper/ink/binding, current actual print cost and proposed launch price/royalty | marketing_autopilot after verified spec |
| Consolidated submission decision | Not ready until exact accepted interior + matching cover + required proof + price exist | central_control_tower |

## Existing Gentle Steps fallback comparison

Existing comparison retained because the matching Optical cover and actual print proof remain unverified. The previous intro digital hold is closed; missing receipts do not prove missing files.

- Current Gentle Steps mailbox confirms app audit/native artifacts, not book release readiness. Android tests are not a book-publication prerequisite.
- [Existing asset inventory](../../marketing/GENTLE_STEPS_ASSET_INVENTORY_2026-10-01.md) names `24 Gentle Paperback ok(3).pdf` and `24 Gentle Steps to Christmas COVER HARDCOVER(2).pdf` in source folder `1SCQUodkBUwSC4Y06EVfdIxya4wUqIASx`. These are historical pointers, not current hash-bound files. A hardcover-named cover cannot be presumed to fit that paperback.
- [Current marketing brief](../../marketing/GENTLE_STEPS_PRODUCT_MARKETING_BRIEF_2026-10-07.md) and [October 13 copy pack](../../marketing/GENTLE_STEPS_A_PLUS_SOCIAL_AMAZON_COPY_PACK_2026-10-13.md) establish the later EN/PL title/subtitle direction. Cover/interior matching against those locks is still unproven. Reuse approved current labels; older examples inside these documents still contain legacy labels.
- EN source content hash `d8970cdb921683f5e9aa32165f03163098f169183e55fecf289bd2cbbc10aef1` is a content-source receipt, NOT a final interior PDF hash.
- PL R6 blob `896cf92bf6ed126ef62e623fd9cac640270e853f` is a source receipt, NOT print proof. [Localization mailbox](../control-plane/mailboxes/polish_localization.yml) explicitly lacks actual current final-template PDF, twelve distinct print-scale page views and reviewer evidence.
- Current book interior/cover hashes, page/trim match, Previewer/physical-proof receipts and actual pricing remain unverified for this fallback.

Decision: DO NOT SWITCH YET. Existing evidence does not establish Gentle Steps as a more complete publishable package. Request existing matching paperback assets and current source-bound proofs from its sole writer; do not open a third product or new renderer.


## Central handoff and next receipt

Central request `first-release-oa-files-20261021` is partially fulfilled by the premium interior and concrete audit response. Explicit acknowledgment of that request ID is still not observed; artifact delivery is not task acknowledgment. The producer explicitly acknowledged only the model policy.

Next action: existing Optical writer exposes the matching full-wrap cover receipt and confirmed paper/ink/binding for this premium48-page hash. Do not repeat the audit, reopen corrected page45/48 copy or rebuild artwork. Marketing then provides source-dated cost/price arithmetic. Existing fallback mailboxes remain unchanged; no evidence supports switching the queue.

## Cost and privacy

No Actions, spending, billing/subscription change, paid proof order, upload, publication, source freeze or production merge. Central writes only its Brain, Control Plane and own mailbox with expected-HEAD protection. Latest separate Mind Bloom/Supabase discussion does not authorize central product or database writes in this release task.
