"""Build an exact, read-only consumer packet; never edit candidate/PDF/renderer.

Usage: python build-integration-packet.py --root PATH --pdf SOURCE.pdf --studio DIR --studio-archive ZIP
The Studio archive is inspected only for routing/capability evidence, never run.
"""
import argparse, collections, hashlib, json, re
from pathlib import Path
import fitz
SOURCE='9db84d4f138cbbde8eb1f4a0f783f4d126c639120a11cabb65fc00711b9f05a0'
CANDIDATE='ec93cfc7a99257113fe33d6536574d2d6889c969ec68dac69ca97ad26010a55e'
INTAKE='fab419c8d30324a04e7368c8acd38faa574088d69169e4451eeb6419cb37a155'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def th(s):return hashlib.sha256(s.encode()).hexdigest()
def write(path,obj):path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def run(root,pdf,studio,studio_archive):
 assert sha(pdf)==SOURCE,'Wrong source PDF'
 assert sha(root/'candidate/candidate.json')==CANDIDATE,'Wrong candidate'
 assert sha(root/'source/intake-v4.json')==INTAKE,'Wrong source intake'
 intake=json.loads((root/'source/intake-v4.json').read_text())['segments']
 candidate=json.loads((root/'candidate/candidate.json').read_text())['segments']
 assert [s['id'] for s in intake]==[s['id'] for s in candidate]
 target={s['id']:s['text'] for s in candidate}; source={s['id']:s for s in intake}
 bypage=collections.defaultdict(list)
 for s in intake:bypage[s['page']].append(s)
 protected=[s['id'] for s in intake if s['protected']]
 changed=[s for s in intake if s['text']!=target[s['id']]]
 assert len(protected)==2367 and all(source[i]['text']==target[i] for i in protected)
 assert len(changed)==91 and len({s['page'] for s in changed})==44
 ledger=json.loads((root/'candidate/change-ledger.json').read_text()); reasons=collections.defaultdict(list)
 for item in ledger:
  for sid in item['actual_changed_ids']:reasons[sid].append(item['defect'])
 assert set(reasons)=={s['id'] for s in changed}
 out=root/'integration';out.mkdir(exist_ok=True)
 doc=fitz.open(pdf);assert len(doc)==225
 image_cache={};pages=[];operations=[]
 for n,p in enumerate(doc,1):
  images=[]
  for info in p.get_image_info(xrefs=True):
   x=info['xref']; entry={'bbox_pt':list(info['bbox']),'transform':list(info['transform']),
    'width_px':info['width'],'height_px':info['height'],'xref_in_this_pdf_only':x}
   if x>0:
    if x not in image_cache:image_cache[x]=hashlib.sha256(doc.extract_image(x)['image']).hexdigest()
    entry['encoded_image_sha256']=image_cache[x]
   else:entry['encoded_image_sha256']=None
   images.append(entry)
  pix=p.get_pixmap(matrix=fitz.Matrix(.5,.5),colorspace=fitz.csRGB,alpha=False)
  vector=repr(p.get_drawings())
  local=[s for s in bypage[n] if s['text']!=target[s['id']]]
  pages.append({'source_folio':n,'page_size_pt':[p.rect.width,p.rect.height],
   'source_native_text_sha256':th(p.get_text()),'source_render_rgb_36dpi_sha256':hashlib.sha256(pix.samples).hexdigest(),
   'render_size_px':[pix.width,pix.height],'vector_repr_sha256':th(vector),'images':images,
   'image_instances':len(images),'source_segment_ids':[s['id'] for s in bypage[n]],
   'protected_segment_ids':[s['id'] for s in bypage[n] if s['protected']],
   'changed_segment_ids':[s['id'] for s in local],
   'raster_or_visually_transcribed_text':any(s['bbox'] is None for s in bypage[n]),
   'semantic_visual_approval':False})
  native_blocks=p.get_text('dict')['blocks']
  for s in local:
   bbox=s['bbox'];spans=[]
   if bbox:
    for b in native_blocks:
     if b['type']!=0:continue
     if not fitz.Rect(b['bbox']).intersects(fitz.Rect(bbox)):continue
     for line in b['lines']:
      for span in line['spans']:
       if fitz.Rect(span['bbox']).intersects(fitz.Rect(bbox)):
        spans.append({'font':span['font'],'size_pt':span['size']})
   dest=n;route='SAME_SOURCE_FOLIO__RESOLVE_SEMANTIC_SLOT'
   if n==16:dest=15;route='CASE01_OPENING_STORY_COMMS_ON_POST_MIGRATION_STUDIO'
   elif n==27:dest=26;route='CASE04_NARRATIVE_ON_POST_MIGRATION_STUDIO'
   elif n==137:route='CASE30_STORY_IN_POST_MIGRATION_MERGED_STORY_COMMS'
   elif n==138:route='CASE30_BOARD_IN_POST_MIGRATION_STUDIO'
   operations.append({'id':s['id'],'source_folio':n,'source_bbox_pt':bbox,
    'before':s['text'],'after':target[s['id']], 'before_sha256':th(s['text']),
    'after_sha256':th(target[s['id']]),'classification':s['classification'],
    'source_font_observations':spans,'defects':reasons[s['id']],
    'consumer_route_hint':route,'post_migration_destination_folio_hint':dest,
    'slot_binding_status':'REQUIRES_PRODUCT_WRITER_RECEIPT',
    'audit_rationale_override':('Retained explicit navigation to duplicate list on p123; original p122 also contains the list inside raster evidence. Historical missing-list rationale superseded.' if s['id']=='page122.block03' else None),
    'automatic_pdf_replacement_authorized':False,
    'raster_text_requires_explicit_asset_or_page_family':bbox is None})
 # Candidate source IDs are immutable; folio hints must never replace them.
 packet={'schema':'rse-detective-editorial-consumer-v1','source_pdf_sha256':SOURCE,
  'source_intake_sha256':INTAKE,'candidate_sha256':CANDIDATE,
  'mode':'upgrade','language':'en','status':'REVIEWED_EDITORIAL__INTEGRATION_PENDING',
  'release_authority':False,'source_folios':225,'total_units':3067,
  'changed_units':91,'changed_source_pages':44,'protected_units':2367,
  'reader_order':{'path':'../candidate/reader-order.json','sha256':sha(root/'candidate/reader-order.json')},
  'post_migration_rule_authority':'Studio spread_layout.py OPENING_BINDINGS/SPECIAL_BINDINGS; hints only until writer verifies consumed code/input revision',
  'units':[{'id':s['id'],'source_folio':s['page'],'protected':s['protected'],
            'source_text_sha256':th(s['text']),'target_text_sha256':th(target[s['id']])} for s in intake],
  'operations':operations,
  'source_conflict':{'id':'CASE03_CAPTION','source_folios':[24,25],
    'status':'OWNER_GATE','text':'ARCHIVED FILE 017 / LATER FILE 071 vs 071 older archive material. Preserve original captions until source/art decision; do not invent chronology.'},
  'requirements':['Emit per-source-ID actual target text and destination slot/folio receipt.',
   'Preserve protected units, clue tokens, figures, 107 solution placements and four plain-zero records.',
   'Never treat the editorial 225-folio text proof as illustrated surface-fit evidence.',
   'Render/review changed illustrated leaves and preserve every other leaf from the chosen exact product base.',
   'Source-render hashes are fingerprint inventory, not semantic review or proof against a reflowed product.']}
 write(out/'EDITORIAL_IMPORT_PACKET.json',packet)
 inventory={'schema':'rse-source-page-art-ledger-v1','source_pdf_sha256':SOURCE,
  'pymupdf_version':fitz.VersionBind,'dpi':36,'meaning':'Read-only source fingerprint inventory; no new product PDF was rendered. Vector repr hashes are version-bound. Encoded image hashes alone do not certify placement/clipping.',
  'reproduction_warning':'MuPDF render caches can depend on prior extraction order. Reproduce hashes with this exact builder order/fresh document; never treat arbitrary cached-render differences as source drift.',
  'pages':pages,'page_count':len(pages),'image_instances':sum(p['image_instances'] for p in pages),
  'unique_image_payloads':len(set(image_cache.values())),'semantic_reviewed_all_pages':False}
 write(out/'SOURCE_PAGE_ART_LEDGER.json',inventory)
 codes={p.name:sha(p) for p in sorted((studio/'rse_factory').glob('*.py'))}
 write(out/'STUDIO_CAPABILITY_SNAPSHOT.json',{'archive_library_file_id':'libfile_60e360a316008191b9b8cf63dd92361e',
  'observed_archive_sha256':sha(studio_archive),
  'historical_checkpoint_archive_sha256':'820b4430f2ecf6c033a48d4be024df64dee03b44d205804f7daa0eee5430d54b',
  'archive_matches_historical_checkpoint':sha(studio_archive)=='820b4430f2ecf6c033a48d4be024df64dee03b44d205804f7daa0eee5430d54b','code_sha256':codes,
  'direct_candidate_json_import':False,'exact_v12_parser_sha256_required':'b39215cb5e26cfb53e624b01fe7e5913654645774fccde8c7ef46b12d5c4001e',
  'basis':'Read source of detective.parse_v12, production.production_build, native_story.render and spread_layout; no production edit or full build.',
  'limitations':['Current parser rejects any V12 byte change.', 'Per-page options control layout, not prose content.',
   'Opening uses raster bindings; source-native narrative imports exact source PDF body.',
   'Product writer must implement/consume versioned semantic-slot adapter; candidate JSON is not a valid direct V12 replacement.']})
 write(out/'INTEGRATION_CHECK.json',{'status':'PASS_SOURCE_IDENTITY_AND_PACKET__PRODUCT_LAYOUT_PENDING',
  'source_pdf_sha256':SOURCE,'candidate_sha256':CANDIDATE,'pages_fingerprinted':len(pages),
  'units':len(intake),'operations':len(operations),'changed_pages':len({s['source_folio'] for s in operations}),
  'protected_unit_drift':0,'raster_changed_units':sum(s['source_bbox_pt'] is None for s in operations),
  'source_pdf_unchanged':sha(pdf)==SOURCE,'candidate_unchanged':sha(root/'candidate/candidate.json')==CANDIDATE,
  'new_production_pdf':False,'print_approval':False})
 print(json.dumps({'pages':len(pages),'operations':len(operations),'image_instances':inventory['image_instances'],'candidate':'KEEP'}))
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--root',type=Path,required=True);a.add_argument('--pdf',type=Path,required=True);a.add_argument('--studio',type=Path,required=True);a.add_argument('--studio-archive',type=Path,required=True);v=a.parse_args();run(v.root,v.pdf,v.studio,v.studio_archive)
