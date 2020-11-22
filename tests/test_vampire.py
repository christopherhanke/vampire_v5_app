import pytest
from vampire import Vampire, Vampire_Dices

@pytest.fixture
def vampire():
    vamp = Vampire()
    attr = vamp.keys_attributes[1]
    vamp.set_attribute(attr, 2)


@pytest.fixture
def dice():
    dice = Vampire_Dices()
    yield dice


def test_dice_count(dice):
    test = dice.d10(10)
    assert len(test) == 10


def test_dice_num():
    for x in range(100):
        my_dice = Vampire_Dices().d10()
        if (my_dice[0] < 0) or (my_dice[0] > 10):
            assert False
    assert True

def test_vampire_skill_firearm():
    vamp = Vampire().get_skill("Firearms")
    if vamp != None:
        assert True
    else:
        assert False
