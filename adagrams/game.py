import random
from lib2to3.pgen2.pgen import DFAState

# initiate the empty list 
# to keep the original pool - make a copy of dictionary
# get letter from the copy dict/pool  random.ran()
# draw one letter a time, x 10, for loop (0, 10),  
# also update the qty. of the letter in each loop
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

def copy_letter_from_original(pool):
    pool_dict_copy = {}
    for key, value in pool.items():
        pool_dict_copy[key] = value
    return pool_dict_copy

def draw_letters():   
    res_letters = []
    letter_bank_dict = copy_letter_from_original(LETTER_POOL)
    while len(res_letters) < 10:   
        letter = random.choice(list(letter_bank_dict.keys()))
        if letter_bank_dict[letter] > 0:
            res_letters.append(letter)
            letter_bank_dict[letter] -= 1
    print(res_letters)
    return res_letters

def create_dict(data):
    # initiatite word_dict 
    data_dict = {}
    for element in data:
        if element not in data_dict:
            data_dict[element] = 1
        else:
            data_dict[element] += 1
    return data_dict

def uses_available_letters(word, letter_bank):
    # convert word to capital
    # for each key, value in word dict.items()
    # check if key of word_dict <= key of letetr_bank dict
    # return True
    # else: return False
    word = word.upper()
    word_dict = create_dict(word)
    letter_bank_dict = create_dict(letter_bank)

    for letter, quantity in word_dict.items():
        if letter not in letter_bank_dict:
            return False
        else:
            if quantity > letter_bank_dict[letter]:
                return False        
    return True

   


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass