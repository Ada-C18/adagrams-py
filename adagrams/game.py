import random
import copy

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

SCORE_CHART = {
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10:["Q", "Z"]		
}



#WAVE ONE
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



#WAVE TWO
def uses_available_letters(word, letter_bank):
    #creates copy of drawn letters in a hand
    letters_hand = copy.deepcopy(letter_bank)
    all_caps = word.upper()
    for letter in all_caps:
        if letter not in letters_hand:
            return False    
        else: 
            letters_hand.remove(letter)    
    else:
        return True

    pass

#WAVE THREE
def score_word(word):




#def get_highest_word_score(word_list):

    pass