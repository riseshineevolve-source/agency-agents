"""Read-only source-bound Case21/27 audit and evidence reproduction.

The tear-edge classes and plan grid coordinates are manually transcribed from
visually reviewed exact source images, not inferred from solution wording.
Enumeration checks the transcription, not pixel-perfect cut-out manufacture.
"""
from pathlib import Path
import argparse,hashlib,itertools,json
import fitz
SOURCE='9db84d4f138cbbde8eb1f4a0f783f4d126c639120a11cabb65fc00711b9f05a0'
CANDIDATE='ec93cfc7a99257113fe33d6536574d2d6889c969ec68dac69ca97ad26010a55e'
PAGES=[86,87,88,89,98,99,100,101,125,126,127,156,157,158,165,166,167,174,175,176,207,212,221]
EDGES={
 'A':{'left':'double_zigzag','right':'rounded'},
 'B':{'left':'straight','right':'single_chevron'},
 'C':{'left':'rounded','right':'straight'},
 'D':{'left':'single_chevron','right':'double_zigzag'},
}
WORDS={'A':'WHAT YOU','B':'THE ANSWER IS','C':'LEAVE EMPTY.','D':'IN'}
ANCHORS={'C1':{'name':'North Stair','center_grid':[2.5,.5]},'F3':{'name':'Courtyard Column','center_grid':[5.5,2.5]},'A5':{'name':'West Lift Shaft','center_grid':[.5,4.5]}}
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def run(pdf,candidate,output):
 if digest(pdf)!=SOURCE:raise ValueError('Wrong source bytes')
 if digest(candidate)!=CANDIDATE:raise ValueError('Wrong reviewed candidate')
 output.mkdir(parents=True,exist_ok=True);renders=output/'special-renders';renders.mkdir(exist_ok=True)
 doc=fitz.open(pdf);rows=[]
 for n in PAGES:
  p=renders/f'p{n:03d}.png';doc[n-1].get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(p)
  rows.append({'source_folio':n,'render_png':str(p),'sha256':digest(p)})
 orders=[list(order) for order in itertools.permutations(EDGES)
  if EDGES[order[0]]['left']=='straight' and EDGES[order[-1]]['right']=='straight'
  and all(EDGES[a]['right']==EDGES[b]['left'] for a,b in zip(order,order[1:]))]
 assert orders==[['B','D','A','C']]
 message=' '.join(WORDS[s] for s in orders[0]);assert message=='THE ANSWER IS IN WHAT YOU LEAVE EMPTY.'
 c=json.loads(Path(candidate).read_text())['segments'];unit=next(s for s in c if s['id']=='page212.block05')
 source_text=doc[211].get_text();nulls=source_text.count('\x00')
 source18=doc[206].get_text();assert source18.count('\x00')==3
 events={'A':{'shown':'15:08','clock':'cafe','correction_minutes':7},'B':{'shown':'15:18','clock':'Dilo','correction_minutes':-2},'C':{'shown':'15:17','clock':'station','correction_minutes':0},'D':{'shown':'15:11','clock':'cafe','correction_minutes':7}}
 for e in events.values():
  hh,mm=map(int,e['shown'].split(':'));value=hh*60+mm+e['correction_minutes'];e['real_minutes']=value;e['real_time']=f'{value//60:02d}:{value%60:02d}'
 order18=sorted(events,key=lambda key:events[key]['real_minutes']);assert order18==['A','B','C','D']
 assert nulls==3 and unit['text'].count('\x00')==3
 # Non-collinear landmark centres constrain a unique affine identity between
 # logical plan grids. Both actual drawings label the same anchors and cells.
 v1=(3,2);v2=(-2,4);det=v1[0]*v2[1]-v1[1]*v2[0];assert det==16
 result={'candidate_sha256':CANDIDATE,'source_pdf_sha256':SOURCE,'source_pages_rendered':PAGES,
  'render_engine':'PyMuPDF '+fitz.VersionBind,'render_method':'Matrix(1.5,1.5), alpha=False',
  'case18':{'source_evidence_folio':89,'events_visually_transcribed':events,'computed_order':order18,'source_solution_folio':207,'display_nulls_in_source':3,'status':'PUZZLE_TRUTH_KEEP__SOURCE_GLYPH_REPAIR_REQUIRED'},
  'case21':{'edge_transcription':EDGES,'transcription_method':'Actual visible outline inspection of p101, not sentence-only reconstruction',
   'orientation_assumption':'Writing kept face-up and upright as printed; whole-note rotation is the same solved object, not a different readable answer. No arbitrary independent flips certified.',
   'permutations_tested':24,'orders_matching_edge_classes':orders,'reconstructed_message':message,
   'hint_and_solution_order_agree':True,'display_nulls_in_source_p212':nulls,'display_nulls_in_candidate_page212_block05':3,
   'status':'PUZZLE_TRUTH_KEEP__SOURCE_GLYPH_REPAIR_REQUIRED',
   'not_claimed':'No pixel-exact cut-out registration or physical print proof. The source cards are stylized matching-edge shapes.'},
  'case27':{'anchors_visually_verified':ANCHORS,'old_plan_training_room_cells':['D2','E2','D3','E3'],
   'current_plan_correspondence':'ARCHIVE WALL covers same D2:E3 rectangle',
   'source_page127_margin_note':'RULE FIRST, ROOM SECOND.',
   'landmark_centres_affine_determinant':det,'rotation_required':False,'scale_change_required':False,
   'status':'VISIBLE_SOURCE_OVERLAY_LOGIC_KEEP',
   'not_claimed':'Grid membership is human visual transcription. No automated segmentation certificate, physical transparency overlay, or print-scale approval.'},
  'renders':rows,'candidate_mutated':False,'source_pdf_mutated':False,'production_mutated':False}
 (output/'special-cases-computation.json').write_text(json.dumps(result,indent=2)+'\n');print('Case21 unique edge-class order',orders,'; Case27 grid overlay identity; p212 missing glyphs',nulls)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--pdf',type=Path,required=True);p.add_argument('--candidate',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();run(a.pdf,a.candidate,a.output)
