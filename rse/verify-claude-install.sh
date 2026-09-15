#!/usr/bin/env bash
set -euo pipefail

MODE="${1:-smart}"
case "$MODE" in
  smart|core|full) ;;
  *) echo "Usage: bash rse/verify-claude-install.sh [smart|core|full]" >&2; exit 2 ;;
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

source_agent_rows() {
  local division dir file name
  for division in "${DIVISIONS[@]}"; do
    dir="$REPO_ROOT/$division"
    [[ -d "$dir" ]] || continue
    while IFS= read -r -d '' file; do
      [[ "$(head -1 "$file")" == "---" ]] || continue
      name="$(get_field name "$file")"
      [[ -n "$name" ]] || continue
      printf '%s\t%s\n' "$name" "$file"
    done < <(find "$dir" -name '*.md' -type f -print0 | sort -z)
  done
}

expected_registered_names() {
  if [[ "$MODE" == "full" ]]; then
    source_agent_rows | cut -f1
  else
    grep -vE '^[[:space:]]*(#|$)' "$CORE_FILE"
  fi
}

valid_claude_frontmatter() {
  local file="$1"
  awk '
    NR==1 { if ($0!="---") exit 1; next }
    $0=="---" { closed=1; exit }
    /^[[:space:]]*$/ { next }
    /^name:[[:space:]]*/ { name=1; next }
    /^description:[[:space:]]*/ { desc=1; next }
    { exit 1 }
    END { if (!closed || !name || !desc) exit 1 }
  ' "$file"
}

fail=0
missing=0
bad_frontmatter=0

[[ -d "$AGENTS_DIR" ]] || { echo "[FAIL] Claude agents directory missing: $AGENTS_DIR" >&2; exit 1; }
[[ -f "$MANIFEST" ]] || { echo "[FAIL] RSE registered manifest missing: $MANIFEST" >&2; exit 1; }

expected=0
while IFS= read -r name; do
  [[ -n "$name" ]] || continue
  expected=$((expected + 1))
  slug="$(slugify "$name")"
  file="$AGENTS_DIR/$slug.md"
  if [[ ! -f "$file" ]]; then
    echo "[MISS] $name -> $file"
    missing=$((missing + 1))
    fail=1
    continue
  fi
  if ! valid_claude_frontmatter "$file"; then
    echo "[BAD FRONTMATTER] $file"
    bad_frontmatter=$((bad_frontmatter + 1))
    fail=1
  fi
done < <(expected_registered_names)

registered=$(grep -cve '^[[:space:]]*$' "$MANIFEST" || true)
source_total=$(source_agent_rows | wc -l | tr -d ' ')

# Detect duplicate source names because Claude routing by role name must be unambiguous.
duplicates=$(source_agent_rows | cut -f1 | sort | uniq -d)
duplicate_count=0
if [[ -n "$duplicates" ]]; then
  duplicate_count=$(printf '%s\n' "$duplicates" | grep -c . || true)
  echo "[DUPLICATE SOURCE NAMES]"
  printf '%s\n' "$duplicates" | sed 's/^/  - /'
  fail=1
fi

lazy_total=0
if [[ "$MODE" == "smart" || "$MODE" == "full" ]]; then
  if [[ ! -f "$RSE_ROOT/LIBRARY_INDEX.tsv" || ! -d "$RSE_ROOT/library" ]]; then
    echo "[FAIL] Lazy library/index missing in $MODE mode." >&2
    fail=1
  else
    lazy_total=$(( $(wc -l < "$RSE_ROOT/LIBRARY_INDEX.tsv") - 1 ))
    if [[ "$lazy_total" -ne "$source_total" ]]; then
      echo "[FAIL] Lazy library index count $lazy_total != source count $source_total" >&2
      fail=1
    fi
  fi
else
  if [[ -d "$RSE_ROOT/library" || -f "$RSE_ROOT/LIBRARY_INDEX.tsv" ]]; then
    echo "[FAIL] CORE mode should not install the lazy library." >&2
    fail=1
  fi
fi

if [[ ! -f "$AGENTS_DIR/rse-orchestrator.md" ]]; then
  echo "[FAIL] RSE Orchestrator is missing." >&2
  fail=1
fi

for meta in AGENT_CATALOG.md CORE_ROSTER.txt WORKFLOWS.md EFFICIENCY_POLICY.md CLAUDE_ROUTING.md; do
  if [[ ! -f "$RSE_ROOT/$meta" ]]; then
    echo "[FAIL] Missing RSE metadata: $RSE_ROOT/$meta" >&2
    fail=1
  fi
done

echo "RSE Claude verification"
echo "  Mode:                    $MODE"
echo "  Expected registered:     $expected"
echo "  RSE registered manifest: $registered"
echo "  Missing expected:        $missing"
echo "  Bad frontmatter:         $bad_frontmatter"
echo "  Full source library:     $source_total"
echo "  Lazy library index:      $lazy_total"
echo "  Duplicate source names:  $duplicate_count"

if [[ "$registered" -ne "$expected" ]]; then
  echo "[FAIL] Registered manifest count $registered != expected $expected" >&2
  fail=1
fi

if [[ "$fail" -ne 0 ]]; then
  echo "[FAIL] Claude adapter verification failed." >&2
  exit 1
fi

echo "[PASS] Claude adapter is complete: RSE Orchestrator present, expected roster registered, routing metadata valid."
