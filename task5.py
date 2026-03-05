escaped= True
good=r'''______________
|\ ___________ /|
| |  /|,| |   | |
| | |,x,| |   | |
| | |,x,' |   | |
| | |,x   |   | |
| | |/    |   | |
| |    /] |   | |
| |   [/ ()\  | |
| |       | \,^%---
| |       | <\/ \ Hello!
| |       |<  | |
| |      ,'<  | |
| |   ,' ^^|\ | |
|_|,'_____/__\|_| ejm'''
bad=r''' ______
   ,-' ;  ! `-.
  / :  !  :  . \
 |_ ;   __:  ;  |
 )| .  :)(.  !  |
 |"    (##)  _  |
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |mt-2_;----.___|
'''
if escaped:
    outcome="Legend: Yay we excaped."
    print(good)
else:
    outcome= ("Doom: Oh no were stuck")
    print(bad)
print(outcome)