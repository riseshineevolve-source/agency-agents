# Commands and observed results

Paths are absolute where passed that way. All writes were under `/workspace/scratch/e6eabdc4c3a0/tool-trial`. The CLI directory was read/executed only.

## Main workflow, in order

```bash
python3 /workspace/scratch/e6eabdc4c3a0/rse/scripts/rse-language.py prepare --source /workspace/scratch/e6eabdc4c3a0/tool-trial/source.json --from en --to pl --mode localize --project generic --scope bounded --preserve-numbers --output /workspace/scratch/e6eabdc4c3a0/tool-trial/run
```

Exit 0: PREPARED, 2 segments. The supplied JSON was created locally using `json.dumps(..., ensure_ascii=False, indent=2) + '\n'` before preparation.

```bash
python3 /workspace/scratch/e6eabdc4c3a0/rse/scripts/rse-language.py packet --run /workspace/scratch/e6eabdc4c3a0/tool-trial/run --brief /workspace/scratch/e6eabdc4c3a0/tool-trial/run/functional-brief.json --output /workspace/scratch/e6eabdc4c3a0/tool-trial/run/writer-packet.json
```

Exit 2: `BLOCK`, `Refusing to overwrite: .../run/writer-packet.json`. The prepare-created placeholder was retained.

```bash
python3 /workspace/scratch/e6eabdc4c3a0/rse/scripts/rse-language.py packet --run /workspace/scratch/e6eabdc4c3a0/tool-trial/run --brief /workspace/scratch/e6eabdc4c3a0/tool-trial/run/functional-brief.json --output /workspace/scratch/e6eabdc4c3a0/tool-trial/run/writer-packet.validated.json
```

Exit 0: READY_FOR_NATIVE_WRITER. The fresh author wrote `candidate.authored.json` from this packet.

```bash
python3 /workspace/scratch/e6eabdc4c3a0/rse/scripts/rse-language.py check --run /workspace/scratch/e6eabdc4c3a0/tool-trial/run --candidate /workspace/scratch/e6eabdc4c3a0/tool-trial/run/candidate.authored.json --output /workspace/scratch/e6eabdc4c3a0/tool-trial/run/check.initial.json
```

Exit 2: `BLOCK`, `Localization requires --packet from the completed functional brief`. This was after the parent updated the CLI; no `check.initial.json` was produced. Help and skill were reread.

```bash
python3 /workspace/scratch/e6eabdc4c3a0/rse/scripts/rse-language.py packet --run /workspace/scratch/e6eabdc4c3a0/tool-trial/run --brief /workspace/scratch/e6eabdc4c3a0/tool-trial/run/functional-brief.json --output /workspace/scratch/e6eabdc4c3a0/tool-trial/run/writer-packet.bound.json
```

Exit 0: READY_FOR_NATIVE_WRITER, packet hash and receipt sidecar. The original isolated author reread this packet and receipt, applied the one reviewer correction and wrote `candidate.final.json` with `writer_packet_sha256`.

```bash
python3 /workspace/scratch/e6eabdc4c3a0/rse/scripts/rse-language.py check --run /workspace/scratch/e6eabdc4c3a0/tool-trial/run --candidate /workspace/scratch/e6eabdc4c3a0/tool-trial/run/candidate.final.json --packet /workspace/scratch/e6eabdc4c3a0/tool-trial/run/writer-packet.bound.json --output /workspace/scratch/e6eabdc4c3a0/tool-trial/run/check.before-final-receipts.json
```

Exit 0: LANGUAGE_REVIEW_REQUIRED; deterministic PASS; specialist_reviews NOT_RUN. This deliberately records the honest pre-receipt state.

```bash
python3 /workspace/scratch/e6eabdc4c3a0/rse/scripts/rse-language.py check --run /workspace/scratch/e6eabdc4c3a0/tool-trial/run --candidate /workspace/scratch/e6eabdc4c3a0/tool-trial/run/candidate.final.json --packet /workspace/scratch/e6eabdc4c3a0/tool-trial/run/writer-packet.bound.json --reviews /workspace/scratch/e6eabdc4c3a0/tool-trial/run/reviews.final.json --output /workspace/scratch/e6eabdc4c3a0/tool-trial/run/check.final.json
```

Exit 0 at that time: OWNER_READ_CANDIDATE, deterministic PASS, four actual specialist stages. This precedes the parent's later source-issue gate; source timing/restart/pass ambiguities are now explicitly open OWNER_GATE ledger items, and the parent owns the current rerun/checkpoint. Transfer-preservation PASS is not a complete playable-game proof. Receipt aggregation asserted every source receipt's stage, final hash and actual overall PASS before assembling the bundle.

```bash
python3 /workspace/scratch/e6eabdc4c3a0/rse/scripts/rse-language.py export --run /workspace/scratch/e6eabdc4c3a0/tool-trial/run --candidate /workspace/scratch/e6eabdc4c3a0/tool-trial/run/candidate.final.json --packet /workspace/scratch/e6eabdc4c3a0/tool-trial/run/writer-packet.bound.json --output /workspace/scratch/e6eabdc4c3a0/tool-trial/export/polish-guide.json
```

Exit 0: WORKING_EXPORT. The payload was read in full and checked for exact candidate segment equality, stable IDs and unchanged metadata. The reader TXT joins the two exported text fields with one blank line.

## Existing localization-engine validation

```bash
python3 /workspace/scratch/e6eabdc4c3a0/rse/scripts/localization-engine.py inventory --source /workspace/scratch/e6eabdc4c3a0/tool-trial/source.json --output /workspace/scratch/e6eabdc4c3a0/tool-trial/engine-inventory.json
python3 /workspace/scratch/e6eabdc4c3a0/rse/scripts/localization-engine.py extract --source /workspace/scratch/e6eabdc4c3a0/tool-trial/source.json --plan /workspace/scratch/e6eabdc4c3a0/tool-trial/engine-plan.json --revision sha256:46fbf894591c73acab01aa54faedbf841bb2e46847fb5e95eeac7ae8651151ad --output /workspace/scratch/e6eabdc4c3a0/tool-trial/engine-check
python3 /workspace/scratch/e6eabdc4c3a0/rse/scripts/localization-engine.py qa --manifest /workspace/scratch/e6eabdc4c3a0/tool-trial/engine-check/source-manifest.json --targets /workspace/scratch/e6eabdc4c3a0/tool-trial/engine-check/targets.final.pl-PL.json --current-source /workspace/scratch/e6eabdc4c3a0/tool-trial/source.json --output /workspace/scratch/e6eabdc4c3a0/tool-trial/engine-check/qa.final.json
```

All exit 0. QA: REVIEW; 2/2 mapped, 2 deterministic passes, 0 errors, 0 engine-language approvals, 4 open review items. Targets were populated from final candidate text and left `review_status: draft`; no engine approval was fabricated. The generic fixture uses no product-specific term IDs.

## Other failed or nonzero invocations

From `rse`:

```bash
git status --short --branch && git rev-parse HEAD && rg --files -g 'AGENTS.md' -g '*lock*' -g '*checkpoint*' -g '*premium*' -g '*PREMIUM*' -g '*native*' -g '*family*' -g '*review*' tools/rse-language orchestration specialized
```

Exit 128 at first command: `fatal: not a git repository (or any of the parent directories): .git`. Later commands did not execute.

The first creation attempt requested workdir `/workspace/scratch/e6eabdc4c3a0/tool-trial` before that directory existed, with this exact command text:

```bash
mkdir -p /workspace/scratch/e6eabdc4c3a0/tool-trial && python3 - <<'PY'
import json
from pathlib import Path
p=Path('/workspace/scratch/e6eabdc4c3a0/tool-trial')
s={'segments':[{'id':'intro','text':'December is busy. You can take a short break together.'},{'id':'game','text':'For 2 minutes, one person starts with a quiet sound. The next person repeats it and adds a sound. Anyone may pass. If you lose the order, start again. Stop when everyone has had a turn. Keep the timer label {minutes}.'}],'edition':'test','year':2026}
(p/'source.json').write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
PY
python3 /workspace/scratch/e6eabdc4c3a0/rse/scripts/rse-language.py prepare --source /workspace/scratch/e6eabdc4c3a0/tool-trial/source.json --from en --to pl --mode localize --project generic --scope bounded --preserve-numbers --output /workspace/scratch/e6eabdc4c3a0/tool-trial/run
```

The process did not start: `exec-server rejected request (-32603): No such file or directory (os error 2)`. No shell command in that request ran. Recovery: `mkdir -p /workspace/scratch/e6eabdc4c3a0/tool-trial` from the existing parent directory, then the source/prepare commands from the new directory.

From `rse`:

```bash
sha256sum scripts/rse-language.py tools/rse-language/profiles/generic.json && rg --files -g 'AGENTS.md' /workspace/scratch/e6eabdc4c3a0 /root/.codex/skills/remote-skills/rse-language
```

Exit 1: hashes printed successfully; `rg` found no AGENTS.md. This is a negative discovery result.

From `tool-trial`:

```bash
cat run/candidate.authored.json run/author-notes.json && sha256sum run/candidate.authored.json
```

Exit 1: candidate printed; optional author-notes file did not yet exist, so sha256sum did not execute. The author later created notes during the bounded correction; its initial SHA had already been computed by the author and independently by reviewers.

```bash
sha256sum run/writer-packet.validated.json run/writer-packet.bound.json run/functional-brief.json run/source.json source.json && cmp -s run/writer-packet.validated.json run/writer-packet.bound.json; test $? -eq 0
diff -u run/writer-packet.validated.json run/writer-packet.bound.json
```

Each exit 1 was expected: packets differ after the parent's CLI update. Diff showed only added voice and per-segment protected-token/number constraints. The functional brief and source bytes remained unchanged.

## Read-only discovery and documentation

Read the installed skill and workflow/examples, the local bootstrap/mailbox, generic profile, applicable specialist roles, and localization-engine README. Ran `rse-language.py --help`, each of its four subcommand helps, and localization-engine `--help`, `qa --help`, `qa-suite --help`, `extract --help`. Re-ran current check/export/packet help after the parent update. These calls succeeded. No regression test suite was run because this was a content workflow and no implementation change was made by this agent.
