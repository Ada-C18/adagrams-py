import random

POOL_OF_LETTERS = {
    "A" : 9,
    "B": 2,
    "C" : 2, 
    "D" : 4,
    "E": 12,
    "F": 2,
    "G": 3,
    "H": 2,
    "I": 9,
    "J": 1,
    "K": 1,
    "L": 4,
    "M": 2,
    "N": 6,
    "O": 8,
    "P": 2,
    "Q": 1,
    "R": 6,
    "S": 4,
    "T": 6,
    "U": 4,
    "V": 2,
    "W": 2,
    "X": 1,
    "Y": 2,
    "Z":1
}

def draw_letters():
    '''
    Returns a list of strings, each string contains one letter
    '''
    letter_bank = []
    all_the_letters = []
    for key,value in POOL_OF_LETTERS.items():
        for count in range(value):
            all_the_letters.append(key)
    
    while len(letter_bank) < 10:
        letter = random.choice(all_the_letters)
        letter_bank.append(letter)
        all_the_letters.remove(letter)
    return letter_bank

def uses_available_letters(word, letter_bank):
    '''
    Input: Word is user input of a word. letter_bank is a list of 10 strings (each a letter)
    Output: Returns True or False if word contains letters within letter_bank
    '''
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass