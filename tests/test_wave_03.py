import pytest

from adagrams.game import score_word

def test_score_word_accurate():
    #Arrange
    words = ["A","DOG","WHIMSY"]
    #Act
    result1 = score_word(words[0])
    result2 = score_word(words[1])
    result3 = score_word(words[2])
    # Assert
    # assert score_word(result1) == 1
    # assert score_word(result2) == 5
    # assert score_word(result3) == 17
    assert result1 == 1
    assert result2 == 5
    assert result3 == 17

def test_score_word_accurate_ignores_case():
    #Arrange
    words = ["a","dog","wHiMsY"]
    #Act
    result1 = score_word(words[0])
    result2 = score_word(words[1])
    result3 = score_word(words[2])
    # Assert
    # assert score_word(result1) == 1
    # assert score_word(result2) == 5
    # assert score_word(result3) == 17
    assert result1 ==1
    assert result2 == 5
    assert result3 == 17

def test_score_zero_for_empty():
    #Arrange
    word = ""
    #Act
    result = score_word(word)
    # Assert
    # assert score_word(result) == 0
    assert result == 0
def test_score_extra_points_for_seven_or_longer():
    #Arrange
    words = ["XXXXXXX","XXXXXXXX","XXXXXXXXX"]
    #Act
    result1 = score_word(words[0])
    result2 = score_word(words[1])
    result3 = score_word(words[2])
    # Assert
    # assert score_word(result1) == 64
    # assert score_word(result2) == 72
    # assert score_word(result3) == 80
    assert result1 == 64
    assert result2 == 72
    assert result3 == 80
    