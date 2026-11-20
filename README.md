# Prisoner's Dilemma Game

A Python simulation of the prisoner's dilemma. Two strategies play
a number of rounds against each other, and the total score for each is returned.

## Files

- `game_rules.py`: the moves (cooperate/defect) and the payoff table
- `strategies.py`: the strategies (always cooperate, always defect, tit-for-tat, random)
- `play_game.py`: `play_game(strategy1, strategy2, rounds, game)` plays two strategies against each other
- `run_games.py`: runs example games with a fixed random seed and records the results
- `test_game.py`: tests that check the functions work as expected

## How to use

Requires Python and no extra packages.

## Adding a strategy

A strategy is a function that takes `(my_history, opponent_history)` and
returns `COOPERATE` or `DEFECT`. Add it to `strategies.py` and pass it to `play_game`.

## Play your own game:

```python
from play_game import play_game
from strategies import tit_for_tat, always_defect

play_game(tit_for_tat, always_defect, 10)   # returns (9, 14)
```

## Results

The random seed is fixed at 42, so these results are the same on every run:

- Tit-for-tat vs always-defect, 10 rounds: (9, 14)
- Tit-for-tat vs random, 10 rounds: (28, 28)

