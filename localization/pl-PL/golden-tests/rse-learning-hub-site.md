# Golden Test: Rise.Shine.Evolve Learning Hub Website

Source domain: `https://rise-shine-evolve-learning-hub.com/`
Target locale: `pl-PL`
Purpose: first integrated validation of RSE Polish Localization Engine.

## Why this is a strong golden test
The site combines:
- brand manifesto copy
- parent-facing marketing
- child-facing language
- gaming metaphors
- humor and microcopy
- recurring Happy-Makers characters
- product descriptions
- app/web terminology
- GIFTS interactive tools
- buttons/CTAs
- account/support copy
- SEO content
- legal/privacy surfaces

A system that can localize this coherently can then be reused for books and apps.

## Important source-of-truth warning
Do not begin full Polish localization until the English production source is frozen for the localization pass.

Current public pages include content that appears to belong to an older product model, including `Project Unstoppable App` language describing a browser-installed PWA, SaaS access, cloud sync, Paddle payment and a 365-day access license. Treat this as `SOURCE_REVIEW_REQUIRED` before translating. Localization must not faithfully polish content that the product team intends to remove or replace.

## Required crawl/scope map
At minimum inspect and segment:

### Global shell
- navigation
- login/account labels
- footer
- social/support labels
- newsletter/account messages
- accessibility/alt text
- reusable CTA components

### Home / Hub
- RISE / SHINE / EVOLVE manifesto
- family-life co-op-game block
- calm/confidence/connection/joy value proposition
- library/gifts pathways
- 'messy Tuesday' type humor
- instant-reset CTA

### Kids
- hero/value proposition
- Happy-Makers family introduction
- Library Collection
- product cards and availability states
- all Explore/Buy CTA text

### Happy-Makers
- Mimi
- Luli
- Dilo
- Alio
- Little Nini
- Grandma Bibi
- family/squad manifesto
- character nicknames/taglines
- recurring jokes and emotional-growth language

### Teenagers
- section hero
- Project Unstoppable references
- product/app status copy
- fallback/promotional content

### Adults
- current adult hub copy
- focus areas
- weekly structure
- FAQ
- product status language

### GIFTS
- section intro
- Family Motto Generator
- Calm + Energy Wheel
- 1-Minute Challenge
- Happy Makers Word Hunt
- Word Search Studio
- coming-soon cards
- mobile tips

### Direct product/library pages
- Level Up Your Brain World 01
- Level Up Your Brain World 02
- The Confident, Mindful & Happy Me Adventure
- 24 Gentle Steps to Christmas
- Grandma Bibi / Anti-Boredom Club
- any active app pages

### Legal / account
- privacy policy
- terms/refund text if present
- unsubscribe/remove account
- data/privacy/account messages

### SEO / metadata
- page titles
- meta descriptions
- H1/H2 hierarchy
- alt text
- schema/structured data where present
- internal-link labels
- slugs only after SEO decision

## Segment classes to exercise
Golden test must include at least one accepted segment for each:
- factual
- educational
- brand
- marketing
- humor
- gaming metaphor
- CTA
- UI label
- child-facing
- parent-facing
- character voice
- legal/privacy
- SEO

## Initial transcreation challenge set
Use these as calibration examples, not mandatory final wording:

1. `family life is an EPIC CO-OP GAME`
   - preserve gaming metaphor and family teamwork
   - avoid stiff literal `epicka gra kooperacyjna` unless context proves it works

2. `some mornings starting on HARD MODE`
   - preserve gamer-language punch
   - Polish may retain `TRYB HARD`/`hard mode` only if consistent with brand glossary

3. `Not just for 'good days'. But for the random messy Tuesday, too.`
   - preserve recognition/humor of an ordinary chaotic weekday
   - do not translate `random messy Tuesday` mechanically

4. `No lectures, no 'perfect kid' pressure.`
   - preserve anti-preachy, anti-perfection stance
   - Polish solution may use different idiom

5. `We take emotional growth seriously. But we never take ourselves too seriously.`
   - preserve elegant contrast and understated humor

6. `Powered by your Happy-Makers.`
   - decide whether gaming/tech metaphor survives naturally in Polish or needs a functional rewrite

## Acceptance criteria
- 100% mapped scope for approved source pages
- stale/obsolete English source identified before translation
- stable glossary for brand/product/character terms
- natural Polish, not literal Polish
- meaning guardian PASS on all published segments
- character voice continuity PASS
- legal route isolated from transcreation
- UI length and implementation constraints checked
- Polish SEO based on Polish search intent, not translated English keywords
- final bilingual QA PASS
