# RSE AI Agency for Codex

A curated Rise.Shine.Evolve agent layer built on top of `agency-agents`.

The goal is not to install the entire upstream roster. RSE uses a compact core team for everyday product, UX, engineering and QA work, plus specialist agents that are added when the task actually needs them.

## Recommended setup

### CORE team

Use `rse/agents-core.txt` for normal day-to-day work. It installs 16 agents, including the custom `RSE Orchestrator`.

### FULL RSE team

Use `rse/agents-all.txt` when you also want release, security hygiene, localization, ASO, publishing and educational specialists available globally.

## Windows installation

Use Git Bash or WSL because the upstream installer is a Bash script.

```bash
git clone https://github.com/riseshineevolve-source/agency-agents.git
cd agency-agents

# Generate Codex agent TOML files from the source Markdown agents.
./scripts/convert.sh --tool codex

# Recommended first install: compact RSE core.
./scripts/install.sh --tool codex --agents-file rse/agents-core.txt
```

The Codex integration installs agents into:

```text
~/.codex/agents/
```

To install the full RSE roster instead:

```bash
./scripts/convert.sh --tool codex
./scripts/install.sh --tool codex --agents-file rse/agents-all.txt
```

Or use the RSE wrapper:

```bash
bash rse/install-codex.sh core
bash rse/install-codex.sh all
```

To preview without changing anything:

```bash
bash rse/install-codex.sh core --dry-run
```

## Verify in Codex

After installation, start Codex and ask for a named agent explicitly, for example:

```text
Use RSE Orchestrator. Inspect this repository, read its AGENTS.md and authoritative specs, then choose the smallest specialist team needed to complete the task and verify the result.
```

Or use a specialist directly:

```text
Use Minimal Change Engineer. Fix only the reported issue and preserve all unrelated UI and behavior.
```

```text
Use Reality Checker. Perform a final independent readiness audit and return PASS, NEEDS WORK, or BLOCKED with evidence.
```

## RSE operating model

The orchestrator follows this priority order:

1. Repository `AGENTS.md` and authoritative project specifications.
2. The user's current explicit request and constraints.
3. RSE workflow rules.
4. Generic upstream agent habits.

This prevents a generic specialist profile from overriding project-specific decisions.

## Recommended workflow examples

### App / major feature

`Product Manager -> UX Architect -> Software Architect -> developer(s) -> Test Automation Engineer -> Accessibility Auditor -> Code Reviewer -> Reality Checker`

### Narrow fix

`Minimal Change Engineer -> targeted tests -> Code Reviewer`

### Final UI audit

`UI Finish-Gate Reviewer + Accessibility Auditor + Test Automation Engineer -> Reality Checker`

### Google Play release

`Mobile App Builder -> Mobile Release Engineer -> Accessibility Auditor -> Data Privacy Officer -> AI-Generated Code Security Auditor -> App Store Optimizer -> Reality Checker`

### KDP / educational product

`Trend Researcher or Research Synthesist -> Product Manager -> relevant educational specialist -> Book Co-Author -> Image Prompt Engineer when visual -> Reality Checker`

## Keeping the fork current

Keep custom RSE files isolated under `rse/` plus `specialized/rse-orchestrator.md`. That makes upstream updates easier.

After cloning, add the original project as an upstream remote once:

```bash
git remote add upstream https://github.com/msitarzewski/agency-agents.git
```

To refresh later:

```bash
git fetch upstream
git checkout main
git merge upstream/main
```

Resolve conflicts only if upstream eventually creates files with the same RSE-specific paths.

## Repository-specific instructions still matter

Do not replace a project's own `AGENTS.md` with this agency configuration. A repository can define product-specific guardrails that the RSE Orchestrator must read before work begins.

This is especially important for products involving children, families, seniors, authentication, uploads, payments or private user data.
