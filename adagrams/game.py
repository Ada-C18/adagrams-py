import random

letter_pool = [['A'] * 9, ['B'] * 2, ['C'] * 2, ['D'] * 4, ['E'] * 12, ['F'] * 2, ['G'] * 3, ['H'] * 2, ['I'] * 9, 'J', 'K' , ['L'] * 4, 
['M'] * 2, ['N'] * 6, ['O'] * 8, ['P'] * 2, 'Q', ['R'] * 6, ['S'] * 4, ['T'] * 6, ['U'] * 4, ['V'] * 2, ['W'] * 2, 'X', ['Y'] * 2, 'Z']
# Nested list that contains all the letters that a player can draw from

def draw_letters():
    
    flat_pool = [l for letter in letter_pool for l in letter]
    # flattened list from letter_pool
    hand = []

    for i in range(10):
        letter = random.choice(flat_pool) # function that chooses a random letter from the flattened list 
        hand.append(letter)
        flat_pool.remove(letter) # after appending each letter remove that letter from letter pool
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