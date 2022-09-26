import copy
import random

def draw_letters():
    ORIGINAL_POOL = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "C", "C",
    "D", "D", "D", "D", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
    "F", "F", "G", "G", "G", "H", "H", "I", "I", "I", "I", "I", "I", "I", "I", "I", 
    "J", "K", "L", "L", "L", "L", "M", "M", "N", "N", "N", "N", "N", "N",
    "O", "O", "O", "O", "O", "O", "O", "O", "P", "P", "Q", "R", "R", "R", "R", "R", "R", 
    "S", "S", "S", "S", "T", "T", "T", "T", "T", "T", "U", "U", "U", "U", 
    "V", "V", "W", "W", "X", "Y", "Y", "Z"]

    hand = []
    game_pool = copy.deepcopy(ORIGINAL_POOL)

    while len(hand) < 10:
        letter = random.choice(game_pool)
        hand.append(letter)
        game_pool.remove(letter)
        print(hand)
    return hand

draw_letters()

# ORIGINAL_POOL = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "C", "C",
# "D", "D", "D", "D", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# "F", "F", "G", "G", "G", "H", "H", "I", "I", "I", "I", "I", "I", "I", "I", "I", 
# "J", "K", "L", "L", "L", "L", "M", "M", "N", "N", "N", "N", "N", "N",
# "O", "O", "O", "O", "O", "O", "O", "O", "P", "P", "Q", "R", "R", "R", "R", "R", "R", 
# "S", "S", "S", "S", "T", "T", "T", "T", "T", "T", "U", "U", "U", "U", 
# "V", "V", "W", "W", "X", "Y", "Y", "Z"]


# print({ORIGINAL_POOL.count("A")})
# print({ORIGINAL_POOL.count("B")})
# print({ORIGINAL_POOL.count("C")})
# print({ORIGINAL_POOL.count("D")})
# print({ORIGINAL_POOL.count("E")})
# print({ORIGINAL_POOL.count("F")})
# print({ORIGINAL_POOL.count("G")})
# print({ORIGINAL_POOL.count("H")})
# print({ORIGINAL_POOL.count("I")})
# print({ORIGINAL_POOL.count("J")})
# print({ORIGINAL_POOL.count("K")})
# print({ORIGINAL_POOL.count("L")})
# print({ORIGINAL_POOL.count("M")})
# print({ORIGINAL_POOL.count("N")})
# print({ORIGINAL_POOL.count("O")})
# print({ORIGINAL_POOL.count("P")})
# print({ORIGINAL_POOL.count("Q")})
# print({ORIGINAL_POOL.count("R")})
# print({ORIGINAL_POOL.count("S")})
# print({ORIGINAL_POOL.count("T")})
# print({ORIGINAL_POOL.count("U")})
# print({ORIGINAL_POOL.count("V")})
# print({ORIGINAL_POOL.count("W")})
# print({ORIGINAL_POOL.count("X")})
# print({ORIGINAL_POOL.count("Y")})
# print({ORIGINAL_POOL.count("Z")})


    # create a list (ORIGINAL_POOL) with all the given letters
    #LOOP:
        # create deep copy of ORIGINAL_POOL (GAME_POOL)
        # use random.choice(list) function to draw from pool (GAME_POOL) of letters
        # make another list for player's hand (HAND)
        # once letter is picked remove letter from pool list
        # use while loop max the letters of player's hand to 10

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass