import copy
import random
    # create a list (ORIGINAL_POOL) with all the given letters
    #LOOP:
        # create deep copy of ORIGINAL_POOL (GAME_POOL)
        # use random.choice(list) function to draw from pool (GAME_POOL) of letters
        # make another list for player's hand (HAND)
        # once letter is picked remove letter from pool list
        # use while loop max the letters of player's hand to 10

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


def uses_available_letters(word, letter_bank):
    upper_word = word.upper()
    copy_bank = copy.deepcopy(letter_bank)
    A = True

    for letter in upper_word:
        if letter in copy_bank:
            copy_bank.remove(letter)
            A = True
        else:
            A = False
    return A

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass