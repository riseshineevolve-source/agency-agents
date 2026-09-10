#!/usr/bin/env bash
set -euo pipefail

MODE="${1:-smart}"
EXTRA_ARGS=()

if [[ "${2:-}" == "--dry-run" || "${1:-}" == "--dry-run" ]]; then
  EXTRA_ARGS+=("--dry-run")
  [[ "$MODE" == "--dry-run" ]] && MODE="smart"
fi

case "$MODE" in
  core)
    INSTALL_ARGS=(--agents-file rse/agents-core.txt)
    VERIFY_MODE="core"
    LABEL="CORE roster"
    ;;
  curated)
    INSTALL_ARGS=(--agents-file rse/agents-all.txt)
    VERIFY_MODE="curated"
    LABEL="RSE curated roster"
    ;;
  smart|full|all)
    INSTALL_ARGS=()
    VERIFY_MODE="smart"
    LABEL="full Agency library with RSE smart-efficient routing"
    ;;
  *)
    echo "Usage: bash rse/install-codex.sh [smart|core|curated] [--dry-run]" >&2
    exit 2
    ;;
esac

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

echo "RSE AI Agency: generating Codex agent definitions..."
./scripts/convert.sh --tool codex

echo "RSE AI Agency: installing $LABEL..."
./scripts/install.sh --tool codex --no-interactive "${INSTALL_ARGS[@]}" "${EXTRA_ARGS[@]}"

echo
if [[ " ${EXTRA_ARGS[*]-} " == *" --dry-run "* ]]; then
  echo "Dry run complete. No Codex agent files were installed."
  exit 0
fi

# Build searchable routing metadata next to the Codex configuration.
CODEX_ROOT="$HOME/.codex"
if [[ -n "${CODEX_AGENTS_DIR:-}" ]]; then
  CODEX_ROOT="$(cd "$(dirname "$CODEX_AGENTS_DIR")" && pwd)"
fi
RSE_META_DIR="$CODEX_ROOT/rse"
mkdir -p "$RSE_META_DIR"

bash rse/generate-agent-catalog.sh "$RSE_META_DIR/AGENT_CATALOG.md"
cp rse/agents-core.txt "$RSE_META_DIR/CORE_ROSTER.txt"
cp rse/WORKFLOWS.md "$RSE_META_DIR/WORKFLOWS.md"
cp rse/EFFICIENCY_POLICY.md "$RSE_META_DIR/EFFICIENCY_POLICY.md"

bash rse/verify-codex-install.sh "$VERIFY_MODE"

echo
echo "RSE AI Agency installation complete."
if [[ "$MODE" == "core" ]]; then
  echo "Installed CORE only. For the full Agency library, run: bash rse/install-codex.sh smart"
elif [[ "$MODE" == "curated" ]]; then
  echo "Installed the curated RSE roster. For the full library, run: bash rse/install-codex.sh smart"
else
  echo "Full Agency library is available to Codex; RSE Orchestrator defaults to SMART EFFICIENT routing and uses specialists only when they add material value."
fi
echo "Restart Codex, then invoke: Use RSE Orchestrator."
