# RSE AI Agency for Claude Code

Claude Code should use the same SMART EFFICIENT operating model as the RSE Codex integration, but avoid registering the full Agency library as startup-visible subagents.

## Default architecture

- Register only the RSE CORE roster as Claude Code subagents in `~/.claude/agents/`.
- Keep the full Agency source library available lazily under `~/.claude/rse/library/`.
- Keep a searchable full catalog at `~/.claude/rse/AGENT_CATALOG.md`.
- Keep exact slug/name/source-path lookup data at `~/.claude/rse/LIBRARY_INDEX.tsv`.
- CORE is a preference, not a whitelist.
- Search the full catalog only when a non-CORE specialist has a clear material advantage.
- Read only the selected specialist definition, not the whole lazy library.

## Delegation rule

Before delegating, the root thread builds a compact project capsule containing:

- current goal;
- authoritative constraints;
- affected files or area;
- known state and relevant checks;
- blockers;
- non-goals;
- exact acceptance criteria.

Pass bounded context to the selected specialist. Do not ask multiple agents to rediscover the same repository history.

When a non-CORE specialist is needed:

1. search `~/.claude/rse/AGENT_CATALOG.md` narrowly;
2. resolve the exact source path from `~/.claude/rse/LIBRARY_INDEX.tsv`;
3. read that single definition from `~/.claude/rse/library/`;
4. use its persona/instruction body as the specialist brief for a tightly scoped Claude delegation;
5. return only the specialist findings needed by the parent task.

Claude Code supports nested subagent delegation. Use it only when the selected specialist itself has a genuinely separable subtask; do not create delegation chains for ordinary work.

## Agent budget

Use the existing RSE SMART EFFICIENT budgets:

- S, tiny/local: root only by default; at most 1 specialist when clearly justified.
- M, normal feature/bug/focused research: normally 1 specialist; add 1 reviewer only when concrete risk justifies it.
- L, substantial cross-cutting work: normally 2-3 specialists with distinct scopes; up to 4 including verification.
- XL, release/security/deep audit: normally 3-5 specialists; maximum 6 concurrent unless the user explicitly requests broader parallel work and each extra agent has a distinct purpose.

Do not turn ordinary work into XL merely because many agents exist.

## Context and cost economy

The full lazy library is an expert bench, not a prompt dump.

Do not preload hundreds of agent descriptions into normal Claude sessions. Keep startup-visible subagents small and stable, then pull one specialist definition only when needed. This protects context window, API cost, and routing quality.

## Verification

Match verification to risk. Prefer targeted checks after narrow changes. Use an independent reviewer when the claim or risk justifies independence. Do not repeat the same successful checks without a relevant change.

Repository-specific `AGENTS.md`, project specifications, and the user's current request remain authoritative over generic RSE habits.
