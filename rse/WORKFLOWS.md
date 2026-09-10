# RSE AI Agency workflows

These are starting commands for Codex when SMART mode is installed. `RSE Orchestrator` should inspect the active repository, read its `AGENTS.md` and authoritative specs, prefer the CORE team when it is a strong fit, and search the full installed Agency catalog when a specialist can materially improve the result.

## Take over an existing project

```text
Use RSE Orchestrator. Inspect the entire current repository and its recent state. Read AGENTS.md and every authoritative product/specification file it points to. Summarize the current implementation, blockers and risks. Prefer the RSE CORE team when it fits, but search the full installed Agency catalog by description for any specialist that materially improves this task. Choose the smallest useful team, work through implementation and QA, and finish with PASS, NEEDS WORK or BLOCKED with evidence. Do not widen scope without a concrete reason.
```

## Build a new app or major feature

```text
Use RSE Orchestrator for an end-to-end app workflow. Read project rules first. Define the product/UX/architecture needs, then inspect the full Agency catalog for platform- or technology-specific specialists before defaulting to generic implementers. Use only the smallest useful team. Parallelize independent exploration/testing, avoid conflicting parallel edits, run appropriate tests and accessibility/security review, and finish with an independent Reality Checker gate.
```

## Fix one issue and nothing else

```text
Use RSE Orchestrator in minimal-change mode. Fix only the issue I described and preserve unrelated design, behavior, APIs and architecture. Prefer Minimal Change Engineer if available. Search the full specialist catalog only if the issue clearly requires a narrower technology/domain expert. Run the smallest sufficient regression checks and have an independent reviewer verify the diff.
```

## Final UX audit

```text
Use RSE Orchestrator for a final UX quality gate. Run UI Finish-Gate Reviewer and Accessibility Auditor, then search the full Agency catalog for any specialist relevant to the actual platform or interaction risk. Run independent checks in parallel where useful, consolidate their evidence, and send it to Reality Checker. Do not return PASS while a blocker, broken flow, hidden navigation problem, layout defect or unverified claim remains.
```

## Security audit of an AI-built app

```text
Use RSE Orchestrator for a security pass focused on AI-generated code. Start with AI-Generated Code Security Auditor, then search the full Security division for narrower specialists that match the actual architecture or findings, for example secrets, AppSec, cloud, compliance, auth or incident expertise. Never print real secret values. Order findings by severity, remediate only confirmed issues, and verify fixes after implementation.
```

## Prepare Android app for Google Play

```text
Use RSE Orchestrator for Google Play release readiness. Read the app's AGENTS.md/specs first. Search the full Agency catalog for Android/mobile release, accessibility, privacy, security and store-optimization specialists. Build the smallest release team, verify the actual release candidate, and do not start store-listing optimization until technical readiness is credible. Finish with PASS, NEEDS WORK or BLOCKED with evidence.
```

## Research and prioritize a new RSE product

```text
Use RSE Orchestrator for product opportunity research. Start with Research Synthesist and/or Trend Researcher when appropriate, then search the full Agency catalog for domain-specific researchers or strategists that can materially improve the decision. Use Product Manager for MVP boundaries and Studio Producer for portfolio tradeoffs. I want a decision, not a brainstorm dump: GO, TEST CHEAPLY, HOLD or DROP, with evidence and reasons.
```

## Educational / children's product

```text
Use RSE Orchestrator for an educational product. Start from the target child age, learning objective and real user context. Search the Academic, Product, Design, Research and relevant specialist catalog entries for the best-fit experts rather than assuming one generic education role. Keep language natural and age-appropriate without making it babyish. Require factual, pedagogical, UX, privacy and safety checks before PASS.
```

## KDP / book workflow

```text
Use RSE Orchestrator for a KDP/product publishing workflow. Search the full Agency catalog for the best market-research, publishing, content, visual and age-fit specialists for this exact product. Use the fewest agents that cover the real work. Check differentiation, consistency, print usability, factual accuracy and audience fit. Finish with Reality Checker before treating the product as final.
```

## Unknown or unusual task

```text
Use RSE Orchestrator. I do not know which Agency agent is best for this. First classify the task, then search ~/.codex/rse/AGENT_CATALOG.md by the concrete domain, technology, deliverable and risk terms. Compare the descriptions of the strongest candidates, choose the smallest useful team, tell me briefly which agents you selected and why, then execute and verify the work.
```
