#!/usr/bin/env bash
set -euo pipefail

MODE="${1:-smart}"
case "$MODE" in
  smart|core|full) ;;
  *)
    echo "Usage: bash rse/install-claude.sh [smart|core|full]" >&2
    exit 2
    ;;
esac

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
CLAUDE_ROOT="${CLAUDE_ROOT:-$HOME/.claude}"
AGENTS_DIR="${CLAUDE_AGENTS_DIR:-$CLAUDE_ROOT/agents}"
RSE_ROOT="${CLAUDE_RSE_DIR:-$CLAUDE_ROOT/rse}"
CORE_FILE="$REPO_ROOT/rse/agents-core.txt"
MANIFEST="$RSE_ROOT/REGISTERED_MANIFEST.txt"

# shellcheck source=../scripts/lib.sh
. "$REPO_ROOT/scripts/lib.sh"

mapfile -t DIVISIONS < <(
  awk '/"divisions"[[:space:]]*:[[:space:]]*\{/{f=1; next} f' "$REPO_ROOT/divisions.json" \
    | grep -oE '"[a-z0-9-]+"[[:space:]]*:[[:space:]]*\{' \
    | sed -E 's/"([a-z0-9-]+)".*/\1/'
)

yaml_quote() {
  printf "'%s'" "$(printf '%s' "$1" | sed "s/'/''/g")"
}

all_agent_files() {
  local division dir file
  for division in "${DIVISIONS[@]}"; do
    dir="$REPO_ROOT/$division"
    [[ -d "$dir" ]] || continue
    while IFS= read -r -d '' file; do
      [[ "$(head -1 "$file")" == "---" ]] || continue
      [[ -n "$(get_field name "$file")" ]] || continue
      printf '%s\0' "$file"
    done < <(find "$dir" -name '*.md' -type f -print0 | sort -z)
  done
}

find_agent_by_name() {
  local wanted="$1" file name
  while IFS= read -r -d '' file; do
    name="$(get_field name "$file")"
    if [[ "$name" == "$wanted" ]]; then
      printf '%s\n' "$file"
      return 0
    fi
  done < <(all_agent_files)
  return 1
}

register_agent_file() {
  local file="$1" name description slug body outfile
  name="$(get_field name "$file")"
  description="$(get_field description "$file")"
  slug="$(slugify "$name")"
  body="$(get_body "$file")"
  outfile="$AGENTS_DIR/$slug.md"

  {
    echo "---"
    echo "name: $(yaml_quote "$slug")"
    echo "description: $(yaml_quote "$description")"
    echo "---"
    echo
    printf '%s\n' "$body"
    if [[ "$name" == "RSE Orchestrator" ]]; then
      echo
      cat "$REPO_ROOT/rse/CLAUDE_ROUTING.md"
    fi
  } > "$outfile"

  printf '%s\n' "$slug" >> "$MANIFEST"
}

install_core() {
  local name file
  while IFS= read -r name; do
    [[ -n "$name" ]] || continue
    file="$(find_agent_by_name "$name" || true)"
    if [[ -z "$file" ]]; then
      echo "[ERR] CORE agent source not found: $name" >&2
      exit 1
    fi
    register_agent_file "$file"
  done < <(grep -vE '^[[:space:]]*(#|$)' "$CORE_FILE")
}

install_all_registered() {
  local file
  while IFS= read -r -d '' file; do
    register_agent_file "$file"
  done < <(all_agent_files)
}

install_lazy_library() {
  local division src dst file name description slug rel
  rm -rf "$RSE_ROOT/library"
  mkdir -p "$RSE_ROOT/library"
  : > "$RSE_ROOT/LIBRARY_INDEX.tsv"
  printf 'slug\tname\tpath\tdescription\n' >> "$RSE_ROOT/LIBRARY_INDEX.tsv"

  for division in "${DIVISIONS[@]}"; do
    src="$REPO_ROOT/$division"
    [[ -d "$src" ]] || continue
    dst="$RSE_ROOT/library/$division"
    mkdir -p "$dst"
    cp -R "$src/." "$dst/"

    while IFS= read -r -d '' file; do
      [[ "$(head -1 "$file")" == "---" ]] || continue
      name="$(get_field name "$file")"
      [[ -n "$name" ]] || continue
      description="$(get_field description "$file")"
      slug="$(slugify "$name")"
      rel="${file#"$REPO_ROOT/"}"
      printf '%s\t%s\t%s\t%s\n' "$slug" "$name" "$rel" "${description//$'\t'/ }" >> "$RSE_ROOT/LIBRARY_INDEX.tsv"
    done < <(find "$src" -name '*.md' -type f -print0 | sort -z)
  done
}

mkdir -p "$AGENTS_DIR" "$RSE_ROOT"

# Remove only RSE-managed registered agents from the prior install. Never touch
# unrelated user-created Claude agents.
if [[ -f "$MANIFEST" ]]; then
  while IFS= read -r slug; do
    [[ -n "$slug" ]] || continue
    rm -f "$AGENTS_DIR/$slug.md"
  done < "$MANIFEST"
fi
: > "$MANIFEST"

# Routing metadata is shared by every mode.
bash "$REPO_ROOT/rse/generate-agent-catalog.sh" "$RSE_ROOT/AGENT_CATALOG.md"
cp "$CORE_FILE" "$RSE_ROOT/CORE_ROSTER.txt"
cp "$REPO_ROOT/rse/WORKFLOWS.md" "$RSE_ROOT/WORKFLOWS.md"
cp "$REPO_ROOT/rse/EFFICIENCY_POLICY.md" "$RSE_ROOT/EFFICIENCY_POLICY.md"
cp "$REPO_ROOT/rse/CLAUDE_ROUTING.md" "$RSE_ROOT/CLAUDE_ROUTING.md"

case "$MODE" in
  smart)
    echo "RSE Claude install: SMART EFFICIENT"
    install_core
    install_lazy_library
    ;;
  core)
    echo "RSE Claude install: CORE only"
    rm -rf "$RSE_ROOT/library"
    rm -f "$RSE_ROOT/LIBRARY_INDEX.tsv"
    install_core
    ;;
  full)
    echo "[WARN] FULL mode registers the entire Agency library as Claude subagents."
    echo "[WARN] This can increase startup context and API cost. SMART is recommended."
    install_all_registered
    install_lazy_library
    ;;
esac

sort -u -o "$MANIFEST" "$MANIFEST"

bash "$REPO_ROOT/rse/verify-claude-install.sh" "$MODE"

echo
echo "RSE AI Agency Claude installation complete."
echo "  Mode:       $MODE"
echo "  Agents:     $AGENTS_DIR"
echo "  RSE data:   $RSE_ROOT"
if [[ "$MODE" == "smart" ]]; then
  echo "SMART keeps CORE startup-visible and the full library lazy."
  echo "Invoke Claude Code and ask: Use RSE Orchestrator."
fi
