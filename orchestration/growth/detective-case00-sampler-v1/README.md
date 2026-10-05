# Detective CASE 00 Sampler V1

Status: NON-PRODUCTION / SOURCE-LOCKED GROWTH SUPPORT
Deployment: NOT DEPLOYED
Paid services: NONE

## Current source lock
Pinned to the current Detective V10 owner-read candidate:
- branch: `feature/detective-en-premium-content-upgrade-20261005`
- commit: `bb76fb19710247800ff0bd6d263c4cf4fcaa165d`
- file: `orchestration/detective/content-upgrade/detective-en-premium-v1/OWNER_READ_CANDIDATE_EN_PREMIUM_V10.md`
- blob: `19df709e381445a6f5a52d7b0c1c898bd5b706be`
- product state: OWNER_READ_CANDIDATE / CONTENT NOT YET FROZEN

The exact six Case 05 clues and all three book Hint Vault levels are reused; no new puzzle truth is invented.

## Deterministic proof
Run `node verify.mjs`. It enumerates all 720 symbol orders and requires exactly one valid order:

`BALL -> STAR -> BOLT -> HEART -> KEY -> MOON`

## Release boundary
This sampler is support-only and fail-closed:
- no deployment until the Detective release source is explicit and this lock is revalidated;
- full-book CTA stays disabled until a verified live listing URL exists;
- no account, backend, external analytics library, paid service, vendor dependency, secret or signing key;
- no Detective product-source mutation;
- no KDP/Play publication, production deploy, spend or owner-gate crossing.

## Growth OS adoption gate
PASS: this extends existing static-web capability; no new tool/vendor/agent is introduced.
