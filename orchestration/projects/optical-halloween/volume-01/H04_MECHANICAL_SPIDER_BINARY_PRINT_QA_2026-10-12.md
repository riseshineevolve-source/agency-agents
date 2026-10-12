# H04 Mechanical Spider — isolated binary/print QA (2026-10-12)
Status: **HOLD for print; owner shortlist untouched; no GOLD promotion.** A source-level QA run only, not a competing Halloween illustration writer. No Optical Animals changes.

## Verified original
Source: ChatGPT Library `/OPTICAL_HALLOWEEN/Volume_1/SELECTED_14/H04_MECHANICAL_SPIDER.png`; GitHub canonical 14-image manifest `orchestration/projects/optical-halloween/volume-01/selected-14/README.md`.
Original SHA-256 **9b7c1081a4837557aa0c1c3a67fe6cd0b05bf5e551384bb84d93fd5152a8f81c**, matches selected-14 manifest. Dimensions **1103 × 1426**, only **129.8 × 129.6 effective DPI** for 8.5 × 11 inches. RGB source: **17.22%** of pixels exactly black/white; **56.74%** contain non-neutral unequal channel values. It is not pure B/W.

## Actually completed local 1-bit tests
Native threshold 127 produces 48.41% black. At nominal 300-DPI canvas (**2550 × 3300 px**), 127 yields **48.39% black**, 150 yields **51.06% black**; both pass #000/#FFF *pixel* checks but neither recovers genuine source resolution. At 127 there are **3937** enclosed white regions; **3421** smaller than 10 mm² (86.9% of regions, covering 13.1% of total enclosed white area), and only **47** larger than 100 mm². The dense clockwork ornament contains many uncolorable microcells. Side-by-side preview clearly shows 150 closes thin details.

## Immutable QA artifact registry
| File | SHA-256 |
|---|---|
| `H04_MECHANICAL_SPIDER_SOURCE_VS_1BIT_QA_CONTACT_V01.png` | cc8c11c33e0829a9f9e3a1715d373a49060b40b7c0c7db9ec0234bb7c9893980 |
| `H04_MECHANICAL_SPIDER_NATIVE_1BIT_QA_V01.png` | fe6c37933cd21ee1c1f2a41f319d3c85b674eade54c104d207dc3bec7c1ae203 |
| `H04_MECHANICAL_SPIDER_PRINT_SCALE_1BIT_TEST_2550x3300_V01.png` | bfc0b3f6b5250470c7fec00d6e86b388e2ee813c9827b0491a9e6b30ea630b5f |
| `H04_MECHANICAL_SPIDER_DARKER_1BIT_ALTERNATE_TEST_2550x3300_V01.png` | 3297d1be3a5fee17ffac5aaaa9ffeb2c4afa57dad9f3a3d429daded77ac9cc1a |
Local files were actually rendered in `/mnt/data/optical_halloween_qa/` in the QA execution session. **These PNG bytes have not been committed to GitHub.** Library upload via `files.manage_library` returned `container_session_unavailable`; do NOT claim images archived in Library without verified subsequent success.

## Artistic and editorial decision
Recognizable imposing mechanical spider and articulated legs. But highly congested micro-work and source effective 130 DPI prevent real premium coloring print clearance. Maintain H04 *candidate* in owner-curated 14, never overwrite. Newer 2026-10-12 six-new-scene list supersedes older conflicting mapping that referred to E04 raven. Six actual open slots are H03/H06/H08/H10/H13/H16. No KDP/factory, no changes to H04.
Next safe independent task: QA of another **existing** locked image while illustration writer continues new assets; owner visual decision is required before modifying H04 line-art.