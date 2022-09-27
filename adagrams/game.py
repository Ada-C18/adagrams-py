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

    random_hand = []

    for letter in LETTER_POOL:
        for _ in range(LETTER_POOL[letter]):
            random_hand += letter
    
    return (random.sample(random_hand,10))


def uses_available_letters(word, letter_bank):

    word_1 = word.upper()

    for letter in word_1:
        for i in letter_bank:
            if letter not in letter_bank or word_1.count(letter) > letter_bank.count(i):
                return False
    return True 

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass