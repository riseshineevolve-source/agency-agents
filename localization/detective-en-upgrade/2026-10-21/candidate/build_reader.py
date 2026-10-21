import json,re,hashlib
from pathlib import Path
R=Path('detective-upgrade');C=R/'candidate';x=json.loads((C/'candidate-segments.json').read_text());ss=x['segments']; pageinfo={p['page']:p for p in json.loads((R/'qa/source-page-map.json').read_text())['pages']}
# Source layout stores dialogue labels and speeches in separate columns on these pages.
# This is a reading order map, not a change to any source/candidate wording.
orders={
141:[('BIBI','When I was your age, my squad started here with zero assumptions. We left route notes so unfinished training could be continued by the next session.'),('LULI','And the route stayed unfinished.'),('MIMI','Until the current roster showed five active field detectives and one empty sixth position.'),('', 'The routing log scrolls.\nROUTE FUNCTION: MATCH / ROUTE / VERIFY\nCASE CREATION: NONE\nFIELD POSITION 06: UNASSIGNED'),('ALIO','So the system did not put the Cup back?'),('EVERYONE','No.'),('DILO','Good. That would have raised several technical questions.'),('BIBI','The cases were real. The old route could flag a current record that matched one of its unfinished training steps, then reopen archived material when a verified step unlocked it.'),('NINI','The 071 photograph.'),('BIBI','Exactly. And later, the old note and the plan. Real archive pieces, reopened at the moment the route needed them.')],
142:[('LULI','It could mark, match and route evidence.'),('MIMI','It could not create a case, choose a suspect or solve anything for us.'),('','Nini looks at the four answers you just entered.'),('NINI','Which is why every field came from work you already did.'),('DILO','The code.'),('LULI','The rule word.'),('ALIO','D3.'),('MIMI','And your call sign.'),('','The screen changes.\nTRAINING ROUTE: COMPLETE\nFIELD POSITION 06: READY FOR CERTIFICATION\nBibi looks at the Recruit Credential you chose to sign at the beginning.'),('BIBI','The system could send an invitation to whoever held the book.'),('NINI','It could not choose your name.')],
143:[('LULI','Or make your verdicts.'),('MIMI','Or keep going for you.'),('','Dilo finally lowers his voice.'),('DILO','So the empty place was real.'),('BIBI','Yes.'),('MIMI','But nobody could fill it for you.'),('','The Academy could open the door.\nOnly you could earn the place.\n\nTHE SIXTH HOOK\nMimi sets the portable certification rack on the table.\nThe same rack you saw beside the Case Table when you claimed your Recruit Credential.\nFive badges already hang in their places.\nHook 06 is still empty.\nNini looks at your Recruit Credential.\nLuli looks at the completed maps.\nDilo looks at the final panel and very deliberately keeps both hands in his pockets.\nAlio has brought the helmet. Nobody asks why.\nBibi turns the empty hook toward you.')],
145:[('','DETECTIVE ACADEMY // FIELD CERTIFICATION\nAWARDED TO:\nOFFICIAL CALL SIGN:\nFOR SOLVING THE MYSTERY OF ROOM ZERO\nBY FOLLOWING THE EVIDENCE ALL THE WAY TO THE TRUTH.\nCERTIFIED FIELD DETECTIVE // FIELD SLOT 06\nROOM ZERO // CASE CLOSED\nSigned: Happy Makers Detective Academy\nArchive confirmation: BIBI // ARCHIVE MENTOR\n\nUse the same call sign from your Recruit Credential. This certificate records what you earned; it is not another recruit card.\n\nMimi clips the badge to the rack.\nFive occupied hooks become six.'),('MIMI','Welcome to the team.'),('LULI','They were already on the team.'),('MIMI','I know. Now the paperwork agrees.'),('DILO','I have never respected paperwork more.'),('BIBI','Enjoy the feeling. It will pass.'),('','No fanfare is required.\nDilo tries a tiny victory noise. Nini adds an even tinier one.\nMimi is smiling too much to overrule either of them.')],
146:[('','For one whole minute, the Academy manages to be quiet.\nAlmost.\nThe team puts down its pencils. Bibi closes the Book 1 routing log and slides it into the archive tray.\nBeside it is a small release flap.\nBibi points at it.\n“That can wait.”\nDilo waits.\nTechnically.\nThen he lifts the flap.\nA dormant slot clicks.\nA new file slides onto the tray.\nThis one does not carry the plain 0.\nOn the cover is a triangular archive symbol.\nLuli freezes.\n"Wait."\nShe flips back to the Look-Twice file from Case 03. The 017 / 071 mismatch sent them to older archive files. The symbol on this new cover gives them another question to record.'),('NINI','One changed number sent us to the archive.'),('LULI','And the archive still has more to tell us.'),('DILO','Case Three has returned from the dead.'),('MIMI','Case Three is solved. This is a new question.')],
147:[('BIBI','Which means we keep the archive trail open.'),('','Inside is an old team photograph.\nOne person has been cut out.\nOn the back, in faded type:\nRETURN BEFORE THE FIRST MEETING.'),('BIBI','I recognize that file. I do not know why it has come back.'),('DILO','That was less than one quiet minute.'),('LULI','An impressively accurate measurement.'),('ALIO','I have not even reassigned the helmet yet.'),('MIMI','Detective, are you still with us?'),('','NEXT FILE INCOMING.')]
}
(C/'reader-order.json').write_text(json.dumps({'candidate_sha256':hashlib.sha256((C/'candidate.json').read_bytes()).hexdigest(),'purpose':'Read-order/attribution only; exact wording is canonical candidate.json. Finale attribution follows independent logic review verified layout mapping.','pages':orders},ensure_ascii=False,indent=2)+'\n')
out=['# Detective Academy\n\nThe Mystery of Room Zero\n\n']
for p in range(1,226):
 out.append(f'\n\n## Page {p}\n\n')
 ps=[s for s in ss if s['page']==p]
 if pageinfo[p]['role']=='puzzle_or_evidence' or any('SOLUTION MAP' in z['target_text'] or 'SOLUTION PHOTO' in z['target_text'] for z in ps):
  out.append(f"Use the original puzzle or evidence artwork on [page {p}](sandbox:/workspace/scratch/e6eabdc4c3a0/upload/DETECTIVE_ACADEMY_EN_20261021_225P.pdf).\n\n")
  continue
 if p in orders:
  for name,t in orders[p]:out.append((f'**{name}:** ' if name else '')+t+'\n\n')
  continue
 groups=[];i=0
 while i<len(ps):
  s=ps[i]
  if s.get('extraction_method')=='ocr_unverified':
   groups.append('*Evidence artwork appears on this page in the book.*');i+=1;continue
  if s['editable'] and p>=19:
   j=i
   while j<len(ps) and ps[j]['editable']:j+=1
   text=''.join(z['target_text'] for z in ps[i:j]);groups.append(text);i=j
  else:groups.append(s['target_text']);i+=1
 # Avoid design-only headers, counters and repeated furniture labels interrupting reader prose.
 for g in groups:
  if re.fullmatch(r'\s*\d{1,3}\s*',g):continue
  if g.strip() in ['HAPPY MAKERS / DETECTIVE ACADEMY','ACADEMY RECORD / STORY CONTINUES','DETECTIVE NOTES','DETECTIVE WORKSPACE']:continue
  g=g.strip()
  m=re.fullmatch(r'(?:\d+\s+)?(MIMI|LULI|DILO|NINI|ALIO|BIBI)\s*(?:\d+)?',g)
  if m:g='**'+m.group(1)+':**'
  g=re.sub(r'\n(?=(?:MIMI|LULI|DILO|NINI|ALIO|BIBI):)', '\n\n',g)
  out.append(g+'\n\n')
(C/'reader-manuscript.md').write_text(''.join(out))
print('Reader pages',len(re.findall(r'^## Page ',''.join(out),re.M)))
