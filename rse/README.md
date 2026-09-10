# RSE AI Agency for Codex

RSE AI Agency is a Rise.Shine.Evolve routing layer on top of the full `agency-agents` catalog.

The recommended setup is **SMART EFFICIENT**:

- install every current Agency custom agent into Codex;
- keep the 16-agent RSE CORE team as the preferred routing tier;
- discover non-CORE specialists only when they materially improve the task;
- minimize duplicated repository reading, repeated tests and unnecessary final gates;
- scale agent count and verification to task risk;
- keep evidence strong enough for the requested claim.

The full library is an expert bench, not a default swarm.

## Recommended installation

For an existing clone:

```bash
cd ~/GitHub/agency-agents
git pull
bash rse/install-codex.sh smart
```

For a fresh clone:

```bash
git clone https://github.com/riseshineevolve-source/agency-agents.git
cd agency-agents
bash rse/install-codex.sh smart
```

SMART mode installs the entire current source catalog. CORE and CURATED remain available for intentionally smaller installations:

```bash
bash rse/install-codex.sh core
bash rse/install-codex.sh curated
```

## Installed locations

Custom agents:

```text
~/.codex/agents/
```

RSE metadata:

```text
~/.codex/rse/
```

including:

- `AGENT_CATALOG.md` - searchable full agent index;
- `CORE_ROSTER.txt` - preferred RSE CORE team;
- `WORKFLOWS.md` - efficient ready-to-use workflow prompts;
- `EFFICIENCY_POLICY.md` - detailed routing and usage policy.

The agent total is derived from the repository at install time rather than hardcoded.

## SMART EFFICIENT routing

`Use RSE Orchestrator` defaults to SMART EFFICIENT. The user does not need to select a mode for ordinary work.

The Orchestrator classifies work into four practical sizes:

- **S:** tiny/local task, root only by default;
- **M:** normal feature/bug/focused research, usually 1 specialist and at most 1 justified reviewer;
- **L:** substantial cross-cutting work, usually 2-3 specialists with distinct scopes;
- **XL:** release/security/deep audit, usually 3-5 specialists and only when the task truly requires it.

The point is not to minimize agent use at all costs. The point is to avoid paying for agents that repeat work already done by the root thread or another specialist.

## Context economy

The root thread builds a compact project capsule and passes bounded context to specialists. It should not ask every agent to reread the full repository, history and specifications.

Direct source reading is still required when exact authoritative wording matters, omitted detail affects the specialist task, or an independent final audit needs source-level verification.

Repository exploration should start from instructions, affected paths, diffs and targeted search. Expand only when evidence shows the problem crosses boundaries.

## Verification economy

Use the smallest meaningful verification first.

- targeted tests/build/lint for affected behavior;
- broader checks for cross-cutting, release-sensitive or security-sensitive work;
- no repeat of the same successful check without a relevant change;
- full suites when repository instructions require them or at meaningful milestones.

Do not launch every reviewer after every edit. Match the independent gate to the actual risk. `Reality Checker` is intended for milestone/final readiness, not every micro-fix.

## Full-library specialist discovery

CORE is a preference, not a whitelist. Search the full catalog when a non-CORE specialist has a clear advantage in a technology, platform, domain, risk or deliverable.

The catalog is normally available at:

```text
~/.codex/rse/AGENT_CATALOG.md
```

Search it narrowly. Do not load the whole catalog into context.

## Model and reasoning policy

RSE Orchestrator does not assume it can change the runtime model. When model/reasoning controls are available, use the least expensive/capable setting that can reliably complete the task:

- efficient/low reasoning for routine navigation, search, simple edits and bounded read-only work;
- balanced/medium reasoning for normal implementation, debugging and review;
- high-capability/high reasoning only for genuinely difficult architecture, security-critical reasoning, ambiguous multi-system debugging or failures that remain unresolved.

Escalate because the problem is hard, not merely because it is long.

## Optional user overrides

Ordinary prompt:

```text
Use RSE Orchestrator.
```

Maximum economy:

```text
Use RSE Orchestrator in economy mode.
```

Broad final assurance:

```text
Use RSE Orchestrator in deep-audit mode.
```

Even in deep mode, every agent must have a distinct purpose.

## RSE CORE team

The current 16-agent preferred roster is maintained in `rse/agents-core.txt`:

- RSE Orchestrator
- Studio Producer
- Product Manager
- Research Synthesist
- UX Architect
- UI Designer
- UI Finish-Gate Reviewer
- Software Architect
- Frontend Developer
- Mobile App Builder
- Backend Architect
- Code Reviewer
- Test Automation Engineer
- Reality Checker
- Accessibility Auditor
- AI-Generated Code Security Auditor

## Verification

A normal installation automatically verifies the expected roster and `RSE Orchestrator`.

You can rerun it with:

```bash
bash rse/verify-codex-install.sh smart
```

Successful SMART verification ends with:

```text
[PASS] All expected agents are installed, including RSE Orchestrator.
```

## Repository-specific instructions remain authoritative

A project's own `AGENTS.md` and linked product specifications remain higher-priority constraints. Do not replace them with RSE guidance.

This is especially important for products involving children, families, seniors, authentication, uploads, payments or private user data.

## Keeping the fork current

Keep RSE custom files isolated under `rse/` plus `specialized/rse-orchestrator.md` so upstream updates remain easy to merge.

After updating the fork, rerun:

```bash
bash rse/install-codex.sh smart
```

That regenerates custom-agent definitions, refreshes routing metadata and verifies the installed roster.
