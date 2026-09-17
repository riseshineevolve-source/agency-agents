# Optical Animals — Agentization Plan

Status: ACTIVE / local production + central supervision

## Source of truth

Local project only for working assets:
`C:\Users\danie\GitHub\optical-animals-book-creator`

Branch:
`feat/optical-animals-book-creator`

Read local `PROJECT_BRIEF.md` and latest approved image decisions before any execution.

## Goal

Create a premium 8.5 x 11 in portrait KDP optical-animal coloring book with exactly 20 final illustrations, while preserving the strongest already-approved artwork and avoiding destructive regeneration.

## First autonomous milestone

Build the curation and assembly workflow before mass production:

1. Inventory candidate illustrations and their current-best versions.
2. Assign only one status per candidate: READY / SMALL FIX / REDO / HOLD.
3. Detect duplicate species, rejected species and empty roster slots.
4. Route only SMALL FIX and REDO assets to the relevant visual/anatomy specialist.
5. Preserve READY assets byte-for-byte until an owner-approved replacement exists.
6. Maintain a machine-readable illustration manifest containing species, source file, accepted version, status, notes and final page order.
7. After the final 20 are owner-locked, use Book Creator automation for ordering, page replacement, PDF assembly and KDP preflight.

## Default agent routing

- CORE Orchestrator / Product Manager
- Visual Art Director / Illustration QA
- Anatomy specialist only for flagged anatomy defects
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

- canonical local candidate manifest exists,
- current-best version of every candidate is known,
- duplicates/rejections/gaps are explicit,
- only weak assets remain in the repair queue,
- one-image replacement does not require manual repagination,
- full KDP master remains blocked until final 20 are approved.
