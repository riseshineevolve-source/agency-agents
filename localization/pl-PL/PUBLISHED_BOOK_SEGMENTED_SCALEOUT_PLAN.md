# RSE Polish Localization — Published Book Segmented Scale-Out Plan

Status: READY FOR OWNER SCALE-OUT GATE  
Date: 2026-09-18  
Source: frozen published 244-page `Paperback final fixed print.pdf`  
Target locale: pl-PL  
Primary audience: children 7–10

## Current evidence

The Polish Localization Engine has passed the controlled calibration ladder:

1. Round 2 accepted regression fixtures.
2. Round 3 generalization tranche, followed by direct bilingual/naturalness/surface review.
3. Complete unseen Day 11 end-to-end pilot.
4. Bounded multi-day batch: Days 05, 20 and 25.
5. Deterministic accepted-fixture regression scan for gendered direct address and locked terminology.

Full one-pass generation remains prohibited.

## Scale-out principle

Translate the remaining published book in bounded complete-day units. Do not split one mission across independent agents or batches.

Every batch follows:

`source pages -> semantic facts -> final PL -> bilingual QA -> regression validator -> checkpoint`

A failed gate stops the next batch.

## Proposed production stages

### Stage S1 — first expansion batch

Size: maximum 4 complete unseen days.

Selection must cover different content risks, prioritizing:
- emotional/wellbeing language,
- instruction-heavy activity,
- dialogue/character voice,
- wordplay or compact designed surfaces.

Requirements:
- every day reviewed against the actual English master,
- no OCR guesswork where text is uncertain,
- any unclear source line is resolved from page image before translation,
- run `python scripts/validate-polish-localization.py`,
- update the accepted regression set only after PASS.

### Stage S2 — stability batch

Size: maximum 6 additional complete days.

Start only if S1 produces:
- no meaning-fidelity BLOCK,
- no recurring terminology drift,
- no repeated gendered-address defect class,
- no repeated designed-surface overflow class,
- no strengthened emotional/wellbeing claim pattern.

If a defect pattern repeats twice, patch the Engine before continuing.

### Stage S3 — segmented production

Translate the remainder in batches of maximum 5 complete days.

Each batch gets:
- source page range,
- immutable facts,
- final Polish,
- QA defects/fixes,
- status PASS/FIX/BLOCK,
- regression check,
- durable GitHub checkpoint.

Do not silently accumulate fixes for the end.

### Stage S4 — whole-book consistency pass

After all day blocks exist:
- terminology recurrence scan,
- character voice consistency,
- titles/headings consistency,
- gender-neutral direct-address scan,
- repeated joke/catchphrase consistency,
- claim-strength audit,
- Polish typography/punctuation pass,
- designed-surface length inventory.

No creative rewriting of the English source during this stage.

### Stage S5 — layout / typesetting integration

Only after text consistency PASS:
- place Polish text into actual designed surfaces,
- inspect wrapping and hierarchy,
- shorten only by native functional localization,
- re-run bilingual QA on any line changed for fit,
- keep character epithets / compact labels provisional until actual layout PASS.

### Stage S6 — final publication gate

Publication/export/store/KDP upload is OWNER GATE.

Required before publication:
- full bilingual QA,
- print/PDF preflight,
- no unresolved FIX/BLOCK,
- final owner visual/layout approval,
- final title/cover choices approved separately.

## Automation

Regression validator:
`scripts/validate-polish-localization.py`

CI workflow:
`.github/workflows/polish-localization-regression.yml`

The validator currently covers the accepted calibration/pilot corpus. When a new production batch reaches PASS, add it to the accepted regression set in the validator in the same commit/checkpoint.

## Stop conditions

Stop batch expansion immediately if:
- source/master identity becomes uncertain,
- source line cannot be recovered reliably,
- a recurring term conflicts with the glossary,
- a wellbeing/educational claim becomes materially stronger,
- character voices collapse into generic narration,
- designed Polish cannot fit without changing meaning,
- a batch repeatedly introduces gendered child address,
- owner-gated title/cover/brand decision is required.

## Current decision gate

The Engine is ready for segmented book production, but `full_book_scaleup_authorized` remains false.

Owner decision required before S1 is treated as the start of the full 244-page Polish production run.

The calibration fixtures and bounded pilots may continue to be maintained and regression-tested without that authorization.
