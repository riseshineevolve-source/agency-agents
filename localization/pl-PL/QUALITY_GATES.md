# RSE Polish Localization Quality Gates

Final status is PASS, FIX or BLOCK.

## Gate 1: Completeness
PASS when every source segment that should be localized has a mapped target segment, with intentional exclusions documented.

## Gate 2: Meaning fidelity
Check facts, numbers, instructions, product claims, chronology, relationships, negation, modality and causal logic. Any invented or lost fact is BLOCK until corrected.

For wellbeing, educational and emotional-support copy, claim strength is part of meaning fidelity. A source that says `can`, `may`, `helps`, `can make it easier` or otherwise expresses uncertainty must not become a guaranteed outcome in Polish. Any materially strengthened promise is FIX or BLOCK depending on risk.

## Gate 3: Natural Polish
Text must sound natively authored. Translationese, literal English syntax, unnatural collocations or synthetic marketing language are FIX.

For direct child address, mechanical gender workarounds are also FIX. Final prose must not use slash forms, parenthetical gender endings or forms such as `Kapitan(a)`. Restructure naturally so the line works without forcing gender marking.

## Gate 4: Cultural fit
References, jokes and examples must make sense to the intended Polish audience. Adapt only when needed. Avoid decorative 'Polishness' and stereotypes.

Coined English terms may be recreated rather than copied literally. The Polish result must look intentionally designed in context. If an invented term reads like an accidental mistranslation, mark FIX.

## Gate 5: Voice
Brand and character voices remain stable. For recurring characters, compare against approved voice profiles and previous accepted segments.

Recurring branded headings, character catchphrases and character-specific labels must be checked against the project glossary. Do not accept a clever one-off rendering that breaks recurrence later.

## Gate 6: Humor function
For humor/puns, compare effect rather than wording. Mark PASS when the Polish version performs the same narrative/emotional job, even with different imagery.

## Gate 7: Audience fit
Check reading level, emotional maturity and register for children, teens, parents/adults or specialists. Children's copy must not become baby talk; teen copy must not chase slang.

For children 7-10, read difficult lines aloud. If the child-facing Polish needs adult interpretation, adult coaching vocabulary or grammatical gymnastics to function, mark FIX.

## Gate 8: Logic and continuity
Check referents, transitions, callbacks, names, chronology, terminology and repeated motifs.

Recurring labels and in-world terms must remain stable after acceptance. Accepted glossary terms are regression-locked unless a deliberate glossary change is approved and all affected occurrences are migrated together.

## Gate 9: Language and typography
Check Polish grammar, spelling, punctuation, inflection, quotation marks, dates, number formats and typographic consistency.

For intentionally coined terms, typography may carry meaning. Verify that capitalization, quotation marks or display treatment make the invention look deliberate and remain consistent across occurrences.

## Gate 10: Surface constraints
For UI/web: length, button fit, pluralization, responsive layout, labels, accessibility text, alt text and metadata.
For books/PDF: page mapping, headings, callouts, dialogue, captions, exercises and layout pressure.

Designed-surface microcopy must be validated on its target surface or against an explicit length budget. Check wrapping, hierarchy, scan speed and Polish expansion. A semantically good translation that breaks the intended surface is FIX.

Recurring labels require both a language pass and a surface pass before they can become glossary-locked.

## Gate 11: Legal/compliance isolation
Legal/privacy/regulatory content must not be creatively transcreated. Verify meaning against source and use appropriate legal/compliance review.

## Gate 12: Final bilingual review
Reviewer sees SOURCE + FINAL PL + immutable facts + content type. Reviewer does not rewrite the whole piece. It returns targeted defects and PASS/FIX/BLOCK.

For child-facing books/apps, final bilingual review must explicitly verify:
- no mechanical gender notation in final prose
- no strengthened wellbeing or educational claims
- recurring labels match the accepted glossary
- coined terms look intentional in Polish
- recurring character labels match the character glossary
- designed labels fit their intended surface or documented length budget

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

## Regression rule for accepted calibration fixtures
Once a golden fixture reaches PASS and its recurring terminology is accepted, later engine changes must not degrade it. Re-run accepted fixtures after any material change to style rules, terminology, transcreation routing or QA gates. A new variant that is merely different is not automatically better.
