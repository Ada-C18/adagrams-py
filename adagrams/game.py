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
def draw_letters():
    letters = []
    letter_pool_dict = LETTER_POOL.copy()
    while len(letters) < 10:
        letter = random.choice(list(letter_pool_dict.keys()))
        for key in letter_pool_dict:
            if key == letter and letter_pool_dict[key] > 0:
                letters.append(letter)
                letter_pool_dict[key] -= 1
    return letters

def uses_available_letters(word, letter_bank):
    word_list = list(word.upper())
    letter_bank_copy = letter_bank.copy()
    return_list = []
    for letter in word_list:
        if letter in letter_bank_copy:
            return_list.append(letter)
            letter_bank_copy.remove(letter)

    if word_list == return_list:
        return True
    else:
        return False

def score_word(word):
    # point values for letters
    value_1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']
    value_2 = ['D', 'G']
    value_3 = ['B', 'C', 'M', 'P']
    value_4 = ['F', 'H', 'V', 'W', 'Y']
    value_5 = ['K']
    value_8 = ['J', 'X']
    value_10 = ['Q', 'Z']
    
    word_list = list(word.upper())
    score_counter = 0
    
    for letter in word_list:
        if letter in value_1:
            score_counter += 1
        elif letter in value_2:
            score_counter += 2
        elif letter in value_3:
            score_counter += 3
        elif letter in value_4:
            score_counter += 4
        elif letter in value_5:
            score_counter += 5
        elif letter in value_8:
            score_counter += 8
        elif letter in value_10:
            score_counter += 10
        else:
            score_counter += 0
    
    if len(word_list) >= 7 and len(word_list) <= 10:
        score_counter += 8

    return score_counter

def get_highest_word_score(word_list):
    pass