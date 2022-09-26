from tests.test_wave_01 import LETTER_POOL


def draw_letters():
    list_1= [k*v for k,v in LETTER_POOL.items()]
    letter_pool_list=[]
    for string in list_1:
        for letter in string:
            letter_pool_list.append(letter)
    
    
    print(letter_pool_list)
  

    return letter_pool_list



    

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass