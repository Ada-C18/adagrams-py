import pytest

from adagrams.game import score_word

SCORE_CHART = {
    "A": 1,
    "B": 3,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 4,
    "G": 2,
    "H": 4,
    "I": 1,
    "J": 8,
    "K": 5,
    "L": 1,
    "M": 3,
    "N": 1,
    "O": 1,
    "P": 3,
    "Q": 10,
    "R": 1,
    "S": 1,
    "T": 1,
    "U": 1,
    "V": 4,
    "W": 4,
    "X": 8,
    "Y": 4,
    "Z": 10
    }

def test_score_word_accurate():

    # Arrange/Act/Assert
    assert score_word("A") == 1
    assert score_word("DOG") == 5
    assert score_word("WHIMSY") == 17

def test_score_word_accurate_ignores_case():
    # Arrange/Act/Assert
    assert score_word("a") == 1
    assert score_word("dog") == 5
    assert score_word("wHiMsY") == 17

def test_score_zero_for_empty():
    # Arrange/Act/Assert
    assert score_word("") == 0

def test_score_extra_points_for_seven_or_longer():
    # Arrange/Act/Assert
    assert score_word("XXXXXXX") == 64
    assert score_word("XXXXXXXX") == 72
    assert score_word("XXXXXXXXX") == 80
    