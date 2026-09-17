# Optical Animals — GitHub-Backed Agentization Plan

Status: ACTIVE / CODE ONLINE + ASSET CURATION + CENTRAL SUPERVISION

## Source of truth

Target repository name:
`riseshineevolve-source/optical-animals-book-creator`

Current local project/root:
`C:\Users\danie\GitHub\optical-animals-book-creator`

Current branch:
`feat/optical-animals-book-creator`

The standalone GitHub repository does not yet exist. Until it is created, the local project plus this orchestration contract remain authoritative.

## What belongs in GitHub

GitHub should contain:
- Book Creator source code,
- manifest/schema for illustration roster,
- assembly logic,
- page ordering and replacement logic,
- KDP preflight checks,
- tests,
- prompts/rules that are genuinely part of reproducible production,
- low-resolution or explicitly approved reference fixtures when licensing/size permits,
- CI configuration and release/export scripts.

Large production image files may be kept outside normal git history if size makes git inefficient. The manifest should still reference their canonical IDs/filenames/checksums so the production pipeline remains reproducible.

## Goal

Create a premium 8.5 x 11 in portrait KDP optical-animal coloring book with exactly 20 final illustrations, while preserving the strongest already-approved artwork and avoiding destructive regeneration.

## First autonomous milestone

Build the curation and assembly workflow before mass production:

1. Inventory candidate illustrations and their current-best versions.
2. Assign one status per candidate: READY / SMALL FIX / REDO / HOLD.
3. Detect duplicate species, rejected species and empty roster slots.
4. Route only SMALL FIX and REDO assets to the relevant visual/anatomy specialist.
5. Preserve READY assets byte-for-byte until an owner-approved replacement exists.
6. Maintain a machine-readable illustration manifest containing species, source file/asset id, checksum, accepted version, status, notes and final page order.
7. Make one-image replacement deterministic so swapping an illustration does not require manual repagination.
8. After the final 20 are owner-locked, use Book Creator automation for ordering, PDF assembly and KDP preflight.
9. Add CI tests for manifest validity, exactly-20 roster lock, duplicates, missing assets and page geometry.

## Default agent routing

- RSE Technical Orchestrator
- Visual Art Director / Illustration QA
- Anatomy specialist only for flagged anatomy defects
- Test Automation Engineer for manifest/assembly regression
- KDP / Print Preflight specialist only after final roster lock

Avoid broad multi-agent generation. The goal is curation and controlled repair, not volume.

## Hard gates

- No mass regeneration.
- No automatic species/roster changes.
- No replacement of approved images without explicit acceptance.
- Preserve project-specific optical background, anatomy, jewelry/inlay and coloring-surface constraints from the latest brief.
- Final visual roster is owner-gated.
- Book Creator may assemble, swap and export; it may not silently choose artwork.

## Definition of done for milestone 1

- standalone repository exists,
- canonical candidate manifest exists,
- current-best version of every candidate is known,
- duplicates/rejections/gaps are explicit,
- only weak assets remain in the repair queue,
- one-image replacement does not require manual repagination,
- automated preflight detects roster/asset/layout failures,
- full KDP master remains blocked until final 20 are approved.
