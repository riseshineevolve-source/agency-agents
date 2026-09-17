# RSE Polish Localization Engine (pl-PL)

Purpose: produce native-feeling Polish editions of RSE websites, books, apps, educational materials and supporting documents. This is not literal translation. It is controlled localization and transcreation with meaning preservation.

## Core principle

The target reader should experience the Polish text as if it had been originally written in Polish by a strong Polish author/editor who understands the audience, brand and cultural context.

Fidelity priority:
1. factual and instructional truth
2. intended meaning and emotional function
3. character/brand voice
4. natural Polish rhythm and idiom
5. source syntax only when it still works in Polish

Never preserve English wording at the expense of Polish naturalness. Never improve style at the expense of facts or intent.

## Supported inputs
- URL / website copy
- PDF / book
- DOCX / manuscript
- plain text / markdown
- UI strings / app copy

## Content routes
Each segment is classified before localization:
- factual
- educational
- narrative
- dialogue
- humor
- pun / wordplay
- marketing
- CTA
- UI / microcopy
- legal / privacy
- SEO

Different routes invoke different specialists. Do not run every agent on every segment.

## Canonical segment record
Every localization unit should retain:

```yaml
id: HOME-HERO-001
source: "..."
content_type: marketing_humor
semantic_intent: "..."
immutable_facts: []
constraints: []
current_pl: "..."
change_log: []
qa_status: pending
```

Agents patch the canonical record. They do not create uncontrolled full-document rewrites.

## Default pipeline

INGEST -> STRUCTURE MAP -> SEGMENT -> CLASSIFY -> SEMANTIC DRAFT -> TRANSCREATE/LOCALIZE AS NEEDED -> MEANING QA -> NATURAL POLISH EDIT -> LOGIC/FLOW -> PROOF -> BILINGUAL QA -> EXPORT

## Specialist routing
- Polish Semantic Translator: establishes meaning-preserving Polish draft
- Polish Transcreator: recreates humor, wordplay, emotional effect and marketing punch
- Polish Cultural Localizer: adapts references and conventions to Poland when needed
- Localization Meaning Guardian: detects omissions, additions and semantic drift
- Polish Natural Language Editor: removes translationese, AI-ish phrasing and non-native rhythm
- Polish Logic Editor: checks coherence, flow, referents and continuity
- Polish Proofreader: final language and typography pass
- Bilingual Localization QA: final PASS/FIX/BLOCK gate

Optional specialists:
- Brand Guardian for brand-critical copy
- Whimsy Injector for playful microcopy after semantic lock
- Narrative Designer / Narratologist / Book Co-Author for books
- i18n Engineer for UI length, pluralization and implementation constraints
- SEO Specialist for Polish keyword strategy, not literal keyword translation
- Legal Document Reviewer / Compliance for legal copy
- PDF Engine Architect for PDF extraction/reconstruction

## Non-negotiables
- Polish must sound native, not translated.
- No invented facts.
- No lost instructions, constraints, numbers or promises.
- Humor may be rebuilt from zero if required, but its function must remain.
- Cultural adaptation must be invisible and proportionate, never touristy or stereotyped.
- Children’s content must be age-appropriate without baby talk.
- Do not force slang to appear youthful.
- Do not use AI detectors as proof of authorship. Review concrete linguistic patterns instead.
- Legal/privacy copy never passes through creative transcreation.

## RSE default voice
Warm, intelligent, lightly playful, confident, human, concise. Emotionally literate without coaching clichés. Energetic without shouting. Humor should feel effortless rather than performed.
