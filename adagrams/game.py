import random
from collections import Counter

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
SCORE_CHART = {
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

def draw_letters():
    letter_pool_dict = LETTER_POOL.copy()
    letter_bank = []
    while len(letter_bank) < 10:
        letter = random.choice(list(letter_pool_dict.keys()))
        if letter_pool_dict[letter] > 0:
            letter_bank.append(letter)
            letter_pool_dict[letter] -= 1

    return letter_bank
        


def uses_available_letters(word,letter_bank):
    for letter in word.upper():
        if letter not in letter_bank:
            return False
        elif word.upper().count(letter) > letter_bank.count(letter):
            return False
    
    return True

    
    #### second solution

    # def uses_available_letters(word,letter_bank):
    # word_dict = dict(Counter(word.upper()))
    # letter_bank_dict = dict(Counter(letter_bank))
    # for k in word_dict:
    #     if k not in letter_bank_dict or word_dict[k] > letter_bank_dict[k]:
    #         return False
    # return True

            
    
def score_word(word):
    score = 0
    if len(word) >= 7:
        score += 8
    for letter in word.upper():
        score += SCORE_CHART[letter]
    return score



def get_highest_word_score(word_list):
    highest_score = 0
    winning_word = None
    for word in word_list:
        score = score_word(word)
    
        # no ties
        if score > highest_score:
            highest_score = score
            winning_word = word


        # handle ties
        if score == highest_score:
            if len(word) == 10 and len(winning_word) != 10:
                winning_word = word
            elif len(word) < len(winning_word) and len(winning_word) != 10:
                winning_word = word

    return winning_word, highest_score







        


    
    





                
 
                
            
            



    
    

