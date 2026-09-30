# Polish Localization Engine Execution Bootstrap

Role: dedicated localization-engine execution/support stream.
GitHub/durable source overrides chat memory.
Do not mutate central RSE priorities.

## Current operating use

1. Support **Gentle Steps PL** now: language master exists; next production risk is real-template fit + owner editorial/safety decisions.
2. Prepare **Detective Academy PL** infrastructure, but do not start full production translation before explicit Detective EN freeze.
3. Keep engine tests/profiles/terminology deterministic and project-specific.

## Immediate bounded work

- verify current branch/PR freshness against main;
- reconcile only if needed and rerun current CI;
- preserve completed Gentle Steps language work;
- package real-template fit checks for Gentle Steps;
- keep Detective pre-freeze readiness current without translating the full book.

Stop for:
- terminology choices that materially affect brand/voice;
- unresolved safety/editorial owner decisions;
- Detective EN freeze gate.
