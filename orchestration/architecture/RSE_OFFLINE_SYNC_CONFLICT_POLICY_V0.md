# RSE Consumer Platform — Offline Sync Conflict Policy v0

Status: SYNTHETIC CONTRACT / NO DEPLOYMENT AUTHORIZATION
Updated: 2026-09-20

## Purpose

Define deterministic merge behavior for ordinary RSE Consumer apps that must continue to work offline and later synchronize without silently losing newer or stronger state.

One generic `last write wins` rule is forbidden.

## Data-class rules

### 1. Progress state

States are ordered:

`not_started < in_progress < completed`

Default merge for the same account/profile + product + content item:
- choose the stronger monotonic completion state;
- never downgrade `completed` because an older/offline device reports `in_progress` or `not_started`;
- preserve the maximum compatible checkpoint/progress marker when the content version remains compatible;
- if content versions are incompatible, preserve both records for explicit migration logic rather than guessing.

Examples:
- server `in_progress`, client `completed` -> `completed`;
- server `completed`, client `in_progress` -> `completed`;
- server `not_started`, client `in_progress` -> `in_progress`.

### 2. Preferences

For non-sensitive preferences such as locale or display settings:
- use explicit revision numbers;
- higher valid revision wins;
- equal revision with conflicting values is a conflict, not an arbitrary timestamp winner;
- invalid/unsupported locale never overwrites a valid locale.

### 3. Entitlements

Entitlements are **server-authoritative only**.

Offline/client state may cache access for a bounded UX policy later approved by product/security review, but sync must never:
- create ownership;
- extend expiry;
- clear revocation;
- promote a different product entitlement;
- treat an old cached purchase as stronger than current server state.

### 4. Privacy/delete state

Deletion/export requests are server-authoritative lifecycle records.
An offline client cannot cancel or erase a newer server-side deletion request by syncing stale profile/progress state.

### 5. Future free-form user data

No generic merge rule is approved for free-form notes/journals/answers.
If a future app introduces such data, it requires an explicit version/conflict strategy before joining the shared platform.

## Sync revision contract

Each cloud-synced product/profile stream carries a monotonic server revision.

Client push must include its last observed server revision.

Decision:
- client base revision == current server revision -> merge according to data-class rule and increment revision;
- client base revision < current server revision -> run deterministic conflict rule;
- client base revision > current server revision -> reject as invalid/fail closed;
- missing revision on an existing cloud stream -> reject or force a safe re-fetch, never blind overwrite.

## Product boundary

A sync operation is scoped by:

`account/profile + product_id`

A World 01 sync packet may not contain World 02 progress. Mixed-product write packets are rejected or partitioned before any write.

## Content-version boundary

Progress includes `content_pack_id` / content version context.

A new content version must define migration compatibility. Until that mapping exists:
- do not erase old progress;
- do not blindly map sequence numbers;
- keep language-neutral content IDs as the stable join key where still valid.

## Offline guest -> account linking

Linking local guest progress to an account is explicit and idempotent.

Rules:
- linking may merge progress using the same monotonic rules;
- linking does not create a purchase entitlement;
- repeating the same link operation must not duplicate progress;
- guest data from another person/device is never attached merely because the same device later logs into an account without explicit link action.

## Fail-closed cases

Reject or require re-fetch for:
- unknown product;
- unknown profile/account relationship;
- future/invalid revision;
- incompatible content version without migration rule;
- attempt to mutate entitlement through sync;
- cross-product packet mutation;
- malformed state enum;
- locale outside the supported set.

## Synthetic acceptance tests

The deterministic suite must prove at least:
1. completed is never downgraded;
2. stronger offline progress can advance server progress;
3. stale weaker progress cannot overwrite newer stronger progress;
4. equal-revision conflicting preference values are surfaced as conflict;
5. future client revision is rejected;
6. client entitlement mutation is rejected;
7. World 01 packet cannot mutate World 02 state;
8. guest-to-account link does not grant entitlement;
9. duplicate guest-link replay is idempotent;
10. incompatible content version does not silently erase old progress.
