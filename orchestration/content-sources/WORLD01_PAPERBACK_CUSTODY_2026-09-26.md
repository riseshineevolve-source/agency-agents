# World 01 published-source custody — 2026-09-26

## Authority and inspected binary

The owner supplied `10 STORIES WORLD 01 FINAL paperback.pdf` as canonical published World 01 evidence for this pilot. The file was inspected read-only outside Git. It is 14,523,549 bytes, SHA-256 `adf9d384985ec7ad0fb1d7f9f6c3d46189592a171474c38ee93ac35bb808c549`, 108 pages, 440.88 × 666 pt, with paperback ISBN `9798247194682` on PDF page 2. Its PDF metadata says title `10 STORIES WORLD 01 FINAL`, author `J.R. Zee`, creator/producer Canva, and creation/modification date 2026-09-18. The binary is deliberately not in the repository.

The existing `level-up-your-brain-world-01.yml` also records a 108-page, image-heavy flattened print master with SHA-256 `25d249a8a36f41e0f25177a87fe3fb75357c6b5605089a9eae561dfa2780dca3` and 134,774,279 bytes. Both have the same recorded page dimensions. These are **different binaries**. Their content equivalence has not been established, and the new PDF does not overwrite the older custody entry. The user-supplied paperback is the governing published evidence for this bounded comparison.

## Reproducible extraction boundary

- `pypdf 6.10.0` successfully extracted text from the supplied 108-page paperback. The first ten mission opener pages are 15, 23, 33, 42, 51, 60, 68, 76, 84, and 92; the game map is on page 13.
- PDF text order is unreliable in speech bubbles. A line can be split, reordered, or merged with nearby labels. Visual inspection was used for the candidate pages 15, 23, and 33 and for discrepancy pages 20, 26, 27, 36, and 37.
- The locked opener evidence manifest is `orchestration/content-sources/world01-paperback-opener-evidence.json`. It records only title, key, and objective for missions 1–3. `scripts/validate-world01-pilot-provenance.py --pdf <private-pdf>` verifies the binary SHA-256, byte count, page count, and those exact fields on the specified pages.
- The app comparison source is private `riseshineevolve-source/spark-joy-fam` `src/data/storyContent.ts`, read through the GitHub connector on 2026-09-26. Its Git blob SHA is `377463e1853743f82d4d3bca5ce89b6e5b05b210`. Nothing was written to that repository.

## Coverage and source gaps

The candidate contains **3 of 10 published mission openers (30%)**, covering **3 of 108 PDF pages as direct pack evidence (2.78%)**. It contains **0 of 10 complete story/console/quest/code units**. These denominators describe different kinds of coverage and must not be collapsed into a full-book parity claim.

The exact remaining gaps are: mission openers 4–10; full narrative, speaker attribution, order, neuro-coaching console, quest, secret code, and artwork for missions 1–10; the preface, character pages, end matter, and bonus pages; published-source equivalence with the older flattened master; approved Polish product prose and layout fit. Scientific/health claims in the book or app have not been independently reviewed here. No source-derived image asset was committed.
