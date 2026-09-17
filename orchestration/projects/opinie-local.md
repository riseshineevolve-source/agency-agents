# Opinie — GitHub-Built, Offline-First Agentization Plan

Status: ACTIVE PREPARATION / CODE ONLINE, RUNTIME DATA OFFLINE

## Architecture decision

The tool itself should be developed as a normal software product with GitHub as the code source of truth, CI, tests, issues and agent-assisted development.

Target repository name:
`riseshineevolve-source/opinie-offline-workbench`

Current local prototype/root:
`C:\Users\danie\AI_LOCAL\opinie`

The repository does not yet exist. Until it is created, this orchestration file is the source of the remote development contract.

## Privacy boundary

GitHub MAY contain:
- application source code,
- build scripts,
- schemas,
- local database migrations,
- agent routing/configuration,
- synthetic or explicitly fabricated test fixtures,
- deterministic calculation tests,
- offline-install documentation,
- CI configuration.

GitHub MUST NOT contain:
- real case files,
- names or identifying data,
- real historical opinions/archive content,
- extracted text from real cases,
- real embeddings/indexes,
- reconstructed real scenes,
- real calculations or reports tied to a case,
- secrets/credentials.

## Product role

AI-assisted expert workbench for road-accident reconstruction. It supports evidence organization, provenance, timelines, calculations, reconstruction variants and review. It must not autonomously issue a final expert opinion.

## Distribution model

Development can happen online in GitHub/Codex/CI using code and synthetic fixtures.

Production use is local/offline:
1. user downloads/clones/releases the application,
2. installation runs on the user's Windows machine,
3. real cases are created in a local workspace outside the repository,
4. case data and indexes remain local,
5. network access is disabled by default for case processing,
6. optional online research, if ever added, must require an explicit sanitized workflow and must never upload confidential case data.

Preferred long-term delivery is a versioned downloadable release/installer or packaged local application, not a hosted SaaS.

## First autonomous development milestone

1. Bootstrap a standalone repository and application skeleton.
2. Define explicit separation between application code and external local case workspaces.
3. Build the smallest synthetic end-to-end pipeline:
   new case -> evidence/provenance -> timeline/scene -> calculations -> reconstruction variants -> review queue -> opinion base.
4. Every derived claim must retain traceable provenance to evidence.
5. Calculations and reconstructions must record assumptions and uncertainty.
6. Add deterministic tests for provenance retention and calculation reproducibility.
7. Add a network/offline policy test or runtime guard proving that ordinary case processing does not require cloud services.
8. Add packaging/run instructions for a clean Windows machine.

## Agent routing

- RSE Technical Orchestrator
- Software Architect
- Evidence / Provenance specialist
- Calculation / numerical verification specialist
- Test Automation Engineer
- Security / Privacy reviewer at milestone gates
- Reality Checker before release

Keep one implementation owner per overlapping code area. Specialists review or implement bounded components rather than producing uncontrolled parallel versions.

## Hard guardrails

- No real confidential data in GitHub or remote agent prompts.
- No mandatory cloud database, remote embeddings or cloud vector store for production case content.
- No telemetry that exposes case content.
- No autonomous final expert opinion.
- No fabricated missing evidence or inferred measurements presented as source facts.
- Original evidence remains immutable; derived artifacts point back to source provenance.
- Offline use must remain a first-class supported mode, not a degraded fallback.

## Definition of done for milestone 1

- standalone repository exists,
- code/data boundary is enforced,
- one synthetic test case passes end-to-end,
- all outputs retain provenance,
- calculations are reproducible,
- runtime clearly distinguishes source fact, derived result, assumption and expert conclusion,
- local Windows run/install path is documented,
- ordinary case processing can run without sending case data outside the machine.
