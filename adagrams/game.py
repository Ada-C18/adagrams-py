import copy
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
    '''
    pulls a random letter from LETTER_POOL and stores it
    in a list, returns list
    '''
    letter_list = generate_letter_list()
    user_hand = []
    
    while len(user_hand) < 10:
        random_letter = random.choice(letter_list)
        user_hand.append(random_letter)
        for letter in letter_list:
            if letter == random_letter:
                letter_list.remove(letter)

    return user_hand

def generate_letter_list():
    '''
    helper function returns letter pool list
    '''
    letter_list = []

    for letter in LETTER_POOL:
        for i in range(LETTER_POOL[letter]):
            letter_list.append(letter)
    
    return letter_list



def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass