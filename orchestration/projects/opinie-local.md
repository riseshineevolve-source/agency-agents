# Opinie — Local-Only Agentization Plan

Status: ACTIVE PREPARATION / CONFIDENTIAL / LOCAL-ONLY

## Privacy boundary

Authoritative working root:
`C:\Users\danie\AI_LOCAL\opinie`

Confidential case files, historical opinions/archive, indexes, embeddings, calculations and analyses must remain local/offline on Windows.

This remote file contains orchestration metadata only. It must never receive case evidence, names, source documents, extracted text, embeddings or reconstructed scenes.

## Product role

AI-assisted workbench for an expert reconstructing road accidents. It supports evidence organization, provenance, timelines, calculations, reconstruction variants and review. It is not an autonomous generator of a final expert opinion.

## First autonomous milestone

Run locally only:

1. Verify the existing CONFIDENTIAL / ONLINE path separation and network guard on the target Windows machine.
2. Read local `PROJECT_BRIEF.md` before touching implementation.
3. Build the smallest end-to-end local pipeline:
   new case -> evidence/provenance -> timeline/scene -> calculations -> reconstruction variants -> review queue -> opinion base.
4. Every derived claim must retain traceable provenance to original local evidence.
5. Calculation and reconstruction outputs require explicit uncertainty/assumption recording.
6. Human expert review remains mandatory before anything becomes opinion-ready.
7. Add deterministic local tests for path separation, provenance retention and calculation reproducibility.

## Local agent routing

- Local Orchestrator
- Evidence / Provenance Extractor
- Timeline / Scene Builder
- Calculation Checker
- Reconstruction Variant Reviewer
- Citation / Provenance QA
- Human Expert Review queue

Specialists should operate sequentially on a shared local case record rather than creating independent uncontrolled case summaries.

## Guardrails

- No confidential source data online.
- No remote embeddings or cloud vector store for case/archive content.
- No GitHub commits containing case material.
- No autonomous final opinion.
- No fabricated missing evidence or inferred measurements presented as facts.
- Preserve original source files untouched; derived artifacts must point back to originals.
- Online research, when separately approved, must use a sanitized request with no confidential case data.

## Definition of done for milestone 1

- privacy/path boundary validated on target machine,
- one synthetic or fully authorized local test case passes through the full pipeline,
- every output has provenance,
- calculations are reproducible,
- review queue clearly separates source fact, derived result, assumption and expert conclusion,
- no confidential bytes leave the local environment.
