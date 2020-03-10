from __future__ import print_function
import time



team_name = 'Team 3'
strategy_name= 'Yes'
strategy_description = 'if count of b is greater or equal to the count of c, then return b; else return c'  


def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    Make my move.
    Returns 'c' or 'b'. 
    '''
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty.
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].

    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    b_count = their_history.count('b') + 1
    c_count = their_history.count('c')
    if len(my_history) == 0:
      return 'b'
    if b_count >= c_count:
      return 'b'
    else:
      return 'c'

