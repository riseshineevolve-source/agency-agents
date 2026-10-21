# World App Factory: Level 19 source recovery

Date: 2026-10-21 (Europe/Warsaw)
Scope: World lane source only; no central priorities or other lane sources changed.

## Source lock and recovery

- Canonical World 02 paperback: ISBN `9798249971823`, 104 pages, 66,576,954 bytes.
- SHA-256: `e94d2937cc459a5c7c3c5968c64ba39f2a03702f929488e42b00b5db3f9f7f76`.
- Current-main base observed: `e99dec925fa1f3edf2f69ed4fe20c218b0f936cb`.
- Recovery branch: `codex/world02-level19-recovery-20261021`.
- Recovered only the exact evidence and typed pack from
  `19d31c8c8c36aafa75516861926146d8b0ed67b3` on
  `codex/world02-level19-canonical-pack-20261008-run3`.
- No wholesale merge of the diverged branch. The similarly named
  `codex/world02-level19-source-graph-20261008-clean` has no Level 19 pair.

Level 19 is **The Pivot Dance**, pages 79–85, 25 ordered nodes;
family code **WE ARE PIVOTING!**. IDs and all source copy are unchanged.

| Artifact | SHA-256 |
|---|---|
| `orchestration/content-sources/world02-level19-page-evidence.json` | `3015f761c6b431831f4646175ae6902c1b4e08f311d5b777a1ea888e6906a69c` |
| `orchestration/content-packs/world02/level19.en.candidate.json` | `fd9cf11a23465f9b62e6d6eead0e0a576bc6dd7c033642ad934aab03df82fafb` |

## Implementation and validation

Builder/validator now admit the bounded Level 19 specification. The existing
Interactive Book Contract workflow rebuilds and validates it and runs the new
10-test source-lock suite. Rebuilding preserves the recovered pack byte for byte.

Local checks: Level 19 10/10 PASS; existing World 02 graph 24/24 PASS;
Level 18 5/5 PASS; World 01 graph 43 PASS and six private-PDF-dependent skips;
World 01 provenance candidate and twelve adversarial mutations PASS.
These are local results, not a claim about a new hosted run.

## Open gates and next work

- World 02 remains hidden. Runtime PR #11 remains open at
  `42465032c7e103bbfe6cc8326843d38fa61a3568`, adding Level 18 to main's 11–17.
- Runtime import of Level 19 requires this exact source pair to be durable and
  a verified narrow integration. Shared heading omission is a separate runtime fix.
- Printed child-safety/science concerns remain open: p82 indoor beach electrical
  arrangement, p84 prediction/pain and blood-oath wording, p85 stress-chemical
  claim. Preserve exact extraction; no public release approval is implied.
- Level 20 and endgame JSON are not present in inspected Git refs. Historical
  local-graph claims are unverified until actual files are recovered. Level 20
  transcription/validation exists; endgame pages 93–104 need explicit coverage.
- No deployment, production merge, backend, pricing, auth, rewards mechanics,
  source freeze or Polish source approval occurred. Gentle Steps remains independent.
