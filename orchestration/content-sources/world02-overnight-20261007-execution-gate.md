# World 02 overnight source-contract handoff — 2026-10-07

Ownership: World 01/02 Interactive App Factory only. This is a non-mergeable dependency checkpoint, not an app release or authoritative replacement for the canonical paperback.

## Live baseline at verification
- agency-agents/main: 3523ab1d770612032c03025a01de3d507830910f
- spark-joy-fam/main: 23c2cf36988a41b785d1409d28488c6b7acbe08f (runtime Levels 11–17)
- Level 18 candidate branch: codex/world02-level18-clean-candidate-20261007 (diverged, 8 ahead / 47 behind main at verification)
- Level 18 content pack blob: 0cd3be9f1657741cce1dd9b9dca12be5e803a0b5
- Level 18 locked page-evidence blob: cb2114bd754923cd5f671113a9f5201de2e79bf0
- Stale PR #35 is draft/non-mergeable; do not merge.

## Independent Level 18 read-only parity check
24/24 nodes and records on published pp. 72–78. Zero pack/evidence mismatches for IDs, type/subtype, speaker, next_id, page/evidence provenance, or exact localized fields. Expected types: opener 1, system_log 6, dialogue 10, console 3, quest 2, science 1, secret_code 1. Family code: I NEED GREEN ENERGY. Canonical paperback SHA-256: e94d2937cc459a5c7c3c5968c64ba39f2a03702f929488e42b00b5db3f9f7f76.

## Write and CI gate
This branch was created from verified agency-agents/main. Its Level 18 canonical-validation markdown was successfully copied. Further standard GitHub contents writes for Level 18 extraction, evidence JSON, and typed pack were rejected by connector write-safety. An attempt to extend scripts/validate-world02-graph.py on the existing candidate branch was also rejected. No alternate low-level git write path was used. No Level 18 validated PR or exact-head contract workflow exists on this branch. Older green workflows cover only Levels 11–17; they must not be represented as a Level 18 CI pass.

## Safe continuation
Once normal authorized contents writes work, consolidate exactly the two locked L18 blobs from clean-candidate into a fresh main-based World lane branch; extend builder (11–18), validator mission spec (24 nodes; pp72–78; exact types), adversarial tests and BOTH workflow triggers plus build/validate steps for 18. Verify deterministic rebuild diff-clean and exact-head Interactive Book Contract before bounded PR/merge. Then proceed to source-proven Level 19 and 20 typed/evidence pairs, separate Android exact-head CI and shared runtime integration, and pp93–104 only where canonical page evidence exists. Preserve World 02 production-nav hiding until complete. No PL, invented XP mechanics, backend, signing, Play upload, or central control-plane changes.
