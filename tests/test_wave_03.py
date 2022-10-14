import pytest

from adagrams.game import score_word

def test_score_word_accurate():
    # Arrange
    word = "A"
    word = "DOG"
    word = "WHIMSY"
    # Act
    # total_score = score_word(word)
    # Assert
    assert score_word("A") == 1
    assert score_word("DOG") == 5
    assert score_word("WHIMSY") == 17

def test_score_word_accurate_ignores_case():
    # Arrange
    word = "a"
    word = "dog"
    word = "wHiMsY"
    # Assert
    assert score_word("a") == 1
    assert score_word("dog") == 5
    assert score_word("wHiMsY") == 17

def test_score_zero_for_empty():
    # Arrange
    word = ""
    # Assert
    assert score_word("") == 0

def test_score_extra_points_for_seven_or_longer():
    # Arrange
    word = "XXXXXXX"
    word = "XXXXXXXX"
    word = "XXXXXXXXX"
    # Assert
    assert score_word("XXXXXXX") == 64
    assert score_word("XXXXXXXX") == 72
    assert score_word("XXXXXXXXX") == 80
    