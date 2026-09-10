# RSE AI Agency efficiency policy

This policy keeps the full Agency bench available while minimizing wasteful Codex/Work usage. The objective is quality per unit of agent work, not the smallest possible number of tokens and not the largest possible team.

## Default mode: SMART EFFICIENT

`Use RSE Orchestrator` should default to SMART EFFICIENT unless the user explicitly asks for a deep audit, maximum assurance, broad parallel research, or another mode.

The full installed agent library remains discoverable. Availability never implies invocation.

## Decision rule before every delegation

Delegate only when at least one of these is true:

- the specialist has materially better domain expertise than the root agent;
- independent verification is necessary for a credible completion claim;
- the work can be parallelized without duplicating context or conflicting writes;
- the specialist can reduce risk or avoid a likely rework loop;
- the user explicitly requests that specialist perspective.

If none applies, keep the work in the root thread.

## Agent budget by task class

### Class S: tiny / local
Examples: one typo, one label, one isolated style fix, one obvious config change, one factual repository lookup.

- Root only by default.
- 0 additional agents.
- Use 1 specialist only if the task is genuinely specialized or high-risk.
- Verify with the smallest meaningful check.

### Class M: normal feature / bug / focused research
Examples: a bounded bug, one screen, one feature slice, one API change, a focused audit.

- Root + 0-1 implementation/domain specialist by default.
- Add 1 independent reviewer only when code changed, risk is meaningful, or the user requests a final gate.
- Typical total specialist launches: 1-2.

### Class L: substantial feature / cross-cutting change
Examples: feature spanning UI and backend, migration, release preparation, multi-surface UX change.

- Use 2-3 specialists with non-overlapping scopes.
- Add a final independent gate only after implementation evidence exists.
- Typical total specialist launches: 2-4.

### Class XL: release / security / deep audit
Examples: production release, auth/privacy audit, major architecture decision, broad pre-publication audit.

- Use 3-5 specialists only when their scopes are independently useful.
- Hard maximum: 6 concurrent agents unless the user explicitly asks for broader parallel analysis and the extra work is justified.
- Do not run this class for ordinary development tasks.

## Context budget

Long context is expensive and often causes duplicated work. Use a project capsule instead of repeatedly asking every agent to rediscover the repository.

The root agent should build a compact project capsule containing only:

- current user goal;
- authoritative constraints;
- affected area/files;
- known implementation state;
- relevant test/build commands;
- current blockers and evidence;
- explicit non-goals.

Pass that capsule plus only task-relevant files/findings to specialists.

Do not make every specialist reread the entire repository, full history, or every specification. A specialist should directly read an authoritative source when exact wording matters, when its task depends on details omitted from the capsule, or when an independent final audit requires source-level verification.

## Repository exploration budget

- Start with targeted paths, search, diff, recent changes, and repository instructions.
- Expand outward only when evidence indicates the issue crosses boundaries.
- Do not perform a full-repository audit as a precondition for a narrow task.
- Do not ask multiple agents to map the same repository independently unless independent comparison is itself the goal.
- Reuse an accurate project map within the same task/session instead of rebuilding it.

## Specialist discovery budget

- Prefer CORE when it is a strong fit.
- Search `AGENT_CATALOG.md` narrowly only when there is a real expertise gap.
- Compare a few plausible descriptions, not the full 280-agent catalog.
- Once an appropriate specialist is selected for a task, do not reopen discovery unless the task changes, the specialist reports a gap, or evidence shows the selection was wrong.

## Delegation packet

Every subagent receives a bounded packet, not a transcript dump:

- exact task and deliverable;
- only relevant constraints;
- relevant file paths or evidence;
- acceptance criteria;
- what must not change;
- a concise output request.

Ask specialists to return concise findings and evidence. Prefer a short actionable result over a narrative of everything inspected.

## Verification budget

Verification is required when it proves something material, but repeated verification without a change is waste.

- After a local change, run the most targeted meaningful test/build/lint check first.
- Broaden checks when the change is cross-cutting, release-sensitive, security-sensitive, or targeted checks reveal uncertainty.
- Do not rerun the same successful test after no relevant code/config change.
- Do not create tests that merely mirror trivial reversible implementation unless they prevent a realistic regression.
- Run full suites at milestone/release gates or when project instructions require them.
- Reuse fresh evidence from another agent instead of independently reproducing it unless independence is necessary.

## Review budget

Independent review is most valuable after there is something concrete to review.

- Do not launch Reality Checker, Code Reviewer, Accessibility Auditor, Security Auditor, and UI reviewer automatically after every small change.
- Use the reviewer whose risk domain matches the change.
- Combine multiple final gates at meaningful milestones rather than after each micro-fix.
- Reality Checker is a milestone/final gate, not a heartbeat monitor.

## Parallelism budget

Parallelize independent read-heavy work when it saves wall-clock time or adds truly independent expertise.

Avoid parallel work when it only duplicates repository reading.

For writes:

- one owner per overlapping file area;
- serialize changes to shared architecture;
- integrate before the next dependent task;
- never create competing edits for the same files merely to compare approaches.

## Model-effort policy

The orchestrator must not assume it can change the runtime model. When model or reasoning controls are available, choose the least expensive/capable setting that can reliably complete the task.

General preference:

- routine navigation, classification, search, simple edits and bounded read-only specialist work: efficient model / low reasoning;
- normal implementation, debugging and review: balanced model / medium reasoning;
- difficult architecture, ambiguous multi-system debugging, security-critical reasoning or unresolved failures: high-capability model / high reasoning only when the harder setting has a clear expected benefit.

Do not escalate model/reasoning merely because a task is long. Escalate because it is hard.

## Tool and retrieval budget

Use the minimum evidence sufficient for a correct decision.

A second search/read/tool loop is justified when a required fact is missing, a claim remains unsupported, the first result is ambiguous, or the user requested exhaustive coverage. Do not continue searching only to collect more examples or restate already-supported findings.

## Failure and escalation

If a focused attempt fails:

1. inspect the concrete failure evidence;
2. decide whether the issue is lack of information, wrong specialist, wrong hypothesis, or genuinely difficult reasoning;
3. escalate one dimension at a time: broader context, better specialist, stronger model/reasoning, or broader test;
4. stop escalating once the blocker is resolved.

Do not respond to one failed attempt by launching a broad agent swarm.

## Stop rule

After every meaningful tool/subagent result ask:

`Can the user's requested outcome now be completed correctly with the evidence already available?`

If yes, finish. Do not add another agent, another search, another audit, or another test solely for reassurance.

## User overrides

The user does not need to name a mode. The orchestrator classifies the task automatically.

Optional explicit overrides:

- `economy`: root + at most 1 specialist unless safety/release correctness requires more;
- `balanced`: SMART EFFICIENT default;
- `deep audit` or `maximum assurance`: allow Class XL routing and multiple independent final gates.

Even in deep mode, every launched agent must have a distinct purpose.
