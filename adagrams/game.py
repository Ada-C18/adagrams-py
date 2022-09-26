import random

def draw_letters():
    
    LETTER_DISTRIBUTION = {
        "A" : 9,
        "B" : 2,
        "C" : 2,
        "D" : 4,
        "E" : 12,
        "F" : 2,
        "G" : 3,
        "H" : 2,
        "I" : 9,
        "J" : 1,
        "K" : 1,
        "L" : 4,
        "M" : 2,
        "N" : 6,
        "O" : 8,
        "P" : 2,
        "Q" : 1,
        "R" : 6,
        "S" : 4,
        "T" : 6,
        "U" : 4,
        "V" : 2,
        "W" : 2,
        "X" : 1,
        "Y" : 2,
        "Z" : 1
    }

    letter_pool = []

    for key, value in LETTER_DISTRIBUTION.items():
        letter_pool += key * value
    
    user_letters = random.sample(letter_pool, k=10)

    return user_letters
    


def uses_available_letters(word, letter_bank):
    available_letters = {}

    for letter in letter_bank:
        available_letters[letter] = available_letters.get(letter, 0) + 1

    for letter in word.upper():
        if letter not in letter_bank or available_letters[letter] == 0:
            return False
        elif available_letters[letter] != 0:
            available_letters[letter] -= 1

    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass
