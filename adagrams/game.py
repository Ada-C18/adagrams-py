import random
import string
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
    count_dict = {}
    new_letter = []
    for i in range(1, 11):
        letter = random.choice(string.ascii_uppercase)
        if letter in count_dict and count_dict[letter] < LETTER_POOL[letter]:
            count_dict[letter] += 1
            new_letter.append(letter)
        elif letter not in count_dict:
            count_dict[letter] = 1
            new_letter.append(letter)
        elif count_dict[letter] > LETTER_POOL[letter]:
            continue
        
    # for letter in new_letter:
    #     if letter in count_dict and count_dict[letter] < LETTER_POOL[letter]:
    #         count_dict[letter] += 1
    #     else:
    #         count_dict[letter] = 1
    # letter_list = [*Counter(count_dict).elements()]
    # letter_list = list(count_dict.keys())
    # print(letter_list)
    print(new_letter)
    return new_letter

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass