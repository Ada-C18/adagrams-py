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
    (0) input: LETTER_POOL in dict as global parameter
    (1) access LETTER_POOL: (key, value) = (letter, how many)
    (2) list of n * letter, e.g. [...'Y', 'Y', 'Z']
    (3) sampling 10 letters from the list ! choice can repeat for the same index !
    '''

    letter_list = []
    for letter, n in LETTER_POOL.items(): 
        letter_list.extend(n * letter)
    letters = random.sample(letter_list, k=10)
    return letters 

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass
