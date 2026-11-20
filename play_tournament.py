from game_rules import standard_game
from play_game import play_game 
from strategies import *
import random



#defining the tournament function
def play_tournament(strategies, games_per_pair, rounds_per_game, game=standard_game):
    # Start every strategy at 0 points
    total_scores = {}
    for strategy in strategies:
        total_scores[strategy.__name__] = 0

    # Go through every pair of strategies
    for i in range(len(strategies)):
        for j in range(i + 1, len(strategies)):
            # Play this pair games_per_pair times
            for round_number in range(games_per_pair):
                score1, score2 = play_game(strategies[i], strategies[j], rounds_per_game, game)  # your loop and play_game call here
                total_scores[strategies[i].__name__] += score1
                total_scores[strategies[j].__name__] += score2 # add each player's score to total_scores
                
    return total_scores



random.seed(42)
all_strategies = [always_cooperate, always_defect, tit_for_tat, always_random]
print(play_tournament(all_strategies, 5, 10)) #returns: 'always_cooperate': 246, 'always_defect': 466, 'tit_for_tat': 305, 'always_random': 337