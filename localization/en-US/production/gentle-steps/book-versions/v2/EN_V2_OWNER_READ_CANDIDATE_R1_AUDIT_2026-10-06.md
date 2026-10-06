# Gentle Steps EN V2 — Owner-Read Candidate R1 Audit

Date: 2026-10-06  
Candidate: `GENTLE_STEPS_EN_BOOK_VERSION_02_OWNER_READ_CANDIDATE_R1_2026-10-06.md`  
Candidate blob: `ae89138636de5a2c3f88896197b301259896601c`

## Verdict

**No redesign required. Bounded completeness fixes remain.**

Reader experience, cultural fit, humor, progression and finale all PASS.

The remaining defects are mostly explicit stopping/reset rules that a premium activity book should not leave implicit.

## FIX

### EN2-F301 — D06.PLAY
Round 2 says to complete 12 steps without a mistake but does not say what to do after a mistake.
Fix: reset the step count to zero and continue.

### EN2-F302 — D11.PLAY
Group version starts another round but does not define total round count; FINale refers to "the last round".
Fix: define three rounds total, each with a different mystery-maker.

### EN2-F303 — D12.PLAY
Next chooser is defined, but there is no explicit stop condition before "last chooser".
Fix: continue until everyone who wants a turn has chosen once; then final chooser may choose harder subject.

### EN2-F304 — D14.PLAY
Each category can take up to three attempts, but the number of categories before the finale is undefined.
Fix: play two or three regular categories, then finale.

### EN2-F305 — D15.PLAY
Pair/trio setup does not state that each pair/trio selects its own leader.
Fix: in each pair/trio, the person wearing more red starts; add a simple tie fallback.

### EN2-F306 — D21.PLAY
Rotation is defined but the ordinary game has no explicit stopping condition before finale.
Fix: continue until everyone who wants a turn has answered once, then finale.

### EN2-F307 — D22.PLAY
Guesser has no time/stop condition.
Fix: allow up to 30 seconds; if not guessed, reveal prompt and move on.

### EN2-F308 — D10.PAUSE
`you may lightly rest shoulders together` is understandable but not native-premium.
Fix: `you may let your shoulders touch lightly`.

### EN2-F309 — D16.PAUSE
`first access to the bathroom` is stiff.
Fix: `first turn in the bathroom`.

## KEEP

Everything else in R1 remains protected.

No change to:
- Day 1 hero opening;
- Day 9 Plan B;
- Day 17 Only Questions;
- Day 18 Chair Mission;
- Day 23 apology;
- Day 24 finale;
- back matter;
- cultural-US/UK framework.

## Status after planned patch

Expected next state:
**R2 candidate -> fresh-eyes publish gate.**
