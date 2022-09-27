import random
import copy

LETTER_DICT = {
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
 
    result = []
    letter_copy = copy.deepcopy(LETTER_DICT)
   
    while len(result) < 10:
        key_list = list(letter_copy.keys())
        rand_char = random.choice(key_list)
        if letter_copy[rand_char] > 0:
            result.append(rand_char)
            letter_copy[rand_char] -= 1
      
    return result 

def uses_available_letters(word, letter_bank):
    print('Hi Aisha!')
    pass
def score_word(word):
    
    pass

def get_highest_word_score(word_list):
    pass