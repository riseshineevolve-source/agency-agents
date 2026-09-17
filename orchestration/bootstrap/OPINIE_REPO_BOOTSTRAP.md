# Opinie Repo Bootstrap

Target repository: `riseshineevolve-source/opinie-offline-workbench`
Status: pending repository creation

## Repository purpose
Develop and verify the full application online using only code, documentation and synthetic fixtures. The production product is distributed for local/offline use. Real case files, historical expert opinions, embeddings, indexes, calculations and generated case outputs never belong in GitHub.

## Privacy architecture

### GitHub / CI MAY contain
- application source code,
- schemas,
- local storage/index interfaces,
- deterministic calculation engine,
- provenance model,
- synthetic accident cases,
- fake PDFs/text fixtures,
- tests and benchmarks,
- packaging scripts,
- offline installer/release pipeline,
- documentation.

### GitHub / CI MUST NOT contain
- real names, plates, addresses or identifiers,
- real police/court/insurance files,
- scans/photos from real cases,
- extracted text from real evidence,
- real historical opinion archive,
- embeddings or vector indexes derived from real files,
- real generated analyses/opinions.

## Required initial structure

```text
/
  PROJECT_BRIEF.md
  AGENTS.md
  CHECKPOINT.yml
  README.md
  PRIVACY_ARCHITECTURE.md
  pyproject.toml
  src/
    opinie/
      ingest/
      provenance/
      timeline/
      scene/
      calculations/
      reconstruction/
      review/
      export/
      local_runtime/
  tests/
    fixtures/synthetic/
    test_offline_guard.py
    test_provenance.py
    test_calculations.py
    test_pipeline.py
  scripts/
    package_windows.*
  .github/workflows/
    quality.yml
    synthetic-e2e.yml
```

## Offline-by-design requirements

1. Production runtime starts with network disabled by policy/default.
2. No telemetry, analytics, remote crash upload or cloud sync by default.
3. Real workspace path is configurable locally and ignored by version control.
4. Source originals are immutable; derived artifacts point back to source IDs/hashes.
5. Every derived factual statement can expose provenance.
6. Calculations record inputs, units, method, assumptions and uncertainty.
7. Reconstruction variants remain distinguishable from source facts.
8. Final expert conclusion always requires human review.
9. Packaging creates a self-contained local application where practical.
10. Any future optional online research connector must be separately enabled and must receive sanitized queries only.

## Synthetic CI pipeline

Use deliberately fake cases to exercise:
`ingest -> provenance -> timeline -> calculations -> reconstruction variants -> review queue -> draft/export base`

The synthetic suite should intentionally include conflicting evidence, missing values and uncertain measurements so the system is tested for restraint rather than fluent guessing.

## Distribution model

Preferred end state:
- tagged GitHub release produces installer/package,
- user downloads and installs locally,
- real case workspace lives outside application/repository directory,
- updates may be downloaded separately, but case processing remains local,
- optional fully air-gapped install remains possible.

## Owner gates
- any cloud processing of real data,
- legal/compliance positioning,
- final opinion/export semantics,
- external research integration,
- production release to real experts.

## First implementation package
Once repository exists:
- migrate current tool code,
- remove any accidental real data before first push,
- add `.gitignore` deny patterns and offline guard tests,
- add synthetic fixture corpus,
- establish the minimal end-to-end pipeline,
- package a local developer build,
- only then improve UX and specialist modules.
