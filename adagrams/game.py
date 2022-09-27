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
    one_point = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u", "L", "l", "N", "n", "R", "r", "S", "s", "T", "t"]
    two_point = ["D", "d", "G", "g"]
    three_point = ["B", "b", "C", "c", "M", "m", "P", "p"]
    four_point = ["F", "f", "H", "h", "V", "v", "W", "w", "Y", "y"]
    five_point = ["k", "K"]
    eight_point = ["J", "j", "X", "x"]
    ten_point = ["Q", "q", "Z", "z"]

    points = 0

    for letter in word:
        if letter in one_point:
            points += 1
        elif letter in two_point:
            points += 2
        elif letter in three_point:
            points += 3
        elif letter in four_point:
            points += 4
        elif letter in five_point:
            points += 5
        elif letter in eight_point:
            points += 8
        elif letter in ten_point:
            points += 10
        else:
            points += 0

    if len(word) > 6:
        points += 8
    return points


def get_highest_word_score(word_list):
    