import random
from play_game import play_game
from strategies import always_cooperate, always_defect, tit_for_tat, always_random

#run seed so results are reproducible for random strategy
random.seed(42)

#game 1: tit-for-tat vs always-defect, 10 rounds
game1_scores = play_game(tit_for_tat, always_defect, 10)
print("Game 1:", game1_scores)
# Result: (9, 14)


#game 2: tit-for-tat vs random, 10 rounds
game2_scores = play_game(tit_for_tat, always_random, 10)
print("Game 2:", game2_scores)
# Result (seed 42): (28, 28)