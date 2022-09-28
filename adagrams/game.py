import random
from re import A

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
    letters = []
    
    for letter in LETTER_POOL:
        for num in range(LETTER_POOL[letter]):
            letters.append(letter)
    

    hand = []

    while len(hand) < 10:
        rand_letter = random.choice(letters)
        hand.append(rand_letter)
        letters.remove(rand_letter)
    return hand 

def uses_available_letters(word, letter_bank):
    available_letters = []

    for letter in letter_bank:
        letter_capitalize = letter.capitalize()
        available_letters.append(letter_capitalize)

    for letter in word:
        letter_capitalize = letter.capitalize()
        if letter_capitalize in available_letters:
            available_letters.remove(letter_capitalize)
        else:
            return False
    return True

def score_word(word):
    letter_value = {"A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "R": 1, "S": 1, "T": 1, "D": 2, "G": 2, "B": 3, "C": 3, "M": 3, "P": 3, "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4, "K": 5, "J": 8, "X": 8, "Q": 10, "Z": 10}

    point = 0
    for letter in word.upper():
        if letter_value[letter]:
            point += letter_value[letter]

    if len(word) >= 7:
        point += 8
    return point


def get_highest_word_score(word_list):
    pass