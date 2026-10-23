from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent;changes=[]
def fix(f,old,new,reason):
 p=R/'candidate'/f;s=p.read_text();assert s.count(old)==1,(f,old);p.write_text(s.replace(old,new));changes.append({'file':f,'before':old,'after':new,'reason':reason})
a='01_grudzien_bez_pospiechu_PL.md';b='02_kalendarz_z_zadaniami_PL.md';c='02_advent_activities_EN.md'
fix(a,'kiedy akurat macie na to przestrzeń','kiedy macie ochotę i kilka minut','PLnative: replace coaching abstraction with ordinary decision and time')
fix(a,'Finał to próba zatrzymania się w tym samym momencie','Jednym z wyzwań jest zatrzymanie się w tym samym momencie','Sourcefinale includes acceleration/slowdown; stopping is only one challenge')
fix(a,' To pytanie do rozmowy, nie obowiązkowa runda podziękowań.','','Audience: optional wording already present; remove defensive editorial explanation')
fix(b,'Zdarzą się ruch, improwizacja i zagadkowe gesty kogoś, kto był absolutnie pewien, że świetnie pokazuje bałwana.','Zdarzą się ruch, improwizacja i gesty, przy których nawet ich autor zaczyna się zastanawiać, co właściwie pokazuje.','Keep strongest actualcharades example; avoid three snowman setups')
fix(b,'zamiast tą, która wszystko rozdaje','zamiast wszystko rozdawać','Nativecase error; recast cleanly')
fix(b,'Jedna osoba zgaduje, pozostali wybierają dla niej po cichu wspólne hasło. Potem pokazują je jednocześnie','Jedna osoba będzie zgadywać. Pozostali wybierają po cichu wspólne hasło, a potem pokazują je jednocześnie','Clarify prompt selection occurs before guessing, not simultaneously')
fix(b,'Kto pierwszy zaczął to mówić albo robić? Czasem śledztwo prowadzi do osoby, która teraz najgłośniej twierdzi, że wcale tak nie mówi.','Od kogo przejęliście te małe zwyczaje? Może ktoś dopiero teraz usłyszy, że wszyscy jego „no dobra” mówią dokładnie tym samym tonem.','Return to direct borrowed habit, not earliest origin hunt')
fix(b,'Warto zajrzeć do środka i pomyśleć o własnej rodzinie przy takiej zabawie. Kto najbardziej komplikowałby kalambury? A kto po minucie nadal tłumaczyłby, że przecież pokazywał zupełnie oczywistego bałwana?\n\n','','Remove repetitive charades cap and imaginedparticipanttarget; keep strong source-backed shared-scene joke')
fix(c,'An Activity Advent Calendar the Grown Ups Can Enjoy Too','An Activity Advent Calendar Where Parents Get to Play Too','Native noun hyphen defect; choose clear parent-facing title')
fix(c,' Nobody has to become a quieter sort of person.','','Remove awkward personality-change reassurance; action already specific')
fix(c,'One person guesses while the others quietly choose a shared prompt. Everyone else then acts it out at once','One person will be guessing. The others quietly choose a shared prompt, then act it out at once','Clarify prompt choice before guessing; same source mechanism')
fix(c,"You can trace a small family habit back to whoever started it, including the person who insists they've never said that in their life.","Which small habit have you borrowed, and from whom? You might even hear a favourite expression delivered in a very familiar tone.",'Source asks direct borrowing, not tracing earliest origin')
fix(c,"Look through the activities with your own family in mind. Who would make charades unnecessarily complicated? Who would still be defending their extremely obvious snowman after the game had finished?","Have a look through the activities and choose something you'd like to join in with. The grown-ups are allowed to be every bit as ridiculous as everyone else.",'Invite adults into shared humour rather than cast family member as target')
(R/'qa/FINAL_CHANGES.json').write_text(json.dumps({'sole_writer':'root','changes':changes,'r1_immutable':'baseline/reviewed-r1','reasons':'Actual independent reviewer findings plus bounded chronology clarification'},ensure_ascii=False,indent=2)+'\n')
print('Applied',len(changes),'bounded changes')
