# Polish Localization — native re-authoring engine checkpoint

Date: 2026-09-30  
Status: **ENGINE + AGENT ROUTING IMPLEMENTED / CI PENDING ON FINAL HEAD / NO MAIN MERGE**

## Owner problem being solved

For creative family products such as Gentle Steps, a good Polish edition must not be produced by translating English sentences and then polishing them.

The required model is:

**English source truth → wording-free functional brief → blind native Polish first-write → Polish-only culture/humor/ear/edit passes → late bilingual fidelity backcheck → logic/proof/surface QA → owner gates.**

English remains authoritative for function, mechanics, facts, character continuity, safety, consent and claim strength. It is not sentence-level wording authority for the Polish first draft.

## Machine implementation

New module:
`scripts/localization/reauthoring.py`

New CLI:
- `reauthor-init`
- `reauthor-writer-packet`
- `reauthor-backcheck-packet`
- `reauthor-final-gate`

Gentle Steps machine profile:
`localization/pl-PL/engine/reauthoring/gentle-steps.json`

Documentation:
`localization/pl-PL/engine/reauthoring/README.md`

### Enforced source isolation

The native writer contract is:

`native_writer_source_visibility = functional_brief_only`

A functional brief is rejected if it leaks sentence-level source or target copy through fields such as:
- `source_text`
- `source_sentence`
- `source_paragraph`
- `source_excerpt`
- `english_copy`
- `literal_translation`
- `draft_pl`
- `target_text`

The generated native-writer packet does not include the source locator either. It contains only function, mechanics, immutable facts, character/safety constraints, tone job and optional cultural/humor/recurrence context.

English source provenance is reintroduced only in the **backcheck packet**, after a native Polish candidate exists.

### Final gate

Every independent review receipt is bound to the exact candidate hash.

The machine returns:
- `BLOCK` if required review stages fail/miss;
- `READY_FOR_OWNER_GATE` when quality stages pass but product decisions remain;
- `PASS` only when required review stages and all owner gates are approved for the exact candidate hash.

## Agent routing

New specialist roles:
- `Localization Source Function Analyst`
- `Polish Native Family Writer`
- `Polish Family Ear Reviewer`

They are registered in `rse/agents-specialists.txt`.

Existing specialists are reused deliberately:
- Polish Cultural Localizer
- Polish Transcreator
- Polish Natural Language Editor
- Localization Meaning Guardian
- Bilingual Localization QA
- Polish Logic Editor
- Polish Proofreader

`specialized/rse-localization-orchestrator.md` now routes re-authoring through this sequence and explicitly bypasses the ordinary Semantic Translator before the native first-write.

`strategy/runbooks/scenario-polish-localization.md` now has two explicit routes:
A. controlled localization/transcreation;
B. native re-authoring from function.

## Gentle Steps source truth

`orchestration/content-sources/24-gentle-steps-to-christmas.yml` now records:
- mode: `native_reauthor_from_function`;
- branch: `codex/polish-engine-main-reconcile`;
- PR: 13;
- historical PL calibration authority: `reference_only`;
- state: `reauthoring_pipeline_ready`;
- first production calibration scope: `days_1_to_3`.

The current owner direction remains:
`localization/pl-PL/GENTLE_STEPS_PL_REAUTHORING_PROFILE.md`.

## CI coverage

New contract test:
`scripts/test-localization-reauthoring.py`

It verifies:
- native writer sees no sentence-level English;
- functional briefs with source/translation leaks fail closed;
- candidate must attest `functional_brief_only` and preserve exact unit IDs;
- English source provenance returns only at late backcheck;
- final gate requires all independent reviews;
- all product owner gates remain explicit.

The Polish Localization Regression workflow now executes this test.

## Product gate

This infrastructure does **not** approve current Polish Gentle Steps copy.

The next production calibration is intentionally bounded to **Days 1–3**, authored from scratch through this pipeline. Scaling to Days 4–24 should occur only after the owner confirms that the first three days sound like a real contemporary Polish family product.

Current recurring labels and Polish title remain provisional/owner-gated.

## Non-actions

This implementation did not:
- change central RSE priorities;
- merge PR #13 into main;
- approve historical Gentle Steps copy;
- create a Polish title decision;
- authorize full-book PL scaleout;
- weaken safety/fidelity requirements.
