from tests.test_wave_01 import LETTER_POOL
import random
import copy

def draw_letters():

    letter_bank = []
    temp_letter_pool = copy.deepcopy(LETTER_POOL)

    while len(letter_bank) < 10:        
        letter = random.choice(list(temp_letter_pool.keys()))
        if temp_letter_pool[letter] > 0:
            temp_letter_pool[letter] -= 1
            letter_bank.append(letter)
        else:
            continue
   
    return letter_bank


def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass