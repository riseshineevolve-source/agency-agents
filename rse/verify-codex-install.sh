#!/usr/bin/env bash
set -euo pipefail

MODE="${1:-smart}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
AGENTS_DIR="${CODEX_AGENTS_DIR:-$HOME/.codex/agents}"
CORE_FILE="$REPO_ROOT/rse/agents-core.txt"

# shellcheck source=../scripts/lib.sh
. "$REPO_ROOT/scripts/lib.sh"

mapfile -t DIVISIONS < <(
  awk '/"divisions"[[:space:]]*:[[:space:]]*\{/{f=1; next} f' "$REPO_ROOT/divisions.json" \
    | grep -oE '"[a-z0-9-]+"[[:space:]]*:[[:space:]]*\{' \
    | sed -E 's/"([a-z0-9-]+)".*/\1/'
)

expected_names() {
  case "$MODE" in
    core)
      grep -vE '^[[:space:]]*(#|$)' "$CORE_FILE"
      ;;
    curated)
      grep -vE '^[[:space:]]*(#|$)' "$REPO_ROOT/rse/agents-all.txt"
      ;;
    smart|full|all)
      for division in "${DIVISIONS[@]}"; do
        dir="$REPO_ROOT/$division"
        [[ -d "$dir" ]] || continue
        while IFS= read -r -d '' file; do
          [[ "$(head -1 "$file")" == "---" ]] || continue
          name="$(get_field name "$file")"
          [[ -n "$name" ]] && printf '%s\n' "$name"
        done < <(find "$dir" -name '*.md' -type f -print0 | sort -z)
      done
      ;;
    *)
      echo "Unknown verification mode: $MODE" >&2
      exit 2
      ;;
  esac
}

[[ -d "$AGENTS_DIR" ]] || {
  echo "[ERR] Codex agents directory does not exist: $AGENTS_DIR" >&2
  exit 1
}

expected=0
missing=0
missing_names=()
while IFS= read -r name; do
  [[ -n "$name" ]] || continue
  expected=$((expected + 1))
  slug="$(slugify "$name")"
  if [[ ! -f "$AGENTS_DIR/$slug.toml" ]]; then
    missing=$((missing + 1))
    missing_names+=("$name")
  fi
done < <(expected_names)

installed=$(find "$AGENTS_DIR" -maxdepth 1 -name '*.toml' -type f 2>/dev/null | wc -l | tr -d ' ')

echo "RSE Codex verification"
echo "  Mode:              $MODE"
echo "  Expected RSE set:  $expected"
echo "  TOML files found:  $installed"
echo "  Missing expected:  $missing"

if [[ "$missing" -gt 0 ]]; then
  echo
  echo "Missing agents:"
  limit=20
  shown=0
  for name in "${missing_names[@]}"; do
    echo "  - $name"
    shown=$((shown + 1))
    [[ "$shown" -ge "$limit" ]] && break
  done
  if [[ "$missing" -gt "$limit" ]]; then
    echo "  ... and $((missing - limit)) more"
  fi
  echo
  echo "[FAIL] Codex agent installation is incomplete." >&2
  exit 1
fi

if [[ ! -f "$AGENTS_DIR/rse-orchestrator.toml" ]]; then
  echo "[FAIL] RSE Orchestrator is missing." >&2
  exit 1
fi

echo "[PASS] All expected agents are installed, including RSE Orchestrator."
