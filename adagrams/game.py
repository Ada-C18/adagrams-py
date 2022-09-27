import random
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

# to keep the original pool - make a copy of dictionary
# initiate the empty list 
# get letter from the copy dict/pool  random.ran()
# draw one letter a time, x 10, for loop (0, 10),  
# also update the qty. of the letter in each loop

def copy_letter_bank_dict(pool_dict):
    pool_dict_copy = {}
    for key, value in pool_dict.items():
        pool_dict_copy[key] = value
    return pool_dict_copy
# print(copy_letter_bank_dict(LETTER_POOL))
print(f"pool before function {LETTER_POOL}")

def draw_letters():
    
    letters = []
    letter_bank_dict = copy_letter_bank_dict(LETTER_POOL)
    for i in range(10): #to do while loop instead since the quantity can be 0
        letter = random.choice(list(letter_bank_dict.keys()))
        # check if there is quantity, append, else > continue
        letters.append(letter)
        # reduce quantity by one from letetr bank
    print(letters)
    return letters
print(f"pool after function {LETTER_POOL}")  

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass