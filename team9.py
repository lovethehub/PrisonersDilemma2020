import random 

team_name = 'NepInc(9)'
strategy_name=  'Beginners Luck'
strategy_description = 'Revenge 1 times And Decrease Trust'
ac = 2
bc = 0
cc = 0
noturningback = False
#Strat :
#Defense : If they betray then betray back 2 times.
#Passive : Everytime betrayed then increase chance of Offense by 10%. 
#Offense : Have a 20% chance of betrayal.

def move(my_history, their_history, my_score, their_score):
  global bc, ac, cc, noturningback
  acv = random.randint(1, 10)
  if (their_history == '') :
    return 'c'
  if (noturningback == True) :
    return 'b'
  if (their_history[-1] == 'c') :
    cc += 1
    if (cc == 3) :
      noturningback = False
  if (their_history[-1] == 'b') :
    bc += 2
    ac += 1
    cc = 0
  if (bc > 0) :
    bc -= 1
    return 'b'
  if (acv <= ac) :
    return 'b'
  else:
    return 'c'
