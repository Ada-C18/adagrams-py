import random
import string
from collections import Counter

def draw_letters():

    letter_pool = {
        "a" : 9,
        "b" : 2,
        "c" : 2,
        "d" : 4,
        "e" : 12,
        "f" : 2,
        "g" : 3,
        "h" : 2,
        "i" : 9,
        "j" : 1,
        "k" : 1,
        "l" : 4,
        "m" : 2,
        "n" : 6,
        "o" : 8,
        "p" : 2,
        "q" : 1,
        "r" : 6,
        "s" : 4,
        "t" : 6,
        "u" : 4,
        "v" : 2,
        "w" : 2,
        "x" : 1,
        "y" : 2,
        "z" : 1,
    }

    letters = string.ascii_lowercase
    drawn_letters = random.choices(letters,k=10)

    count = Counter(drawn_letters)
    
    for each_letter in drawn_letters:
        if count[each_letter] > letter_pool[each_letter]:
            # each_letter = "e" 
            # drawn_letters = random.choices(letters,k=10)

    return drawn_letters


def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass