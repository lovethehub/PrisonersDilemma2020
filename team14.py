
team_name = 'Dragons Hoard'
strategy_name = 'Gotta keep that #1'
strategy_description = 'We steal when our score is lower or if they have stolen in the past 5 turns.'

def move(my_history, their_history, my_score, their_score):
  if len(my_history)==0:
    return 'c'
    if my_score <= their_score:
      return 'b'
    elif len(my_history) >=1 and their_history[:-5] == 'b':
      return 'b'
    else: 
      return 'c'
