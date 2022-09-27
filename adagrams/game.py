import random

distribution_of_letters = {
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
    adagrams_bag = []
    for key,value in dict.items():
        for i in range(value):
            adagrams_bag.append(key)
    return adagrams_bag

def draw_letters():
    
    adagrams_bag = dict_to_list(distribution_of_letters)
    hand_as_numbers = []
    hand_as_letters = []
    
    while len(hand_as_letters) < 10:
        index = random.randint(0,len(adagrams_bag)-1)
        if index not in hand_as_numbers:
            hand_as_numbers.append(index)
            hand_as_letters.append(adagrams_bag[index])
    return hand_as_letters

    
# SCORES = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
#           "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
#           "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
#           "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
#           "x": 8, "z": 10}


def uses_available_letters(word, letter_bank):
    pass


def get_highest_word_score(word_list):
    pass