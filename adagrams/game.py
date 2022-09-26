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
    
        


# - Has two parameters:
#    - `word`, the first parameter, describes some input word, and is a string
#    - `letter_bank`, the second parameter, describes an array of drawn letters in a hand. You can expect this to be an array of ten strings, with each string representing a letter
# - Returns either `True` or `False`
# - Returns `True` if every letter in the `input` word is available (in the right quantities) in the `letter_bank`
# - Returns `False` if not; if there is a letter in `input` that is not present in the `letter_bank` or has too much of compared to the `letter_bank`

def uses_available_letters(word, letter_bank):
    #Check for len(word) is > len(letter_bank)
    #change case to .upper()
    #check if letter not in letter_bank
        #return false
    #check if letter is in letter_bank
    #check for correct letter availability in letter_bank
    #check if every letter in word is avail
    
    for letter in word:
        if letter not in letter_bank:
            return False
        elif letter in letter_bank:
            pass
    return True



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
