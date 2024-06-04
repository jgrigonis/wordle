import pytest

from game import Game
from wordle import Wordle


@pytest.fixture
def mygame():
    mygame = Game()
    return mygame


def test_unused(mygame):
    assert (
        mygame.show_unused()
        == "Unused letters:\na b c d e f g h i j k l m n o p q r s t u v w x y z \n"
    )
