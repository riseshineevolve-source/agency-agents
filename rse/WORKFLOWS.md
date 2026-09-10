# RSE AI Agency workflows

These are starting commands for Codex. The `RSE Orchestrator` should still inspect the active repository, read its `AGENTS.md` and authoritative specs, and choose only the specialists that materially help.

## Take over an existing project

```text
Use RSE Orchestrator. Inspect the entire current repository and its recent state. Read AGENTS.md and every authoritative product/specification file it points to. Summarize the current implementation, blockers and risks, then choose the smallest specialist team needed for my request. Work through implementation and QA until you can return PASS, NEEDS WORK or BLOCKED with evidence. Do not widen scope without a concrete reason.
```

## Build a new app or major feature

```text
Use RSE Orchestrator for an end-to-end app workflow. Start with Product Manager and UX Architect, involve Software Architect only for decisions that need architecture, then delegate implementation to the appropriate Frontend Developer, Mobile App Builder and/or Backend Architect. Run automated tests, accessibility review, independent code review and a final Reality Checker gate. Preserve all repository-specific constraints.
```

## Fix one issue and nothing else

```text
Use RSE Orchestrator in minimal-change mode. Delegate implementation to Minimal Change Engineer. Fix only the issue I described, preserve unrelated design, behavior, APIs and architecture, run the smallest sufficient regression checks, then have Code Reviewer independently verify the diff.
```

## Final UX audit

```text
Use RSE Orchestrator for a final UX quality gate. Run UI Finish-Gate Reviewer, Accessibility Auditor and the relevant test agent independently. Consolidate their evidence and send it to Reality Checker. Do not return PASS while a blocker, broken flow, hidden navigation problem, layout defect or unverified claim remains.
```

## Security audit of an AI-built app

```text
Use RSE Orchestrator for a security pass focused on AI-generated code. Use AI-Generated Code Security Auditor and, when credentials or tracked environment files are involved, Secrets & Credential Hygiene Engineer. Check authentication boundaries, authorization, database/RLS rules, exposed secrets, unsafe client assumptions and data handling. Never print real secret values. Return concrete findings ordered by severity and verify fixes after implementation.
```

## Prepare Android app for Google Play

```text
Use RSE Orchestrator for a Google Play release-readiness workflow. Use Mobile App Builder and Mobile Release Engineer for the release candidate, then Accessibility Auditor, Data Privacy Officer and AI-Generated Code Security Auditor. Only after technical readiness, use App Store Optimizer for the listing. Finish with Reality Checker and provide PASS, NEEDS WORK or BLOCKED with evidence.
```

## Research and prioritize a new RSE product

```text
Use RSE Orchestrator for product opportunity research. Use Product Trend Researcher and/or Research Synthesist for evidence, Product Manager for the MVP and Studio Producer to compare opportunity cost against the existing RSE portfolio. Finish with Reality Checker. I want a decision, not a brainstorm dump: GO, TEST CHEAPLY, HOLD or DROP, with reasons.
```

## Educational / children's product

```text
Use RSE Orchestrator for an educational product. Start from the target child age, learning objective and real user context. Use Research Synthesist and Product Manager, involve Academic Psychologist only where age/development/behavior is genuinely relevant, and use UX/visual specialists as needed. Keep language natural and age-appropriate without making it babyish. Require factual, pedagogical, UX and safety checks before PASS.
```

## KDP / book workflow

```text
Use RSE Orchestrator for a KDP/product publishing workflow. Validate the niche with Product Trend Researcher or Research Synthesist, define the differentiated product with Product Manager, then use Book Co-Author and Image Prompt Engineer as appropriate. Check consistency, age fit, print usability and commercial differentiation. Finish with Reality Checker before treating the product as final.
```
