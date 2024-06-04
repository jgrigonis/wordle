import pytest

from wordle import Letter
from wordle import Wordle
from wordle import Word


def test_set_answer():
    mywordle = Wordle()
    mywordle.set_answer("testy")
    assert mywordle.answer == "testy"


def test_first_pass():
    mywordle = Wordle("sweet")
    output, remainder = mywordle.first_pass("tweet")
    assert remainder == ["s"]
    assert output == ["", Letter("w"), Letter("e"), Letter("e"), Letter("t")]


def test_first_pass_2():
    mywordle = Wordle("eweet")
    output, remainder = mywordle.first_pass("tweet")
    assert remainder == ["e"]
    assert output == ["", Letter("w"), Letter("e"), Letter("e"), Letter("t")]


def test_first_pass_3():
    mywordle = Wordle("sweat")
    output, remainder = mywordle.first_pass("tweet")
    assert remainder == ["s", "a"]
    assert output == ["", Letter("w"), Letter("e"), "", Letter("t")]


def test_first_pass_miss():
    mywordle = Wordle("sweat")
    output, remainder = mywordle.first_pass("mound")
    assert remainder == ["s", "w", "e", "a", "t"]
    assert output == ["", "", "", "", ""]


def test_output_letter_list():
    mywordle = Wordle()
    mylist = mywordle.output_letter_list(Word(a_string="pound"))
    assert mylist == ["p", "o", "u", "n", "d"]


def test_second_pass():
    mywordle = Wordle("trees")
    output, remainder = mywordle.first_pass("sweet")
    assert remainder == ["t", "r", "s"]
    assert output == ["", "", "e", "e", ""]
    output = mywordle.second_pass("sweet", output, remainder)
    assert output == [
        Letter("s", "YELLOW"),
        Letter("w", "RED"),
        Letter("e", "GREEN"),
        Letter("e", "GREEN"),
        Letter("t", "YELLOW"),
    ]
