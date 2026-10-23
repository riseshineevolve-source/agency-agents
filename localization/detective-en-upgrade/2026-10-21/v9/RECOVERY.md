# Recovery and reproduce

Current readable results are the two proof/PDFs. Current canonical text is candidate/candidate.json, full225folio reading order is reader-manuscript.md and complete34scene source is final-scenes.json. Do not revert puzzle mechanics to older originals.

1. Restore this directory as detective-v9, with engine/ alongside. The archive also retains theexactV8baselinePDF andV8readingadapter for reproducibleproofs.
2. `python detective-v9/build_candidate.py` re-appliesonlytheauthorisedfinaldialogue, checksprotectedcanonicaltext and225readerpageprojections. It neverauthorsproseautomatically.
3. `python detective-v9/build_proofs.py` makesbothPDFs withsamefullwording andretainedV8leaves. `python detective-v9/render_poppler.py` makesfreshaccuraterasterQA.
4. ReproducedPDFmetadatamaychangebytehash. Do notcopyoldhash-boundapprovalreceiptsonto newbytes: comparetext/rendercontentandrebindhonestly. Candidateprosehashmustremainexact.
5. Actualdiagnostic,R1FIX,finalPASSandproof-onlyFIXhistory remainunderreviews. Use thefinalreceipts,notoldFIXversions. No neweditingroundisneededwithoutanactualdefectorownerrequest.

BookFactory production import belongs to the existing exclusive productwriter. Preserve full dialogue andportraitorder; doclayouts inthisarchivearereadingproofs.
