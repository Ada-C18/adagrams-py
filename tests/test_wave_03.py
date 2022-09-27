import pytest

from adagrams.game import score_word

def test_score_word_accurate():
    #Act
    word1 = "A"
    word2 = "DOG"
    word3 = "WHIMSY"
    #Arrange
    score1 = score_word(word1)
    score2 = score_word(word2)
    score3 = score_word(word3)
    # Assert
    assert score1 == 1
    assert score2 == 5
    assert score3 == 17

def test_score_word_accurate_ignores_case():
    # Assert
    assert score_word("a") == 1
    assert score_word("dog") == 5
    assert score_word("wHiMsY") == 17

def test_score_zero_for_empty():
    # Assert
    assert score_word("") == 0

def test_score_extra_points_for_seven_or_longer():
    # Assert
    assert score_word("XXXXXXX") == 64
    assert score_word("XXXXXXXX") == 72
    assert score_word("XXXXXXXXX") == 80
    