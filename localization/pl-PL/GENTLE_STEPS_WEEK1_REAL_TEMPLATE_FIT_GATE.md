# 24 Gentle Steps to Christmas — Week 1 real-template fit gate

Status: **REFERENCE-ONLY GEOMETRY GATE — CANNOT APPROVE PRODUCTION COPY**  
Updated: 2026-09-30  
Source of truth for voice/workflow: [GENTLE_STEPS_PL_REAUTHORING_PROFILE.md](GENTLE_STEPS_PL_REAUTHORING_PROFILE.md)  
Historical source layout: published English paperback, 104 pages

## Why this changed

The owner has explicitly directed that the Polish Gentle Steps product be re-authored from function as native contemporary Polish, not produced as a close translation/transcreation of English sentences.

Therefore the previous Week 1 Polish headings and calibration prose are preserved as **historical localization and layout evidence only**. They are no longer production-approved language candidates.

This gate may still validate the real template, page mapping, renderer, typography and Polish diacritic handling. It may not promote the old copy into production.

## Historical mapping retained for geometry evidence

| Source PDF page | Source heading surface | Historical PL calibration | Historical safe line break |
|---|---|---|---|
| 25 | `Fun Spark - Family Sound Symphony` | `ISKRA ZABAWY — RODZINNA SYMFONIA DŹWIĘKÓW` | `ISKRA ZABAWY — RODZINNA SYMFONIA` / `DŹWIĘKÓW` |
| 26 | `Family Connection - What I Love About Being Us` | `CHWILA BLISKOŚCI — CO LUBIĘ W NASZEJ RODZINIE` | `CHWILA BLISKOŚCI —` / `CO LUBIĘ W NASZEJ RODZINIE` |
| 35 | `Family Connection - The Sound I Love at Home` | `CHWILA BLISKOŚCI — MÓJ ULUBIONY DŹWIĘK DOMU` | `CHWILA BLISKOŚCI —` / `MÓJ ULUBIONY DŹWIĘK DOMU` |
| 38 | `Family Connection - A Word of Calm` | `CHWILA BLISKOŚCI — SŁOWO NA SPOKÓJ` | one line first; otherwise `CHWILA BLISKOŚCI —` / `SŁOWO NA SPOKÓJ` |

These strings are deliberately retained so old render evidence remains reproducible. Their presence here is **not** a language approval.

## Reference-only pass / fail rule

The historical geometry check is complete only when all four mapped pages are rendered on the actual editable/rendering surface and:
- no glyph is clipped;
- no heading collides with body copy, character note or decoration;
- body-copy font size and leading are unchanged;
- Polish diacritics render correctly at print size;
- tracking remains visually acceptable;
- the render and template are bound to hashes and reviewer evidence.

If all checks succeed, the machine result is **REFERENCE_PASS**, never production `PASS`.

Any clipping, collision, stale heading, proxy surface, missing artifact, altered body typography or missing print-scale review is **BLOCK**.

## Production fit remains open

Production Polish fit can close only after:
1. a new native Polish candidate is created under the re-authoring profile;
2. owner-gated title/recurring-label decisions needed for that candidate are resolved;
3. the exact candidate text is bound to a new fit spec;
4. the real production template renders that exact text;
5. readability is preserved without shrinking body text;
6. final Polish proof receives visual/editorial approval.

No historical Week 1 render can substitute for this sequence.

## Executable historical geometry contract

The retained reference strings and mappings live in [engine/gentle-steps-fit.json](engine/gentle-steps-fit.json), now marked `copy_authority: REFERENCE_ONLY`.

Generate the historical render request with:

```sh
python scripts/localization-engine.py fit-request --output build/gentle-fit/reference-request.json
```

After genuine renderer and print-scale evidence exists:

```sh
python scripts/localization-engine.py fit-proof --evidence REAL_EVIDENCE_DIR/evidence.json --output build/gentle-fit/reference-result.json
```

A clean historical proof returns `REFERENCE_PASS` and a non-zero CLI exit status by design, so automation cannot mistake it for production approval.

## Current owner gate

There is no owner gate for preserving this evidence. The next real language gates are the final Polish title, materially voice-defining recurring labels, unresolved editorial/safety choices and final full-proof approval.
