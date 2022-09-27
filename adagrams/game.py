import random

def draw_letters():
    # Import random - assign the randomized number to the index
    # "bag" of letters will be a dictionary as shown below
    # hand will be a list
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
    bag_of_letters_dict = {
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
    bag_of_letters_list = []
    for key, value in bag_of_letters_dict.items():
        for letter in range(value):
            bag_of_letters_list.append(key)

    hand = []

    while len(hand) < 10:
        for letter in bag_of_letters_list:
            hand.append(letter)
            letter_of_index = bag_of_letters_list.index(letter)
            bag_of_letters_list.pop(letter_of_index)
            break
    return hand

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass