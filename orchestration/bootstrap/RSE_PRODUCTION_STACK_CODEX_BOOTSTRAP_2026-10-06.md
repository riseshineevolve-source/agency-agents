# RSE Production Stack v1 — Codex Bootstrap

Status: AUTHORIZED IMPLEMENTATION SEQUENCE
Date: 2026-10-06

## First read

1. `orchestration/architecture/RSE_PRODUCTION_STACK_V1.md`
2. `orchestration/architecture/RSE_VISUAL_PAGE_FACTORY_V1.md`
3. `orchestration/architecture/RSE_BOOK_AGENT_V3.md`
4. `orchestration/architecture/RSE_BOOK_MAP_CONTRACT_V1.md`
5. `orchestration/architecture/RSE_CONSUMER_PLATFORM_APP_FACTORY.md`
6. `orchestration/architecture/RSE_PRODUCTION_AGENT_ROUTING_V1.yml`

For Detective implementation also read current live control on:
`riseshineevolve-source/RISE.SHINE.EVOLVE / feature/rse-book-factory-v2`.

## Codex mandate

Do not invent another renderer.

Implement the smallest missing deterministic layers that make the Production Stack operational.

### Slice P1 — Visual Page Factory foundation

In the current Book Factory:
- add a schema for `visual-scene-spec-v1`;
- add explicit page-family registry;
- register Detective Pages 1–15 taxonomy from `RSE_VISUAL_PAGE_FACTORY_V1.md`;
- implement source-span completeness validation;
- implement scene-spec hash;
- implement template/asset dependency edges into Book Map;
- implement changed-page-only scene compilation input/output;
- do not create final new visual template geometry yet.

Acceptance:
- same source + registry → same scene spec;
- omitted or duplicate source span fails;
- unknown family/variant fails;
- one source-page change invalidates only its true page scene;
- no canonical text rewrite.

### Slice P2 — Template family runtime

After P1:
- derive templates from current owner-approved/owner-baseline visuals;
- start only with 3 representative families:
  1. cinematic_invitation (Page 03)
  2. character_dossier_trio (Pages 07–08)
  3. process_rail or orientation_menu (Page 04 or 10)
- render with existing React/CSS/SVG/Vivliostyle;
- art remains external atomic assets;
- use Playwright screenshots/contact sheets.

Stop at one owner look gate for the 3 families.

Do not ask owner to approve every page separately.

### Slice P3 — Scale Pages 1–15

Only after template-family approval:
- populate all Pages 1–15 from exact current source;
- preserve baseline page if no source/template/asset delta is approved;
- small changed-page review packet only.

### Slice P4 — App production lane

Do not start another backend.

Wrap the existing RSE Interactive Book / Consumer Platform contracts into:
- product manifest;
- content-pack validation;
- reusable app shell config;
- Playwright/device QA packet;
- release manifest.

Select one already-authorized real product only when central owner/source gate allows it.

## Tooling

Current:
- GitHub/GitHub Actions;
- Playwright;
- Vivliostyle.

Prepare interfaces, do not hardwire secrets, for:
- OpenAI Agents SDK;
- n8n ops glue;
- Temporal durable workflow pilot.

No secret/API keys in repository.
No paid external service creation without owner gate.
