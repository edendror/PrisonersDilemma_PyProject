from game_rules import standard_game

#defining the main game function
def play_game(strategy1, strategy2, rounds, game=standard_game):
    #each player's list of past moves, starting empty
    player1_history = []
    player2_history = []

    #running totals, starting at zero
    player1_score = 0
    player2_score = 0

    for round_number in range(rounds):
        #each strategy sees its own history first, the opponent's second
        move1 = strategy1(player1_history, player2_history)
        move2 = strategy2(player2_history, player1_history)

        #look up the payoffs for this combination of moves
        score1, score2 = game[move1][move2] #the only change in this function - fetching from matrix instead of dict

        #add this round's payoffs to the totals
        player1_score += score1
        player2_score += score2

        # Record the moves so strategies can see them next round
        player1_history.append(move1)
        player2_history.append(move2)

    return player1_score, player2_score