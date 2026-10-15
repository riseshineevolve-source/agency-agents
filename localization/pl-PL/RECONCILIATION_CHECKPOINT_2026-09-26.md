# Polish Localization Engine: current-main reconciliation

- Date: 2026-09-26
- Branch: `codex/polish-engine-main-reconcile`
- Starting HEAD: `7a0b1d7`
- Current main integrated: `ff091c9`
- Proven source: `rse/polish-localization-engine-v1@f9d9386`

## Files brought forward

The source branch was compared against current main. Its localization-only delta
was ported as 55 files: all 26 `localization/pl-PL/` contracts, terminology,
style rules, fit specification and golden fixtures; 17 localization scripts,
tests and the `check-divisions.sh` registry adjustment; the dedicated regression
workflow; nine specialist role definitions; their RSE roster entries; and the
Polish localization runbook.

The current main branch was merged first. Older source-branch portfolio,
marketing and orchestration edits were not imported. This retains current main's
2026-09-26 Detective and Gentle Steps operating state, including the parallel
lane and owner-gate checkpoint.

## Reconciliation decisions

- The engine architecture, hash-bound source/target approvals, backcheck
  provenance, fit verifier, canonical `terminology.json`, forbidden AI-ism list
  and all seven accepted fixture sets were kept intact.
- `scripts/check-divisions.sh` now classifies `localization/` as an infrastructure
  directory, so the existing division validator remains correct when these
  resources are tracked.
- `DETECTIVE_PL_EXECUTION_CHECKPOINT.md` now reflects the current 146-page
  English candidate and its open visual-system/physical-proof/freeze gates.
  The page count is not used as a substitute for the later frozen source hash.
- Historical calibration fixtures remain evidence of their accepted bounded
  scopes; none is promoted to a full-book Detective translation or a real
  Gentle Steps template-fit proof.

## Local verification

Run with Python 3.12.14, PyYAML 6.0.3 installed into ignored
`build/localization-deps/`, and that directory on `PYTHONPATH`:

| Command | Result |
|---|---|
| `python scripts/localization-engine.py terms-doc --check` | PASS |
| `python scripts/test-localization-engine.py` | PASS, 55 tests |
| `python scripts/test-localization-backcheck.py` | PASS, 5 tests |
| `python scripts/test-localization-fixtures.py` | PASS, 7 accepted fixtures, 31 bilingual segments, 5 Detective logic anchor groups |
| `python scripts/validate-polish-localization.py` | PASS, 7 accepted fixtures, 37,159 candidate characters |
| `bash scripts/check-divisions.sh` | PASS, 18 divisions |
| `bash scripts/check-runbooks.sh` | PASS, 4 runbooks, 64 agent references |
| `bash scripts/lint-agents.sh` on the nine new roles | PASS, 0 errors; 36 nonblocking recommended-section warnings |
| `bash scripts/check-agent-originality.sh` on the nine new roles | PASS |
| `bash scripts/check-tools.sh` | PASS, 16 tools |
| `python scripts/check-hermes-plugin.py` | PASS |
| `bash -n` on the division and RSE installer scripts | PASS |
| `bash scripts/test-convert-frontmatter.sh` | PASS, Gemini CLI/OpenCode/Qwen frontmatter |
| `bash scripts/test-agent-selection.sh` | PASS |

Windows shell checks used Git Bash with `/usr/bin:/bin` on `PATH`, the bundled
Python exposed as `python3`, and `PYTHONUTF8=1` for the originality scan.
The generated `build/localization-proof/summary.md` has zero deterministic
errors and 31/31 mapped segments; its aggregate status is **REVIEW** with 34
open fit or provisional-terminology items. This is the expected evidence
boundary, not a publication PASS.

## Remaining gates

- Detective English interior is **not frozen**. Owner visual review, physical
  proof, explicit English freeze, source/alias hash receipt and later bilingual
  and real-layout review precede full Polish production.
- Gentle Steps Week 1 remains a language candidate. The four accepted headings
  need genuine editable-template renders at print scale; proxy fit is not PASS.
- Pull-request CI still needs to run the full cross-tool converted-output
  invariant check. Its manifest drift is advisory for agent additions on PRs;
  maintainers regenerate `scripts/convert-outputs.sha256` when landing to main.
- No full Detective translation, merge to main, KDP publication or other
  publication occurred in this reconciliation.
