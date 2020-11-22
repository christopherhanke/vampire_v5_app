import pytest
import vampire

def test_dice_count():
    my_dice = vampire.Vampire_Dices().d10(10)
    assert len(my_dice) == 10

def test_dice_num():
    for x in range(100):
        my_dice = vampire.Vampire_Dices().d10()
        if (my_dice[0] < 0) or (my_dice[0] > 10):
            assert False
    assert True
