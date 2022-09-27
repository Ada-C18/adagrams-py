from gzip import BadGzipFile
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
    bag_of_letters = []
    hand = []
    # based on the value add the letter n times to alphabet list
    for letter,value in LETTER_POOL.items():
        for i in range(value):
            bag_of_letters.append(letter)

    while len(hand) != 10:
        draw = random.choice(bag_of_letters)
        hand.append(draw)
            

        #     bag_of_letters.remove(letter)
    # print(bag_of_letters)
    return hand
    
    
    
    


    # pass

    


def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass