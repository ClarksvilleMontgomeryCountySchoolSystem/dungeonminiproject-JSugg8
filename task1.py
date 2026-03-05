torch_lit=True
good = r'''
           /|
        /\/ |/\
        \  ^   | /\  /\
  (\/\  / ^   /\/  )/^ )
   \  \/^ /\       ^  /
    )^       ^ \     (
   (   ^   ^      ^\  )
    \___\/____/______/
    [________________]
     |              |
     |     //\\     |
     |    <<()>>    |
     |     \\//     |
      \____________/
          |    |
          |    |
          |    |
          |    |
          |    |
          |    |
          |    |
Zot
'''
bad =r''' _                 _     
| |               | |    
| |_ ___  _ __ ___| |__  
| __/ _ \| '__/ __| '_ \ 
| || (_) | | | (__| | | |
 \__\___/|_|  \___|_| |_|
                         
                         

'''
if torch_lit:
    outcome = "Flicker: The torch is still lit"
    print(good)
else:
    outcome = "Doom: The torch is out"
    print(bad)
print(outcome)
