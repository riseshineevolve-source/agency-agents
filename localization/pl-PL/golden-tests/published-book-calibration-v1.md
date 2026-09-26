# Published Book Calibration Corpus v1

## Purpose

Calibrate the RSE Polish Localization Engine on an immutable, already-published English RSE book before localizing the production website.

Source of truth: `Paperback final fixed print.pdf`, 244 pages. The English source is frozen. The localization engine adapts to the source; the source is never rewritten to make localization easier.

Primary audience: children 7–10.

Target effect: contemporary, intelligent, playful Polish that feels originally written in Poland. No baby talk, no forced youth slang, no English coaching/gaming calques, no generic AI-motivational voice.

## Calibration method

For every test unit preserve:

- SOURCE
- content type
- semantic intent
- immutable facts/instructions
- constraints
- draft PL
- transcreation/localization decisions
- QA defects
- accepted PL
- reusable engine lesson

Run CORE-first and specialists only when required by content type. Re-run the same corpus after every engine patch. A patch passes only when it fixes the target weakness without degrading previously accepted samples.

## Golden Test 01 — Dedication / brand voice / gaming humor

**PDF:** page 3

**Content type:** dedication + brand voice + humor + gaming references

**Semantic intent:** Make the child feel capable, seen and in charge. Build a playful alliance between child and grown-up without sounding childish or motivationally generic. Gaming/space imagery should feel natural to Polish children rather than translated.

**Immutable facts/functions:**
- child is Captain/Hero/Legend-in-training
- rainy afternoon can become an imaginary rocket launch
- sharing is framed as co-op / Player 2
- kindness can be brave when life feels like Expert Mode
- grown-ups are Ground Control / hold the map; child holds controller
- book can be a secret base, daily giggle, reminder
- LEGO and Grumpy Monster before breakfast joke
- closing encouragement

**Primary risks:** literal `Legenda w trakcie szkolenia`; stiff `misja kooperacyjna`; translated `Tryb Eksperta`; generic `dasz radę`; over-capitalization; babyish tone.

**Acceptance:** Polish should read aloud smoothly, land at least two jokes naturally, and retain the child-as-agent framing.

## Golden Test 02 — Introduction / core product promise

**PDF:** page 5

**Content type:** introduction + educational marketing + brand voice

**Semantic intent:** Welcome the child into the Happy-Makers world, normalize big feelings, make the book feel useful and adventurous rather than therapeutic or school-like.

**Immutable facts/functions:**
- adventures need not happen only in movies/through hidden portals
- everyday life can feel legendary
- strengths are already inside the child
- worry and big feelings can make growing up chaotic
- book is a Survival Kit / power-up style guide to understanding self/world
- confidence, calm and ordinary-to-spectacular transformation
- child is Captain; Happy-Makers are co-pilots

**Primary risks:** therapy-speak; coaching clichés; literal `odblokuj wewnętrzną siłę`; excessive English gaming vocabulary; grandiose marketing.

**Acceptance:** energetic and reassuring, but concrete and believable for 7–10-year-olds.

## Golden Test 03 — No-Stress Manual / recurring UI-like labels

**PDF:** pages 7–8

**Content type:** instructions + recurring labels + microcopy

**Semantic intent:** Explain the book structure simply and lower performance pressure.

**Immutable labels/functions to solve consistently:**
- Survival Kit
- Mission
- Secret Hack
- Mini-Mission
- The Gentle Why
- Your Turn to Create
- Gentle Step
- Pause & Breathe
- Play Zone
- No-Stress Manual

**Immutable facts/instructions:**
- not school homework
- no wrong answers
- words/doodles/stickers/comics are allowed
- five missions correspond to weeks
- no rush
- daily mission max 10 minutes

**Primary risks:** inconsistent recurring terminology; overly literal labels; imported English capitalization; school/therapy register.

**Acceptance:** labels must be short enough for designed pages, memorable, natural and reusable across the whole edition.

## Golden Test 04 — Day 1 Family Anchors / sensory instructions

**PDF:** pages 21–24

**Content type:** educational + activity instructions + calming exercise

**Semantic intent:** Use familiar sensory details of home to create a feeling of safety and grounding, then convert that idea into a concrete child-friendly activity.

**Immutable facts/instructions:**
- identify favorite smells, sounds and safe places
- home is more than walls
- create a Cozy Map using smell/sound/taste plus favorite cozy spot
- sit in favorite cozy spot for 1–3 minutes
- three deep breaths on pause page
- marker bleed-through joke/function: `Secret Shield: This page blocks marker spots!`

**Primary risks:** unnatural Polish equivalents for `grounded`, `anchor`, `cozy`; overly therapeutic claims; awkward sensory instructions; loss of print-page joke.

**Acceptance:** child can perform the activity without adult interpretation; emotional language stays gentle, not clinical.

## Golden Test 05 — Day 4 Gratitude + humor

**PDF:** pages 40–43

**Content type:** activity instructions + metaphor + short calming copy + factual humor + completion microcopy

**Semantic intent:** Turn gratitude into a playful concrete ritual without sounding preachy, then switch naturally into absurd/factual humor.

**Immutable facts/instructions:**
- four-petal flower
- thanks for favorite food, person, safe place, enjoyable activity
- small gratitude symbol such as button or stone in pocket
- touch it and think of one grateful thing
- Gray Glasses metaphor and imaginary Gratitude Button
- octopuses have three hearts
- cardio-workout joke
- mission completion / color the star

**Primary risks:** moralizing gratitude language; literal `Szare Okulary` that sounds accidental rather than coined; adult mindfulness tone; unfunny direct translation of cardio joke.

**Acceptance:** instructions are immediately understandable; coined metaphors sound intentional; humor lands without changing the factual statement.

## Regression rule

After a Polish version of any test becomes ACCEPTED, preserve it as a regression fixture. Future engine changes must be compared against all accepted fixtures. Do not accept a local improvement that causes broader voice, meaning, terminology or audience-fit regression.

## Promotion gate

Do not translate all 244 pages yet. First reach stable PASS across these five units after at least one deliberate engine-feedback cycle. Then expand the regression corpus to cover dialogue, longer educational passages, puzzles/riddles, emotionally sensitive sections, character-specific voices, repeated calls-to-action and dense activity pages before full-book production.