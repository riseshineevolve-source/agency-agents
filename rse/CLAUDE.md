# RSE AI Agency for Claude Code

The recommended Claude Code setup is **SMART EFFICIENT**.

Unlike the Codex integration, SMART does **not** register the full Agency library as startup-visible Claude subagents. It registers the 16-agent RSE CORE roster and keeps the full source catalog available lazily. This reduces routine context and API cost while preserving specialist access.

## Install

```bash
cd ~/GitHub/agency-agents
git pull
bash rse/install-claude.sh smart
```

Restart Claude Code after installation, then ask:

```text
Use RSE Orchestrator.
```

## Modes

Recommended:

```bash
bash rse/install-claude.sh smart
```

CORE only:

```bash
bash rse/install-claude.sh core
```

Full registration, not recommended for normal API-billed use:

```bash
bash rse/install-claude.sh full
```

`full` registers the complete library as Claude subagents and prints a warning because hundreds of startup-visible agent descriptions can increase context and cost.

## Installed locations

Registered Claude subagents:

```text
~/.claude/agents/
```

RSE routing data:

```text
~/.claude/rse/
```

SMART mode creates:

- `AGENT_CATALOG.md` — searchable full catalog;
- `CORE_ROSTER.txt` — preferred CORE roster;
- `WORKFLOWS.md` — workflow guidance;
- `EFFICIENCY_POLICY.md` — RSE routing policy;
- `CLAUDE_ROUTING.md` — Claude-specific lazy-routing guidance;
- `LIBRARY_INDEX.tsv` — exact slug/name/source-path lookup for the lazy library;
- `library/` — full Agency source definitions organized by division;
- `REGISTERED_MANIFEST.txt` — RSE-managed Claude subagent files.

The installer removes only RSE-managed registered agents from its previous manifest. It does not delete unrelated user-created Claude agents.

## SMART routing

The RSE Orchestrator should use CORE first and search the full lazy library only when a non-CORE specialist adds material value. It should read only the selected specialist definition and delegate a bounded task with a compact project capsule.

The existing S/M/L/XL RSE agent budgets remain in force. Availability of the full library never implies spawning the full library.

## Verification

The installer runs verification automatically. You can rerun it with:

```bash
bash rse/verify-claude-install.sh smart
```

Verification checks:

- expected registered roster;
- RSE Orchestrator presence;
- Claude-compatible generated frontmatter;
- lazy-library count against the source catalog;
- missing metadata;
- duplicate source agent names.

A successful run ends with:

```text
[PASS] Claude adapter is complete: RSE Orchestrator present, expected roster registered, routing metadata valid.
```
