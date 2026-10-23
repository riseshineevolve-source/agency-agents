from pathlib import Path
import json,yaml
R=Path(__file__).resolve().parent;prefix='localization/campaigns/gentle-steps/2026-10-23/v4/'
q=json.loads((R/'qa/FINAL_SUMMARY.json').read_text());stage=R/'git-stage';stage.mkdir(exist_ok=True)
mail=yaml.safe_load((R/'baseline/MAILBOX_BEFORE.yml').read_text());mail['updated']='2026-10-23';mail['status']='GENTLE_STEPS_ARTICLES_V4_OWNER_READ_CANDIDATE__PL_EN_SAME_LANGUAGE_UPGRADES'
mail['branch_or_repo_state']['gentle_articles_upgrade_branch']='codex/gentle-steps-articles-upgrade-20261023'
mail['branch_or_repo_state']['gentle_articles_parent_head']='00beb0ffe274eb68ef424ece01b175194884c898'
mail['milestone']='Owner-requested V4 same-language upgrades complete for twoGentleSteps articles inPLandEN. One writer and three actual independent reviewers, eight real finalstagePASS receipts; both rse-language checksPASS. Exact PL '+q['candidates']['pl']+'; EN '+q['candidates']['en']+'. TwoWord readercopies render-verified, fourMarkdownsources/SEOupdated with original Libraryidentities. All prior book/app/site work unchanged.'
for d in mail['dependencies_needed']:
 if d['lane']=='central_control_tower' and 'bilingual Gentle Steps guides' in d['need']:
  d['need']='Consume V4 bilingual Gentle Steps articles at '+prefix+' after owner editorial acceptance. Two distinct intents, four same-language upgrades, eight actualreviewstagesPASS and twoCLIchecksPASS. Preserve exact candidate hashes; website sole writer attaches verified matching preview/product route and actual format availability. No website/app/book changes or publication by localization.'
for f in ['README.md','candidate/candidate-pl.json','candidate/candidate-en.json','qa/FINAL_SUMMARY.json','qa/LIBRARY_RECEIPT.json']:
 x=prefix+f
 if x not in mail['reusable_outputs']:mail['reusable_outputs'].append(x)
mail['next_safe_task']='Owner reads twoPL/twoEN V4articles. Existing sole websitewriter may consume exact approved Markdown and attach verified matching preview route; verify actualpagefit and current formats before any separate publication. Existing DetectiveV10handoff remains valid and unchanged.'
mail['checkpoint_reference']=prefix+'qa/FINAL_SUMMARY.json';mail['revenue_policy_ack']='Bounded twoarticles xPL/EN; one writer, threeactualreviewers, targeted13phraseclosure. No book/puzzle re-audit, newenginefeatures, paidfallback or publication.'
(stage/'mailbox.yml').write_text(yaml.safe_dump(mail,allow_unicode=True,sort_keys=False,width=110))
current={'version':'V4','date':'2026-10-23','status':'OWNER_READ_CANDIDATE','path':prefix,'candidates':q['candidates'],'source_baseline':'V3editorial at00beb0ffe274eb68ef424ece01b175194884c898, comparedwitholderLibraryV2','no_website_app_or_book_changes':True}
(stage/'CURRENT_ARTICLES.json').write_text(json.dumps(current,indent=2)+'\n')
files=[]
for p in R.rglob('*'):
 if not p.is_file() or any(x in p.parts for x in ['render','private-helpers','git-stage','__pycache__','engine-snapshot']):continue
 rel=p.relative_to(R)
 if p.suffix not in ['.md','.json','.py','.yml']:continue
 if p.name.endswith('UPLOAD_REQUEST.json'):continue
 if p.name in ['source-bundle.json','git-payload.json','UPLOAD_REQUEST.json','GITHUB_SAVE.json']:continue
 files.append({'path':prefix+str(rel),'mode':'100644','type':'blob','content':p.read_text()})
files.extend([{'path':'orchestration/control-plane/mailboxes/polish_localization.yml','mode':'100644','type':'blob','content':(stage/'mailbox.yml').read_text()},{'path':'localization/campaigns/gentle-steps/CURRENT_ARTICLES.json','mode':'100644','type':'blob','content':(stage/'CURRENT_ARTICLES.json').read_text()}])
(R/'git-payload.json').write_text(json.dumps(files,ensure_ascii=False));print(json.dumps({'files':len(files),'chars':len((R/'git-payload.json').read_text())}))
