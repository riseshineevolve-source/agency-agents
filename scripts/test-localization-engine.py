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
from localization.fixtures import detective, web, gentle, approved
from localization.fit import fit_request, check_evidence
from localization.gates import qa, load_terms, language_issues, placeholders
from localization.io import ContractError, load, dump, digest, get
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
        for m,t in [detective(),web(),*gentle()]:
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
        for token in ['{name', '{{name}', '${name', '{count, plural, one {item} other {items}}']:
            m,t=sample('Open {name}','Otwórz '+token)
            self.assertFails(m,t,'placeholder_parity')

    def test_missing_extra_duplicate_keys(self):
        m,t=sample()
        for mutation in [[],t['segments']+[dict(t['segments'][0])],[dict(t['segments'][0],id='TRANSLATED_KEY')]]:
            changed=copy.deepcopy(t);changed['segments']=mutation
            self.assertFails(m,changed,'source_coverage')

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


if __name__ == '__main__':
    unittest.main(verbosity=2)
