import string
from random import sample
from collections import Counter

def draw_letters():

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
        'Z': 1
    }
# APPROACH # 1
    # letters = string.ascii_lowercase
    # drawn_letters = random.choices(letters,k=10)

    # count = Counter(drawn_letters)
    
    # for each_letter in drawn_letters:
    #     if count[each_letter] > letter_pool[each_letter]:
    #         drawn_letters = random.choices(letters,k=10)

    drawn_letters = sample(LETTER_POOL.keys(), k=10, counts=LETTER_POOL.values())

    return drawn_letters


def uses_available_letters(word, letter_bank):

    word = word.upper()

    for letter in word:
        if letter not in letter_bank:
            return False

    count_word = Counter(word)
    count_letter_bank = Counter(letter_bank)

    for k, v in count_word.items():
        if k in count_letter_bank:
            if v <= count_letter_bank[k]:
                return True

    return False


def score_word(word):
    LETTERS_VALUES = {
        "A" : 1,
        "E" : 1,
        "I" : 1,
        "O" : 1,
        "U" : 1,
        "L" : 1,
        "N" : 1,
        "R" : 1,
        "S" : 1,
        "T" : 1,
        "D" : 2,
        "G" : 2,
        "B" : 3,
        "C" : 3,
        "M" : 3,
        "P" : 3,
        "F" : 4,
        "H" : 4,
        "V" : 4,
        "W" : 4,
        "Y" : 4,
        "K" : 5,
        "J" : 8,
        "X" : 8,
        "Q" : 10,
        "Z" : 10,
    }
    word = word.upper()
    word_value = 0
    for letter in word:
        if letter in LETTERS_VALUES:
            word_value += LETTERS_VALUES[letter]
    if len(word) > 6:
        word_value += 8
    return word_value

def get_highest_word_score(word_list):
    pass