"""Post-freeze preparation for the existing Book Factory YAML schema.

This produces untranslated source plans, never translations or semantic atoms.
Unknown fields stop preparation, so source additions cannot disappear silently.
"""
from __future__ import annotations

import re
from .contracts import require
from .io import leaves, get, digest

VISIBLE = [
    r'/book/(title|subtitle|strapline|opening_code|rule_zero|edition)',
    r'/characters/[^/]+/(name|tag)',
    r'/opening/(acceptance_letter/(headline|body|note)|squad_intro|how_to_play/\d+)',
    r'/missions/\d+/(rank|title|status|hook|objective|meta_reveal|nudge|hints/\d+|solution_steps/\d+|dialogue/\d+/text)',
    r'/missions/\d+/(spatial_copy|spatial)/clue_cards/\d+',
    r'/missions/\d+/tutorial/(clues/\d+|guided_steps/\d+|verdict|rooms/\d+/name)',
    r'/missions/\d+/code/clues/\d+',
    r'/missions/\d+/visual/(meaningful|decoys)/\d+',
    r'/missions/\d+/checkpoint/(instruction|evidence/\d+/item)',
    r'/missions/\d+/classification/(case_window|question|reason|items/\d+/(item|label))',
    r'/missions/\d+/consistency/(reason|statements/\d+/text|timeline/\d+/event)',
    r'/missions/\d+/route/options/\d+/fails',
    r'/missions/\d+/timeline_visual/evidence/\d+',
    r'/missions/\d+/fact_theory_sort/(cards/\d+/text|rule_zero)',
    r'/missions/\d+/finale/(reader_payoff|reveal|series_hook|stages/\d+/prompt)',
    r'/missions/\d+/reconstruction/(scraps/\d+/text|answer_text)',
    r'/missions/\d+/timeline/(records/\d+/(event|source)|rules/\d+)',
    r'/missions/\d+/visual_sequence/rule',
    r'/story_spine/beats/\d+/(eyebrow|headline|question|evidence/\d+|squad/\d+/text|reader_move|progress)',
]
PROTECTED = [
    r'/book/language', r'/characters/[^/]+/asset', r'/status',
    r'/production_state/.+', r'/story_spine/(status|purpose)',
    r'/story_spine/beats/\d+/(code|squad/\d+/speaker)',
    r'/missions/\d+/(type|spatial_source_id|guides/\d+|dialogue/\d+/speaker|meta_letter)',
    r'/missions/\d+/(spatial_copy|spatial)/(answer|answer_coordinate|final_space_skin)',
    r'/missions/\d+/spatial/(puzzle_asset|solution_asset|source_page_asset|source_pdf_sha256|asset_manifest|case_id|title|status)',
    r'/missions/\d+/tutorial/(answer|cols/\d+|people/\d+|positions/[^/]+|rooms/\d+/cells/\d+)',
    r'/missions/\d+/code/(symbols/\d+|answer/\d+)',
    r'/missions/\d+/(visual|checkpoint|classification|consistency|route|visual_sequence)/answer',
    r'/missions/\d+/checkpoint/evidence/\d+/mark',
    r'/missions/\d+/classification/items/\d+/id',
    r'/missions/\d+/consistency/(map/edges/\d+/\d+|statements/\d+/speaker|timeline/\d+/time)',
    r'/missions/\d+/route/(start|goal|options/\d+/(id|path/\d+))',
    r'/missions/\d+/timeline_visual/(answer/building|candidate_buildings/\d+)',
    r'/missions/\d+/fact_theory_sort/(cards/\d+/bucket|missing_word)',
    r'/missions/\d+/finale/stages/\d+/(answer(?:/\d+)?|id|source_case)',
    r'/missions/\d+/map_overlay/(anchors/\d+/(current|old)|answer|current_covering_space|old_only_space)',
    r'/missions/\d+/reconstruction/(answer_order/\d+|joins/\d+/\d+|scraps/\d+/(id|left_edge|right_edge))',
    r'/missions/\d+/timeline/(answer_order/\d+|records/\d+/(id|real|shown))',
    r'/missions/\d+/visual_sequence/(positions/\d+|prints/\d+/(position|tread_arrow))',
]


def freeze_gate(receipt, source_sha256):
    require(receipt.get('owner_instruction') == 'FREEZE EN INTERIOR', 'Owner EN freeze has not been recorded')
    require(bool(receipt.get('owner_evidence')) and bool(receipt.get('source_revision')), 'Freeze needs owner evidence and source revision')
    require(receipt.get('source_sha256') == source_sha256, 'Frozen source bytes do not match receipt')
    require(receipt.get('all15_status') == 'PASS' and bool(receipt.get('all15_evidence')), 'ALL-15 PASS evidence is required')
    require(receipt.get('aliases_frozen') is True and bool(receipt.get('aliases_sha256')), 'Final alias map must be frozen')


def prepare(document, receipt, source_sha256, alias_document=None):
    freeze_gate(receipt, source_sha256)
    require(alias_document is not None and receipt['aliases_sha256'] == digest(alias_document), 'Alias snapshot hash mismatch')
    require([m.get('number') for m in document.get('missions',[])] == list(range(1,31)), 'Expected composed 30-mission master in canonical order')
    segments, protected, unknown, review = [], [], [], []
    alias_cases = {}
    for case in alias_document.get('cases', []):
        require(case['id'] not in alias_cases, 'Duplicate alias case ID')
        alias_cases[case['id']] = case
    for pointer, text in leaves(document):
        if not isinstance(text, str):
            continue
        visible = any(re.fullmatch(pattern,pointer) for pattern in VISIBLE)
        fixed = any(re.fullmatch(pattern,pointer) for pattern in PROTECTED)
        require(not (visible and fixed), f'Conflicting Detective source rules: {pointer}')
        if fixed:
            protected.append(pointer)
            continue
        if not visible:
            unknown.append(pointer)
            continue
        mission_match = re.match(r'/missions/(\d+)/(.*)',pointer)
        suffix = pointer.strip('/')
        mission_id = 'SYSTEM'
        mission = None
        if mission_match:
            mission = document['missions'][int(mission_match[1])]
            mission_id = f"M{mission['number']:02d}"
            suffix = mission_match[2]
        elif pointer.startswith('/story_spine/beats/'):
            index = int(pointer.split('/')[3])
            beat = document['story_spine']['beats'][index]
            mission_id = 'AFTER' + str(beat['after_case']).zfill(2)
            suffix = '/'.join(pointer.split('/')[4:])
        # Mission IDs survive re-pagination. List ordinals are source ordering,
        # frozen by the snapshot; source edits require a deliberate ID migration.
        sid = 'HMDA.' + mission_id + '.' + suffix.replace('/','.').upper()
        logic = bool(mission and not re.fullmatch(r'(rank|title|status|hook|dialogue/\d+/text)', suffix)) or pointer.startswith('/story_spine/beats/')
        surface = 'heading' if suffix.endswith(('title','headline')) else 'badge' if suffix in {'rank','status'} else 'clue_card' if 'clue' in suffix or 'hints/' in suffix else 'map_label' if '/rooms/' in pointer else 'body_block'
        mappings = []
        if mission and mission.get('spatial_source_id'):
            case = alias_cases.get(mission['spatial_source_id'])
            require(case is not None, f"Missing alias case: {mission['spatial_source_id']}")
            for person in case['characters']:
                if re.search(r'\b'+re.escape(person['source_name'])+r'\b',text,re.I):
                    mappings.append({'source':person['source_name'],'target_forms':[person['display_name']], 'case_id':case['id']})
        segment = {'id':sid,'source_path':pointer,'content_type':'detective_clue' if logic else 'dialogue' if 'dialogue' in suffix else 'narrative',
                   'surface_type':surface,'logic_sensitive':logic,'character_sensitive':bool(mappings) or 'dialogue' in suffix,
                   'semantic_risk':True,'logic_atoms':[],'identity_mappings':mappings,'fit_budget':None,
                   'mission_id':mission_id,'meta_sensitive':'meta' in suffix or '/story_spine/' in pointer or '/finale/' in pointer}
        segments.append(segment)
        if logic:
            review.append({'id':sid,'gate':'Annotate bilingual logic atoms from frozen truth before extraction; do not infer semantic PASS'})
    require(not unknown, 'Unmapped frozen-source fields; extend source rules explicitly: ' + ', '.join(unknown))
    require(len({s['id'] for s in segments}) == len(segments), 'Stable ID collision')
    return {'version':1,'product':'detective-academy','adapter':'puzzle','scope':'full_book','owner_freeze_evidence':receipt['owner_evidence'],
            'segments':segments,'protected_paths':protected,'excluded_paths':{},'review_queue':review,
            'freeze_receipt':receipt,'limits':'Source plan only. Empty logic atoms and real surface budgets intentionally require annotation; no target prose generated.'}
