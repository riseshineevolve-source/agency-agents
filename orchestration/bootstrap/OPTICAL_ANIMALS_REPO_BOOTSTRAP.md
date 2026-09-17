# Optical Animals Repo Bootstrap

Target repository: `riseshineevolve-source/optical-animals-book-creator`
Status: pending repository creation

## Repository purpose
Code and manifests for curation, assembly, replacement, QA and KDP export of the Optical Animals book. Approved source artwork may be stored only when repository size/licensing/workflow makes that appropriate; otherwise keep artwork external and track it by stable manifest references.

## Required initial structure

```text
/
  PROJECT_BRIEF.md
  AGENTS.md
  CHECKPOINT.yml
  README.md
  pyproject.toml or requirements.txt
  src/
    optical_animals/
      manifest.py
      validation.py
      assembly.py
      preflight.py
  manifests/
    illustrations.yml
  tests/
    test_manifest.py
    test_roster.py
    test_preflight.py
  docs/
    STYLE_LOCK.md
    KDP_SPEC.md
  .github/workflows/
    quality.yml
```

## Initial automation goals

1. Validate exactly one canonical record per candidate illustration.
2. Enforce statuses: `READY`, `SMALL_FIX`, `REDO`, `HOLD`, `FINAL`.
3. Detect duplicate species in final roster.
4. Block final export unless exactly 20 unique final animals are owner-approved.
5. Preserve stable IDs so swapping one illustration never changes unrelated page identities.
6. Assemble book from manifest order.
7. Run deterministic KDP preflight on trim size, page count, image resolution and missing assets.
8. Produce derived preview/PDF artifacts without changing source artwork.

## Owner gates
- final 20 roster,
- replacement of an already-approved masterpiece,
- major style-lock change,
- final KDP publication.

## First implementation package
Once repository exists:
- copy current local code without restructuring for aesthetics,
- add PROJECT_BRIEF/AGENTS/CHECKPOINT,
- inventory current scripts and assets,
- create canonical `illustrations.yml`,
- wrap existing assembly behavior in tests before changing it,
- then automate curation/preflight incrementally.

## Codex budget rule
Do not use Codex to visually re-evaluate every image repeatedly. Use deterministic manifest/preflight work in code; use visual specialists only for candidates explicitly flagged SMALL_FIX/REDO or at the final roster gate.
