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
    #Act
    word1 = "a"
    word2 = "dog"
    word3 = "wHiMsY"

    #Arrange
    score1 = score_word(word1)
    score2 = score_word(word2)
    score3 = score_word(word3)
    # Assert
    assert score1 == 1
    assert score2 == 5
    assert score3 == 17

def test_score_zero_for_empty():
    #Act/Arrange
    score = score_word("")
    # Assert
    assert score == 0

def test_score_extra_points_for_seven_or_longer():
    # Arrange/Act
    score1 = score_word("XXXXXXX") 
    score2 = score_word("XXXXXXXX") 
    score3 = score_word("XXXXXXXXX") 

    #Assert
    assert score1 == 64
    assert score2 == 72
    assert score3 == 80
    