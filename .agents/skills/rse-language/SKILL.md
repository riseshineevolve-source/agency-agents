---
name: rse-language
description: Create natural Polish or English RSE book editions from an original, or improve an existing language version. Use for translate, localize, native rewrite, premium content upgrade, popraw polski/angielski or zrób książkę po polsku/angielsku. Preserve approved text, facts, games, puzzle solutions, character voices and terminology. Support manuscripts, activities, articles and UI; consume RSE localization tools and project locks.
---

# RSE Language Studio

Accept short requests such as `Zrób tę książkę po polsku`, `Improve the English`, or `Dopracuj te artykuły`. Infer project, audience, scope and voice from current project files. Ask only for genuinely missing source/target language or a material owner choice. Do the writing and review, not just preparation.

## Resolve current authority

Use GitHub `riseshineevolve-source/agency-agents`. Read this lane's bootstrap and mailbox plus relevant project checkpoint/locks. Read [workflow.md](references/workflow.md) and the relevant profile in `tools/rse-language/profiles/`. Find the current feature branch from the mailbox or open PR; a file on an unmerged branch is not on main. Inspect existing local work before changing branches. Never blindly merge diverged engine branches.

Author localization-owned candidates/tooling and this lane's mailbox. Let the product writer consume the result. Preserve the current product master. Do not modify a website, app, Book Factory renderer or another lane's mailbox through this skill.

Locate `scripts/rse-language.py` on the current reviewed language-tool branch. If absent from the checkout, fetch the exact path/profile from the language-tool PR linked in the mailbox, pin its commit and run locally. If repository access fails, preserve the last checkpoint and report the actual blocker. Never fabricate a GitHub save or CI result.

## Execute

1. Inventory relevant versions, hashes and approvals. Newest is not automatically best. Save immutable baseline bytes and create a separate working master. Register accepted/strong segments as GOLDEN_KEEP. Record source conflict instead of mixing editions silently.
2. Choose `upgrade` when source and target language match; `localize` otherwise. Honor an explicit route. For creative localization first extract a wording-free function brief, then have a fresh native writer work from that brief. Reopen original wording only for meaning/backcheck. Keep legal/privacy/regulated passages on a conservative meaning-preserving route; never creatively re-author those passages.
3. Run preparation, for example:

   `python3 scripts/rse-language.py prepare --source manuscript.docx --from en --to pl --mode localize --project generic --output work/book-pl`

   The CLI snapshots/extracts/checks; it does not generate prose. Complete the brief, truth/mechanics/voice/repetition maps, classify KEEP/FIX/BLOCK/OWNER_GATE, and write the actual candidate. Use stable IDs; include captions, dialogue, hints, solutions, instructions, front/back matter and intended exclusions explicitly.
4. For cross-language work, use the CLI `packet` command after completing the functional brief. Assign the returned `packet_sha256` to `candidate.writer_packet_sha256`; pass the validated `--packet` path to cross-language `check`/`export`. Keep its receipt sidecar. Give only that generated packet to the native writer. Do not send source sentences, a literal draft or an existing translation to this first writer. Exact brand strings and necessary clue/pun tokens are permitted as declared locks. Never create a literal intermediate draft as a shortcut.
5. Assign one candidate writer. Other agents review independently, returning segment IDs, KEEP/FIX/BLOCK/OWNER_GATE, evidence and targeted fixes. Use up to four useful specialists, batching compatible concerns. Run actual reviewers; listing role names is not evidence they ran. Apply only fixes that solve a concrete defect; KEEP beats needless rewrite.
6. Protect segments outside the declared change allowlist, previous freezes, immutable truth and dependency closure. After each edit compare actual vs allowed changed IDs and protected hashes. Revert collateral drift. Do not serially rewrite the whole book through every reviewer.
7. Run `check` on the exact candidate with real hash-bound review receipts. Inspect the report and resolve material defects. Re-run after changes; stale receipts cannot approve new wording. Deterministic PASS is not native-language, semantic or print approval. Use existing `scripts/localization-engine.py` validators, project profiles and terminology when available and applicable; record NOT RUN when unavailable rather than bypassing them silently.
8. Read the complete candidate at initial diagnostic, before owner reading/content freeze, and after structural changes. After a bounded fix inspect changed units, neighbors, dependency closure and global invariants. Audit repeated functions/mechanics as well as words. Stop rewriting once substantive defects are resolved.
9. Save the exact candidate, clean reader-facing manuscript, source inventory, GOLDEN_KEEP, content map, issue ledger, QA evidence and hashes. Keep internal metadata out of reader pages. Use document/PDF skills for an owner-read proof when requested or required; render the exact candidate hash. Maintain DRAFT → PREMIUM_WORKING → OWNER_READ_CANDIDATE → CONTENT_APPROVED → FROZEN_CONTENT; print and release are separate gates.
10. Commit to a dedicated feature branch/PR. Update only `orchestration/control-plane/mailboxes/polish_localization.yml` with reusable paths, source/candidate hashes, tests, actual CI state and consumer handoff. Do not merge main, publish, grant a freeze or authorize release without explicit user instruction. A mailbox write does not wake another chat or prove acknowledgment.

## Language and truth

Write as a strong native author for the actual reader. Retain sense, function, facts, chronology, relationships, numbers, negation/modality, puzzle truth, mechanics, consent, safety and claim strength. Rebuild sentence structure, humor and rhythm where needed. Preserve good approved wording in same-language editing.

PL: contemporary, idiomatic, precise; no calques, coaching/wellness filler, forced youth slang, baby talk, mechanical gender slashes or long dash as a sentence hinge. Read aloud and inspect book register. EN: natural idiom, coherent variety inferred from source/project, contractions when appropriate; no Polish-shaped syntax or forced sentiment. Do not equalize sibling campaign wording merely to make paragraphs look parallel.

For activities retain who starts, order, timing/counts, resets, ending, variants, consent and necessary instructions. Clarity beats brevity. For marketing distinguish teasers from playable instructions; never expose an entire calendar day accidentally or invent availability, benefits or purchase links.

## Current project exceptions

- Gentle Steps: protect the 24-day body/R6; use October 13 campaign locks over obsolete PDF labels. PL `ŚWIĘTA SĄ TEŻ PO DRODZE`; EN `BEFORE CHRISTMAS SLIPS BY`. Keep the packaging subtitle separate from the short strapline. Read the live campaign master, not just bundled defaults. Article work does not authorize rewriting book/app masters.
- Detective: reuse verified PL V04 R8, FINAL70 and four zero marks. Do not start a competing translation. Designed proof of that candidate is already authorized. Migrating to a later EN master/full production localization needs explicit source authority/freeze for the exact hash; historical V10 freeze does not authorize later EN editions. Use the CLI freeze receipt rather than a boolean assertion in chat.
- Generic new books: derive a profile before volume production, calibrate across content types, complete one whole logical unit, then scale in bounded batches. Do not import Advent/Detective locks into unrelated books.

## References

- [Workflow and review contract](references/workflow.md): read before execution.
- [Invocation examples](references/examples.md): use to resolve short requests or demonstrate the tool.

Never call a candidate PRINT_READY from text-only QA. Complete safe authorized work before stopping at a genuine owner/source/freeze/release gate.
