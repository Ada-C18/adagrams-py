import random
LETTER_POOL = [{
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
}]
def draw_letters():
    letters = []
    remaining_letters_pool = {}
    
    if len(letters) < 11:
        for dict in LETTER_POOL:
            for key, value in dict.items():
                if key not in remaining_letters_pool and value > 0:
                    remaining_letters_pool[key] = value
    while len(letters) < 10:
        random_letter = random.choice(list(remaining_letters_pool))
        for letter in list(remaining_letters_pool):
            if remaining_letters_pool[letter] == 0:
                remaining_letters_pool.pop(letter)
            elif random_letter == letter:
                remaining_letters_pool[letter]-= 1
                letters.append(random_letter)
                
    return letters


def uses_available_letters(word, letter_bank):
    dict_word={}
    word=word.upper()
    word_list=[]
    values_dict=[]
    
    for letter in word:
        dict_word[letter]=False
    for letter in word:
        word_list.append(letter)
    for letter in word_list:
        if letter in letter_bank:
            freq_letter=word_list.count(letter)
            freq_letter_bank=letter_bank.count(letter)
            if freq_letter == freq_letter_bank:
                dict_word[letter]=True
            elif freq_letter>freq_letter_bank:
                dict_word[letter]=False
            elif freq_letter<freq_letter_bank:
                dict_word[letter]=True
        else:
            dict_word[letter]=False
    for key,value in dict_word.items():
        values_dict.append(value)
    if False in values_dict:
        return False
    else:
        return True





def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass