# RSE Quick Desk — Owner Decision Inbox

Status: QUICK DESK HANDOFF QUEUE
Canonical authority: Central RSE Orchestrator
Location for individual notes: `orchestration/quick-desk/inbox/`

## Purpose

This is the holding area for durable owner decisions or cross-project instructions that arise during fast Quick Desk conversations.

It is NOT a replacement for:
- `orchestration/brain/DECISION_LEDGER.md`;
- `orchestration/brain/RSE_BRAIN_MASTER.md`;
- `orchestration/brain/OWNER_GATES.md`;
- `orchestration/brain/COMMERCIAL_PRIORITY_STACK.md`.

Quick Desk records candidates here.
Central RSE Orchestrator reconciles them into canonical state.

## When Quick Desk should create an inbox note

Create a note only when the owner clearly makes a durable decision, for example:
- "ustalamy, że...";
- "od teraz...";
- "to ma być nowa zasada...";
- "zmieniamy priorytet...";
- "zapisz to do RSE...";
- a cross-project instruction that should survive the chat.

Do not log:
- brainstorming;
- tentative ideas;
- ordinary questions;
- temporary preferences;
- facts already canonical in current repo state.

## Note naming

Use:
`YYYY-MM-DD-HHMM-<short-slug>.md`

Example:
`2026-09-30-1600-quick-desk-operating-model.md`

## Required note structure

```md
# Quick Desk Owner Decision Candidate

Status: PENDING CENTRAL RECONCILIATION
Date:
Scope:
Source conversation: RSE Quick Desk

## Owner decision
<concise durable decision>

## Reason / context
<why this matters>

## Affected canonical surfaces
- <paths or NONE>

## Safe immediate effect
<what Quick Desk may do now without touching central canonical state>

## Central reconciliation required
<what Central Orchestrator should update/check>

## Conflict check
<known conflicts, or NONE FOUND>
```

## Reconciliation rule

Central Orchestrator should:
1. verify the decision against current repo truth;
2. resolve conflicts if any;
3. update canonical Brain/ledger/registry/gates only if appropriate;
4. leave durable evidence that reconciliation occurred.

Until that happens, an inbox note is an owner-decision candidate, not canonical portfolio truth.

## Initial owner-approved operating decision — 2026-09-30

The owner approved creation of an RSE Quick Desk as a fast conversational interface to RSE.

Intended split:
- Central RSE Technical Orchestrator = heavy execution, canonical portfolio coordination, Brain/priority mutations;
- RSE Quick Desk = fast questions, targeted status retrieval, decision support and handoff preparation;
- delegated execution chats = project-specific workers as already defined by current RSE Brain.

This file itself does not modify central Brain or portfolio sequencing.
