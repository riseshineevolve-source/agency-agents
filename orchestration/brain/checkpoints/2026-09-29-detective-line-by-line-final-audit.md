# Detective Academy Book 1 EN — Line-by-line final reader audit

Date: 2026-09-29
Authority: Central RSE Technical Orchestrator
Reviewed artifact:
`HMDA_Book1_EN_FINAL_FIVE_BLOCKERS_OWNER_REVIEW_2026-09-29.pdf`
SHA-256:
`98f45753327f01e9da0bc4cc994408b38c2da1e3307af60f34ef318256425947`
Pages: 180

Status:
**FULL LINE-BY-LINE + VISUAL AUDIT COMPLETE / MICROFIX GATE / DO NOT FREEZE EN YET**

## Overall

The 30-case structure, main Room Zero chain, all locked spatial solutions, Case03 exact-ten mechanism, Case05 code, Case21 message, Case26 extraction, Case27 sealed-room logic, Case29 D3, Case30 call-sign finale and Book2 callback are intact.

KDP print geometry is strong: 8.5x11, 180 even pages, >=300 effective image DPI, >=0.75pt functional linework, margins above the current 151-300-page minimum, physically upright pages.

However the artifact is not yet a literal 100% freeze candidate because the line-by-line reader audit found bounded editorial/fair-play/layout issues.

## Must fix before KDP Previewer

1. Page 7 still says `Turn to the upside-down section at the back`, but the final Hint Vault/Solutions are upright. Replace with back-of-book / STOP divider wording.

2. Case28 fair-play gap: reader is instructed to restore/copy the full Rule Zero, but before the solution the book never prints the exact fixed wording `NOTICE FIRST. THEORIZE SECOND.`. Add a damaged-rule evidence template such as:
`ZERO ____________. NOTICE FIRST. THEORIZE SECOND.`
Then sorting supplies `ASSUMPTIONS`.
Also change `Sort every card into the three printed zones` to the physically explicit `Write each claim letter A-F in the correct zone`.

3. Page47 US-English inconsistency: `MIMI - DO NOT CATALOGUE` -> `MIMI - DO NOT CATALOG`.

4. Case22 story/evidence-purpose mismatch: current story says Zara's room is a snapshot of which instrument case was beside her, while the actual puzzle identifies the human witness beside Zara. Rephrase the sentence so the room snapshot identifies who was beside Zara before the cases were moved.

5. Page98 overclaim: Case25 reconstructs Nori's snapshot/companion, not a full parcel route. Replace `opens the parcel using the witness route you reconstructed` with a handoff-confirmation line tied to Nori's companion.

6. Page42 and page65 running headers are visibly truncated:
- `ROOM ZERO THREAD // BIBI REMEMBER`
- `ROOM ZERO CHECKPOINT // RULE 0 FI`
Shorten header labels so they render complete.

7. Case27 fair-play/nomenclature:
- Case28 says the old-plan margin contains `RULE FIRST, ROOM SECOND`, but page102 does not visibly print the margin note. Add it to the old-plan evidence.
- Hints/solution call anchors `North Stair / Courtyard Column / West Lift Shaft` while evidence labels only `STAIR / COLUMN / LIFT`. Either use the same full labels on evidence or simplify hint/solution wording to exactly match what is printed.

8. Source-of-truth drift: canonical V3 in both agency-agents and Book Factory still contains the obsolete upside-down back-matter copy, FALSE LEADS Case Wall copy and old Case08 wall-crossing wording. The final PDF currently depends on renderer substitutions. Before EN freeze, sync the final printed reader wording back into canonical V3 and update the verifier/blob lock so a future build cannot regress.

## Strong polish, not puzzle blockers

- Front-matter pages 4 and 9 use plain `HAPPY MAKERS CHAT` bullets rather than the established COMMS treatment. Decide whether this is intentional.
- Front-matter headings `PAGE 4 //`, `PAGE 5 //`, etc. read slightly like production labels because the physical page number already exists.
- Page30 standalone Heritage COMMS is intentionally cinematic but still has very large unused white space.
- Several full Evidence Grid parity pages are visually near-identical; they preserve LEFT Witness Board -> RIGHT Map, but physical proof should confirm they feel like brand pacing rather than filler.
- Room Zero debrief pp113-115 is the densest white-on-black reading section; physical proof must confirm comfortable readability for age 8-12.
- Case22/other contact cases occasionally close only at “we now have someone to ask”; optional local-story closure lines could improve satisfaction, especially the parrot-password file.
- Field Certification line `Signed: Happy Makers Detective Academy Archive confirmation: BIBI // ARCHIVE MENTOR` would read more cleanly with a separator or line break.
- Archive File 001 dialogue uses bullets rather than COMMS; acceptable as an archive epilogue if intentional.
- Solution text + solution maps are not consistently facing spreads; usable but not maximally convenient.

## Reading-level note

Overall main-book reading level is appropriate for the target band (rough aggregate FK ~4.7), but Case File intros alone are materially harder (median rough FK ~7.2). The hardest intros are Case15 (~9.6), Case23 (~8.7), Case18 (~8.6), Case11/16 (~8.5). This is driven mainly by long sentences, not unsuitable vocabulary. If optimizing for independent 8-year-old reading, split the longest intro sentences without simplifying the detective voice.

## KDP / metadata cleanup

- Used Arial/Arial Bold are embedded, but PDF resources still list unused Helvetica as unembedded. Strip that resource before final upload if practical, because KDP's official guidance requires fonts in submitted PDFs to be embedded.
- Metadata Creator remains `anonymous` and Subject `unspecified`; non-blocking but can be cleaned for final artifact hygiene.
- ISBN checksum is valid, but ownership/assignment and exact match to KDP title/cover metadata cannot be verified from the interior PDF alone.
- Final cover/spine remains downstream of Previewer + physical proof + explicit EN freeze.

## Gate

Do NOT call EN frozen yet.
Do NOT merge main or publish.
Apply only the bounded fixes above; rerender; rerun deterministic QA; Central rechecks changed pages + contact sheets. Then KDP Previewer can be the next gate.
