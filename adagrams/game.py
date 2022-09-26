import string
import random

def draw_letters():
    
    pool_of_letters_dict = {
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
    string.ascii_letters

    letters_in_hand = []
    counter = 0
    while counter < 10:
        choice =(random.choice(string.ascii_letters))
        choice = choice.capitalize()

        if pool_of_letters_dict[choice] > 0:
            letters_in_hand.append(choice)
            counter+=1
    print(letters_in_hand)  
    return letters_in_hand 

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass