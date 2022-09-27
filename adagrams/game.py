import random
from itertools import chain
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
    letter_pool = list(chain(*[random.choices(key, k = val) for key, val in letter_bank.items()]))
    hand = []
    
    for i in range(10):
        letter = random.choice(letter_pool)
        hand.append(letter)
        letter_pool.remove(letter)
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

    for point, letters in score_chart.items():
        for char in word.upper():
            if char in letters:
                score += point
    return score

def get_highest_word_score(word_list):
    pass