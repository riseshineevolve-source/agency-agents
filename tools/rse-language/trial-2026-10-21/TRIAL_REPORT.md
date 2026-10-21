# Local RSE Language trial

Completed the normal bounded en→pl workflow for the supplied two-segment family guide. No remote services were used, no repository implementation was changed, and no review result was invented.

## Produced

- `export/polish-guide.json`: reconstructed source-shaped Polish payload. IDs, `edition: "test"`, `year: 2026`, digit `2` and `{minutes}` are preserved.
- `export/polish-guide.txt`: clean text, with both supplied text fields and no QA metadata.
- `run/candidate.final.json`: exact reviewed candidate.
- `run/functional-brief.json`, `writer-packet.bound.json` and its receipt: wording-free handoff and current CLI binding.
- `run/source-inventory.json`, `golden-keep.json`, `content-map.json`, `change-scope.json`, `scope-invariants.final.json`, `issue-ledger.json`, and immutable source/initial-target snapshots.
- Four actual final review receipts and `run/reviews.final.json`, plus retained first-pass reviews.
- `run/check.final.json`, `run/qa-summary.json`, and `engine-check/qa.final.json`.

| Artifact | Raw-byte SHA-256 |
|---|---|
| source.json and run/source.json | 46fbf894591c73acab01aa54faedbf841bb2e46847fb5e95eeac7ae8651151ad |
| first authored candidate | a00cf5b64d347206e6ee30d93ad5a07ce8a250a23e94b23a943a1c6f2cd22905 |
| final candidate | 1fff0878dd99472827fd9f0633576a3be46b7c33ad17d28afe41db3892989983 |
| current writer packet | 710bdea889818fa676e5b7c815c4e012263c18fdd77c3d0c425e34ba3a29ddbe |
| exported Polish JSON | 235186a96dd3917cdae7a91d448037c311e00c93c896ae43852edf270162485e |

## Actual writing and reviews

The first author was a fresh agent with no inherited conversation. It read only the generated wording-free packet and the assigned native-family-writer role. It later read the updated bound packet, its receipt and its own output. It did not read the English source. `run/author-notes.json` records its actual inputs.

Three independent review agents performed four stages: native-language/book register; bilingual meaning/mechanics; audience/family ear/consent; logic/continuity. They read all two segments. The native reviewer found one concrete collocation defect: `gdy każdy będzie już po swojej kolejce` → `gdy każdy będzie już po swojej turze`. The sole author applied that correction. Intro remained unchanged. All reviewers then read the complete final candidate, independently computed its hash and issued fresh receipts. All four final stages returned PASS. The CLI receipt bundle is an aggregation of those actual reports, not synthetic reviews.

The check performed during the trial returned `OWNER_READ_CANDIDATE`, deterministic PASS, and all four specialist stages. The export returned `WORKING_EXPORT`. That check predates the parent's additional source-issue gate. The transfer-preservation and Polish-language review PASS does **not** establish a complete ready-to-use game proof: three source-clarity OWNER_GATE items remain open in the issue ledger. The parent will rerun/checkpoint the current gating; this agent did not rerun after that patch. No owner approval, freeze, print approval or release authority was granted.

The existing localization engine also ran inventory, extraction and QA on a separate bounded book contract. It reported 2/2 mapped segments, 2 deterministic passes and zero errors. Its overall state remains REVIEW: two missing surface-fit budgets and two engine-specific semantic-review bindings. The rse-language receipts are a different contract and were not represented as imported engine approvals.

## Gaps and limitations observed

1. The provided `rse` directory is a sparse tool workspace without `.git`. Local branch/commit freshness could not be verified. Remote work was explicitly excluded from this trial; the parent owns repository persistence and CI.
2. `prepare` creates a placeholder `writer-packet.json`. My first attempt to use that same path for `packet --output` correctly refused to overwrite it. A distinct validated packet path worked.
3. The parent updated the CLI during this trial. Initial help lacked `check/export --packet`; the first check then required it. I reread the updated skill/help and regenerated a bound packet plus sidecar. The writer added `writer_packet_sha256` and reread the new packet. The old and new packets are retained. The new packet also carries the voice and explicit per-segment token/number constraints.
4. Initial script SHA-256 was `5e7906ff1895444c8a089eaed02c0f26b0bee23240ed3ca6463986bb9242ed16`; the final observed script SHA-256 was `28786cdac0dddc2654d307ee000ccf212c072ac329c9815e6c8246e5b4574935`. I did not modify either version.
5. The source leaves duration versus completion precedence, restart scope/turn counting, and passing versus completion partly unspecified. These are recorded in the actual meaning review and explicitly remain open material OWNER_GATE items in the issue ledger. They affect playability, while transfer-preservation review can pass. No new rule was invented and no source fix was fabricated.
6. The final timer-label sentence is intentionally part of the supplied fixture text. It remains in the game segment. Its editorial nature was raised by the Polish-only reviewer and resolved against the required input coverage; it was not silently removed or relocated.
7. No PDF/layout/device/print proof, human-family read-aloud, remote commit or CI was run. This short plain-text/JSON trial does not require a designed proof.

Exact CLI commands and nonzero/failed invocations are in `COMMANDS.md`. Setup and artifact derivation were local Python/file operations inside `tool-trial` only. Source and initial/first-authored snapshots were made read-only after verification.

## Final guard after source-diagnostic repair

The parent reran the strengthened current CLI against unchanged final candidate and real final reviews. `CHECK.final.json` now returns OWNER_GATE for the three recorded source-game ambiguities, with deterministic QA PASS. The earlier OWNER_READ_CANDIDATE result above is historical and superseded for readiness. The standalone tool has 31 passing regression tests. A correct transfer is not a complete usable-game proof. Source authority was not invented and no user decision is needed for this synthetic trial fixture.
