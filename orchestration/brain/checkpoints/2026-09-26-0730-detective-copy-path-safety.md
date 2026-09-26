# Detective EN copy-polish path safety

Date: 2026-09-26
English freeze: FALSE.

Deterministic dry-run against the exact owner V4.1 master proves that copy normalization must be path-bounded.

A blind spelling replacement would modify 45 locked spatial asset/provenance scalar paths because canonical filenames contain the token "relabelled". That would break exact-source identity.

Safe invariant:
- modify reader-facing copy fields only;
- preserve every asset/provenance scalar byte-for-byte;
- exact dry-run target is 34 reader-copy scalar paths representing 17 mirrored corrections;
- audited UK spellings remaining in non-asset copy after the bounded transform: zero;
- asset-path changes after the bounded transform: zero.

This supersedes any whole-file replacement strategy. Product source was not changed because the connected product-repository write was blocked before mutation.
