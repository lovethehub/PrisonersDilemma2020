team_name = 'Dragons Hoard'
strategy_name = 'Gotta keep that #1'
strategy_description = 'We steal when our score is lower or collude if our score is higher.'

def move(my_history, their_history, my_score, their_score):
  if len(my_history)==0:
    return 'c'
  else:
    if my_score <= their_score:
      return 'b'
    else: 
      return 'c'
