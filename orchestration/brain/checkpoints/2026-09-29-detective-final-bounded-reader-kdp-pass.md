# Detective Academy — Final bounded reader/KDP source pass

Date: 2026-09-29
Authority: Central RSE Technical Orchestrator
Status: SOURCE PUSHED / CURRENT-HEAD CI GREEN / EXACT OWNER PDF REVIEW REQUIRED / EN NOT FROZEN

## Durable source state

Production repo:
`riseshineevolve-source/RISE.SHINE.EVOLVE`

Branch:
`feature/detective-book-factory`

HEAD:
`2c8145699887980536e11ada28211892b72b879d`

Commit message:
`Complete bounded Book 1 reader and print QA fixes`

PR #571:
- state: OPEN
- draft: YES
- mergeable: YES
- mergeable_state: CLEAN
- head: `2c8145699887980536e11ada28211892b72b879d`

Current-head CI:
- Build Detective Academy PDF #201: SUCCESS
- SEO Validation #777: SUCCESS

Exact five non-private source files changed:
1. `tools/detective-book-factory/render_book.py`
2. `tools/detective-book-factory/scripts/audit_v3_premium_interior.py`
3. `tools/detective-book-factory/scripts/build_v3_premium_interior.py`
4. `tools/detective-book-factory/scripts/finalize_v3_premium_qa.py`
5. `tools/detective-book-factory/scripts/prepare_v3_print_derivatives.py`

Private production assets and generated `dist/` binaries remain excluded from GitHub.

## Owner-reported local artifact

`HMDA_Book1_EN_FINAL_BOUNDED_READER_KDP_OWNER_REVIEW_2026-09-29.pdf`

Owner-reported SHA-256:
`5212f7c3ebc4c5228516c18c31be84a54eaf0d147a1e439150225b4f5192aa22`

Owner-reported local validation:
- 180 pages;
- no renderer overflow;
- 714 reader-copy fragments present;
- 15/15 spatial cases uniquely solvable;
- embedded images >= 312.8 effective DPI;
- all nine contact sheets + enlarged changed-page samples reviewed;
- resampling improves effective print DPI but does not add source-image detail.

## Interpretation

GitHub source and current-head CI are now durable and green.
The exact private-input owner-review PDF itself is still a local artifact and cannot be independently certified from normal CI.

Next gate:
1. owner uploads/shares the exact PDF above;
2. Central performs final regression/readability audit of the changed bounded-fix pages plus whole-artifact integrity;
3. if clean -> KDP Previewer;
4. representative physical proof;
5. explicit owner EN freeze;
6. final cover/spine from frozen final page count;
7. owner-controlled KDP publication.

No merge, EN freeze or publication is authorized by this checkpoint.
