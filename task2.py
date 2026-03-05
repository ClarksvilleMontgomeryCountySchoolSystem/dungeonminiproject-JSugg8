has_key= True
good=r'''  ___________ @ @
          /         (@\   @
          \___________/  _@
                    @  _/@ \_____
                     @/ \__/-="="`
                      \_ /
                       <|
                       <|
              jgs      <|'''
bad=r""" ,,,,,,,,,,,,,,,,,,,,
&&&&&&&&&&&&&&&&&&&&/
&&&&&&&M|" "|M&&&&&&/
&&&&&&M|     |M&&&&&/ '94-the wolfe
&&&&&&&M|   |M&&&&&&/
&&&&&&&&M| |M&&&&&&&/
&&&&&&&&M\_/M&&&&&&&/
&&&&&&&&&&&&&&&&&&&&/"""
if has_key:
    outcome="Click: You can unlock the door"
    print(good)
else:
    outcome = "Doom: You are locked out"
    print(bad)
print(outcome)