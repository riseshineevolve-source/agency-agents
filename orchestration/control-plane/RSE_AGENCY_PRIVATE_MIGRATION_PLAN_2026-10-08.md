# RSE Agency Private Migration Plan — 2026-10-08

Status: REQUIRED / NOT YET EXECUTED
Current repository: riseshineevolve-source/agency-agents
Current visibility: PUBLIC
Current relationship: fork of msitarzewski/agency-agents

## Owner intent

Move the RSE control-plane/agency source of truth to a private independent repository without interrupting the active RSE Factory.

## Why this is a migration, not a visibility toggle

The current repository is a public fork. Treat fork-network visibility/history as an external constraint. Do not attempt an unsafe in-place conversion while the Control Plane, n8n and active lane workflows depend on the existing remote.

## Safe sequence

1. Freeze a migration cut SHA on current agency-agents main.
2. Create a new independent PRIVATE repository under riseshineevolve-source.
3. Mirror the full RSE-owned branch/history needed for operations.
4. Verify files, branches, tags, default branch and current Control Plane CI in the private repository.
5. Update:
   - local remotes/worktrees;
   - n8n GitHub API repository references;
   - automation prompts/checkpoints;
   - lane bootstrap links;
   - any connector/repo allowlists.
6. Run Control Plane v1 and n8n WF-01/WF-02 against the private repository.
7. Require green evidence before switching source-of-truth authority.
8. Mark the old public fork as retired/read-only/archive only after cutover.
9. Never delete the old public fork until rollback confidence is established.

## Naming

Final private repository name remains an owner choice unless an existing canonical name is already recorded. Do not silently create multiple competing central repos.

## Release rule

This migration is operational/security work, not a reason to stop product release lanes. Execute it in parallel with Detective/Optical/Gentle/World only when it does not destabilize active source-of-truth workflows.
