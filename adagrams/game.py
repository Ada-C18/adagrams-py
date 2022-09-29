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

import random
import string


def draw_letters():
    hand = []
    keep_going = True
    while keep_going:
        letter = random.choice(string.ascii_uppercase)
        if hand.count(letter) == LETTER_POOL[letter]:
            continue
        else:
            hand.append(letter)
        if len(hand) == 10:
            keep_going = False

    return hand

def uses_available_letters(word, letter_bank):
    
    letters = {}
    word = word.upper()

    for letter in string.ascii_uppercase:
        letters[letter] = 0
    
    for letter in letter_bank:
        letters[letter] += 1
    
    for letter in word:
        if word.count(letter) > letters[letter]:
            return False
    
    return True

def score_word(word):
    # change this to a constant big O rather than linear by looking up by key (changing key to the letter)
    # because looking it up by key is constant whereas looking it up by value and returning the key linear
    score_chart = {
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
    

def get_highest_word_score(word_list):