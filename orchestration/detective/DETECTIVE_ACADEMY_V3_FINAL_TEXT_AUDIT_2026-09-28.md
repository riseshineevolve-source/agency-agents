# Detective Academy Book 1 — V3 Final Text Audit

Date: 2026-09-28
Authority: Central RSE Technical Orchestrator
Status: FINAL TEXT CANDIDATE AUDIT COMPLETE / LAYOUT STILL PAUSED

## Canonical text

`orchestration/detective/DETECTIVE_ACADEMY_BOOK1_TEXT_GOLD_MASTER_V3.md`

Latest commit:
`25eacd6f5e085313283591548c0a9787b336e4b7`

The version family remains **V3**. No V4 created.

## Audit scope

The full V3 text was read end-to-end as:
- an 8–12-year-old reader;
- a continuity editor;
- a puzzle/answer consistency reviewer;
- a grammar/punctuation reviewer;
- a repetition/pacing reviewer;
- a Happy Makers voice/relationship reviewer.

No puzzle geometry, locked answer, Case 03 exact-ten mechanic, owner art truth or Room Zero chain was redesigned.

## Final corrections made

1. Opening recruitment:
   - `completed recruitment` corrected to `started recruitment`;
   - recruit credential remains free of Field Position 06;
   - reader-facing field-role reveal stays at the finale.

2. Front-matter compression:
   - removed meta-author commentary explaining why cases come from different places;
   - kept the same world logic in natural story prose.

3. Objective/response alignment:
   - Case 01 objective now includes the required square;
   - Case 11 objective now asks for the reason the timestamp is outside the case window;
   - Case 28 objective now includes recovery of the missing Rule Zero word.

4. Case-story upgrades:
   - Case 04 tightened and strengthened as Academy Open Night evidence-box misroute;
   - Case 06 tightened as Heritage Gallery dragon-tooth/Roman-spoon incident;
   - Case 10 explicitly occurs during the Academy Science & Prototype Fair;
   - Case 11 uses the same Science & Prototype Fair time window;
   - Case 12 now has a coherent Scenario Theater + visiting animal-care rehearsal setup;
   - Case 20 has a concrete Flight Simulation Wing paint-smear incident;
   - Case 29 now follows Rule Zero logically: the team stops guessing and requests the service-level access record.

5. Bibi repetition:
   - Case 09 intro no longer says she recognizes the mark;
   - HM Chat no longer repeats the recognition;
   - the recognition is revealed once, after the reader completes the classification.

6. Case Wall:
   - final interlude now explicitly uses page 9 as the collection point;
   - Case 30 uses Case Wall for RULE / ROOM / CODE and Recruit Credential for DETECTIVE;
   - the ROOM field is explicitly explained as expecting the Case 29 access coordinate.

7. Hint Vault:
   - removed stale old page numbers from Case 26 MAP LOOKUP;
   - uses case numbers only so later pagination cannot invalidate the hint.

8. Case 09 precision:
   - final solution wording uses `recurring Academy mark`, not `signal`, because meaning is still unproved.

9. Production integrity:
   - added an explicit Evidence/Puzzle hydration lock: locked Witness Boards, map clues, owner-controlled photo evidence and other authoritative puzzle payloads must be hydrated from current source/raster truth rather than rewritten from the prose master.

10. Markdown/PDF integrity:
   - fixed one missing blank line before Appendix E1 heading;
   - editorial PDF re-rendered successfully.

## Deterministic checks

PASS:
- 30/30 main cases
- Case Index titles = main case titles = Solution File titles
- Hint Vault Level 1: 30/30
- Hint Vault Level 2: 30/30
- Hint Vault Level 3: 30/30
- immediate reader-facing CASE RESULT blocks: 0
- immediate reader-facing WHAT THIS PROVES blocks: 0
- `FIND ALL 10 DIFFERENCES` appears once in reader-facing Case 03 instructions
- old fixed Case 26 page references: 0
- old 4-symbol Case 05 answer: 0
- six-symbol Case 05 constraints have exactly one solution:
  `BALL -> STAR -> BOLT -> HEART -> KEY -> MOON`
- stale QUINN / ZANE reader-facing aliases: 0
- current Case 01 Hint Vault uses QUILL / MORSE / PIP / KNOX
- Field Position 06 appears only in earned-finale context
- Case Wall remains page 9 and is not used as a generic duplicate-answer sheet

## Narrative conclusion

The current V3 is substantially stronger than prior text layers:
- one Academy world rather than random unrelated locations;
- varied case-entry mechanisms;
- clear time progression across days;
- local mysteries that are worth solving even before Room Zero matters;
- stronger transitions;
- less repeated explanation;
- Happy Makers chats carry humor, relationship and supportive thinking without carrying hidden puzzle rules;
- Room Zero escalation remains earned rather than constant.

No further broad text rewrite is recommended before owner review.
Future changes should be bounded to a concrete owner-found sentence/logic defect.

## Next gate

**Owner text review -> explicit V3 text lock -> renderer/layout consolidation.**

The renderer may not:
- shorten story intros to fit boxes;
- reintroduce immediate answers/results;
- reduce Case 05 back to four symbols;
- reintroduce stale aliases;
- rewrite locked puzzle evidence;
- duplicate coordinate systems;
- invent extra Room Zero marks;
- remove explicit Case Wall instructions.



---

## Owner-feedback final microfix pass — 2026-09-28

This pass responds to the owner's final instruction to read the book as a reader, remove residual repetition, make every case introduction causally clear, and make the Room Zero explanation logically airtight without reverting or redesigning any locked puzzle truth.

Latest V3 text commit touching the canonical master:
`3e534a2a5fe95dc183a0825071ae064175803a0b`

The version family remains **V3**. No V4 was created.

### Corrections completed

- Case 02 now states exactly why Max matters: he is the last verified record tied to the Founders' Cup, and the person with him is the best witness to the missing handoff.
- Case 03 no longer claims that two physically different evidence scenes were photographed one minute apart. They are now two file copies of the same evidence photograph that should be identical but are not; the locked exact-ten mechanic is unchanged.
- Spatial/contact case intros were de-formulaized. They explain the fixed anchor and the concrete investigative value of the room companion instead of repeating the Objective as "find who shared X's room."
- Case 05 no longer implies that the locker itself sealed the old envelope.
- Case 28 locates RULE FIRST, ROOM SECOND in the old-plan margin instead of having the instruction appear vaguely "beside" the room.
- The Room Zero explanation now distinguishes routing from investigation: the old route can select/tag suitable records, preserve/reopen material and use completed filed work, but it does not create incidents or solve cases.
- Book 2 hook is labeled **ARCHIVE FILE 001 // STILL OPEN**, avoiding confusion with Book 1 Case 01.
- Repetitive Solution File consequences were tightened so WHY IT MATTERS advances the story rather than restating the answer.
- The duplicated second Case 03 ten-difference list was removed.
- Appendix drift was corrected: Case 05 = six ordered symbol slots; Case 04 source = Trace Lab evidence-box misroute to Pickup Tent; stale V2 wording for Case 26 removed.
- US English is now internally consistent for Theater / labeled / traveling / gray.
- One accidental duplicate final narrative paragraph in canonical Markdown was removed.

### Deterministic non-regression after the microfix

PASS:
- reader-facing cases: 30/30
- Hint Vault Level 1: 30/30
- Hint Vault Level 2: 30/30
- Hint Vault Level 3: 30/30
- Solution Files: 30/30
- Case 05 six-symbol solution remains unique:
  `BALL -> STAR -> BOLT -> HEART -> KEY -> MOON`
- stale `find who shared` formula in case intros: 0
- stale `taken one minute apart`: 0
- stale `4 ordered symbol slots`: 0
- stale `Forensic Kitchen`: 0
- duplicated `VERIFIED TEN DIFFERENCES` block: 0
- stale `CASE 001 // STILL OPEN` Book 2 hook: 0
- stale QUINN/ZANE aliases: 0
- Field Position 06 appears before the earned finale: 0
- UK-spelling leftovers checked (Theatre / labelled / travelling / grey): 0

### Reader-name / renderer cross-check

Current production renderer alias file:
`riseshineevolve-source/RISE.SHINE.EVOLVE@feature/detective-book-factory:tools/detective-book-factory/content/spatial_character_aliases.yml`

Alias blob at verification:
`a5f3385bc3d2955367164134d31994a764f3e60c`

For all 15 spatial cases in that alias layer, the named Solution File answer is present in the reader-facing alias roster: **15/15 PASS**.

Case 01 remains a separate hydration check because its canonical display aliases are QUILL / MORSE / PIP / KNOX while older renderer production source still contains internal identities ARI / BEA / COLE / DANI. The final renderer must apply the current display alias layer and re-run the evidence-name consistency gate after hydration.

### KDP-readiness implication

The **text master is now the current final V3 owner-review candidate**.

It is not yet honest to call the attached 71-page editorial PDF a KDP-ready interior. It is a text-only review artifact and intentionally omits the final Witness Boards, maps, photographs and other evidence surfaces. The next production step is to hydrate this exact current V3 into the book factory, regenerate the full print interior, then run source/name/answer consistency + KDP preflight + full visual audit before physical proof.

