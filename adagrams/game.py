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

    # for letter in word:
    #     if letter not in letter_bank:
    #         return False

    for letter in string.ascii_uppercase:
        letters[letter] = 0
    
    for letter in letter_bank:
        letters[letter] += 1
    
    for letter in word:
        if word.count(letter) > letters[letter]:
            return False
    
    return True

        
def score_word(word):
    score_chart = {
        1:["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2:["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"]
    }

    word = word.upper()
    score = 0

    if len(word) == 0:
        return score
    
    for letter in word:
        for key, value in score_chart.items():
            if letter in value:
                score += key
    if len(word)>= 7:
        score += 8
    return score

def get_highest_word_score(word_list):
    pass