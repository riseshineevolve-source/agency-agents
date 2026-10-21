# Studio release —21 October2026

The complete225-page Detective Academy EN interior and local Studio have now been exercised on the owner's four actual sources. The GUI performs immutable import, full builds, version history, selected-page corrections, explicit freeze/unfreeze, comparison and PDF/report downloads.

Code: 01a5fb9d1635a1d0ea0da26a32a7e61ef0d17ab7 on feature/rse-book-factory-v2.

Evidence:60targeted tests PASS; real Chromium workflow PASS; selected25 correction preserves224other leaves pixel-exactly; finalPDF has225Letter pages,0native placeholders,0off-trim native text and0unexpected blanks.107solved-map placements equal originalRC23. Actual Case03glyph interiors were checked in rendered pixels; PDF render mode alone had missed an excessive stroke, now corrected to .55pt.

The complete production code generates the book; the chat does not manually assemble the final artifact. Full build101.86s; final23selected leaves46.5s including assembly/preflight. New dialogue layouts preserve all21source conversation pages. Large/small box source tests cover1..12panels and600words in two readable columns. Text overrides alter only the narrative slot and retain Comms/art. Unsupported families reject overrides explicitly.

Deliverables:
- DETECTIVE_ACADEMY_EN_20261021_225P.pdf — libfile_a2e7cf9799e48191811991e63cddcb3c — SHA2569db84d4f138cbbde8eb1f4a0f783f4d126c639120a11cabb65fc00711b9f05a0.
- RSE_BOOK_FACTORY_STUDIO_20261021.zip — libfile_60e360a316008191b9b8cf63dd92361e — SHA256820b4430f2ecf6c033a48d4be024df64dee03b44d205804f7daa0eee5430d54b.
- DETECTIVE_ACADEMY_QA_20261021.pdf — libfile_27578ff05fd48191819f1639907ba8ea.

Unzip the Studio separately, run START_WINDOWS.cmd, then follow START_FULL_BOOK_POLSKI.md. Three exact reference PNGs and extracted source fonts are bundled privately; none are committed toGit. The4author source inputs stay separate. The release includes its QA/contact/evidence files but no job cache or manuscript copies.

Remaining review: source artwork has296image instances under300effectivePPI; original frame example127.5PPI. No upscaling or KDP-readiness claim. Owner sign-off, Print Previewer and print proof are pending. Existing flattened lettering is preserved; it is not editable native type. Complex future books need their own family profile. Test approval records were cleared and do not represent owner approval. No publication, main merge or paid action occurred.

Product final documentation head: 8f7f7f05b4a82f8eef1692b2fe41b81be25887d9. Previous offline blocker resolved; files saved successfully. Exclusive Book Factory ownership unchanged. No other lane was edited.
