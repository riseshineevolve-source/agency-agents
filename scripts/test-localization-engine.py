#!/usr/bin/env python3
"""Adversarial infrastructure tests. Synthetic strings are not product copy."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from localization.contracts import extract, segment_policy_hash, source_contract_hash
from localization.fixtures import detective, web, gentle, app, approved
from localization.detective import prepare, freeze_gate
from localization.fit import fit_request, check_evidence
from localization.gates import qa, load_terms, language_issues, placeholders, aggregate_reports
from localization.io import ContractError, load, dump, dump_payload, digest, get, file_digest
from localization.packaging import package, build_memory, reuse_memory

ROOT = Path(__file__).resolve().parents[1]
TERMS = load(ROOT / 'localization/pl-PL/engine/terminology.json')
FIT = load(ROOT / 'localization/pl-PL/engine/gentle-steps-fit.json')


def sample(source='Open {name} at B2.', target='Otwórz {name} w B2.', **policy):
    spec = dict(id='TEST.001', source_path='/copy', content_type='ui', surface_type='button', logic_sensitive=False, character_sensitive=False, semantic_risk=True, fit_budget={'max_chars':100, 'requires_real_surface':False})
    spec.update(policy)
    m,t = extract({'copy':source,'key':'protected.id','answer':'B2'}, {'version':1,'product':'synthetic-test-only','adapter':'app','segments':[spec], 'protected_paths':['/key','/answer']}, 'synthetic.json', 'revision-1')
    t['segments'][0]['target_text'] = target
    t['segments'][0]['review_status'] = 'draft'
    return m,t


class Gates(unittest.TestCase):
    def assertFails(self, m, t, category):
        report = qa(m,t,TERMS)
        self.assertTrue(any(i['category'] == category and i['severity'] == 'error' for i in report['issues']), report)

    def test_authorized_bilingual_fixtures(self):
        for m,t in [detective(),web(),app(),*gentle()]:
            with self.subTest(product=m['product']):
                self.assertEqual(qa(m,t,TERMS)['counts']['errors'],0)

    def test_changed_number(self):
        m,t=sample('Take 3 cards.','Weź 4 karty.')
        self.assertFails(m,t,'number_coordinate_logic_failures')

    def test_changed_coordinate(self):
        m,t=sample(target='Otwórz {name} w B3.')
        self.assertFails(m,t,'number_coordinate_logic_failures')

    def test_placeholder_name_and_multiplicity(self):
        for target in ['Otwórz {other} w B2.','Otwórz {name} {name} w B2.','Otwórz w B2.']:
            m,t=sample(target=target)
            self.assertFails(m,t,'placeholder_parity')

    def test_interpolation_styles_and_malformed_tokens(self):
        for token in ['{name}', '{{name}}', '${name}', '%s', '%1$s', '%(name)s', '{0}', '{value:.2f}']:
            with self.subTest(token=token):
                m,t=sample('Open '+token,'Otwórz '+token)
                self.assertEqual(qa(m,t,TERMS)['categories']['placeholder_parity'],0)
        for token in ['{name', '{{name}', '${name', '%q', '{count, plural, one {item} other {items}}']:
            m,t=sample('Open {name}','Otwórz '+token)
            self.assertFails(m,t,'placeholder_parity')

    def test_missing_extra_duplicate_keys(self):
        m,t=sample()
        for mutation in [[],t['segments']+[dict(t['segments'][0])],[dict(t['segments'][0],id='TRANSLATED_KEY')]]:
            changed=copy.deepcopy(t);changed['segments']=mutation
            self.assertFails(m,changed,'source_coverage')
        changed=copy.deepcopy(t);changed['segments']*=2
        self.assertEqual(qa(m,changed,TERMS)['counts']['deterministic_pass'],0)

    def test_forged_metadata(self):
        m,t=sample();t['segments'][0]['source_path']='/answer'
        self.assertFails(m,t,'protected_token_failures')

    def test_source_tamper(self):
        m,t=sample();m['segments'][0]['source_text']='Different source'
        with self.assertRaises(ContractError):qa(m,t,TERMS)

    def test_stale_target_hash(self):
        m,t=sample();t['segments'][0]['source_sha256']='old'
        self.assertFails(m,t,'stale_translations')

    def test_dropped_negation(self):
        m,t=detective();t['segments'][16]['target_text']='Echo było w Warsztacie.'
        self.assertFails(m,t,'number_coordinate_logic_failures')

    def test_changed_row_column_count_direction_adjacency(self):
        for index,text in [(14,'Nova była w trzecim rzędzie, w kolumnie B.'),(14,'Nova była w drugim rzędzie, w kolumnie C.'),(15,'Clover była w rogu mapy daleko od lodówki.'),(17,'Blaze znajdowała się na północ i na wschód od Novy.'),(18,'W pomieszczeniu Sage znajdowały się dokładnie dwie osoby.')]:
            m,t=detective();t['segments'][index]['target_text']=text
            self.assertFails(m,t,'number_coordinate_logic_failures')

    def test_identity_substitution(self):
        m,t=detective();t['segments'][14]['target_text']='Echo była w drugim rzędzie, w kolumnie B.'
        self.assertFails(m,t,'protected_token_failures')

    def test_scoped_alias_mapping_and_unexpected_identity(self):
        m,t=sample('BOBBY was in B2.','Nova była w B2.',identity_mappings=[{'source':'BOBBY','target_forms':['Nova','Novy','Novę'],'case_id':'TEST_ONLY'}])
        m['product']='detective-academy';m['contract_sha256']=source_contract_hash(m);t.update(product=m['product'],contract_sha256=m['contract_sha256'])
        self.assertEqual(qa(m,t,TERMS)['counts']['errors'],0)
        t['segments'][0]['target_text']='Nova i Echo były w B2.'
        self.assertFails(m,t,'protected_token_failures')

    def test_ordering_constraints(self):
        atom={'kind':'order','value':['A','B'],'source_anchor':'before B','target_anchor':'przed B'}
        m,t=sample('A before B.','A po B.',logic_sensitive=True,logic_atoms=[atom])
        self.assertFails(m,t,'number_coordinate_logic_failures')

    def test_answer_atom_mutation(self):
        m,t=detective();t['segments'][14]['logic_atoms'][0]['value']=9
        # Source and target atom lists must be independently owned.
        self.assertEqual(m['segments'][14]['logic_atoms'][0]['value'],2)
        self.assertFails(m,t,'number_coordinate_logic_failures')

    def test_code_strings(self):
        m,t=sample('Use `SAFE_42`.','Użyj `SAFE_43`.')
        self.assertFails(m,t,'protected_token_failures')

    def test_link_anchor_and_html_mutations(self):
        for target in ['<a href="/wrong#start" id="cta">Otwórz</a>','<a href="/path#start" id="wezwanie">Otwórz</a>','<a href="/path#start" id="cta">Otwórz']:
            m,t=sample('<a href="/path#start" id="cta">Open</a>',target)
            self.assertFails(m,t,'protected_token_failures')
        m,t=sample('[Open](/path#start)','[Otwórz](/path#changed)')
        self.assertFails(m,t,'protected_token_failures')

    def test_valid_visible_link_copy(self):
        m,t=sample('<a href="/path#start" id="cta">Open</a>','<a href="/path#start" id="cta">Otwórz</a>')
        self.assertEqual(qa(m,t,TERMS)['counts']['errors'],0)

    def test_untranslated_and_empty(self):
        for target in ['', 'Open {name} at B2.']:
            m,t=sample(target=target)
            self.assertFails(m,t,'untranslated_segments')

    def test_terminology_drift(self):
        m,t=detective();t['segments'][4]['target_text']='TABLICA ŚWIADKÓW'
        self.assertFails(m,t,'terminology_violations')

    def test_terms_conflicts(self):
        changed=copy.deepcopy(TERMS);changed['terms'].append(copy.deepcopy(changed['terms'][0]))
        with self.assertRaises(ContractError):load_terms(changed)
        changed=copy.deepcopy(TERMS);extra=copy.deepcopy(changed['terms'][0]);extra.update(id='new-conflict',products=['detective-academy'],targets=['INNE']);changed['terms'].append(extra)
        with self.assertRaises(ContractError):load_terms(changed)

    def test_approval_hashes(self):
        m,t=sample();approved(m['segments'][0],t['segments'][0],'synthetic QA test')
        self.assertEqual(qa(m,t,TERMS)['status'],'PASS')
        t['segments'][0]['target_text']='Sprawdź {name} w B2.'
        self.assertFails(m,t,'semantic_review_queue')

    def test_no_semantic_proof_from_regex(self):
        m,t=sample()
        report=qa(m,t,TERMS)
        self.assertEqual(report['status'],'REVIEW')
        self.assertGreater(report['categories']['semantic_review_queue'],0)

    def test_fit_overflow_preserves_copy(self):
        m,t=sample(fit_budget={'max_chars':2,'requires_real_surface':False})
        before=copy.deepcopy(t)
        self.assertGreater(qa(m,t,TERMS)['categories']['fit_risks'],0)
        self.assertEqual(t,before)

    def test_invalid_linebreak_diacritics(self):
        m,t=sample('Continue','Dalej',fit_budget={'approved_line_breaks':['Dąlej'],'requires_real_surface':False})
        self.assertFails(m,t,'fit_risks')

    def test_real_fit_never_passes_from_counts(self):
        for m,t in gentle():
            self.assertEqual(qa(m,t,TERMS)['status'],'REVIEW')

    def test_language_signals_are_warnings(self):
        fixtures=[('parent','W dzisiejszym dynamicznym świecie odkryj magię.'),('child_address','Zrobiłeś(-aś) zadanko.'),('family_activity','Celebrujcie wspólne chwile.'),('detective_clue','Połączenie rodzinne.'),('cta','Kliknij tutaj, aby zacząć.'),('short_label','Chwileczka'),('humorous_character_note','Wyjątkowa więź')]
        for kind,text in fixtures:
            issues=language_issues(text,kind,['odkryj magię'])
            self.assertTrue(issues,(kind,text))
            self.assertTrue(all(i[1]=='review' for i in issues))
        self.assertEqual(language_issues('Bez brokatu. Serio.','parent',[]),[])


class ContractsAndAdapters(unittest.TestCase):
    def test_unclassified_source_fails(self):
        with self.assertRaises(ContractError):
            extract({'copy':'Open','key':'id'}, {'version':1,'product':'test','adapter':'app','segments':[]},'source.json','r1')

    def test_unknown_surface_boolean_and_budget_fail(self):
        for policy in [{'surface_type':'mystery'}, {'logic_sensitive':'false'}, {'fit_budget':{'max_chars':-1}}, {'logic_sensitive':True}]:
            with self.assertRaises(ContractError):sample(**policy)

    def test_duplicate_json_and_yaml_keys_fail(self):
        with tempfile.TemporaryDirectory() as td:
            for suffix,content in [('.json','{"key":1,"key":2}'),('.yml','key: 1\nkey: 2\n')]:
                p=Path(td)/('source'+suffix);p.write_text(content,encoding='utf-8')
                with self.assertRaises(ContractError):load(p)

    def test_yaml_roundtrip_and_protected_ids(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'source.yml';p.write_text('copy: "Open {name} at B2."\nkey: protected.id\nanswer: B2\n',encoding='utf-8')
            m,t=sample();self.assertEqual(load(p),m['source_document'])
            result=package(m,t,TERMS)
            self.assertEqual(result['localized_payload'],dict(copy='Otwórz {name} w B2.',key='protected.id',answer='B2'))

    def test_integer_yaml_keys_survive_export(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'source.yml';p.write_text('copy: Open\nanswers:\n  2: B2\n  3: C3\n',encoding='utf-8')
            doc,key_types=load(p,with_key_types=True)
            self.assertEqual(key_types,{'/answers/2':'integer','/answers/3':'integer'})
            m,t=sample('Open','Otwórz')
            spec=copy.deepcopy(m['segments'][0]);spec={k:v for k,v in spec.items() if k not in {'source_text','source_sha256','source_file','source_revision'}}
            m,t=extract(doc,{'version':1,'product':'test','adapter':'book','segments':[spec],'protected_paths':['/answers/2','/answers/3']},str(p),'r1',key_types)
            t['segments'][0].update(target_text='Otwórz',review_status='draft')
            result=package(m,t,TERMS)
            out=Path(td)/'pl.yml';dump_payload(out,result['localized_payload'],result['source_key_types'])
            import yaml
            self.assertEqual(yaml.safe_load(out.read_text(encoding='utf-8'))['answers'],{2:'B2',3:'C3'})
            with self.assertRaises(ContractError):dump_payload(Path(td)/'pl.json',result['localized_payload'],result['source_key_types'])

    def test_integer_string_yaml_key_collision_fails(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'source.yml';p.write_text('1: a\n"1": b\n',encoding='utf-8')
            with self.assertRaises(ContractError):load(p,with_key_types=True)

    def test_current_rse_yaml_metadata_protected(self):
        doc=load(ROOT/'orchestration/content-sources/24-gentle-steps-to-christmas.yml')
        self.assertEqual(doc['source_artifacts']['print_master']['filename'],'24 Gentle Paperback ok.pdf')

    def test_pointer_escapes_and_array_identity(self):
        doc={'a/b':{'~key':['one','two']}}
        self.assertEqual(get(doc,'/a~1b/~0key/1'),'two')
        for pointer in ['/a~9b','/a~1b/~0key/-1','/a~1b/~0key/01']:
            with self.assertRaises(ContractError):get(doc,pointer)

    def test_all_adapters_keep_source_keys_and_truth(self):
        for adapter in ['book','app','web','puzzle','structured']:
            m,t=sample();m['adapter']=adapter;m['contract_sha256']=source_contract_hash(m);t['contract_sha256']=m['contract_sha256']
            result=package(m,t,TERMS)
            self.assertEqual(set(result['localized_payload']),set(m['source_document']))
            self.assertEqual(result['localized_payload']['answer'],'B2')
            self.assertEqual(result['localized_payload']['key'],'protected.id')
            self.assertEqual(result['bilingual_segments'][0]['source']['source_text'],m['segments'][0]['source_text'])

    def test_export_blocks_failure_and_unreviewed_release(self):
        m,t=sample()
        with self.assertRaises(ContractError):package(m,t,TERMS,release=True)
        t['segments'][0]['target_text']='Wrong'
        with self.assertRaises(ContractError):package(m,t,TERMS)

    def test_deterministic_export(self):
        m,t=web()
        self.assertEqual(digest(package(m,t,TERMS)),digest(package(m,t,TERMS)))

    def test_aggregate_uses_same_qa_format(self):
        m,t=web();report=qa(m,t,TERMS)
        suite=aggregate_reports([report,report])
        self.assertEqual(suite['format'],report['format'])
        self.assertEqual(suite['counts']['source_segments'],8)
        self.assertEqual(suite['counts']['errors'],0)
        self.assertEqual(suite['status'],'REVIEW')

    def test_cli_extract_export_and_live_source_drift(self):
        with tempfile.TemporaryDirectory() as td:
            td=Path(td);source=td/'source.json';plan=td/'plan.json';out=td/'candidate'
            dump(source,{'copy':'Open {name} at B2.','key':'fixed.id'})
            spec={'id':'TEST.001','source_path':'/copy','content_type':'ui','surface_type':'button','logic_sensitive':False,'character_sensitive':False}
            dump(plan,{'version':1,'product':'synthetic-test-only','adapter':'app','segments':[spec],'protected_paths':['/key']})
            def cli(*args):
                return subprocess.run([sys.executable,str(ROOT/'scripts/localization-engine.py'),*map(str,args)],capture_output=True,text=True)
            result=cli('extract','--source',source,'--plan',plan,'--revision','test','--output',out)
            self.assertEqual(result.returncode,0,result.stderr)
            targets=load(out/'targets.pl-PL.json');targets['segments'][0].update(target_text='Otwórz {name} w B2.',review_status='draft');dump(out/'targets.pl-PL.json',targets)
            common=['--manifest',out/'source-manifest.json','--targets',out/'targets.pl-PL.json','--current-source',source]
            result=cli('export',*common,'--output',out/'package.json','--payload-output',out/'pl.json')
            self.assertEqual(result.returncode,0,result.stderr)
            self.assertEqual(load(out/'pl.json')['key'],'fixed.id')
            result=cli('export',*common,'--output',out/'package.json','--payload-output',source)
            self.assertEqual(result.returncode,1)
            dump(source,{'copy':'Changed source','key':'fixed.id'})
            result=cli('qa',*common,'--output',out/'qa.json')
            self.assertEqual(result.returncode,1)
            self.assertIn('Current source changed',result.stderr)


class Memory(unittest.TestCase):
    def setup_memory(self):
        m,t=sample();approved(m['segments'][0],t['segments'][0],'synthetic test')
        return m,t,build_memory(m,t,TERMS)

    def test_only_approved_segments(self):
        m,t=sample()
        self.assertEqual(build_memory(m,t,TERMS)['entries'],[])

    def test_unchanged_reuse_and_provenance(self):
        m,t,memory=self.setup_memory();original=t['segments'][0]['target_text'];t['segments'][0].update(target_text='',review_status='untranslated');t['segments'][0].pop('semantic_review')
        result,events=reuse_memory(m,t,memory,TERMS)
        self.assertEqual(result['segments'][0]['target_text'],original)
        self.assertEqual(events[0]['status'],'reused')
        self.assertIn('source_revision',result['segments'][0]['reuse_provenance'])
        self.assertEqual(qa(m,result,TERMS)['status'],'PASS')

    def test_source_change_never_reuses(self):
        m,t,memory=self.setup_memory();m2,t2=sample('Open {name} at B3.','')
        result,events=reuse_memory(m2,t2,memory,TERMS)
        self.assertEqual(result['segments'][0]['target_text'],'')
        self.assertEqual(events[0]['status'],'stale_memory')

    def test_existing_stale_target_invalidated(self):
        m,t,memory=self.setup_memory();m2,t2=sample('Open {name} at B3.','Otwórz {name} w B2.')
        result,_=reuse_memory(m2,t2,memory,TERMS)
        self.assertEqual(result['segments'][0]['review_status'],'stale')

    def test_policy_or_term_changes_block_reuse(self):
        m,t,memory=self.setup_memory();m2,t2=sample(target='',fit_budget={'max_chars':20,'requires_real_surface':False})
        self.assertEqual(reuse_memory(m2,t2,memory,TERMS)[1][0]['status'],'stale_memory')
        changed=copy.deepcopy(TERMS);changed['terms'][0]['rationale']='Updated policy'
        self.assertEqual(reuse_memory(m,t,memory,changed)[1][0]['status'],'stale_memory')

    def test_tampered_or_duplicate_memory_rejected(self):
        m,t,memory=self.setup_memory();memory['entries'][0]['target']['target_text']='Tampered'
        with self.assertRaises(ContractError):reuse_memory(m,t,memory,TERMS)
        m,t,memory=self.setup_memory();memory['entries']*=2
        with self.assertRaises(ContractError):reuse_memory(m,t,memory,TERMS)

    def test_source_revision_alone_can_reuse_unchanged_text(self):
        m,t,memory=self.setup_memory();m['source_revision']='revision-2';m['segments'][0]['source_revision']='revision-2';m['contract_sha256']=source_contract_hash(m);t['contract_sha256']=m['contract_sha256'];t['segments'][0].update(target_text='',review_status='untranslated')
        result,events=reuse_memory(m,t,memory,TERMS)
        self.assertEqual(events[0]['status'],'reused')
        self.assertEqual(qa(m,result,TERMS)['counts']['errors'],0)


class RealFit(unittest.TestCase):
    def test_four_exact_pages_and_open_gate(self):
        request=fit_request(FIT)
        self.assertEqual([p['source_pdf_page'] for p in request['pages']],[25,26,35,38])
        self.assertEqual(request['status'],'BLOCKED_REAL_TEMPLATE')

    def test_proxy_and_missing_artifacts_never_pass(self):
        with tempfile.TemporaryDirectory() as td:
            result=check_evidence(FIT,{'surface_kind':'proxy','spec_sha256':digest(FIT),'pages':[]},td)
            self.assertEqual(result['status'],'BLOCK')
            self.assertTrue(any('Proxy' in i for i in result['issues']))

    def test_cli_missing_real_template_returns_block(self):
        with tempfile.TemporaryDirectory() as td:
            result=subprocess.run([sys.executable,str(ROOT/'scripts/localization-engine.py'),'fit-proof','--output',str(Path(td)/'result.json')],capture_output=True,text=True)
            self.assertEqual(result.returncode,2,result.stderr)
            self.assertEqual(load(Path(td)/'result.json')['status'],'BLOCK')

    def evidence(self,td):
        # Synthetic evidence validates the schema only, never the real product.
        base=Path(td);template=base/'template.test';template.write_bytes(b'synthetic-test-template')
        evidence={'format':'rse-real-template-fit-evidence-v1','surface_kind':'actual_template','spec_sha256':digest(FIT),'renderer':'unit-test-only','renderer_revision':'synthetic','reviewer':'unit-test-only','template':{'path':template.name,'sha256':file_digest(template)},'pages':[]}
        for spec in FIT['pages']:
            p=base/f"{spec['source_pdf_page']}.png";p.write_bytes(b'\x89PNG\r\n\x1a\n'+str(spec['source_pdf_page']).encode())
            page={'source_pdf_page':spec['source_pdf_page'],'heading':spec['approved_line_breaks'][0], 'heading_sha256':digest(spec['approved_line_breaks'][0]),'render':{'path':p.name,'sha256':file_digest(p)},'source_body_font_pt':11,'rendered_body_font_pt':11,'source_body_leading_pt':14,'rendered_body_leading_pt':14,'review':{'render_sha256':file_digest(p)}}
            page['review'].update({k:True for k in ['no_clipping','no_collisions','diacritics_correct','print_scale_reviewed','heading_legible','tracking_acceptable']})
            evidence['pages'].append(page)
        return evidence

    def test_evidence_schema_and_typography_mutations(self):
        with tempfile.TemporaryDirectory() as td:
            evidence=self.evidence(td)
            self.assertEqual(check_evidence(FIT,evidence,td)['status'],'PASS')
            for field,value in [('rendered_body_font_pt',9),('rendered_body_leading_pt',12),('heading','Wrong heading')]:
                changed=copy.deepcopy(evidence);changed['pages'][0][field]=value
                self.assertEqual(check_evidence(FIT,changed,td)['status'],'BLOCK')

    def test_fit_stale_hash_duplicate_page_and_review(self):
        with tempfile.TemporaryDirectory() as td:
            evidence=self.evidence(td)
            variants=[]
            changed=copy.deepcopy(evidence);changed['spec_sha256']='stale';variants.append(changed)
            changed=copy.deepcopy(evidence);changed['pages'][1]=changed['pages'][0];variants.append(changed)
            changed=copy.deepcopy(evidence);changed['pages'][0]['review']['diacritics_correct']=False;variants.append(changed)
            changed=copy.deepcopy(evidence);changed['pages'][0]['render']['path']='../outside.png';variants.append(changed)
            for variant in variants:self.assertEqual(check_evidence(FIT,variant,td)['status'],'BLOCK')


class DetectiveHandoff(unittest.TestCase):
    def source(self):
        # Schema-only synthetic master; no book prose is translated for testing.
        doc={'book':{'title':'TEST ONLY','language':'EN'},'missions':[{'number':i,'title':'TEST ONLY','type':'test','code':{'answer':['X'],'clues':['X before Y.']}} for i in range(1,31)]}
        aliases={'cases':[]}
        receipt={'owner_instruction':'FREEZE EN INTERIOR','owner_evidence':'synthetic test fixture, not a real authorization','source_revision':'test','source_sha256':'test-hash','all15_status':'PASS','all15_evidence':'synthetic schema test','aliases_frozen':True,'aliases_sha256':digest(aliases)}
        return doc,aliases,receipt

    def test_freeze_missing_or_stale_blocks(self):
        with self.assertRaises(ContractError):freeze_gate({},'anything')
        doc,aliases,receipt=self.source();receipt['source_sha256']='stale'
        with self.assertRaises(ContractError):prepare(doc,receipt,'test-hash',aliases)

    def test_preparation_keeps_ids_answers_and_empty_targets(self):
        doc,aliases,receipt=self.source();plan=prepare(doc,receipt,'test-hash',aliases)
        self.assertIn('/missions/0/code/answer/0',plan['protected_paths'])
        self.assertEqual(plan['segments'][1]['id'],'HMDA.M01.CODE.CLUES.0')
        self.assertTrue(plan['review_queue'])
        self.assertFalse(any('target_text' in s for s in plan['segments']))

    def test_unmapped_frozen_fields_fail_closed(self):
        doc,aliases,receipt=self.source();doc['new_reader_copy']='TEST ONLY'
        with self.assertRaises(ContractError):prepare(doc,receipt,'test-hash',aliases)


if __name__ == '__main__':
    unittest.main(verbosity=2)
