"""Verify exported handoff bytes/coverage independently; no product approval."""
import argparse,hashlib,json
from pathlib import Path

def main(root):
 load=lambda p:json.loads((root/p).read_text())
 source=load('source/intake-v5.json')['segments'];target=load('candidate/candidate.json')['segments']
 packet=load('integration/EDITORIAL_IMPORT_PACKET.json');art=load('integration/SOURCE_PAGE_ART_LEDGER.json')
 s={v['id']:v for v in source};t={v['id']:v['text'] for v in target};ops=packet['operations'];h=lambda v:hashlib.sha256(v.encode()).hexdigest()
 checks={
  'source_candidate_packet_same_order':[v['id'] for v in source]==[v['id'] for v in target]==[v['id'] for v in packet['units']],
  'all_operation_bytes_match':all(v['before']==s[v['id']]['text'] and v['after']==t[v['id']] for v in ops),
  'all_operation_hashes_match':all(h(v['before'])==v['before_sha256'] and h(v['after'])==v['after_sha256'] for v in ops),
  'all_unit_hashes_match':all(v['source_text_sha256']==h(s[v['id']]['text']) and v['target_text_sha256']==h(t[v['id']]) for v in packet['units']),
  'protected_original_unchanged':all(v['text']==t[v['id']] for v in source if v['protected']),
  'exact_changed_set':{v['id'] for v in ops}=={v['id'] for v in source if v['text']!=t[v['id']]},
  'no_duplicate_operations':len(ops)==len({v['id'] for v in ops})==93,
  'all_source_folios_accounted':list(range(1,226))==[v['source_folio'] for v in art['pages']],
  'all_page_unit_sets_exact':all(v['source_segment_ids']==[x['id'] for x in source if x['page']==v['source_folio']] for v in art['pages']),
  'source16_comms_routes15':next(v for v in ops if v['id']=='page016.block04')['post_migration_destination_folio_hint']==15,
  'case04_narrative_routes26':all(v['post_migration_destination_folio_hint']==26 for v in ops if v['source_folio']==27),
  'page122_rationale_corrected':'raster evidence' in next(v for v in ops if v['id']=='page122.block03')['audit_rationale_override'],
  'no_slot_or_print_approval':not any(v['automatic_pdf_replacement_authorized'] for v in ops),
  'candidate_hash_bound':hashlib.sha256((root/'candidate/candidate.json').read_bytes()).hexdigest()==packet['candidate_sha256'],
  'intake_hash_bound':hashlib.sha256((root/'source/intake-v5.json').read_bytes()).hexdigest()==packet['source_intake_sha256']}
 result={'status':'PASS' if all(checks.values()) else 'FAIL','candidate_sha256':packet['candidate_sha256'],'source_pdf_sha256':packet['source_pdf_sha256'],'checks':checks,
  'packet_sha256':hashlib.sha256((root/'integration/EDITORIAL_IMPORT_PACKET.json').read_bytes()).hexdigest(),
  'ledger_sha256':hashlib.sha256((root/'integration/SOURCE_PAGE_ART_LEDGER.json').read_bytes()).hexdigest(),
  'meaning':'Independent byte/coverage assertions over built handoff; not product render verification.'}
 (root/'integration/PACKET_VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n')
 print(result['status'],len(checks),'checks')
 if result['status']!='PASS':raise SystemExit(1)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,required=True);main(p.parse_args().root)
