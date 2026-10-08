# Before Christmas Slips By — exact-head checkpoint 16

Date: 2026-10-07

Canonical app source is Gentle_Steps_EN_V2_R3_FINAL_CONTENT_PLUS_FIXES_CORRECT(1).pdf, SHA-256 d8970cdb921683f5e9aa32165f03163098f169183e55fecf289bd2cbbc10aef1, 52 pages. The earlier original-preserved attachment is excluded.

Owner lock: THE HAPPY MAKERS PRESENT / BEFORE CHRISTMAS SLIPS BY / 24 Ten-Minute Family Activities for Less Rush, More Laughter, and Time to Really Be Together.

App repository branch gentle-steps/app-en-full24-purple-gold exact HEAD: e790eba36d03ac433daea24e208b6eaa3f673c25.

Migration verification:
- 24 days / 72 sections
- 24 PAUSE / 24 PLAY / 24 BETWEEN US
- all 24 days contain TRY IT TOMORROW
- full Before Day 1 and After 24 Days experiences
- exact five Christmas Happy Makers: Mimi, Luli, Dilo, Alio, Nini
- annual completion state is year-scoped
- local reminder permission, Android exact-alarm check, Dec 1–24 scheduling and tap/cold-start routing are present

Exact-head CI:
- English App 37596345358 / #190 SUCCESS
- SEO 37596345337 / #1098 SUCCESS
- Android 37596345317 / #143 SUCCESS

Lighthouse artifact 11469904299, digest sha256:6037483e423ec5d38e82d7160acf6fd65531a874f73c4794d4dc27e9f2167920.
Home and Day 22 both score 100/100/100/100. Home LCP 1522.84 ms; Day 22 LCP 1445.89 ms; TBT 0 and CLS 0 on both.

Visual artifact 11469754538, digest sha256:d9f74a0aa2d7ec6b49936272131c0a2e37a9b4c41061eae25a0e79c0fb7cf57d. Coverage includes Home, Family, Before Day 1, Days 01/12/18/22/23/24, completion and branding review.

Android artifact 11470009461, digest sha256:c2fef46642bab5e4d2a1fa97fea0514d707e55f9b727f5cd4ebad24a76f2bd31.
APK SHA-256 4da7830986eaa8eee0cfb517b99d4f7633e1496bc231f34622d343ed3ed93afc.
AAB SHA-256 20db154fd24fb078c3eb555821b81d25fbec2fb65796b7a58b5b092f11910720.
SDK 36, debug lint, release lint, APK/AAB and dependency HIGH gate are green. Three moderate transitive advisories remain.

Strict verdict: READY FOR INTERNAL TESTING NO. Runtime/content/tests are green, but the complete authorized production source for the exact approved five-person city/home-life Christmas splash is still unavailable. Current Android splash branding remains provisional. Do not substitute or redraw.

Real-device accessibility and notification delivery remain unverified owner/device gates.

A legacy release-audit file still contains pre-V2 wording. The current V2 internal-testing handoff and this checkpoint are the authoritative state until that legacy audit is synchronized.
