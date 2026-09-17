# RSE Polish Localization Quality Gates

Final status is PASS, FIX or BLOCK.

## Gate 1: Completeness
PASS when every source segment that should be localized has a mapped target segment, with intentional exclusions documented.

## Gate 2: Meaning fidelity
Check facts, numbers, instructions, product claims, chronology, relationships, negation, modality and causal logic. Any invented or lost fact is BLOCK until corrected.

## Gate 3: Natural Polish
Text must sound natively authored. Translationese, literal English syntax, unnatural collocations or synthetic marketing language are FIX.

## Gate 4: Cultural fit
References, jokes and examples must make sense to the intended Polish audience. Adapt only when needed. Avoid decorative 'Polishness' and stereotypes.

## Gate 5: Voice
Brand and character voices remain stable. For recurring characters, compare against approved voice profiles and previous accepted segments.

## Gate 6: Humor function
For humor/puns, compare effect rather than wording. Mark PASS when the Polish version performs the same narrative/emotional job, even with different imagery.

## Gate 7: Audience fit
Check reading level, emotional maturity and register for children, teens, parents/adults or specialists. Children's copy must not become baby talk; teen copy must not chase slang.

## Gate 8: Logic and continuity
Check referents, transitions, callbacks, names, chronology, terminology and repeated motifs.

## Gate 9: Language and typography
Check Polish grammar, spelling, punctuation, inflection, quotation marks, dates, number formats and typographic consistency.

## Gate 10: Surface constraints
For UI/web: length, button fit, pluralization, responsive layout, labels, accessibility text, alt text and metadata.
For books/PDF: page mapping, headings, callouts, dialogue, captions, exercises and layout pressure.

## Gate 11: Legal/compliance isolation
Legal/privacy/regulatory content must not be creatively transcreated. Verify meaning against source and use appropriate legal/compliance review.

## Gate 12: Final bilingual review
Reviewer sees SOURCE + FINAL PL + immutable facts + content type. Reviewer does not rewrite the whole piece. It returns targeted defects and PASS/FIX/BLOCK.

## Recommended scored diagnostics (not publication verdict)
Use these only to locate weak areas:
- semantic fidelity: 0-5
- native naturalness: 0-5
- voice fit: 0-5
- cultural fit: 0-5
- audience fit: 0-5
- logic/continuity: 0-5
- polish correctness: 0-5

Any semantic fidelity below 5 requires correction before publication. Final publication state is categorical PASS/FIX/BLOCK, not an averaged score.
