from tests.test_wave_01 import LETTER_POOL

import random
def draw_letters():
    list_1= [k*v for k,v in LETTER_POOL.items()]
    letter_pool_list=[]
    for string in list_1:
        for letter in string:
            letter_pool_list.append(letter)
    
    
    print(letter_pool_list)
    user_hand= (random.choices(letter_pool_list,k=10))

    return user_hand 
    



    

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass