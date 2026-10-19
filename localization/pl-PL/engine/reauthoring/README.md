# Native Polish re-authoring engine

This lane is for creative products where English is a **reference for function/truth**, not sentence wording.

It is intentionally separate from ordinary translation/transcreation.

## Core invariant

The native Polish first writer must not receive sentence-level English source copy.

Machine-enforced value:

`native_writer_source_visibility = functional_brief_only`

## Pipeline

1. Capture the English source bytes/revision.
2. Localization Source Function Analyst creates a wording-free functional brief.
3. Engine validates the brief and creates the writer packet.
4. Polish Native Family Writer creates Polish from that packet only.
5. Polish Cultural Localizer checks real Polish context.
6. Polish Transcreator handles humor and character voice.
7. Polish Family Ear Reviewer runs the parent/child anti-cringe ear test without English.
8. Polish Natural Language Editor removes coaching, therapy-speak and translationese.
9. Only now is English reopened for Meaning Guardian / Bilingual QA.
10. Logic, proof and exact surface QA follow.
11. Final machine gate stops at unresolved product owner decisions.

## Commands

### 1. Start a run

```sh
python scripts/localization-engine.py reauthor-init \
  --source ORIGINAL_EN_FILE \
  --profile localization/pl-PL/engine/reauthoring/gentle-steps.json \
  --revision SOURCE_REVISION \
  --output build/reauthor/run.json
```

The source can be any stable file whose bytes can be hashed, including a PDF. The engine does not pretend to semantically parse a binary PDF; the Source Function Analyst performs the semantic extraction.

### 2. Validate the functional brief and generate the blind writer packet

```sh
python scripts/localization-engine.py reauthor-writer-packet \
  --run build/reauthor/run.json \
  --profile localization/pl-PL/engine/reauthoring/gentle-steps.json \
  --brief build/reauthor/functional-brief.json \
  --output build/reauthor/writer-packet.json
```

The brief must contain function, mechanics, immutable facts, character roles, safety/claim boundaries and source locators, but **no copied source sentence, excerpt, literal translation or Polish draft**.

The generated writer packet drops source locators as well.

### 3. Native Polish first-write

Polish Native Family Writer receives only:
- the writer packet;
- voice/character profile;
- approved product context.

Candidate format: `rse-native-pl-candidate-v1`.

It must attest:

`authoring_basis = functional_brief_only`

### 4. Re-open English for fidelity only after Polish exists

```sh
python scripts/localization-engine.py reauthor-backcheck-packet \
  --run build/reauthor/run.json \
  --profile localization/pl-PL/engine/reauthoring/gentle-steps.json \
  --brief build/reauthor/functional-brief.json \
  --writer-packet build/reauthor/writer-packet.json \
  --candidate build/reauthor/candidate.json \
  --output build/reauthor/backcheck-packet.json
```

This packet gives the bilingual reviewer the English source provenance/locator and the already-authored Polish candidate. Reviewers verify truth; they must not pull Polish style back toward English.

### 5. Final gate

After all required independent stages record review receipts for the exact candidate hash:

```sh
python scripts/localization-engine.py reauthor-final-gate \
  --run build/reauthor/run.json \
  --profile localization/pl-PL/engine/reauthoring/gentle-steps.json \
  --writer-packet build/reauthor/writer-packet.json \
  --candidate build/reauthor/candidate.json \
  --reviews build/reauthor/reviews.json \
  --output build/reauthor/final-gate.json
```

Possible status:
- `BLOCK`: a required independent review failed or is missing;
- `READY_FOR_OWNER_GATE`: quality reviews pass, but product-specific owner decisions remain;
- `PASS`: required reviews and all owner gates are approved for the exact candidate hash.

## Why this is safer than “translate, then improve”

A first draft anchored to English wording tends to keep the same metaphors, rhetoric and sentence architecture even after several editing passes.

This engine changes the information flow itself:
- one role sees English and extracts function;
- the Polish author sees function but not wording;
- Polish-only editors judge credibility on its own terms;
- bilingual review happens later and is limited to truth/fidelity.

That makes “written in Polish first” an execution constraint rather than a style aspiration.
