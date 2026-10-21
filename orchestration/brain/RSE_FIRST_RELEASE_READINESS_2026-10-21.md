# First release readiness — 2026-10-21

Status: INTERIOR_DELIVERED__COVER_METADATA_PROOF_PRICE_AND_FINAL_REVIEW_OPEN
Scope: central receipt reconciliation only; no product files changed.
Evidence snapshot: agency-agents @ cd3c51119a4c1aaed6d37002bc44c90f4f415c02; Optical mailbox blob 7d562791485a6a533b78cdcea105f34ef405f63d; full-book checkpoint blob 2096643c8e2d284b781d1b23b0fd3db16ec27595.
Primary remains Optical Animals / Wild Illusions. Gentle Steps remains the existing fallback.

## Optical Animals: current exact artifact

| Field | Producer receipt |
|---|---|
| Full interior | `WILD_ILLUSIONS_KDP_INTERIOR_FINAL_48P_PRINT.pdf` |
| SHA256 | `42befffa23a295d0e05c7020fba66f765158c2714000a71af735fab366513516` |
| Location | Library `libfile_889cc56741a48191a8df99b6c5f86acc`, version 1; `/AI AGENTS/WILD_ILLUSIONS_KDP_INTERIOR_FINAL_48P_PRINT.pdf` |
| Size / format | 104,811,441 bytes; 48 single pages; PDF 1.7 |
| Bleed page | 621 × 810 pt (8.625 × 11.25 in) |
| Trim | 612 × 792 pt (8.5 × 11 in); alternating outer bleed |
| Preserved body | All 43 pages 6–48: original order, identical content/image streams and rendered pixels; compressed image streams byte-identical; body image placements minimum 300 ppi |
| Original V4 | SHA256 `2dbe312fe0b8df5cecac2c1bf2c90e20d7ab69a30996eee05d444e98a9174e13` remains unchanged |
| Full-wrap cover | No exact matching filename/hash/specification receipt in the inspected current evidence; UNKNOWN |

Source: [producer full-book receipt](../projects/optical-animals/checkpoints/2026-10-21-full-book-print-interior.md) and [producer mailbox](../control-plane/mailboxes/optical_animals.yml).
These are producer-reported hashes and checks verified against durable Git receipts. Central has not independently downloaded/rehashed or rerendered private PDF bytes. This is a delivered interior candidate, not release approval.

## Resolved assembly and superseded evidence

The latest accepted five-page selection is: attached paired-peacock title; newest large-bird Publishing; newest large-bird Before You Begin; attached Color Your Way; attached broad-left-optical-frame Enter the Collection. This explicitly supersedes the previous sparse 2.81%-black Enter selection.

Intro uses faithful scalable black contour tracing of approximately 127 ppi sources, with a bounded Publishing type repair. It is not native 300 ppi source detail and not a native-typesetting rebuild. Producer reports independent visual QA, outlined type, stable post-save hash, strict parsing and all 48 pages rendered successfully. The old blanket “not integrated / print derivatives not delivered” blocker is closed by this receipt; physical print quality still requires proof.

Earlier five-page art-refinement PDF version 5 is historical visual work, not the current full interior. Malformed version 4 remains excluded.

## Actual remaining gates

| Requirement | Current evidence / next remedy | Existing owner |
|---|---|---|
| Digital assembly/preflight | Producer PASS; exact 48-page interior now identified. No duplicate render or art revision requested centrally | optical_animals |
| Latest owner review | Owner subsequently requested detailed audit, specifically blank pages 44–45 before butterfly, possible minimal closing sentence on blank page 48, and whether “Optical” accurately describes title/art. This is review feedback, not authority to silently alter art, page count or title. No resulting audit receipt observed yet | optical_animals |
| Matching full wrap | Expose existing exact cover filename/location/SHA256 and binding, paper, ink, bleed/trim, page-count match. Do not recreate a cover before resolving existing assets | optical_animals |
| Final metadata | Exact title/subtitle/author/language/ISBN choice must match accepted interior, cover and listing. Blank ISBN label is not a finalized ISBN choice. Review of “Optical” remains with product/owner | optical_animals; marketing consumes accepted facts |
| Previewer / physical proof | No actual KDP Previewer or physical paper/ink/gutter proof receipt supplied. Digital preflight is separate; no paid proof order or upload authorized | optical_animals / authorized owner |
| Rights / AI declaration / account | Provenance, rights, truthful generated-content declaration and required account setup status remain unverified; keep private account details outside public Git | optical_animals / authorized owner |
| Price and royalty | Marketplace/currency, confirmed paper/ink/binding, actual current print cost and proposed launch price/royalty missing. Digital page geometry alone does not settle print cost | marketing_autopilot after verified specification |
| Consolidated submission decision | Not ready until accepted exact interior + matching cover + required proof + price exist | central_control_tower |

Producer lists blank pages 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 45, 48; capybara spread 6–7 and butterfly 46–47. Those existing page identities explain the focused owner review; they are not central authorization to remove pages or insert copy.

## Existing Gentle Steps fallback comparison

Triggered by the concrete Optical intro print hold, not by assumption that missing receipts prove missing files.

- Current Gentle Steps mailbox confirms app audit/native artifacts, not book release readiness. Android tests are not a book-publication prerequisite.
- [Existing asset inventory](../../marketing/GENTLE_STEPS_ASSET_INVENTORY_2026-10-01.md) names `24 Gentle Paperback ok(3).pdf` and `24 Gentle Steps to Christmas COVER HARDCOVER(2).pdf` in source folder `1SCQUodkBUwSC4Y06EVfdIxya4wUqIASx`. These are historical pointers, not current hash-bound files. A hardcover-named cover cannot be presumed to fit that paperback.
- [Current marketing brief](../../marketing/GENTLE_STEPS_PRODUCT_MARKETING_BRIEF_2026-10-07.md) and [October 13 copy pack](../../marketing/GENTLE_STEPS_A_PLUS_SOCIAL_AMAZON_COPY_PACK_2026-10-13.md) establish the later EN/PL title/subtitle direction. Cover/interior matching against those locks is still unproven. Reuse approved current labels; older examples inside these documents still contain legacy labels.
- EN source content hash `d8970cdb921683f5e9aa32165f03163098f169183e55fecf289bd2cbbc10aef1` is a content-source receipt, NOT a final interior PDF hash.
- PL R6 blob `896cf92bf6ed126ef62e623fd9cac640270e853f` is a source receipt, NOT print proof. [Localization mailbox](../control-plane/mailboxes/polish_localization.yml) explicitly lacks actual current final-template PDF, twelve distinct print-scale page views and reviewer evidence.
- Current book interior/cover hashes, page/trim match, Previewer/physical-proof receipts and actual pricing remain unverified for this fallback.

Decision: DO NOT SWITCH YET. Existing evidence does not establish Gentle Steps as a more complete publishable package. Request existing matching paperback assets and current source-bound proofs from its sole writer; do not open a third product or new renderer.


## Central handoff and next receipt

Central's own mailbox request `first-release-oa-files-20261021` is now partially fulfilled by the exact full-interior delivery and body-custody/preflight evidence. No explicit acknowledgment of that request ID was observed; artifact delivery must not be mislabelled as task acknowledgment.

Next action: existing Optical writer exposes the matching full-wrap cover receipt and confirmed paper/ink/binding for the 48-page interior, and records its bounded response to the owner's blank-page/title audit. Marketing can then supply a source-dated cost/price calculation. No new renderer, third product, source freeze, paid order, publication or production merge.

Gentle Steps and marketing mailbox blobs remain unchanged from the previous comparison. No evidence supports switching the launch queue.

## Cost and privacy

No Actions run/retry, spending, billing/subscription change or repo visibility change performed. Owner's stated $7 ceiling is not verified remaining balance. Art bytes and private account details remain outside Git. Central edits only its Brain, Control Plane and own mailbox, with expected-HEAD protection.
