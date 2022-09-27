import random
import copy

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
    temp_letter_bank = copy.deepcopy(letter_bank)

    for letter in word:
        if letter.upper() in temp_letter_bank:
            temp_letter_bank.remove(letter.upper())
        else:
            return False
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass