import random
from random import choices
import copy

LETTER_DICT = {
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

def draw_letters():

    letter_bank = []
    letter_copy = copy.deepcopy(LETTER_DICT)

    while len(letter_bank) < 10:
        key_list = list(letter_copy.keys())
        random_letter = random.choice(key_list)
        if letter_copy[random_letter] > 0:
            letter_bank.append(random_letter)
            letter_copy[random_letter] -= 1
    print(letter_bank)
    return letter_bank 


def uses_available_letters(word, letter_bank):

    case_word = word.upper()
    letter_bank_copy = copy.deepcopy(letter_bank)
    for letter in case_word:
        if letter.upper() not in letter_bank_copy:
            return False
        elif letter.upper() in case_word:
            letter_bank_copy.remove(letter)
    return True
    

def score_word(word):
    
    SCORE_DICT = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
    }

    case_word = word.upper()
    sum_list = []
    for letter in case_word:
        for key, value in SCORE_DICT.items():
            if letter == key:
                sum_list.append(value)
    n = len(case_word)
    if n == 7 or n==8 or n==9 or n==10:
        sum_list.append(8)
    return sum(sum_list)

def get_highest_word_score(word_list):
    word_and_score = []
    highest_score = 0 
    for word in word_list:
        if score_word(word) > highest_score:
            highest_score = score_word(word)
            word_and_score


    
