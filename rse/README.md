# RSE AI Agency for Codex

RSE AI Agency is a Rise.Shine.Evolve routing layer on top of the full `agency-agents` catalog.

The recommended setup is **SMART mode**:

- install every current Agency custom agent into Codex;
- keep a compact RSE CORE team as the default preference;
- let `RSE Orchestrator` discover a non-CORE specialist only when that specialist materially improves the task;
- keep noisy exploration/review work in bounded subagent threads;
- require evidence before final `PASS`.

Installing the full library does **not** mean running the full library. The agents are an available bench. The Orchestrator should normally choose only a handful.

## Installation modes

### SMART - recommended

Installs the **entire current source catalog** and generates a searchable local agent index.

```bash
bash rse/install-codex.sh smart
```

`smart` is also the default when no mode is supplied:

```bash
bash rse/install-codex.sh
```

Use this when you want RSE Orchestrator to be able to discover any useful specialist from the Agency library without you needing to know that specialist exists.

### CORE

Installs only the 16-agent RSE CORE roster:

```bash
bash rse/install-codex.sh core
```

Useful for a deliberately small installation, but non-CORE specialists are not available as custom Codex agents.

### CURATED

Installs CORE plus the preferred RSE specialists listed in `rse/agents-all.txt`:

```bash
bash rse/install-codex.sh curated
```

This is a middle ground. Despite its historical filename, `agents-all.txt` is the RSE curated list, **not** the entire upstream Agency catalog.

## What SMART mode installs

Codex custom agents are installed to:

```text
~/.codex/agents/
```

RSE routing metadata is installed to:

```text
~/.codex/rse/
```

including:

- `AGENT_CATALOG.md` - searchable names, slugs, divisions, CORE/SPECIALIST tier and descriptions;
- `CORE_ROSTER.txt` - the preferred RSE CORE team;
- `WORKFLOWS.md` - ready-to-use RSE workflow prompts.

The exact total agent count is derived from the source repository at install time. It is intentionally not hardcoded, because upstream can add or remove agents.

## Windows setup

Use Git Bash or WSL for these repository scripts.

For a fresh clone:

```bash
git clone https://github.com/riseshineevolve-source/agency-agents.git
cd agency-agents
bash rse/install-codex.sh smart
```

For an existing clone:

```bash
cd ~/GitHub/agency-agents
git pull
bash rse/install-codex.sh smart
```

The conversion step can take a little while because it generates Codex definitions for the full source catalog.

## Automatic verification

A normal non-dry-run installation automatically runs:

```bash
bash rse/verify-codex-install.sh smart
```

For SMART mode the verifier compares the installed TOML files with every current source agent and checks that `RSE Orchestrator` is present.

Successful output ends with:

```text
[PASS] All expected agents are installed, including RSE Orchestrator.
```

You can rerun verification at any time:

```bash
bash rse/verify-codex-install.sh smart
```

## Dry run

Preview without installing:

```bash
bash rse/install-codex.sh smart --dry-run
```

The conversion step may still regenerate files inside the repository's `integrations/codex/` output directory, but the installer does not copy agents into your Codex configuration during a dry run.

## How routing works

RSE Orchestrator follows this order:

1. Read repository `AGENTS.md` and authoritative project specifications.
2. Understand the user's exact request and what must not change.
3. Classify the work by domain, technology, lifecycle stage, audience, risk and deliverable.
4. Prefer a CORE agent when it is already a strong fit.
5. If there is a real expertise gap, search the full installed custom-agent catalog by description.
6. Select the smallest useful team.
7. Parallelize independent/read-heavy work when useful; avoid conflicting parallel code edits.
8. Require independent verification and a final evidence-based gate for substantial work.

The searchable catalog is normally available to the local Codex environment at:

```text
~/.codex/rse/AGENT_CATALOG.md
```

RSE Orchestrator is instructed to search it narrowly rather than loading the whole catalog into context.

## RSE CORE team

The 16-agent preferred team is maintained in `rse/agents-core.txt` and currently includes:

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

CORE is a routing preference, not a hard whitelist in SMART mode.

## Example first prompt in Codex

```text
Use RSE Orchestrator. Read this repository's AGENTS.md and authoritative specs first. Understand my request, then choose the smallest useful team. Prefer RSE CORE when it is a strong fit, but search the full installed Agency catalog for a better specialist when the task has a real expertise gap. Delegate independent work where useful, avoid conflicting parallel edits, verify the result, and finish with PASS, NEEDS WORK, or BLOCKED with evidence.
```

You do not need to know the names of all installed agents. Specialist discovery is part of the Orchestrator's job.

## Repository-specific instructions remain authoritative

Do not replace a project's own `AGENTS.md` with this agency configuration.

Repository instructions and linked product specifications remain higher-priority project constraints. This is especially important for products involving children, families, seniors, authentication, uploads, payments, or private user data.

## Keeping the fork current

Keep RSE custom files isolated under `rse/` plus `specialized/rse-orchestrator.md` so upstream updates remain easy to merge.

Add the original repository as an upstream remote once:

```bash
git remote add upstream https://github.com/msitarzewski/agency-agents.git
```

Refresh later with:

```bash
git fetch upstream
git checkout main
git merge upstream/main
```

After an upstream refresh, rerun:

```bash
bash rse/install-codex.sh smart
```

That regenerates the Codex definitions and agent catalog from the new source roster, then verifies the installation.
