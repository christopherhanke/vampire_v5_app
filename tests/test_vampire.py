import pytest
from vampire import Vampire

@pytest.fixture
def vamp():
    vamp = Vampire.new_Vampire()
    attr = vamp.keys_attributes[1]
    vamp.set_attribute(attr, 2)
    yield vamp

@pytest.fixture
def vamp_file():
    vamp_file = Vampire.new_Vampire_from_file("file_name_here")
    yield vamp_file


def test_dice_count(vamp):
    test = vamp.d10(10)
    assert len(test) == 10

def test_dice_num(vamp):
    for x in range(100):
        my_dice = vamp.d10()
        if (my_dice[0] < 0) or (my_dice[0] > 10):
            assert False
    assert True


def test_vampire_skill_default():
    vamp = Vampire().get_skill("Firearms")
    if vamp != None:
        assert True
    else:
        assert False

def test_vampire(vamp):
    attr = vamp.get_attribute(vamp.keys_attributes[1])
    assert attr == 2

def test_vampire_file(vamp_file, capsys):
    out, err = capsys.readouterr()
    # TODO get the printout tested - out is empty now    
