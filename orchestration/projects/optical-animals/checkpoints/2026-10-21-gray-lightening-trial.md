# Optical Animals — owner retains grayscale; one-image lightening trial

Date: 2026-10-21
Status: GRAYSCALE_SELECTED__ONE_IMAGE_TRIAL_DELIVERED__OWNER_TONAL_CHOICE

Owner explicitly chose retaining gray shading rather than the pure black/white alternative, and requested a trial on one image with roughly10–15% lighter/less gray. This does not cancel the previously selected RSE Optical Art Series identity, shared intro typography, single-sided wording or restrained copy system.

## Completed scope

Lion, actual book page27, exact native2588×3375 grayscale source pixels. Source decoded pixels independently matched the retained premium grayscale PDF image. Neither the full book nor any approved source file was overwritten.

Two derivatives and an original/10%/15% comparison with matched face detail were delivered:
- Comparison: WILD_ILLUSIONS_LION_GRAY_LIGHTENING_COMPARE.png; libfile_452c81f31b44819182aed386057e1439 v0; SHA25665a07dcbb6210bdc59540abf5bb0d8b0095dede712bc83250ca0ffc87d62d742.
-10%: WILD_ILLUSIONS_LION_GRAY_LIGHTER_10.png; libfile_d4b0d0861bd88191a46c02d27ec6116d v0; SHA256c7398cf7a94b153c0a239a775c2575438c9a99107b9ecb271816350068b9edd8.
-15%: WILD_ILLUSIONS_LION_GRAY_LIGHTER_15.png; libfile_654e400d6660819194db2cf4557bdf7e v0; SHA2569fe519cfbda4689a9604957bf6c2aa62f97edf2a6e1509fd75be1cc37578fe5a.

All three saves succeeded. Both variant assets are native-size lossless L-mode PNGs tagged300ppi. Preview only; not assembled into a new full-book PDF.

## Exact method and QA

Pointwise tonal mask on original pixels. Values0–24, including black solids/outlines, and white255 are locked. Smooth weighting24–72 avoids tonal discontinuities; higher grays brighten toward white. Strength is calibrated separately to reduce digital nonprotected-gray density sum(255-value) by approximately10% and15%. Actual measured reductions9.9982% and15.0001%. This metric describes encoded tones, not measured physical printing-ink consumption.

No crop, resampling, anatomy/pattern changes, generation, dithering or spatial cleanup in the variant assets. Asserted monotonic LUT, no darkened pixel, exact locked-black/white equality, lossless readback and original hashes unchanged. Comparison resizing is presentation-only.

Visual judgment:15% is the stronger candidate on this lion; lighter shading still retains3D modeling. Owner has not yet selected a strength for the whole book. Do not apply global changes based solely on the recommendation.

## Canonical continuation

- Art direction now grayscale retained. Pure B/W deliverables are an archived alternative, not the chosen publication treatment.
- Retained grayscale PDF WILD_ILLUSIONS_PREMIUM_FINAL_48P.pdf, libfile_507fe3cae5088191be459397753617d0 v1, SHA256bf12439907c4481d91926bc34ef86ed51d7667a17fc712a5e8261fa33963a6ef remains unchanged.
- The old grayscale premium PDF predates the latest shared RSE typography/story handoff. A future chosen-gray master must combine selected gray artwork treatment with that latest intro/copy system; do not silently roll back those changes by treating the older grayscale PDF as the new final.
- Latest layout/copy/handoff baseline: orchestration/projects/optical-animals/checkpoints/2026-10-21-rse-pure-bw-canva.md.
- Next gate: owner visual choice after one-image trial. Then apply only the selected tonal treatment to grayscale art derivatives, retain exact black/original custody, assemble grayscale KDP/Canva masters and preflight. Actual Canva import, physical proof, cover and release remain separate unfinished steps.
- Product branch unchanged. No publication, paid order or external messages.

Workspace reproducible producer: /workspace/scratch/b288b564abb1/tmp/gray-lift-preview/make_preview.py and qa.json. Durable images above are the handoff of record.

model_policy_ack: rse-weekly-usage-2026-10-21-v1
recommended_profile: production
runtime_model_observed: UNKNOWN
runtime_reasoning_observed: UNKNOWN
runtime_speed_observed: UNKNOWN
application_status: RECOMMENDATION_ONLY
