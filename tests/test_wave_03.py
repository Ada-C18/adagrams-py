import pytest

from adagrams.game import score_word

def test_score_word_accurate():
    # Arrange
    #create a variable that represents a word
    word_test = "word"
    
    # Act   
    word_score = score_word(word_test)

    # Assert
    assert score_word("A") == 1
    assert score_word("DOG") == 5
    assert score_word("WHIMSY") == 17
    assert word_score == 8

def test_score_word_accurate_ignores_case():
    # Arrange
    word = "AqUaphoBia"
    
    # Act
    word_score = score_word(word)
    
    # Assert
    assert score_word("a") == 1
    assert score_word("dog") == 5
    assert score_word("wHiMsY") == 17
    assert word_score == 34

def test_score_zero_for_empty():
    # Arrange
    word = ""
    
    word_score = score_word("")
    
    # Assert
    assert score_word("") == 0
    assert word_score == 0

def test_score_extra_points_for_seven_or_longer():
    # Arrange
    word = "DICTIONARY"
    
    # Act
    word_score = score_word("DICTIONARY")
    
    # Assert
    assert score_word("XXXXXXX") == 64
    assert score_word("XXXXXXXX") == 72
    assert score_word("XXXXXXXXX") == 80
    assert word_score == 24
    