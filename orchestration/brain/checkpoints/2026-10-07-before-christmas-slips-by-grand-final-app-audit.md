# BEFORE CHRISTMAS SLIPS BY — Grand Final App Audit

Date: 2026-10-07
Audit mode: FINDINGS ONLY — no product mutations in this audit
Application repo: `riseshineevolve-source/RISE.SHINE.EVOLVE`
Application branch: `gentle-steps/app-en-full24-purple-gold`
Exact audited HEAD: `d62eb1ff3a4a539efb73fea09e8cba6d412e6c7e`

Canonical title package:
- THE HAPPY MAKERS PRESENT
- BEFORE CHRISTMAS SLIPS BY
- 24 Ten-Minute Family Activities for Less Rush, More Laughter, and Time to Really Be Together

Canonical marketing brief:
`marketing/GENTLE_STEPS_PRODUCT_MARKETING_BRIEF_2026-10-07.md`

Content authority used:
`Gentle_Steps_EN_V2_R3_FINAL_CONTENT_PLUS_FIXES_CORRECT(1).pdf`
SHA-256: `d8970cdb921683f5e9aa32165f03163098f169183e55fecf289bd2cbbc10aef1`

The other PDF attached in the same owner turn was explicitly ignored as instructed.

## RSE audit board

Technical:
- Test Automation Engineer
- Mobile Release Engineer
- Engineering Code Reviewer
- Accessibility Auditor
- Performance Benchmarker
- Privacy Engineer
- Application Security Engineer
- Reality Checker / Evidence Collector

Product / family experience:
- UI Finish-Gate Reviewer
- UX Researcher
- Persona Walkthrough Specialist

Family walkthrough is a qualitative simulated usability review, not statistical user research.

## Exact-head automated evidence

- Gentle Steps English App #195 — PASS
- Android Build #148 — PASS
- SEO Validation #1119 — PASS
- browser smoke — PASS, 43 assertions, zero uncaught runtime exceptions
- all 24 direct day routes — PASS
- Home / Before Day 1 / Family / Days 01, 12, 18, 22, 23, 24 / Completion visual proofs — produced
- completion persistence + reload + undo — PASS
- offline reload — PASS
- 320 / 390 / 768 px no-horizontal-overflow checks — PASS
- Lighthouse Home: 100 performance / 100 accessibility / 100 best practices / 100 SEO
- Lighthouse Day 22: 100 / 100 / 100 / 100
- Home FCP ~0.98s, LCP ~1.71s, TBT 0, CLS 0
- Day 22 FCP ~0.96s, LCP ~1.56s, TBT 0, CLS 0
- Android lintDebug + lintVitalRelease — PASS
- debug APK + AAB — produced
- APK hash `f2a343486b974f2da70ff3f060abef6349c07fa3324b4496619a712285c60fd9`
- AAB hash `3b88e824e1be79024e4dafb795d44a21991b476e5fb1890d1fc29ac22642d1a3`

## Overall verdict

### Technical core: PASS
### Automated web/runtime accessibility: PASS
### Performance: PASS
### Privacy architecture: PASS
### AppSec runtime: PASS with toolchain watch
### UX / product finish: HOLD for a short closing slice
### Google Play production: HOLD

No architecture rewrite is justified. Remaining issues are bounded product/UX/copy/testability defects.

# Findings — must resolve before production

## P1-01 — Long dialogs open near the bottom instead of the beginning

Exact-head visual evidence:
- `before-day1-en-visual-v2-390x844.png` opens around the lower Happy Makers paragraphs rather than at the first “Before Day 1” paragraph.
- `completion-en-visual-v2-390x844.png` opens in the later Happy Makers letter, near the bottom.

Cause hypothesis supported by implementation:
- the long native HTML dialogs have no explicit initial focus target at the top;
- the first focusable control is the close button at the bottom;
- there is no `scrollTop = 0` + heading-focus step after `showModal()`.

Impact:
- first-time users miss the beginning of the onboarding;
- the completion letter appears to start halfway through;
- this makes polished content feel broken.

Required:
- top-focus + top-scroll for Before Day 1 and After 24 Days;
- regression test asserting dialog scrollTop near zero after open.

## P1-02 — Full real-device internal test cannot be performed now without changing the phone date

Current production lock is intentionally date-based.
Native runtime explicitly disables `?preview=1`.
On 2026-10-07 the debug APK therefore opens with all 24 days locked.

Impact:
- QA can install and test icon/splash/Home/Family/reminders, but cannot realistically exercise Days 1–24, completion, long-day scrolling, next/previous or persistence on the phone today.

Required:
- a debug/internal-testing-only day-unlock mechanism, build flag, or internal QA variant that cannot ship in release;
- OR explicitly accept changing device date during device test.

This is a release-engineering/testing blocker, not a consumer feature request.

## P1-03 — Android system Back behavior is not explicitly modeled or regression-tested

The SPA changes the DOM without browser-history navigation and no Capacitor `backButton` listener is present.

Risk:
- Day -> Android Back may exit/background the app instead of returning to the calendar;
- system Back behavior while a Family / Before Day 1 / Reminder / completion dialog is open is unverified.

Required before Play:
- real-device Back test;
- if behavior is undesirable, add native back handling with dialog -> day -> calendar semantics.

## P1-04 — Day 10 / 12 / 16 contain visible carried-over list numbering artifacts

Owner-approved source and runtime contain:
- Day 10 Family Machine: `6. / 7. / 8.`
- Day 12 Five Words. Two Lies.: `9. / 10.`
- Day 16 Live Radio: `11. / 12. / 13. / 14.`

These are understandable but look like pagination/editor numbering leakage rather than intentional per-activity numbering.

For a premium app, reset each local list or render as bullets.

This should be corrected in the canonical content source or through an explicitly approved normalization rule, not silently rewritten downstream.

## P1-05 — The 24/24 finale exists but is buried and the hero resets to “Open Day 1”

The app has a good completion card and a substantial Happy Makers closing letter.

However:
- `nextJourneyDay()` falls back to Day 1 when no incomplete day exists;
- after 24/24 the first-screen hero CTA can therefore still say `Open Day 1`;
- the completion card is rendered *after* the full 24-day calendar;
- completing Day 24 does not automatically surface the finale.

Impact:
the emotional payoff is much weaker than the Day 24 content deserves.

Required:
- dedicated completed state in the first viewport;
- primary CTA should become completion/letter action, not Open Day 1;
- keep the calendar available as secondary navigation.

# Findings — important polish / owner decisions

## P2-01 — Remaining old-identity copy in runtime

Canonical current brand is `Happy Makers` and `Before Christmas Slips By`.

Runtime still contains:
- `Meet the Happy-Makers`
- `Meet the Happy-Makers Family`
- aria label `The Happy-Makers family...`
- locked-day text `Your next Gentle Step will be here...`
- error text `Gentle Steps could not load.`

These are small but visible/assistive-tech-facing identity leaks.

## P2-02 — Tiny topbar duplicates the full title and wraps heavily

At 390px the brand lockup repeats the full `BEFORE CHRISTMAS SLIPS BY` in several short lines directly above the large hero version.

The page remains readable, but this is visually less refined than the main hero.

Consider a compact topbar identity such as the short product name / Happy Makers mark while preserving the full locked title in the hero and metadata.

## P2-03 — Family sheet is visually repetitive

The Family modal uses:
1. a five-portrait cluster;
2. immediately followed by the same five people as profile rows.

It is clear and attractive, but reads slightly like a directory rather than a lived-in family moment.

Not a blocker. One genuine group image or a smaller cluster would reduce repetition if desired.

## P2-04 — “Ten-minute” promise is strongest on most days, but a few days need real timing validation

Current runtime word counts, including character notes:
- Day 1 ~502 words
- Day 9 ~470
- Day 18 ~507
- Day 24 ~533

Most days are ~330–410 words.

Highest PLAY instruction loads:
- Day 9 Plan B ~285 words
- Day 18 Chair Mission ~290
- Day 24 Four Minutes. Four Missions. ~315

The content correctly gives permission to stop early / count shorter evenings, but a real family should time these days before marketing the ten-minute claim as universally literal.

Recommendation: measure, do not rewrite yet.

## P2-05 — Circle/starter mechanics remain a mild recurring pattern

Across the final 24-day source:
- `circle` appears about 12 times;
- starter selection still frequently uses age, names, position, clothing or birthday.

This is dramatically improved versus the earlier content and is not currently a blocker.

Family persona reaction after ~10 days:
“Fun, but we notice the author keeps deciding who starts.”

If real-family testing confirms friction, simplify only the repeated starter mechanics, not the activities.

## P2-06 — Pre-Dec consumer experience is intentionally limited

Before Dec 1 production users see the locked calendar plus Family / How it works, but cannot try a real day.

This is coherent for an Advent countdown, but the canonical marketing brief includes `SEE HOW A DAY WORKS` as a prelaunch CTA.

Owner decision:
- app launches very close to Dec 1 -> current strict lock is fine;
- app is available meaningfully earlier -> consider one non-progress sample day or demo, without weakening the December lock.

# Family persona walkthrough

Persona:
- busy parent after work / dinner;
- 11-year-old who rejects anything that feels babyish or preachy;
- 8-year-old who needs rules that can be understood quickly.

## Home — PASS

Five-second answers:
- What is this? Clear.
- Is this for us? Clear: family, 10 minutes, 24 days.
- What do we do? Clear primary CTA.

Strong:
- title + subtitle directly express the real December problem;
- purple/gold Christmas aesthetic feels distinctive;
- Happy Makers make the app feel authored and warm;
- no “mindfulness app” / therapy tone.

## Before Day 1 — CONTENT PASS / UI HOLD

Content is excellent:
- acknowledges work/school/errands;
- explicitly says this is not another task;
- gives permission for a six-minute evening;
- explains PAUSE / PLAY / BETWEEN US clearly.

But current dialog opens near its lower section, so the best onboarding copy can be missed.

## Days 1–6 — strong opening

Highlights:
- Day 1 Invisible Ball is an excellent opening mechanic;
- Day 3 Freeze Frame feels immediate and low-pressure;
- Day 4 Same Line, Different Story is funny without being childish;
- Day 5 counting game is easy to start;
- Day 6 is slightly more facilitator-heavy but still workable.

Parent reaction:
“This fits an ordinary evening better than the old version.”

Older child reaction:
“Games feel like actual games, not activities pretending to be games.”

## Days 7–12 — mostly strong; Day 9 is the first density spike

Best:
- Chain Reaction;
- Story Nobody Planned;
- household mystery;
- Five Words. Two Lies.

Day 9 Plan B is highly on-positioning and clever, but it is instruction-heavy and can feel like a family logistics workshop if the family is already exhausted.

Day 10/12 list-number artifacts reduce polish.

## Days 13–18 — best entertainment run, with one over-instructed day

Standouts:
- Instant Expert;
- 3, 2, 1... Same?;
- Mirror Without a Mirror;
- Live Radio;
- Only Questions.

These are the days most likely to make an older child voluntarily say “again.”

Day 18 Chair Mission is now much safer than the earlier Trust Web:
- short route;
- hazards removed;
- eyes-open is explicitly a full version;
- navigator does not touch;
- stop rule;
- safety watcher for a group of three.

Residual issue is *instruction burden*, not a major safety defect.

## Days 19–23 — good late-December fit

Strong:
- What Changed?;
- Silent Line;
- No Yes. No No.;
- Reverse Charades;
- Luckily / Unfortunately.

Day 23 apology has been fixed well:
- explicitly not required;
- directed only to the person involved;
- no forced “it’s okay” response;
- skip is allowed.

This no longer reads as a forced family-therapy exercise.

## Day 24 — content PASS / app payoff HOLD

Content finale is excellent:
- callbacks to earlier days;
- Four Missions feels like an earned finale rather than a random new game;
- Invisible Ball returns;
- Between Us asks what to keep;
- optional song is an encore, not another obligation.

The app fails to capitalize on this because the 24/24 completion state is buried below the calendar and the hero can still say Open Day 1.

# Content-system assessment

## Major improvement vs old version

The final source is substantially less repetitive and less “mindfulness-coded.”

PAUSE now varies through:
- task release;
- paced breathing;
- feet/shoulders;
- sensory listening;
- finger pacing;
- body support;
- heartbeat;
- 3-2-1 grounding;
- side-by-side quiet;
- jaw/forehead release;
- eye focus;
- slow motion;
- warm hands;
- shoulders;
- hand movement;
- stretch;
- empty hands;
- squeeze/release;
- sound reduction;
- near/far eye focus;
- permission to postpone;
- final no-planning minute.

PLAY variety is now a genuine strength.

BETWEEN US is much more real-family / less therapeutic.

Happy Makers humor is significantly more character-specific.

## Source-quality finding

The source still labels itself PREMIUM_WORKING / NOT CONTENT-FROZEN / NOT PRINT-READY and preserves the historical title at the top, while the app correctly applies the separate owner brand lock.

That is acceptable for app source-control because the app source lock explicitly records the owner title override. It is not an app defect.

# Technical/security/privacy assessment

## PASS
- no backend account;
- no cloud progress;
- no remote API dependency;
- no Firebase/Supabase/OpenAI runtime;
- native package contains content locally;
- offline browser reload passes;
- source copy is escaped before HTML insertion;
- progress storage is season-scoped by year;
- exact-alarm permission check/settings route exists;
- reminder scheduling errors are caught;
- notification tap -> correct day logic exists;
- focus restoration and scroll-to-top day navigation pass;
- performance is excellent.

## WATCH
- current npm audit still reports 3 moderate `uuid` advisories via `xcode -> @capacitor/cli`;
- high-severity audit gate passes;
- do not force-fix across Capacitor versions without a bounded compatibility test.
- package id remains `PROVISIONAL_PRE_PLAY`.
- Play signing/Data Safety/store/legal remain owner/external gates.

# Physical-device evidence still missing

Must be tested on a real Android phone:
- launcher icon;
- approved family splash;
- system Back;
- actual notification permission;
- exact-alarm settings flow;
- actual reminder delivery;
- notification tap;
- kill/restart persistence;
- airplane-mode restart;
- Android font scaling;
- TalkBack;
- resume after background/rotation if supported.

# Final scores

Technical correctness: A
Performance: A
Automated accessibility: A
Privacy: A
Runtime security: A-
Visual brand: A-
Home/onboarding concept: A
Actual onboarding dialog behavior: C until scroll/focus is fixed
Daily content quality: A-
Playfulness / family appeal: A-
Ten-minute credibility: B+ pending real timing
Completion experience: C+ despite excellent closing content
Production readiness: HOLD for bounded closing slice + real-device pass

## Recommended decision sequence

Do not rewrite the product again.

First closing slice should be limited to:
1. long-dialog top-focus/top-scroll;
2. debug-only native QA unlock or explicit date-change test protocol;
3. Android Back behavior;
4. local list-number artifacts 6–14;
5. 24/24 first-viewport completion state;
6. canonical Happy Makers / no legacy Gentle Steps strings.

Then:
- rerun exact-head CI;
- run the same family walkthrough only on changed surfaces;
- physical Android smoke;
- only then move to Play owner gates.
