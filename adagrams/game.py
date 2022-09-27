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
    letter_list = (list(LETTER_DICT))
    weight_list = list(LETTER_DICT.values())
    letter_bank = random.choices(letter_list, weight_list ,k=10)

    dict_copy = copy.deepcopy(LETTER_DICT)

    for letter in letter_bank:
        letter_count =letter_bank.count(letter)
        if letter in LETTER_DICT.keys():
            print(letter)
        print (letter_count)
    print (letter_bank)
    # return letter_bank


    letter_freq = {}
    for letter in letter_bank:
        if letter in letter_freq:
            letter_freq[letter] += 1
        else:
            letter_freq[letter] = 1


def uses_available_letters(word, letter_bank):
    for letter in word:
        if letter in letter_bank:
            return True




def score_word(word):
    
    pass

def get_highest_word_score(word_list):
    pass