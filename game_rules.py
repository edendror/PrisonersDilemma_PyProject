# The two moves a player can make
COOPERATE = "cooperate"
DEFECT = "defect"

# Payoff table: (player 1 move, player 2 move) : (player 1 score, player 2 score)
standard_game = {
    (COOPERATE, COOPERATE): (3, 3),
    (COOPERATE, DEFECT): (0, 5),
    (DEFECT, COOPERATE): (5, 0),
    (DEFECT, DEFECT): (1, 1),
}