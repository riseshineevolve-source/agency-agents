# RSE AI Agency workflows

These prompts assume SMART mode. `RSE Orchestrator` defaults to SMART EFFICIENT: the full Agency bench stays available, but only agents with a distinct useful role should be launched.

## Default project task

```text
Use RSE Orchestrator in SMART EFFICIENT mode. Read repository instructions and only the authoritative material required for this task. Inspect the affected area first, not the entire repository. Use the root thread when sufficient; delegate only when a specialist adds material expertise, necessary independent verification, or useful non-duplicative parallel work. Reuse fresh evidence and do not repeat successful checks without a relevant change. Complete the task with the smallest meaningful verification.
```

## Take over an existing project efficiently

```text
Use RSE Orchestrator in SMART EFFICIENT mode. Read AGENTS.md and the authoritative project spec required by it. Build one compact project capsule: current phase, major architecture, active constraints, relevant build/test commands, known blockers and next likely work. Use at most one read-only specialist unless the project evidence shows a real second expertise gap. Do not independently remap the same repository with multiple agents. Do not modify files unless I ask.
```

## Fix one issue and nothing else

```text
Use RSE Orchestrator in SMART EFFICIENT minimal-change mode. Inspect only the affected path plus repository instructions. Fix the issue and preserve unrelated behavior/design. Use Minimal Change Engineer or a narrower specialist only if it materially improves the fix. Run the smallest meaningful regression check. Add Code Reviewer only when the diff or risk justifies independent review. Do not launch broad final-gate agents for a micro-fix.
```

## Normal feature

```text
Use RSE Orchestrator in SMART EFFICIENT mode. Define the bounded acceptance criteria, inspect the affected feature slice, and select at most one best implementation specialist by default. Add a second specialist only for a distinct backend/platform/domain boundary or an independent review that materially improves confidence. Verify affected behavior first; broaden tests only if the change or evidence requires it.
```

## Substantial cross-cutting feature

```text
Use RSE Orchestrator. Treat this as Class L only if the feature truly crosses multiple boundaries. Use 2-3 non-overlapping specialists, avoid parallel writes to shared files, integrate once, then run one appropriate independent gate. Reuse repository/spec context through a concise project capsule instead of asking every agent to rediscover the project.
```

## Final UX audit

```text
Use RSE Orchestrator for a real milestone UX gate. Use UI Finish-Gate Reviewer and Accessibility Auditor when both risks are relevant. Add a platform-specific specialist only for a distinct uncovered risk. Run independent checks in parallel where useful, consolidate evidence once, and use Reality Checker only after concrete audit evidence exists.
```

## Security audit

```text
Use RSE Orchestrator for a security-sensitive audit. Start with the most relevant security specialist, not a broad agent swarm. Add a narrower auth/secrets/privacy/cloud specialist only when the architecture or first findings justify it. Never print secret values. Verify confirmed findings and fixes; do not repeat scans without a relevant change.
```

## Google Play / release readiness

```text
Use RSE Orchestrator for a release milestone. This may use Class XL routing because release evidence spans distinct domains. Select only specialists relevant to the actual app: mobile release, accessibility, privacy/security and store optimization as needed. Run technical readiness before listing optimization. Consolidate evidence and use Reality Checker once at the final gate.
```

## Product research

```text
Use RSE Orchestrator in SMART EFFICIENT mode. Start with one research specialist. Search for a second domain specialist only if the first pass leaves a material evidence gap. Use the minimum sources needed for a decision. Stop when the evidence supports GO, TEST CHEAPLY, HOLD or DROP; do not keep researching merely to collect more examples.
```

## Educational / children's product

```text
Use RSE Orchestrator. Preserve age fit, privacy and learning goals. Use one primary education/product specialist first. Add psychology, UX, research or safety expertise only for a distinct decision that needs it. Do not ask several agents to restate the same age-appropriateness guidance. Run broader final gates only at a meaningful publication/release milestone.
```

## KDP / publishing

```text
Use RSE Orchestrator. Separate market validation, content/visual production and final print review into meaningful stages. Use the best specialist for the current stage rather than running the full publishing team each time. Reuse established product/style constraints across pages. Use Reality Checker only for milestone/final readiness.
```

## Deep audit / maximum assurance

```text
Use RSE Orchestrator in deep-audit mode. This is an intentional Class XL task. Select 3-5 specialists with non-overlapping scopes and a clear reason for each. Parallelize independent read-only audits, avoid duplicated repository mapping, consolidate evidence once, then use Reality Checker for the final status. Do not exceed 6 concurrent agents unless I explicitly request broader analysis and every extra agent has a distinct purpose.
```

## Economy override

```text
Use RSE Orchestrator in economy mode. Root thread first. Use at most one specialist unless a security/release/safety requirement makes another independent check necessary. Prefer targeted files, concise findings and the smallest meaningful verification.
```
