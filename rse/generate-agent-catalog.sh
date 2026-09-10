#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
OUT="${1:-$HOME/.codex/rse/AGENT_CATALOG.md}"
CORE_FILE="$REPO_ROOT/rse/agents-core.txt"

# Shared frontmatter helpers used by the upstream converter/installer.
# shellcheck source=../scripts/lib.sh
. "$REPO_ROOT/scripts/lib.sh"

mkdir -p "$(dirname "$OUT")"

mapfile -t DIVISIONS < <(
  awk '/"divisions"[[:space:]]*:[[:space:]]*\{/{f=1; next} f' "$REPO_ROOT/divisions.json" \
    | grep -oE '"[a-z0-9-]+"[[:space:]]*:[[:space:]]*\{' \
    | sed -E 's/"([a-z0-9-]+)".*/\1/'
)

core_contains() {
  local name="$1"
  grep -vE '^[[:space:]]*(#|$)' "$CORE_FILE" | grep -Fxq "$name"
}

count=0
{
  echo "# RSE AI Agency - Agent Catalog"
  echo
  echo "Generated from the current source roster. Use this as a targeted routing index, not as a prompt to spawn everyone."
  echo
  echo "Routing rule: prefer CORE when it is a strong fit; search the full catalog when a specialist can materially improve quality, speed, safety, or domain accuracy."
  echo

  for division in "${DIVISIONS[@]}"; do
    dir="$REPO_ROOT/$division"
    [[ -d "$dir" ]] || continue

    echo "## $division"
    echo

    while IFS= read -r -d '' file; do
      [[ "$(head -1 "$file")" == "---" ]] || continue
      name="$(get_field name "$file")"
      description="$(get_field description "$file")"
      [[ -n "$name" ]] || continue
      slug="$(agent_slug "$file")"
      tier="SPECIALIST"
      if core_contains "$name"; then tier="CORE"; fi
      printf -- '- **%s** `%s` [%s] - %s\n' "$name" "$slug" "$tier" "$description"
      count=$((count + 1))
    done < <(find "$dir" -name '*.md' -type f -print0 | sort -z)

    echo
  done

  echo "---"
  echo
  echo "Total source agents: $count"
} > "$OUT"

echo "[OK] RSE agent catalog: $count agents -> $OUT"
