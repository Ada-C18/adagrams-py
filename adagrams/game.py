### Wave 1: draw_letters
from itertools import repeat
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

#letter_bank: list of 10 letter for the player
#word: word user comes up with
#word_list: list of words user comes up with

def draw_letters():
#Create LETTER_POOL variable 
#   houses letters and availability
#Randomly pull 10 letters from letter pool
#   store in variable: letters
#   list of strings
    # letter not selected too many times
#       keep track of letter availability
#       decrement every time letter is drawn
#letter_pool resets after every round

    letters=[]
    letter_bank=[]
    for letter in LETTER_POOL.items():
        letters.extend(repeat(letter[0],letter[1]))
    
    while len(letter_bank)<10:
        random_letter=random.choice(letters)
        letter_bank.append(random_letter)
        letters.remove(random_letter)
        if len(letter_bank)==10:
            break

    return letter_bank
    
        


draw_letters()

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass


# | A : 9  | N : 6 |
# | B : 2  | O : 8 |
# | C : 2  | P : 2 |
# | D : 4  | Q : 1 |
# | E : 12 | R : 6 |
# | F : 2  | S : 4 |
# | G : 3  | T : 6 |
# | H : 2  | U : 4 |
# | I : 9  | V : 2 |
# | J : 1  | W : 2 |
# | K : 1  | X : 1 |
# | L : 4  | Y : 2 |
# | M : 2  | Z : 1 |
