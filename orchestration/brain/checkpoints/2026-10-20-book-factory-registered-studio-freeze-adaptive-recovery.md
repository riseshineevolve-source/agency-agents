# Book Factory — registered Studio recovery and new owner requirements

Date:20October2026. Exclusive writer remains codex_work_29b36a8d7861. This supersedes the older local-only implementation state in the earlier recovery checkpoint.

## Durable source
Product repo:riseshineevolve-source/RISE.SHINE.EVOLVE
Branch:feature/rse-book-factory-v2
Implementation milestone:1a5c5bc13cd0a16e9439110c002dee5b1fabd825
Control checkpoint:d45d4f602de35c2d3a2d319365d1b29d15d77e8a
Source:tools/rse-book-factory-v2/studio/
Entry:full_gold_volume.production_build imports production.production_build.
Recovered original Studio and NEW modules are now actually committed, not just transient workspace files. Initial source registration07e1427d; production integrationb14f9de5; testworkflow900de97d; narrative-only safetyfix1a5c5bc1. Do not revert these to old privateZIP blindly.

## New user requirements implemented in source, validation pending
- Approved page freeze per version, PDFSHA and renderedpageSHA. Explicitunfreeze; staleversion guards; olderPDFsneveroverwritten.
- Build only selected physicalfolios; preserve ALL otherpages from exactbasePDF; freeze/selectedconflicts rejected. Production rechecks unchangedrenderhashes afterassembly; UI also rechecks approvals before publication.
- Adaptive measured1–12boxes,center/justify, consistent11.5–14ptbody, contentweights and boundedpadding, automaticcolumns, completewordpreservation, overflowfailsbeforepartialpaint. Explicitshort-content unusedspace receipt; no inventedfiller. Textoverrides target only narrative slot and preserve existing Comms/art/Notes.
- SourceCase03 unchangedA017/B071 photos now facing24left/25right at identical512×384ptpositions. FullwidthbothphotoscannotfitoneLetterpageatthisreadablesize. BelowPhotoB10stroke-only hollowquestionglyphs;not solidquestions/numbers.26is10observationworksheet;225physicalcountretained. QA must updateexpectedA/Bfolios from25/26to24/25.
- OriginalV12SHA lock stays unchanged;9auditedCase03derivative/callbackcorrections ineditorial_reconciliation.py.4plain0records andseparate6symbolcode unaffected.
- Recoveredopening7/8,exact4manualevidencefamilies,full115footprints+FROM/TO,nativeNARRATIVEbodyimport(including143),all16solvedmapnativeaxes/markers/rosters present in source. These modules had isolatedactualsource tests before second outage.

## Evidence and limits
RecoveredUI9/9testsPASS; real4fileHTTPupload/previewPASS(session495cbb396d174ddf). NativeNARRATIVE15folios/46avatars+sourcevectors testsPASS; opening/evidence/family/solvedmodule groupsPASS as recorded in agentmessages. DO NOT sum overlappinggroups into a fictitiousglobalcount.
Current combined production.py/updatedGold/adaptive/newfreeze actual225p path HAS NOT RUN. Last priorfullHTTP225p candidate97,733,779bytes was frombeforethisnewintegration andbefore143repair; not final. Newselected/frozenproof stillPENDING. Gold/adaptivetestsrequiringprivate3PNGmasters need theirhydratedsourceenvironment. Historicaltestsrejecting9clues/oldclue_font_pxmetricsneedmigration to currentcontract.
AddedCIworkflow.github/workflows/book-factory-studio.yml with compilation/UI/adaptive/photo-outline/native-sourcecontracts. Run39487502681 failed in3seconds with job118851644797 andZEROsteps. Exactrunner-startfailurereasonnotreturned by availableconnector; do not callthisatestfailureorPASS. Do not assume billingissuewithoutproof.

## Current hard blocker
The shared executor disconnected again after code/modules were restored. Evenpwd/read-onlycalls hang; latestterminalresponse409environment_offline:Environment is not connected. This blocks localread/write/render/package/Librarysaving. Root no longer starts parallelheavyPDFjobs; cause is unproven.
RemoteDesktopCommander listdevices on intendedlink rise.shine.evolve@gmail.com returnedNOconnecteddevices twice. To use thatfallback, owner must connectdeviceathttps://mcp.desktopcommander.app/ andkeepRemote terminalrunning. No credentials/spend/mainmerge requested.

## Next safe actions, already authorized
1.Recover one workingexecutor orconnectedRemoteDesktop device. No need re-askwriterpermission.
2.Hydratecodefromproductbranch,originalinputs+3referencePNGsfromLibraryZIP. Originalinputs/referencehashes inearlierrecoverycheckpoint. The priorworkingdirectorymayagainbemissing; GitHubnowholdsallnewsource.
3.Runcompile/boundedtestgroupsSEQUENTIALLY; fixactualexceptions (newproductionenginehasnotbeencompiledyet). CompletefontfallbackCI/generic preview; production restores exactembeddedsourcefonts.
4.RealHTTPfull225pbuildfromUI, inspectPhoto24/25/outlinedmarks+143+allaffectedfamilies;sourcecoverage/canonical90hints/30solutions/15puzzlemaps/16solvedmaps. UpdateQAphotoexpectations24/25andmanualrasterevidenceproofmethodology.
5.Approve/freezechosenrealpages; editoneotherfolio withrealengine; assertallunselected/frozenpixelsidentical; retrycachedownloadidenticalSHA. Teststaleversion andmodifiedapprovalPDFrefusal.
6.Migrateold9clue/metricregressions; verify600naturalwordlayoutandsafeoverflow. No tinytypeorblankplaceholderfallback.
7.PackageusableStudioZIPincludingprivate3masterPNGsbutnot402MBinputs/cache/jobs; savefinalPDF+toolZIPpersistently throughcurrentLibraryworkflow. No finalnewdeliverables saved yet becauseexecutionisoffline.
8.Updateproductandcentrallaneonlywithverifiedcompletion. Finalprint/nativePPIlimitationshonest;notKDPpublished/approvedbyinference.
