from game_rules import COOPERATE, DEFECT
from strategies import always_cooperate, always_defect, tit_for_tat, always_random
from play_game import play_game
import random


def test_always_cooperate():
    assert always_cooperate([], []) == COOPERATE


def test_always_defect():
    assert always_defect([], []) == DEFECT


def test_tit_for_tat_cooperates_first():
    #no history yet, so tit-for-tat should cooperate
    assert tit_for_tat([], []) == COOPERATE


def test_tit_for_tat_copies_opponent():
    #opponent's last move was defect, so tit-for-tat defects
    assert tit_for_tat([COOPERATE], [DEFECT]) == DEFECT


def test_always_random_returns_valid_move():
    assert always_random([], []) in [COOPERATE, DEFECT]


def test_tit_for_tat_vs_always_defect():
    assert play_game(tit_for_tat, always_defect, 3) == (2, 7)


def test_two_tit_for_tats_cooperate_forever():
    assert play_game(tit_for_tat, tit_for_tat, 10) == (30, 30)


def test_two_always_defects():
    assert play_game(always_defect, always_defect, 10) == (10, 10)


def test_random_game_is_reproducible_with_seed():
    #same seed twice should give the same result
    random.seed(42)
    first_result = play_game(tit_for_tat, always_random, 10)
    random.seed(42)
    second_result = play_game(tit_for_tat, always_random, 10)
    assert first_result == second_result


#run every test; if one fails, Python stops and shows which one
test_always_cooperate()
test_always_defect()
test_tit_for_tat_cooperates_first()
test_tit_for_tat_copies_opponent()
test_always_random_returns_valid_move()
test_tit_for_tat_vs_always_defect()
test_two_tit_for_tats_cooperate_forever()
test_two_always_defects()
test_random_game_is_reproducible_with_seed()
print("All tests passed")