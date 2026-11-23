# The two moves a player can make
COOPERATE = 0
DEFECT = 1

# Payoff matrix: standard_game[player 1 move][player 2 move] = (player 1 score, player 2 score)
standard_game = [
    # Player 2: COOPERATE (0)   Player 2: DEFECT (1)
    [(3, 3), (0, 5)], # Player 1: COOPERATE (0)
    [(5, 0), (1, 1)], # Player 1: DEFECT (1)
]