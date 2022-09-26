# from tests.test_wave_01 import LETTER_POOL
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
    'Z': 1
}

def draw_letters():
    # aria *********
    # add letter and frequency to their own lists
    letters = []
    frequency_of_letters = []
    for letter, frequency in LETTER_POOL.items():
        letters.append(letter)
        frequency_of_letters.append(frequency)
    # return list of 10 random letters using random.sample
    random_letters_list = random.sample(letters, counts=frequency_of_letters, k=10)
    return random_letters_list



def uses_available_letters(word, letter_bank):
    # aria *********
    # copy letter bank list
    copy_letter_bank = letter_bank.copy()
    # make string all upper
    # check to see if letter in word is in letter bank
    for letter in word.upper():
    # if letter is in letter bank, remove from letter bank 
        if letter in copy_letter_bank:
            copy_letter_bank.remove(letter)
    # if letter is not in letter bank, return false
        elif letter not in copy_letter_bank:
            return False
    # if loop finishes and doesn't return false, all the letters are in word, return true
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass