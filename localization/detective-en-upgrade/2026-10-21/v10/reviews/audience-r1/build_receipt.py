import json
from pathlib import Path

r=Path('/workspace/scratch/e6eabdc4c3a0/detective-v10')
d=json.loads((r/'candidate/final-scenes.json').read_text())
sha='7b5d441751ec0be8622ca5afd76aea7203f6bc752bc27b2fdee472e31c1bcef2'
assert d['candidate_sha256']==sha
notes={
'INTRO07':('PASS','The command not to move anything becomes Luli’s excuse for leaving Mom’s lost phone lost; Dilo claims a family chore as detective work. Immediate familiar family stakes.'),
'CASEWALL12':('PASS','Dilo’s self-importance, Alio’s comparison trick, and Nini’s unknown corner give distinct desires. Bibi joins the joke; Mimi lets the reader see through the family physically occupying the wall. No lesson after punch.'),
'CASE01':('PASS','A minivan with family seats makes the absurd theory visual and gives Nini and Dilo a way to play along. Luli’s sharp transport jab does not become a pile-on.'),
'CASE02':('PASS','Alio’s suspicious tidiness becomes an everyday scissors argument; he pushes back. The blank return sheet remains recognizable. Nini’s no-pockets line follows the Cup comparison without relying on a puzzle answer.'),
'CASE03':('PASS','Sparkle gets a name and Dilo wants its easy important-looking job. Luli’s chair-at-lunchtime jab targets his comfort, not his worth. Ten differences supplies task context without teaching a method.'),
'CASE04':('PASS','Dilo gives himself the seated duty, Mimi catches him, Alio contests the senior privilege, and Mimi takes the walking job. Everyone can tease and answer; the box is clearly sealed.'),
'CASE05':('PASS','Dilo reserves the right to say he nearly solved it. Luli’s answer-space jab and locker’s unfair knowledge turn a competitive kid habit into a concrete joke. More legible than conflict of interest.'),
'THREAD34':('PASS','Luli recognizes Dilo’s inability to accept an easy answer. Nini’s thing-from-thing note is familiar to young readers. Bibi’s archive visit turns backs-of-things into a family callback.'),
'CASE06':('PASS','Nini wants to keep her dragon; Luli helps; Dilo adds a real cooking question. Grandma’s burned dinners are the surprise and she answers Nini cleanly: Those dinners happened. Adults can be silly and useful.'),
'CASE07':('PASS','Mimi is tired of cupboards; Alio insists the search did eliminate places. Nini’s huge costume makes the physical mismatch clear. Brooms get names as a cap, not a safety lecture.'),
'CASE08':('PASS','As comedy, the saved-time/locked-door exchange is clear and Alio owns a face-saving delay. Dilo wants to sit while reconsidering, a recognizable family complaint. This audience pass does not override the separate story-truth objection to asserting a locked door.'),
'CASE09':('FIX','Alio’s Mine keeps agreeing with Grandma has no established witness referent. His own memory, himself, and another family member are possible. The punchline asks the reader to reconstruct who Mine is rather than enjoy Grandma exposing the self-promised cake.'),
'CASE10':('PASS','Dilo wants the rover beside him and Luli sees the motive. He bargains rather than merely accepting a lesson. Temporary rover sitter is readable desire, not evidence of incompetence.'),
'CASE11':('PASS','The rapid phone/oat-bar/source exchange retains its strong nucleus. Dilo can cite Mom’s own standard; her eating the source delivers a concrete final turn rather than explaining the joke.'),
'CASE12':('PASS','Nini interprets the parrot’s cracker request while Dilo understands the bird but wants his serious question answered. Slow waiter gives a clear comic result; no child is lectured to listen better.'),
'CASE13':('PASS','Nini now helps Alio’s tiny camera equipment fantasy; Luli is drawn in too. This restores a playmate and a comeback instead of everyone disproving the fox. Clear to readers without solving camera case.'),
'CASE14':('PASS','The book-lunch memory is shown through checking chapters and a fictional feast. Mom sharing sandwich is care shown in the family anecdote. Luli admits fallibility and ends with a dry answer.'),
'CASE15':('PASS','Mimi wins with tags and Alio immediately returns fire about her phone. Both remain competent enough to propose solutions; cardboard does not become a lecture about technology.'),
'CASE16':('PASS','Bibi counters the hat insult with a grandmother already occupying it and successful sandwich shelter. Mimi’s own childhood memory broadens affection. The family participates in the architecture conceit.'),
'CASE17':('PASS','Backpack danger, Coming through, and a tiny sandwich make the railway helmet physical rather than bureaucratic. Alio answers back. Optional craft concern: three relatives target him here; avoid sharpening all three jabs in revision, since he needs his dignity across the book.'),
'CASE18':('PASS','Watch dignity versus owner pride is short and readable. Dilo has already corrected himself; Luli works with him rather than praising improvement. The separate introduced-watch-source truth issue remains outside this comedy pass.'),
'CASE19':('PASS','Luli admits she wanted to tease; Nini hosts the waiting ghost; Dilo withholds Wi-Fi. Luli’s thwarted-teasing line is a sibling desire rather than a lesson about speculation. Ghost requires no supernatural knowledge.'),
'CASE20':('PASS','Pear’s eyebrows and literal name make the visual game concrete. Mimi is gently impatient and lands the straight paint line. Strong alibi stops the scene where it should stop.'),
'CASE21':('PASS','Dilo’s short regret is answered by an actual job beside Luli. Bibi’s uncertain recognition stays uncertain. No joke exploits the torn paper; Dilo takes one edge and gives the reader the next. Quiet care preserved.'),
'CASE22':('PASS','Left changes as Alio walks around the table; labels do not. This is an understandable spatial joke with Alio owning the failure of his temporary system. Story guard must separately resolve whether labels are falsely offered as the puzzle solution.'),
'CASE23':('FIX','The first three lines are excellent. The last line says boasting on the walk is not to count as playing, but no rule or competing interpretation has established why it might count. That final reservation is too hard to cash out as a joke; give him an immediately clear complaint about leaving his scoreboard rival.'),
'CASE24':('PASS','Voluntarily is an affectionate sibling sting; Alio’s phone/fair-album comeback balances Mom’s photographing rare quiet. The scene shows looking before speaking without narrating his moral progress.'),
'CASE25':('PASS','Over-helped parcel, pocketed hands and impossible cookie delivery form a physical sequence. Alio has an answer to being suspected and Mimi changes the rule for food. Family warmth comes from shared cookies.'),
'THREAD120':('PASS','Dilo showing off a solved stack is earned silly pride. Bibi’s unfinished-project jab is pointed but supports the achievement, and Mom’s trapped elbow gives it a physical cost. No motivational tag.'),
'CASE26':('FIX','Nobody personification works in Dilo and Luli’s lines. Mimi’s Nobody didn’t get a word in then, either combines that personification with an ordinary double negative; it takes a second parse to see that nobody is the silent witness. Preserve the pointed footnote-at-dinner jab and Bibi enjoying it, but make the silence outcome immediately readable.'),
'CASE27':('PASS','Bibi sets one care boundary, invites Alio to show his observation, and defends him against Dilo while still protecting the map. Alio’s excitement has a real place. Her warmth appears as trust and comic spatial preference, not praise.'),
'CASE28':('PASS','Evidence question, decorative confidence, and adults asking for their own cards make a clear escalation. Abstract phrase has a visible theory card and heading for support. Adults are implicated without a long confession.'),
'CASE29':('PASS','Team makes room and holds the curling map; Nini’s patience has a concrete job. Dilo offers quiet and Luli postpones teasing. Bibi leaves space for thought. Shared patience survives, with no demand for speed or extra reassurance sermon.'),
'CASE30':('FIX','Luli explicitly puts Dilo’s victory noise in his head. Nini’s Mine’s in there too points into that same head, so crowded appears to mean noises sharing Dilo’s head. Give Nini her own head or a different unambiguous shared space; retain the held-breath family anticipation.'),
}
scenes=[]
for s in d['scenes']:
    status,reason=notes[s['id']]
    scenes.append({'id':s['id'],'status':status,'finding':reason,'turn_count':len(s['turns'])})
assert len(scenes)==34 and sum(x['turn_count'] for x in scenes)==183
out=r/'reviews/audience-r1'
receipt={'candidate_sha256':sha,'candidate_file':'candidate/final-scenes.json','reviewer_role':'Audience/family-ear editorial reviewer, ages 8–12','scope':'All 34 actual R1 scenes / all 183 turns, read with CASE_CONTEXT_PACKET.md, VERSION_REFERENCE.md, source-scenes.json and baseline character/story context. No candidate edits.','overall_status':'FIX','required_fix_ids':[s['id'] for s in scenes if s['status']=='FIX'],'limits':'Editorial inference, not testing with children or psychological evaluation. PASS evaluates comprehension, humor and family voice; it does not overrule story/fact/solver guards. PDF readability sample pending.','scenes':scenes}
(out/'audience.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
lines=['# R1 audience / family-ear review','',f'Exact candidate: `{sha}`. All 34 scenes / 183 turns read in actual case context. **Overall: FIX.**','', 'The family is now substantially more readable and more fun to spend time with. Most replies have clear personal wants, the adults can lose an argument, Nini can play along, and Alio receives an ally instead of repeated correction. The quiet care of 21 and shared patience of 29 remain intact. This is an editorial assessment for ages 8–12, not a child test.','', 'Required fixes are bounded to unclear comic references/endings in 09, 23, 26 and 30. They do not require a new direction or a rewrite of the surrounding scenes. Separate story-truth checks on 08, 18 and 22 still apply.','']
for s in scenes:lines.extend([f"## {s['id']} — {s['status']}",'',s['finding'],''])
(out/'FINDINGS.md').write_text('\n'.join(lines))
print('R1 receipt complete:',receipt['required_fix_ids'])
