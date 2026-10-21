from pathlib import Path
import json,yaml,hashlib
R=Path(__file__).resolve().parent;W=R.parent
def dump(p,o):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
delivery=json.loads((R/'integration/LOCAL_DELIVERY.json').read_text())
receipt=json.loads((R/'integration/PERSISTENCE_RECEIPT_V7.json').read_text())
assert receipt['status']=='SAVED' and receipt['all_local_bytes_unchanged']
ch=delivery['candidate_sha256']
mail=yaml.safe_load((R/'integration/mailbox-before.yml').read_text())
mail['status']='V7_OWNER_READ_CANDIDATE__HM_COMMS_AND_EN_EDITORIAL_UPGRADE'
mail['milestone']['detective_en_v7_editorial']={
 'owner_authority':'Explicit wholeEnglishupgrade with rse-language and witty, affectionate, story-useful HMComms; current21October2026request.',
 'path':'localization/detective-en-upgrade/2026-10-21/v7','candidate_sha256':ch,
 'baseline_v6_sha256':'d9dcc50eaccea03f693b1ade4ea001d522379d9def9f0467dd2e21ddd7e9fedc',
 'source_folios':225,'stable_units':3067,'changed_units_from_v6':229,'changed_folios':48,
 'main_comms_assessed':30,'main_comms_changed':25,'spoken_turns_changed':105,'whole_golden_scenes':[5,11,16,17,27],
 'prior_audit':'V6vsowner225 changed15mainComms/27turns;15unchanged; V5toV6Commsdelta0.',
 'all27_v6_repairs_preserved':True,'mechanics':'Allclues/maps/90hints/30answers/reasoning exactV6; only nonmechanic212summary chronologycorrected.',
 'reviews':'Twoactualindependent agents full225folioR1 plus8-unitclosure; native/audience/meaning/logic PASS exacthash.',
 'cli':'run-r2 OWNER_READ_CANDIDATE; deterministicPASS; no unresolvedissues/sourceambiguities.',
 'reading_proof_sha256':delivery['reading_pdf']['sha256'],'reading_proof_pages':225,
 'proof_checks':'225copy/offpage and52pixel-identityPASS; independent69folio/25fullsizevisualsamplePASS; unsampled156excluded.',
 'comms_comparison_sha256':delivery['comparison_pdf']['sha256'],'comms_comparison_pages':34,
 'comparison_qa':'All34pages visuallyinspected;495mainspoken-versionroundtripsPASS.',
 'archive_sha256':delivery['archive_sha256'],'library':receipt['files'],
 'production_source_or_renderer_changed':False,'main_merged':False,'published':False,'frozen':False,
 'ci':'FinalheadhostedgreenNOT_CONFIRMED; no Actionsdispatch.',
 'handoff':'ExistingsoleBookFactorywriter consumes exact V7importpacket with allV6repairs andunchangedfigurecontract. Actualimport/fit/printreceipts pending; no PLmigration.'}
mail['next_safe_task']='Existing sole BookFactory writer consumes exact V7 editorial import packet and preserved V6 figures; bind mapped import and final typesetting/print receipts. No further prose rewrite without a concrete defect or new owner request.'
mail['checkpoint_reference']='localization/detective-en-upgrade/2026-10-21/v7/CHECKPOINT.md'
mail['revenue_policy_ack']='Owner-requested completeEnglisheditorialreview andboundedprose/Commsupgrade; noenginefeatures, competingtranslation, publication or productrendererchanges.'
for item in mail.get('dependencies_needed',[]):
 if item.get('lane')=='detective_book_factory' and 'exact owner-authorized V6' in item.get('need',''):
  item['need']='Consume exact V7 candidate '+ch+' and v7/integration/EDITORIAL_IMPORT_PACKET_V7.json.229V6deltas/310original225deltas;3067targethashes. All27V6repairs andfourcorrectedsourceleaves24/25/97/211 retained. Existingfolioremap16→15/27→26 retained. Supplyactualfinaltypesetimport/fitreceipts; no chatdelivery or printapproval inferred.'
current_mail=yaml.safe_dump(mail,allow_unicode=True,sort_keys=False,width=120)
(R/'integration/polish_localization.yml').write_text(current_mail)
active={'state':'V7_OWNER_READ_CANDIDATE__INDEPENDENT_REVIEWS_PASS__PRODUCTION_HANDOFF_PENDING',
 'owner':None,'candidate_sha256':ch,'checkpoint':'v7/CHECKPOINT.md',
 'rule':'V6preservedhistorically;V7isowner-authorizedsame-languageeditorialupgrade. ExistingBookFactoryremainsexclusiveproductionwriter.',
 'next_safe_task':mail['next_safe_task']}
dump(R/'integration/ACTIVE_WRITER.json',active)
root='localization/detective-en-upgrade/2026-10-21/'
current_readme='''# Detective Academy English editorial candidate

Current owner-read candidate: **V7**, in [v7](v7/README.md). Exact text, full-book reading proof, original/V6/V7 Comms comparison and independent review receipts are complete. The source master is [v7/candidate/candidate.json](v7/candidate/candidate.json).

V7 reviews all225folios and30mainComms;25scenes/105turns change, alongside targeted narrative clarity. All27V6source repairs and all actual puzzle/hint/answer/mechanics truth remain. One nonmechanic solution summary corrects instruction chronology. [Current checkpoint](v7/CHECKPOINT.md) names exact hashes and evidence.

V5 and [V6](v6/README.md) remain historical checkpoints. Their artifacts must not silently replace current V7. The owner's earlier225-page source is still the immutable comparison baseline. No PL source migration is authorized by this evolving EN edition.

The existing sole BookFactory writer consumes [V7's import packet](v7/integration/EDITORIAL_IMPORT_PACKET_V7.json). Final product import, layout and print proof remain separate; no renderer changed, main merged, freeze granted or publication made here. No hosted CI green is claimed.
'''
elements=[{'path':root+'README.md','mode':'100644','type':'blob','content':current_readme},
 {'path':root+'CHECKPOINT.md','mode':'100644','type':'blob','content':(R/'CHECKPOINT.md').read_text()},
 {'path':root+'ACTIVE_WRITER.json','mode':'100644','type':'blob','content':json.dumps(active,ensure_ascii=False,indent=2)+'\n'},
 {'path':'orchestration/control-plane/mailboxes/polish_localization.yml','mode':'100644','type':'blob','content':current_mail}]
def include(p):
 rel=p.relative_to(R)
 if any(z.startswith('.') or z=='__pycache__' for z in rel.parts):return False
 if rel.parts[0] in ['tmp','baseline','run']:return False
 if p.suffix not in ['.json','.py','.md','.txt','.yml']:return False
 if p.name=='mailbox-before.yml':return False
 if rel.as_posix() in ['candidate/candidate-segments.json','candidate/candidate-pages.json']:return False
 if rel.parts[0]=='run-r2' and p.name not in ['RUN_RECEIPT.json','change-scope.json','issue-ledger.json','SOURCE_AND_WORKFLOW.md']:return False
 return True
for p in sorted(p for p in R.rglob('*') if p.is_file() and include(p)):
 elements.append({'path':root+'v7/'+p.relative_to(R).as_posix(),'mode':'100644','type':'blob','content':p.read_text()})
payload={'repository_full_name':'riseshineevolve-source/agency-agents','base_tree_sha':'3f58d7d7ac3c9719a53fa0d808269e53d9d8603b','tree_elements':elements}
dump(R/'tmp/git-payload.json',payload)
body='''The English candidate now has a full-book editorial pass focused on funny, affectionate Happy Makers Comms that add story value and bring the reader into the team.25 of30main scenes change (105spoken turns); strong scenes05/11/16/17/27remain. Luli joins the play, adults share the teasing, and reader support appears through practical actions. The original/V6/V7comparison makes every prior and new dialogue change reviewable.

V7 changes229stable units on48source folios from V6, preserves all27V6repairs and all clue/map/hint/answer/reasoning text, and corrects only one nonmechanic summary's chronology. The225folio reading artifact includes locked evidence art; the34page comparison covers30main and3support conversations. No product source or renderer changed.

Validation: actual independent full225folio native/audience/meaning/logic reviews plus exact8-unit closure PASS; CLI OWNER_READ_CANDIDATE/deterministicPASS;225leaf copy/offpage and52pixel-identity checksPASS. Independent69folio/25fullsize reading-PDF visual samplePASS; comparison34pages visualPASS and495speech-version roundtripsPASS. No final print/layout approval or hosted CI green is claimed.

Canonical candidate: v7/candidate/candidate.json (SHA256 df4b39f8793de32ace25998ae2986dfb708ad08a5bb80b6f0b8c0eecef49eeb1). Exact original/V6 import operations,3067targethashes and unchanged corrected figure contract are in v7/integration/EDITORIAL_IMPORT_PACKET_V7.json. Full files are saved; stable Library identities/version receipts are in v7/integration/PERSISTENCE_RECEIPT_V7.json. Existing sole BookFactory writer retains production import, final fitting and print proof. No main merge, freeze, publication or PLmigration.
'''
(R/'tmp/pr-body.md').write_text(body)
print(json.dumps({'git_elements':len(elements),'payload_bytes':(R/'tmp/git-payload.json').stat().st_size,'candidate_sha256':ch},indent=2))
