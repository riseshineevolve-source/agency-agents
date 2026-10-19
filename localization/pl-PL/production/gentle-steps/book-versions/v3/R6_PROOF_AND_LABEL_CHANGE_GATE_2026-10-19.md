# Gentle Steps PL R6: source lock, actual-template proof, and proposed labels
Date: 2026-10-19
Status: R6 LANGUAGE SOURCE VERIFIED; PRODUCTION TEMPLATE PROOF BLOCKED; NEW LABELS OWNER CANDIDATES
Writer scope: Polish Localization Engine only. This document is NOT an app/website change.

## Exact source reconciliation

- Source: GENTLE_STEPS_PL_BOOK_VERSION_03_PACKAGING_CANDIDATE_R6_2026-10-08.md
- Git blob: 896cf92bf6ed126ef62e623fd9cac640270e853f
- R6 == exact file consumed in RISE.SHINE.EVOLVE/gentle-steps-app/content/pl/source/ on gentle-steps/app-en-full24-purple-gold at observed HEAD 308201f2da4d3f3083ebc6643d272b0503dc8421.
- Structural inspection: 24 DZIEŃ units; each has one ZWOLNIJ section, one GRAMY section, one MIĘDZY NAMI section and NA JUTRO. No reader-facing em dashes.
- R5 and R6 text from day 1 to end is identical. R6 changed only front subtitle from R5.
- These are structural/source-consumption assertions. They do NOT equal full editorial, actual-template/print-scale, human accessibility or release approval.

## Owner candidate: recurring labels and English back-brief

The previous conversation proposed these more everyday, family-voiced labels. Treat as **CANDIDATE, not an amendment to R6** until the owner locks the entire set.

| Existing PL R6 | PL proposed | Existing EN | Proposed EN |
|---|---|---|---|
| ZWOLNIJ | ZŁAPMY CHWILĘ | PAUSE | LET'S TAKE A MOMENT |
| GRAMY | ZRÓBMY COŚ RAZEM | PLAY | LET'S DO THIS TOGETHER |
| MIĘDZY NAMI | POGADAJMY | BETWEEN US | LET'S TALK |

PL book title remains **ŚWIĘTA SĄ TEŻ PO DRODZE**.
Existing approved PL subtitle remains **Rodzinny kalendarz adwentowy na 24 dni. Nic do kupienia. Nic do przygotowania. Tylko WY. 10 minut razem.**

EN subtitle proposed (NOT migrated): **A 24-Day Family Advent Calendar. Nothing to Buy. Nothing to Prep. Just You. Ten Minutes Together.**

**Approval impact:** if labels are accepted, produce a new versioned PL source (do NOT patch R6 in place), replace all 72 section headings plus front-matter explanations and any legitimate mentions of the old system; update app content/notifications/UI and EN labels/subtitle through the respective product writer, preserving exact activity mechanics, NA JUTRO, safety/consent and character identities. Regenerate source hashes, source-to-app parity, relevant visual fits and localization tests. The current R6 proof cannot approve a future R7. If declined/deferred, continue R6 print proof unchanged.

## Missing actual production evidence (blocker)

Required producer: Gentle Steps book/template writer. Not Localization and not a synthetic/proxy renderer.

Use contract:
V03_R6_FINAL_TEMPLATE_PROOF_CONTRACT_2026-10-08.json

The producer must provide **all together**:
1. real editable final template snapshot;
2. full-book PDF generated from that template with exact R6 source;
3. twelve DISTINCT print-scale PNGs from that PDF, with filenames corresponding to front_title_subtitle, front_happy_makers, front_how_book_works, day_24, day_18, day_09, day_01, day_23, day_07, day_21, day_22, day_10;
4. named renderer/revision, exact hashes and named print-scale reviewer;
5. no-clipping, no-collision, diacritics, typography, legibility, completeness and consent/safety review with case-specific corrections.

The R6 CLI below creates a deliberately **BLOCKED** evidence draft from files. The renderer and human reviewer must supply genuine evidence; this CLI never renders or approves pages.

From agency-agents root, with an evidence directory containing template/final_template.html, book/full_book.pdf, and reviews/<surface_id>.png:

    python scripts/gentle-steps-r6-proof.py draft \
      --artifact-root REAL_EVIDENCE_DIR \
      --renderer-name REAL_RENDERER \
      --renderer-revision EXACT_RENDERER_REVISION \
      --output REAL_EVIDENCE_DIR/evidence.json

Before verification the reviewer MUST examine every actual page at print scale, fill:
- surface_kind: actual_final_template;
- reviewer name and timezone-aware reviewed_at;
- actual source/rendered body font size AND leading (in pt);
- body_font_reduced_to_force_fit: false, only if true in real layout;
- every six review flags true only when individually verified;
- REMOVE the _draft_status marker only after genuine review.

Then:

    python scripts/gentle-steps-r6-proof.py verify \
      --artifact-root REAL_EVIDENCE_DIR \
      --evidence REAL_EVIDENCE_DIR/evidence.json \
      --output REAL_EVIDENCE_DIR/proof-result.json

Exit 2 / BLOCK for wrong R6 blob, missing PDFs/PNGs, reused screenshots, old R5, absent reviewer, unreviewed draft, proxy, shrinking body type, unverified review flags or broken hashes.

A structural PASS is **only an intake/attestation gate**. Editorial/safety human proof, physical/visual owner review, CONTENT_FROZEN, PRINT_READY and KDP publication remain independent owner gates. Do not fabricate rendered proof or auto-certify reviewer flags.

## Other lanes / scope guard

- No changes to English/Polish app source, CSS, website, marketer-owned copy or any other writer's mailbox.
- Polish website: Route B native re-authoring and method-focused SEO remain website/central-owned implementation, not a replacement of approved EN/PL texts by Localization.
- Detective PL: existing work retained. A 2026-10-08 owner directive freezes EN V10 **for its named Polish source**; current EN Book Factory has later evolving versions. No new full-book translation or automatic V10-to-newer-source substitution until current EN authority and explicit freeze gate are reconciled.
