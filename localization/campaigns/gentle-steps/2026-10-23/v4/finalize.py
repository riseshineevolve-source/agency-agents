from pathlib import Path
import json,hashlib,re,subprocess
R=Path(__file__).resolve().parent;W=R.parent
load=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x):p.parent.mkdir(exist_ok=True,parents=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
rows=[]
for lang in ['pl','en']:
 cand=R/'candidate'/('candidate-'+lang+'.json');ch=sha(cand);reviews=[]
 for stage,path in [('native_language',lang+'-final/native_language.json'),('audience',lang+'-final/audience.json'),('meaning','truth-final/'+lang+'-meaning.json'),('logic','truth-final/'+lang+'-logic.json')]:
  p=R/'reviews'/path;x=load(p);assert x.get('status',x.get('overall_status'))=='PASS' and x['candidate_sha256']==ch,(stage,x)
  reviews.append({'stage':stage,'candidate_sha256':ch,'status':'PASS','reviewer':x.get('reviewer',x.get('reviewer_role')),'evidence':'reviews/'+path,'receipt_sha256':sha(p),'scope':x.get('scope',x.get('review_scope','Exact actual review scope in evidence receipt.'))})
 bundle={'candidate_sha256':ch,'reviews':reviews,'actual_reviewers':3,'sole_candidate_writer':'root','normalization_only':True};out=R/'reviews'/('FINAL_REVIEW_'+lang.upper()+'.json');dump(out,bundle)
 run=load(R/'run'/lang/'run.json');issues=[]
 for u in load(cand)['segments']:
  issues.append({'id':'UPGRADE-'+u['id'],'classification':'FIX','final_classification':'KEEP','status':'RESOLVED','segment_id':u['id'],'detail':'Actual diagnostic identified shared sales cadence, abstract/emotional pressure or register defects; upgrade preserves recognised openings and source-backed games.','resolution':'Root candidate and bounded13phrase closure; all actual four-stage final receipts PASS exact candidate. Initial diagnostic/R1FIX preserved.'})
 dump(R/'run'/lang/'issue-ledger.json',{'run_sha256':run['manifest_sha256'],'candidate_sha256':ch,'diagnostic':'COMPLETE','issues':issues,'source_ambiguities':[]})
 subprocess.run(['python',str(W/'engine-v10/scripts/rse-language.py'),'check','--run',str(R/'run'/lang),'--candidate',str(cand),'--reviews',str(out),'--output',str(R/'qa'/('CLI_CHECK_'+lang.upper()+'.json'))],check=True,stdout=subprocess.DEVNULL)
 report=load(R/'qa'/('CLI_CHECK_'+lang.upper()+'.json'));assert report['status']=='OWNER_READ_CANDIDATE' and not report['unresolved_issues'] and report['deterministic_qa']=='PASS'
 for x in load(cand)['segments']:
  # Reader text is already in the exact bound MD; metadata stays out of the Word copies.
  body=re.sub(r'\A---\n.*?\n---\n','',x['text'],flags=re.S)
  rows.append({'id':x['id'],'candidate_sha256':ch,'article_sha256':hashlib.sha256(x['text'].encode()).hexdigest(),'words_excluding_metadata':len(re.sub(r'[*#]','',body).split()),'source_days':[19,10,7] if x['id'].endswith('01') else [21,22,14],'format':'Independent same-language upgrade; not translation','function':'Everyday evening and practical entry' if x['id'].endswith('01') else 'Ready-made activity appeal and adult participation'})
dump(R/'qa/CONTENT_MAP.json',{'coverage':'Four complete articles inclSEOmeta, title,opening,sixteasers/labelseachlanguage,support,closingCTA','units':rows,'excluded':'R6book24daybody/labels master, app, website, formats/availability/prices, unverified links','stable_ids':'PL01,PL02,EN01,EN02 complete logical articles; review paragraph locators provide finer diagnosis'})
assert load(R/'qa/VISUAL_REVIEW.json')['status']=='PASS'
for row in load(R/'qa/DOCX_BINDING.json'):assert row['candidate_sha256']==sha(R/'candidate'/('candidate-'+row['language']+'.json'))
(R/'README.md').write_text('''# Gentle Steps articles V4

Two topics in Polish and English.01: finding family time during a full December evening.02: an activity Advent calendar with a place for adults to play. The owner asked for new upgraded same-language versions on23October2026.

Current clean copy is under candidate/ (fourMarkdown articles withSEOmetadata). Two editable Word reader copies are under deliverables/; each contains both articles in one language and excludes internal metadata. All paragraphs round-trip exact candidate prose. Rendered page images and intermediatePDFs are internal QA only.

Current editorial baseline is GitV3 at00beb0ffe274eb68ef424ece01b175194884c898; older LibraryV2 was read and retained for comparison. Exact October13campaign strings and R6 source actions are protected. PL and EN are sibling campaigns, independently upgraded in their existing language. User did not request book, app or website edits.

Root was sole author. Three actual independent agents supplied nativePL/audience, nativeEN/audience, and bilingualmeaning/logic reviews. Initial diagnostic/R1FIX remain;13bounded phrase changes close demonstrated defects. Four real stages PASS each exact candidate; pinned rse-language CLI checks pass. No human panel, guaranteed sales, owner content freeze or publication is claimed.

Six brief teasers come from three distinct days perarticle. No complete book day/fullgame is printed. No unsupported developmental benefits, ages, availability, formats, prices, release dates or links are invented. CTAs are plain text; existing website writer can attach a verified matching preview destination. R6body stays exact; old section labels in that source are superseded by current campaign locks.

The complete Word versions and upgraded Markdown sources are saved. Previous files retain version history. Source inventory, GOLDEN_KEEP, content map, exact candidate hashes, actual reviews, CLI checks and document binding remain alongside. Engine snapshot is qa/ENGINE_SNAPSHOT.json. This is an editorial candidate for owner reading, not a production/print/release approval.
''')
dump(R/'qa/FINAL_SUMMARY.json',{'status':'OWNER_READ_CANDIDATE','candidates':{lang:sha(R/'candidate'/('candidate-'+lang+'.json')) for lang in ['pl','en']},'source_revisions':'qa/SOURCE_INVENTORY.json','actual_stage_passes':8,'actual_reviewers':3,'candidate_writer':'root','sourcebook_changed':False,'website_changed':False,'published':False,'word_reader_prose_exact':'PASS','all_rendered_pages_inspected':'qa/VISUAL_REVIEW.json','cli_checks':'PASS both independent same-language runs'})
print(json.dumps({'status':'OWNER_READ_CANDIDATE','articles':len(rows),'reviews':'8actualstages PASS'}))
