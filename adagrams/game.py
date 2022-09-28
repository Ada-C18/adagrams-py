import random
from typing import Counter
letter_bank = {
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
    letter_pool = [key for key, val in letter_bank.items() for i in range(val)]
    last_index = len(letter_pool) - 1
    hand = []
    
    while last_index > 0:
        rand_index = random.randint(0, last_index)
        letter_pool[last_index], letter_pool[rand_index] = letter_pool[rand_index], letter_pool[last_index]
        last_index -= 1
        
    for i in range(10):
        hand.append(letter_pool[i])
    return hand
def uses_available_letters(word, letter_bank):
    pass

def score_word(word):

    score_chart = {
        1: 'AEIOULNRST',
        2: 'DG',
        3: 'BCMP',
        4: 'FHVWY',
        5: 'K',
        8: 'JX',
        10: 'QZ'
    }
    score = 0
    if len(word) >= 7:
        score += 8

    for points, letters in score_chart.items():
        for char in word.upper():
            if char in letters:
                score += points
    return score

def get_highest_word_score(word_list):
    pass