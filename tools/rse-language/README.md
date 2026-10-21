# RSE Language Studio

One short instruction starts an RSE language run:

> Użyj $rse-language. Zrób tę książkę po polsku. Oryginał w załączniku.

> Użyj $rse-language. Dopracuj angielską wersję tej książki.

> Użyj $rse-language. Ulepsz oba artykuły Gentle Steps po polsku i angielsku.

The calling assistant performs the actual writing and specialist review. The
Python tool provides reproducible intake, immutable snapshots, guarded writer
packets, completeness/lock checks, review binding and working exports. No API key
is needed by the Python tool. This is not an unattended translation service.

## Run from the repository

Read `.agents/skills/rse-language/SKILL.md` or use the installed `$rse-language`
skill. Use the current language-tool branch/PR while it is unmerged. This addition
does not merge the older diverged Polish engine branches into main.

```bash
python3 scripts/rse-language.py prepare --source manuscript.docx --from en --to pl --project generic --mode localize --output work/book-pl
python3 scripts/rse-language.py packet --run work/book-pl --brief work/book-pl/functional-brief.json --output work/book-pl/writer-packet.ready.json
python3 scripts/rse-language.py check --run work/book-pl --candidate work/book-pl/candidate.json --packet work/book-pl/writer-packet.ready.json --output work/book-pl/check-01.json
python3 scripts/rse-language.py export --run work/book-pl --candidate work/book-pl/candidate.json --packet work/book-pl/writer-packet.ready.json --output work/book-pl/working-master.md
```

Between prepare and packet, the assistant completes the functional brief. Between
packet and check, it declares `change-scope.json`, assigns the returned `packet_sha256` to
`candidate.writer_packet_sha256` and writes/reviews the candidate. Cross-language
checks/exports require the validated `--packet` and its receipt sidecar.
An unfinished template cannot stand in for writing or review. Check output is
new-file-only; use a new numbered report after each revision.

For same-language work choose matching `--from`/`--to` and `--mode upgrade`.
Prefer `--scope bounded` for an article or diagnostic slice. The default scope is
`full_book`. For explicit literal numeric invariants use `--preserve-numbers`, or
declare per-segment `protected_numbers`; native wording of numbers still needs
meaning review.

Source formats: MD, TXT, JSON, DOCX and text PDF. PDF needs `pypdf` or `pdftotext`.
Scans need OCR and visual/source completeness review. DOCX extraction includes body paragraphs/tables and header/footer/note parts
with textboxes. Images, fields, tracked-change policy and reading order still
need explicit source inventory. This version exports working text/JSON, not a designed
DOCX or KDP book. Native DOCX/PDF proofs use the existing document/production tools.

## Project profiles

- `generic`: PL/EN house voice, placeholders and review contract.
- `gentle-steps`: current locked title, subtitle and labels; R6 body protected.
- `detective-academy`: existing PL R8/FINAL70 reuse and exact EN-freeze requirement.

`--profile path.json` can supply a project-specific extension. Keep the profile's
`project` equal to `--project`; reconcile against current owner locks before use.
Do not use `generic` to evade a known product freeze or content lock.

For Detective production a receipt must contain the exact source SHA-256,
`project: detective-academy`, `approved: true`, and the real owner approval
`reference`. The calling assistant verifies the referenced authority; a JSON
boolean does not create permission. Existing R8 designed proof remains authorized
and must not be replaced with a competing translation.

## Structured text and reviews

For precise segment protection use JSON with
`segments: [{id, text, protected?, protected_tokens?, protected_numbers?}]`.
The tool preserves those IDs and nontext data on export. Arbitrary JSON strings
are otherwise extracted by JSON pointer; classify metadata/IDs before authoring.

Candidate format is `rse-language-candidate-v1`, with `language`, `run_sha256` and
ordered `segments: [{id,text}]`. Keep every source ID exactly once. Full-section
omission requires an explicit contract change, not deletion from the candidate.

`check --reviews reviews.json` accepts actual hash-bound receipts. The bundle and
each receipt name the raw candidate file SHA-256. Required stages are
`native_language`, `meaning`, `audience`, `logic`; each includes `reviewer`,
`status: PASS` and substantive `evidence`. The assistant records actual independent
findings. Code checks bindings; it cannot prove quality or reviewer independence.

An unrun diagnostic means `DIAGNOSTIC_REQUIRED`; unresolved source defects, FIX,
BLOCK or OWNER_GATE entries prevent owner-read readiness. With a complete clean
diagnostic, missing reviews mean `LANGUAGE_REVIEW_REQUIRED`, even when
deterministic QA passes.
Complete receipts permit `OWNER_READ_CANDIDATE`, never owner approval, print
readiness or release. Text may not be silently shortened by layout/render agents.

## Verify

```bash
python3 scripts/test-rse-language.py
```

Use existing `scripts/localization-engine.py` QA/terminology/real-template guards
when present on the authorized engine branch. This facade supplements that engine
and does not declare absent checks PASS. Current reviews, physical proofs,
publication and production integration remain distinct evidence.

A real isolated-writer trial and actual review receipts are retained under
`tools/rse-language/trial-2026-10-21/`. It deliberately preserves three ambiguous
source rules and demonstrates the final OWNER_GATE instead of a false readiness
claim. This is evaluation evidence, not a production game release.
