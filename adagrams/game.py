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
    upper_case_word = word.upper()
    for letter in upper_case_word:
        if letter not in letter_bank:
            return False
        elif upper_case_word.count(letter) > letter_bank.count(letter):
            return False
    
    return True

    
    #### second solution:

    # word_dict = dict(Counter(word.upper()))
    # letter_bank_dict = dict(Counter(letter_bank))
    # for k in word_dict:
    #     if k not in letter_bank_dict or word_dict[k] > letter_bank_dict[k]:
    #         return False
    # return True

            

            
def score_word(word):
    pass
    


def get_highest_word_score(word_list):
   pass
                
 
                
            
            



    
    

