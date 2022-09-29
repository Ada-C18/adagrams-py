from operator import length_hint
from platform import win32_edition
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

SCORE_POOL = {
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

def copy_dictionary(pool):
    """
    Returns a copy of a dictionary.
    """
    pool_dict_copy = {}
    for key, value in pool.items():
        pool_dict_copy[key] = value
    return pool_dict_copy

def draw_letters(): 
    """
    Returns an array of ten random strings from letter pool.
    """  
    res_letters = []
    letter_bank_dict = copy_dictionary(LETTER_POOL)
    while len(res_letters) < 10:   
        letter = random.choice(list(letter_bank_dict.keys()))
        if letter_bank_dict[letter] > 0:
            res_letters.append(letter)
            letter_bank_dict[letter] -= 1
    return res_letters

def create_dict(data):
    """
    Returns dictionary with key "element" and
    with value equal to the frequency of the element.
    """
    data_dict = {}
    for element in data:
        if element not in data_dict:
            data_dict[element] = 1
        else:
            data_dict[element] += 1
    return data_dict

def uses_available_letters(word, letter_bank):
    """
    Returns True if every letter from word 
    belongs to the letter bank, otherwise False.
    """
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
    """
    Returns the score of the given word.
    """
    total_score = 0
    word = word.upper()
    if len(word) >= 7 and len(word) <= 10:
        total_score += 8
    for letter in word:
        if letter in SCORE_POOL.keys():
            total_score += SCORE_POOL[letter]
    return total_score

def get_highest_word_score(word_list):
    """
    Returns a tuple of a winning word and it's score.
    """  
    max_score = 0
    win_name = ""
    tie_word_dict = {}
    for word in word_list:
        word_score = score_word(word)
        if word_score > max_score:
            max_score = word_score
            win_name = word           
    
    for word in word_list:
        if score_word(word) == max_score:
            tie_word_dict[word] = len(word)
    
    # check if only one word in tie_word_dict
    if len(tie_word_dict) == 1:
        return win_name, max_score
    
    #check if len of word in tie_word_dict = 10, this word win
    for word, length in tie_word_dict.items():
        while length == 10:
            return (word, max_score)                
    
    #check if len of word != 10, word with fewest len win 
    #and if words with the same length -> pick the first one in tie_word_dict
    else:
        mini_length = 10
        for word, length in tie_word_dict.items():  
            if length < mini_length:
                mini_length = length
        key_list = list(tie_word_dict.keys())
        val_list = list(tie_word_dict.values())
        win_name = key_list[val_list.index(mini_length)]        
    return (win_name, max_score)        