from collections import Counter
import random

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1,
}

LETTER_VALUES = {
    "A": 1,
    "B": 3,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 4,
    "G": 2,
    "H": 4,
    "I": 1,
    "J": 1,
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
    "Z": 10,                 
}


def draw_letters() -> list:
    """
    Returns a list with ten letter-tiles chosen randomly from LETTER_POOL
    """
    letter_pool_copy = LETTER_POOL.copy()
    hand = []
    while len(hand) < 10:
        letter = random.choice(list(letter_pool_copy.keys()))
        if letter_pool_copy[letter] > 0:
            hand.append(letter)
            letter_pool_copy[letter] =- 1

    return hand


def uses_available_letters(word: str, letter_bank: list) -> bool:
    """
    Returns True if all letters from word are available in letter_bank, else returs False. 
    """
    letters_count = Counter(letter_bank)
    for letter in word:
        if letters_count[letter.upper()] > 0:
            letters_count[letter.upper()] -= 1
            continue
        else:
            return False

    return True


def score_word(word: str) -> int:
    score = 0
    for letter in word:
        score += LETTER_VALUES[letter.upper()]
    if len(word) > 6:
        score += 8
    
    return score


def get_highest_word_score(word_list: list) -> tuple:
    """
    Returns a tuple (word, score) with the highest score. 
    If there is a tie, it will be solved depending on the length of the words.
    """
    score = score_word 
    highest_score = ("", 0)

    for word in word_list: 
        if score(word) > highest_score[1]:
            highest_score = (word, score(word))
        elif score(word) == highest_score[1]: 
            if len(highest_score[0]) == 10: 
                highest_score = highest_score 
            elif len(word) == 10: 
                highest_score = (word, score(word))
            elif len(word) < len(highest_score[0]):
                highest_score = (word, score(word))
                
    return highest_score
