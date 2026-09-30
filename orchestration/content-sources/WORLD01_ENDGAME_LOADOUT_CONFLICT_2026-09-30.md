# World 01 endgame loadout source inconsistency

Date: 2026-09-30
Status: **OWNER COPY GATE BEFORE FINAL RELEASE**

The canonical published World 01 paperback is internally inconsistent between
the mission-end Secret Family Code pages and the summary table printed on
pages 102–103 (`ULTIMATE LOADOUT: KEYS & FAMILY CODES`).

This is a source inconsistency, not a Lovable divergence. It must not be
silently normalized.

## Codes that agree

Levels 1–6 match between the mission pages and the endgame loadout:

- Level 1 — `DECOMPRESSION MODE`
- Level 2 — `MY BUCKET TIPPED OVER!`
- Level 3 — `I AM FARMING XP!`
- Level 4 — `SPY GEAR OFFLINE`
- Level 5 — `LIZARD ON THE CONTROLLER!`
- Level 6 — `BRAIN UNDER CONSTRUCTION!`

## Codes that conflict

| Level | Mission-end Secret Family Code | Page 102–103 loadout summary |
|---|---|---|
| 7 | `MAKING A DEPOSIT` | `MY LEAVES ARE DROOPING!` |
| 8 | `FERRARI MAINTENANCE` | `FERRARI TO THE CAR WASH!` |
| 9 | `BUILDING WITH BRICKS` | `I NEED BRICKS, NOT STRAW.` |
| 10 | `EATING THE FROG` | `ENERGY VAMPIRE ATTACK!` |

## Runtime disposition

The Android runtime uses the full mission-level source graphs for Levels 1–10
and therefore preserves each mission's printed Secret Family Code.

The contradictory `ULTIMATE LOADOUT` table is **not** currently reproduced in
the app. Other endgame pages (Mission Accomplished, Command Transferred, Create
Your Own Secret Code, Never Fight Solo, Developer Notes, certificate and Bonus
Level/Hub) may be implemented directly because they do not require resolving
this conflict.

## Owner gate

Before a final Play release, choose one:

1. keep mission-end codes as authoritative and update the digital loadout to
   those codes;
2. intentionally use the page 102–103 summary variants;
3. expose both with explicit labels explaining that the book contains a summary
   variant.

No choice is made automatically.
