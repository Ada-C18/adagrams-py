import random

def draw_letters():
    POOL = {
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
    
    hand = random.sample(sorted(POOL), 10, counts=POOL.values())
    
    return hand

def uses_available_letters(word, letter_bank):
    test_word = word.upper()
    hand = []

    for letter in letter_bank:
        hand.append(letter)

    try:
        for letter in test_word:
            hand.remove(letter)

    except ValueError:
        return False

    return True

def score_word(word):
    SCORE_CHART= {
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
    
    score = 0
    score_word = word.upper()

    for letter in score_word:
        score += SCORE_CHART[letter]

    if len(word) >= 7:
        score += 8
    
    return score

def get_highest_word_score(word_list):
    highest_score = ("",0)
    for word in word_list:
        current_tuple = (word, score_word(word))
        if current_tuple[1] > highest_score[1]:
            highest_score = current_tuple
        elif current_tuple[1] == highest_score[1]:
            if len(highest_score[0]) == 10 or len(current_tuple[0]) == len(highest_score[0]):
                continue
            elif len(current_tuple[0]) == 10 or len(current_tuple[0]) < len(highest_score[0]):
                highest_score = current_tuple
            
    return highest_score
    
