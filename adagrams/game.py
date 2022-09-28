import string
from random import sample
# from collections import Counter

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
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass