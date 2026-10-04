# Detective PL execution checkpoint

Status: **INFRASTRUCTURE READY / FULL-BOOK TRANSLATION OWNER-FROZEN**.
No 141-page book translation was started by the hardening sprint. Existing
English source, puzzle truth, approved Polish calibration and publication gates
remain authoritative. This checkpoint replaces discovery with explicit inputs
and commands; semantic annotation, translation and real-layout QA remain actual
production work after the freeze.

## Canonical English input and freeze

Expected Book Factory location:
`C:/Users/danie/GitHub/detective-academy/tools/detective-book-factory/`.
Durable composition entry: `content/book1_en_master.yml`; it composes
`content/book1_en_phase1.yml`, `book1_en_phase2.yml`, `book1_en_phase3.yml` and
`book1_story_spine.yml` through `scripts/build_book1_master.py`. The normal
composed output is `dist/book1_en_master.yml`. Use the **owner-frozen final
snapshot**, including its final 15 spatial assets, rather than assuming that a
local intermediate with the same filename is the frozen 141-page edition.

After the owner says **FREEZE EN INTERIOR**, record the actual owner message,
source commit, frozen composed file SHA-256, ALL-15 PASS evidence, and frozen
runtime alias snapshot in a private copy of
[detective-freeze.example.json](engine/detective-freeze.example.json). Its default
PENDING fields deliberately fail. `source_sha256` hashes raw file bytes;
`aliases_sha256` hashes canonical parsed JSON with `localization.io.digest`.
Receipt fields are provenance assertions, not an alternate authorization channel.

If composition is needed after freeze, run the existing Book Factory builder in
that project with the owner-frozen spatial asset manifest:

```sh
python scripts/build_book1_master.py --spatial-assets PRIVATE_FROZEN_SPATIAL_ASSETS.json --output PRIVATE_FROZEN_MASTER.yml
```

Do not run this against an evolving master or change the phase sources. The
runtime alias input has the existing renderer's `cases[].id` and
`cases[].characters[].source_name/display_name` shape. Keep private source and
runtime files outside this public repository's tracked files.

## Immediate production sequence

From the agency-agents root (use the verified Python environment with PyYAML):

```sh
python scripts/localization-engine.py detective-prepare --source PRIVATE_FROZEN_MASTER.yml --freeze PRIVATE_FREEZE_RECEIPT.json --aliases PRIVATE_FROZEN_RUNTIME.json --output build/detective-pl/source-plan.json
```

This command checks the freeze receipt, exact source bytes, alias snapshot and
30-mission sequence. It classifies the known current Book Factory schema,
preserves answer/code/coordinate/character IDs, derives stable `HMDA.Mxx.*` and
`HMDA.SYSTEM.*` IDs, and writes a logic-annotation queue without creating target
prose. Interlude IDs use the stable `AFTERxx` case reference. Unknown fields block
instead of disappearing. List ordinals are frozen source ordering, not page
numbers; if a source list changes, deliberately migrate its IDs.

1. Annotate source propositions for the logic queue, carrying identity, row,
   column, room/zone, count, negation, adjacency, direction, order, answer and
   callback atoms. Record narrow bilingual lexical anchors in the bounded
   production batch. A copied atom list is never bilingual semantic approval.
2. Add measured fit budgets from the frozen renderer to the generated plan.
   Preserve existing body typography. Use the established F0–F5 classes from
   [the segmentation contract](DETECTIVE_ACADEMY_SEGMENTATION_CONTRACT.md) and
   their corresponding engine surface types. Missing measurements remain review
   items, not guessed PASS values.
3. Keep raw source names and answer IDs untouched. Case-scoped
   `identity_mappings` come from the frozen alias runtime. Add only the approved
   unambiguous declensions from the canonical identity catalog (e.g. the existing
   Nova forms); do not transliterate aliases or invent new name variants.
4. Extract the annotated plan; missing logic atoms fail closed:

```sh
python scripts/localization-engine.py extract --source PRIVATE_FROZEN_MASTER.yml --plan build/detective-pl/source-plan.json --revision FROZEN_SOURCE_COMMIT --output build/detective-pl
python scripts/test-localization-fixtures.py
python scripts/localization-engine.py tm-reuse --manifest build/detective-pl/source-manifest.json --targets build/detective-pl/targets.pl-PL.json --memory build/localization-proof/approved-memory.json --output build/detective-pl/reused.pl-PL.json
```

Memory keys are product + stable ID. Calibration IDs do not silently become real
mission approvals. Unchanged production IDs can reuse their own approved memory;
terminology applies to new IDs separately. Translate only mission-complete bounded
batches, with existing calibration as evidence of voice. Keep spoiler-sensitive
notes internal. Review actual source/target meaning, natural Polish and logic,
then record hash-bound language QA on each approved segment.

5. Build the reviewable Polish source package:

```sh
python scripts/localization-engine.py qa --manifest build/detective-pl/source-manifest.json --targets build/detective-pl/targets.pl-PL.json --current-source PRIVATE_FROZEN_MASTER.yml --output build/detective-pl/qa.json
python scripts/localization-engine.py export --manifest build/detective-pl/source-manifest.json --targets build/detective-pl/targets.pl-PL.json --current-source PRIVATE_FROZEN_MASTER.yml --output build/detective-pl/candidate-package.json --payload-output build/detective-pl/book1_pl_candidate.yml
```

The package retains source/target pairs and fit/semantic risks; YAML payload
restores integer source keys rather than coercing answer dictionaries. No English
source file is overwritten. Candidate export is blocked on deterministic errors.
For bounded production, split the source plan into complete missions and record
other paths as excluded with a reason; do not claim a partial batch as full-book
coverage. Full-book export needs targets for the entire intended scope.

6. Feed the candidate to the existing Book Factory rendering pipeline. Validate
   all 15 spatial cases against unchanged solution truth, inspect Polish paired
   pages at print scale, check the book-long callback/voice sequence, run bilingual
   QA and KDP preflight. Engine regex gates are not a spatial solver. Existing
   English renderer literals and asset labels must be explicitly included in the
   production scope when the frozen surface is materialized; protected IDs are
   never translated to make a page appear localized.

## Regression and remaining gates

```sh
python scripts/localization-engine.py terms-doc --check
python scripts/test-localization-engine.py
python scripts/test-localization-fixtures.py
```

Canonical terminology: [engine/terminology.json](engine/terminology.json).
No second Detective glossary is maintained. The five original Detective anchor
groups remain enforced alongside the general invariant checks. Provisional ranks,
Room Zero surface wording and all unmeasured designed surfaces keep their gates.

Blocking inputs now: actual owner EN freeze, its final source/hash and alias
snapshot. After that, the planned production work is source logic annotation,
bounded translation, language review, real PDF fit and print preflight. KDP
publication, cover, pricing and physical-proof decisions retain their owner gates.
