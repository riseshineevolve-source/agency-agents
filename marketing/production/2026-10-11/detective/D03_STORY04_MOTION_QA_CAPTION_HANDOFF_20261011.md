# Detective Academy D03 Story 04 — motion derivative | owner review

**2026-10-11 | PRELINK | OWNER REVIEW / HOLD | EN V12 product scope**  
**Marketing-only production; no KDP publication, public post, schedule, paid media or product-source change.**

## Real new deliverable

From the existing, already rendered **D03 Story 04** typography graphic, produced an **8-second vertical silent H.264 MP4** with a subtle 1.028× center zoom, a 0.38s fade-in and 0.45s fade-out. **No fake book pages, mockups, puzzle solutions or altered Happy Makers likenesses.** This is promotional typography, **not proof of a printed or released book**.

- Output: `DETECTIVE_D03_STORY04_MOTION_PRELINK_1080x1920_8S_20261011.mp4`
- Output SHA-256: `6a21732bacdfef7b44cb7fa8b72cf7c7f245412e5e757d7b06bce223b67822da`
- Output bytes: `1,493,855`; 1080×1920; H.264/yuv420p; 30fps; 240 frames; 8.000 seconds; no audio stream.
- Source PNG exact SHA-256: `e21fd603afebf7951fe8b9dc0d6c3eee86a9381f5a726f9071c5cb0c19fe6e75`
- Source SVG Git blob: `3b2c338a0610d356d5f7c67ee42f064a5b5e8a26`, [existing source graphic](https://github.com/riseshineevolve-source/agency-agents/blob/marketing/detective-proof-led-20261011/marketing/production/2026-10-11/detective/D03_STORY_04_READER_PLACE_INSIDE_CASE_1080x1920.svg).
- Exact marketing-brief blob: `771a659398d6eae3cefe8f6206e4c3f97b96f1c3` ([product marketing brief](https://github.com/riseshineevolve-source/agency-agents/blob/main/marketing/DETECTIVE_ACADEMY_PRODUCT_MARKETING_BRIEF_2026-10-07.md)).
- Local owner-review ZIP: `DETECTIVE_D03_STORY04_MOTION_OWNER_REVIEW_20261011.zip`, SHA-256 `f93dfab3ae8a4c1933724050823ffbd6e4ded1851550426d40d296c1c67eaff2`; six entries (MP4, input PNG, five-frame contact sheet, 390px sample, this scope's caption/readme, QA JSON). Delivered as this chat's attached sandbox artifact; **not committed as a binary to GitHub and not uploaded to Library** (Library container path upload returned `container_session_unavailable`).
- QA JSON SHA-256: `e9a8f72fae6e1db4ba5894f10b6b9accd8013c8e96cad20815b6b8000821a8be`.

## Verified QA

**PASS:** ffprobe H.264, 1080×1920, 30fps, exactly 240 frames/8.000s, no audio, yuv420p; successful actual frame decode at 0.6/2.5/4.0/6.5/7.4s. Five-frame contact sheet inspected; lettering, case claim and CTA visible without clipping at the inspected moments. At 390px downscale, "PICK YOUR CALL SIGN." remains readable. A source-graphic promotional animation is **not** a genuine book sampler.

**NOT TESTED:** native Instagram/Facebook Story UI overlay on a physical phone, exact platform compression, native poll/question sticker. No 141-page release baseline reused; no V12 interior page images portrayed.

## One CTA + platform-ready text

**On-screen CTA:** **PICK YOUR CALL SIGN.**

**Optional native Story description (not published):**
> One detective is still missing. Your child can take that place in THE HAPPY MAKERS' DETECTIVE ACADEMY: THE MYSTERY OF ROOM ZERO. Book 1. Thirty connected cases, one hidden mystery. What would their call sign be?

**Alt text:** A dark navy-and-gold Detective Academy poster moves with a slow camera push. Cream headline lettering reads "The reader gets a place inside the case." A gold-outlined panel asks "Pick your call sign." The Happy Makers, Detective Academy and The Mystery of Room Zero appear in the header. Faint scanner rings sit behind the wording.

## Deterministic motion recipe

Starting from the exact SHA-pinned source PNG:

```bash
ffmpeg -loop 1 -framerate 30 -i D03_STORY_04_READER_PLACE_INSIDE_CASE_1080x1920.png \
  -vf "zoompan=z='min(zoom+0.000115,1.028)':x='(iw-iw/zoom)/2':y='(ih-ih/zoom)/2':d=240:s=1080x1920:fps=30,fade=t=in:st=0:d=0.38,fade=t=out:st=7.55:d=0.45,format=yuv420p" \
  -frames:v 240 -an -c:v libx264 -preset veryfast -crf 19 \
  -movflags +faststart DETECTIVE_D03_STORY04_MOTION_PRELINK_1080x1920_8S_20261011.mp4
```

Video SHA may vary with codec build; the recorded QA checks apply to the artifact hashed above.

## Gate

**OWNER REVIEW / HOLD.** The four-frame D03 family has not received collective owner approval. The actual MP4 and QA files were delivered in the current conversation, not to GitHub/Library. No external post, schedule, listing link, KDP claim or publication. Keep first-live new family publication owner-gated and check live platform UI before any future use.
