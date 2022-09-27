import random
import copy

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

def dict_to_list(dict):
    bag_of_letters = []
    for key, value in dict.items():
        new_letters = [key] * value
        bag_of_letters.extend(new_letters)
    
    return bag_of_letters

def draw_letters():
    bag_of_letters = dict_to_list(LETTER_POOL)
    hand_as_numbers = []
    hand_as_letters = []
    
    while len(hand_as_letters) < 10:
        index = random.randint(0,len(bag_of_letters)-1)
        if index not in hand_as_numbers:
            hand_as_numbers.append(index)
            hand_as_letters.append(bag_of_letters[index])
    
    return hand_as_letters


def uses_available_letters(word, letter_bank):
    copy_of_letter_bank = copy.deepcopy(letter_bank)
    all_caps_word = word.upper()
    for letter in all_caps_word:
        if letter not in copy_of_letter_bank:
            return False
        else:
            copy_of_letter_bank.remove(letter)
    return True


def get_highest_word_score(word_list):
    pass