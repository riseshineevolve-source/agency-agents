# RSE Asset Vault Protocol v1

Status: CANONICAL
Date: 2026-10-07
Parent: orchestration/control-plane/RSE_UNIVERSE_MAP_V1.md

## Purpose

Prevent approved images/PDFs/media masters from being trapped inside one chat.

## Storage law

Durable asset bytes:
- ChatGPT Library / Google Drive / project-local protected storage according to product needs.

Durable metadata:
- GitHub manifest with semantic ID, SHA-256, size, source/approval state and durable storage path.

Chat attachments alone are never sufficient production custody.

## Ingest rule

When the owner provides an asset that becomes production-relevant:
1. preserve original bytes;
2. compute SHA-256;
3. copy to durable Asset Vault;
4. assign stable semantic ID;
5. write/update manifest;
6. mark status CANDIDATE / OWNER_APPROVED / FROZEN_ASSET;
7. consuming lanes reference semantic ID + hash, not chat filename.

## Identity assets

For character/brand identity:
- exact approved bytes are authoritative;
- no lookalike substitution;
- deprecated conflicting versions remain identifiable but are not production candidates;
- Dilo/Alio and other similar characters must have distinct stable IDs.

## Cross-chat rule

Any chat may READ Asset Vault manifests.
Only the asset-owning lane or Central during initial owner-ingest may register a new owner-supplied asset.
Product lane remains responsible for integrating it into its own repository/asset registry.

## AI rule

Image generation/editing may create candidate atomic art.
It may not silently replace an OWNER_APPROVED/FROZEN_ASSET.
A generated candidate becomes usable only after registry + QA + applicable owner gate.

## Confidential exception

Opinie real case media/evidence remains local/offline and must not enter shared Asset Vault unless explicitly sanitized and authorized.
