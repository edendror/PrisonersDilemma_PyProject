
#importing the game rules defined in game_rules file
from game_rules import COOPERATE, DEFECT
#other imports
import random

#defining strategy 1's parameters - ignores the history and always returns COOPERATE
def always_cooperate(my_history, opponent_history):
    return COOPERATE

#defining strategy 2 - ignores the history and always returns DEFECT
def always_defect(my_history, opponent_history):
    return DEFECT

#defining strategy 3 - "tit-for-tat" - the most optimal according to Robert Axelrod
def tit_for_tat(my_history, opponent_history):
    # Cooperate on the first round, then copy the opponent's last move
    if len(opponent_history) == 0:
        return COOPERATE
    return opponent_history[-1]

#defining strategy 4 - ignores the history and always returns a random response
def always_random(my_history, opponent_history):
    # ignore the history and return a random response
    return random.choice([COOPERATE, DEFECT])