# First release readiness — 2026-10-21

Status: BLOCKED_BEFORE_CONSOLIDATED_RELEASE_DECISION
Scope: central receipt reconciliation only; no product files changed.
Evidence snapshot: agency-agents @ 1c205adf39752eb91922b02854375049fbb1734c; new Optical producer receipt @ 74e9fef07e55f9c4fb3e2e7b14e1908feb077045.
Primary remains Optical Animals / Wild Illusions. Gentle Steps is the existing fallback, not a second active launch.

## Optical Animals: exact artifact identities

| Artifact | Producer receipt | Release meaning |
|---|---|---|
| Owner canonical V4 interior | SHA256 `2dbe312fe0b8df5cecac2c1bf2c90e20d7ab69a30996eee05d444e98a9174e13`; 48 pages; 621 × 810 pt (8.625 × 11.25 in) | Preserved source, not a newly accepted final interior. Exact original filename/location still required from writer. |
| Current five-page visual intro | `WILD_ILLUSIONS_DECORATIVE_BIRD_INTRO_FINAL_5_PAGES.pdf`; SHA256 `ea50f7dd0100cafa45be8477eb469b76d5a803919b1c87e6509a2952cc79f216`; Library `libfile_a7c748e88e408191a99a329b0f60b2f2`, version 3 | Completed visual design; five pages, 621 × 810 pt. NOT a final 48-page interior. Supersedes version 2; no body integration or KDP approval. |
| Current Before You Begin image | SHA256 `caa1b5a84c5c3b2755b9fb49418fdc9b19d049c285ec236219112a5609e8f95b` | Part of decorative-bird family; raster lettering still requires faithful print typography. |
| Full-wrap cover | No matching exact cover receipt in the inspected current producer mailbox/checkpoints | UNKNOWN, not evidence that no cover exists. Writer must expose existing source before any new creation. |

These are producer-reported artifact hashes, verified against their durable Git receipts; central has NOT independently rehashed private PDF/image bytes.

Producer evidence:
- [Copy recovery and source geometry](../projects/optical-animals/checkpoints/2026-10-21-owner-copy-recovery-intro-review.md)
- [Completed decorative-bird five-page visual receipt](../projects/optical-animals/checkpoints/2026-10-21-decorative-bird-five-intro-final-design.md)
- [Producer mailbox](../control-plane/mailboxes/optical_animals.yml)

## Optical Animals: actual remaining gates

| Requirement | Evidence / status | Existing owner of remedy |
|---|---|---|
| Accepted production intro | DESIGN DELIVERED: owner selected decorative bird for all five pages; producer reports copy/visual QA PASS and corrected Color test-panel overlap. Final visual feedback remains open. Current rasters are 1103 × 1426 (~127 ppi), not production masters | optical_animals |
| Native print quality | BLOCKED: faithful print derivatives/native typography and proof remain. No more family-selection task; producer reports Publishing AI note inside safe white inset, but physical print safety is not proven. No central resampling/rebuild | optical_animals |
| Final interior retention | PENDING: integrate only accepted intro; retain approved V4 artwork/order and verify unchanged pages. Review-only page identity checks are not full final-interior preflight | optical_animals |
| Cover/interior geometry | UNKNOWN: expose full wrap, SHA256, trim/bleed, binding, paper, ink and exact 48-page dependency. Source page geometry alone does not certify cover fit | optical_animals |
| Title/subtitle/author/language/ISBN | PARTIAL: Wild Illusions project identity observed; final exact metadata lock not supplied. Series name unchosen in source receipt; blank ISBN instructed; unrelated reference ISBN 9798177104409 must not be copied | optical_animals; marketing consumes verified facts |
| Previewer and physical proof | NOT PROVIDED in current receipts; gutter and single-sided wording exceptions for existing spreads remain. Preserve physical-proof gate | optical_animals |
| Price and royalty | NOT PROVIDED: marketplace/currency, exact print specification, current actual print cost and proposed price/royalty needed. No invented price | marketing_autopilot after product specification |
| Rights/AI declaration/account setup | UNVERIFIED: source/rights and truthful generated-content declaration receipt needed; private account status stays with authorized owner | optical_animals / authorized account owner |
| Consolidated submission decision | NOT READY: exact final interior + wrap + evidence + price must exist first | central_control_tower |

## Existing Gentle Steps fallback comparison

Triggered by the concrete Optical intro print hold, not by assumption that missing receipts prove missing files.

- Current Gentle Steps mailbox confirms app audit/native artifacts, not book release readiness. Android tests are not a book-publication prerequisite.
- [Existing asset inventory](../../marketing/GENTLE_STEPS_ASSET_INVENTORY_2026-10-01.md) names `24 Gentle Paperback ok(3).pdf` and `24 Gentle Steps to Christmas COVER HARDCOVER(2).pdf` in source folder `1SCQUodkBUwSC4Y06EVfdIxya4wUqIASx`. These are historical pointers, not current hash-bound files. A hardcover-named cover cannot be presumed to fit that paperback.
- [Current marketing brief](../../marketing/GENTLE_STEPS_PRODUCT_MARKETING_BRIEF_2026-10-07.md) and [October 13 copy pack](../../marketing/GENTLE_STEPS_A_PLUS_SOCIAL_AMAZON_COPY_PACK_2026-10-13.md) establish the later EN/PL title/subtitle direction. Cover/interior matching against those locks is still unproven. Reuse approved current labels; older examples inside these documents still contain legacy labels.
- EN source content hash `d8970cdb921683f5e9aa32165f03163098f169183e55fecf289bd2cbbc10aef1` is a content-source receipt, NOT a final interior PDF hash.
- PL R6 blob `896cf92bf6ed126ef62e623fd9cac640270e853f` is a source receipt, NOT print proof. [Localization mailbox](../control-plane/mailboxes/polish_localization.yml) explicitly lacks actual current final-template PDF, twelve distinct print-scale page views and reviewer evidence.
- Current book interior/cover hashes, page/trim match, Previewer/physical-proof receipts and actual pricing remain unverified for this fallback.

Decision: DO NOT SWITCH YET. Existing evidence does not establish Gentle Steps as a more complete publishable package. Request existing matching paperback assets and current source-bound proofs from its sole writer; do not open a third product or new renderer.

## Central handoffs and next receipt

Specific requests are recorded only in central's own mailbox under `release_packet_requests`.
No producer has yet explicitly acknowledged those new request IDs. Optical's model-policy acknowledgment is real; the new design delivery does not explicitly acknowledge the central revenue request IDs.

Next action: Optical writer returns existing V4 filename/location and matching full-wrap cover receipt, plus faithful print derivatives/native typography for the delivered decorative-bird designs; Gentle Steps writer exposes the already-existing matching book pair for comparison. Central then reconciles only changed receipts and assembles one exact files/price/submission decision when ready.

No publication, store price, spending, source freeze, production merge or proof waiver is authorized.

## Latest owner cost and privacy direction

Owner permits extremely sparing Actions within a stated $7 budget; this is not evidence of current remaining balance. No cloud run, retry, billing change, repo-visibility change or n8n subscription was performed for this reconciliation. Use local deterministic validation for this central metadata change and skip push-triggered CI. Preserve the privacy review; add no private artwork/account data to public Git. Central mailbox notice routes the constraint without claiming lane receipt.
