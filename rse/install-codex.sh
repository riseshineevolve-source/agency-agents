#!/usr/bin/env bash
set -euo pipefail

MODE="${1:-core}"
EXTRA_ARGS=()

if [[ "${2:-}" == "--dry-run" || "${1:-}" == "--dry-run" ]]; then
  EXTRA_ARGS+=("--dry-run")
  [[ "$MODE" == "--dry-run" ]] && MODE="core"
fi

case "$MODE" in
  core)
    AGENTS_FILE="rse/agents-core.txt"
    ;;
  all|full)
    AGENTS_FILE="rse/agents-all.txt"
    ;;
  *)
    echo "Usage: bash rse/install-codex.sh [core|all] [--dry-run]" >&2
    exit 2
    ;;
esac

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

echo "RSE AI Agency: generating Codex agent definitions..."
./scripts/convert.sh --tool codex

echo "RSE AI Agency: installing '$MODE' roster using $AGENTS_FILE..."
./scripts/install.sh --tool codex --agents-file "$AGENTS_FILE" "${EXTRA_ARGS[@]}"

echo
if [[ " ${EXTRA_ARGS[*]-} " == *" --dry-run "* ]]; then
  echo "Dry run complete. No Codex agent files were installed."
else
  echo "RSE AI Agency installation complete."
  echo "Start Codex and invoke: Use RSE Orchestrator."
fi
