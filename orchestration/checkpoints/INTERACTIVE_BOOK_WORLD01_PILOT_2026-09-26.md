# Interactive Book Factory — World 01 bounded real pilot checkpoint

Date: 2026-09-26

Status: **PASS for a source-backed English mission-overview candidate; full story and release gates remain open**

## Proven

- Contract audit: two historical v0 validators coexist with different schema keys, activity allow-lists, and locale policies. `scripts/validate-interactive-book-pack.py` plus `orchestration/architecture/fixtures/interactive-book/synthetic_world.valid.json` is the active CI contract used for this candidate. The separate `scripts/validate-rse-interactive-book-pack.py` accepts its older `interactive-book-v0/synthetic-world-valid.json` fixture, but it is not the candidate validator. Both historical synthetic fixtures passed locally. A future full-story graph should consolidate these contracts before runtime implementation.
- The owner-supplied 108-page paperback is available read-only, hashed, visually inspected for the candidate pages, and recorded without committing the binary. Its source record and the older flattened-master record remain distinct.
- The existing v0 validator accepts the three-activity, English-only `info_card` candidate. Activity IDs are language-neutral, copy is separate from behavior, and the candidate contains no image dependency or account/entitlement logic.
- The dedicated provenance validator ties all nine product copy fields (title, objective, key for each of three cards) to locked page evidence and rejects extra app copy, unapproved locale claims, incorrect source hash/page, and changed runtime behavior. With `--pdf`, it also verifies the actual private binary and page text.
- The derivative audit found specific speaker/scene divergences. No app-only subtitle or scene copy was promoted as canonical.

## Not proven / blocked by source work

- Complete story parity: **0/10 missions**. The candidate is **3/10 mission opener cards (30%)**, **3/108 pages of direct pack evidence (2.78%)**.
- Published speaker/order parity, console/quest/secret-code parity, visual asset rights/transfer, all remaining mission openers, and equivalence with the prior flattened master.
- `pl-PL` copy, Polish quality gate, accessibility review for rich content, UI fit, science/health claim review, and release readiness. `pl-PL` is planned in one runtime but is not a supported locale in this candidate.

## Next bounded slice

Transcribe and visually audit **Level 1 pages 16–22** at dialogue/console/quest/code granularity, including speaker IDs and order, then add a source-verified complete Level 1 content graph with the same provenance check. Do not ingest Level 2 dialogue from the app until the confirmed page-26 speaker errors are resolved against the paperback.

No deployment, backend creation, pricing, store publication, user migration, or merge to main was performed.
