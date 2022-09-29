import random
from adagrams.const_dicts import *

def draw_letters():
    letter_pool_list = []
    for letter, number in LETTER_POOL.items():
        letter_pool_list.extend([letter]*number)
    hand_list = []
    while len(hand_list) < 10:
        random.shuffle(letter_pool_list)
        hand_list.append(letter_pool_list.pop())
    return hand_list

def uses_available_letters(word, letter_bank):
    word = word.upper()
    new_letter_bank = []
    new_letter_bank.extend(letter_bank)
    for letter in word:
        if letter in new_letter_bank:
            new_letter_bank.remove(letter)
        else:
            return False
    return True


def score_word(word):
    word = word.upper()
    sum = 0
    if len(word) >= 7:
        sum += 8
    for letter in word:
        sum += SCORE_CHART_DICT[letter]
    return sum

def get_highest_word_score(word_list):
    highest_score = 0
    highest_score_word = ""

    for word in word_list:
        score = score_word(word)
        if score > highest_score:
            highest_score = score
            highest_score_word = word 
        elif score == highest_score:
            if len(highest_score_word) == 10 and len(word) < len(highest_score_word) or len(word) == len(highest_score_word):
                continue
            elif len(word) < len(highest_score_word) or len(word) == 10:
                highest_score_word = word
    return (highest_score_word, highest_score)