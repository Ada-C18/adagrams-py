import random
def draw_letters():
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
    letter_bank = []
    tile_num_list=[]
    users_hand = []
    for letter, frequency in LETTER_POOL.items():
        string_of_one_character = letter * frequency
        tiles = list(string_of_one_character)
        letter_bank += tiles
        for i in range(frequency):
            tile_num_list.append(frequency)
        # tile_num_list=list(tile_num)
    users_hand = random.choices(letter_bank,weights=[tile_num_list],k=10)
    return users_hand


# No parameters
draw_letters()


# No parameters
draw_letters()

# The letters should be randomly drawn from a pool of letters

# This letter pool should reflect the distribution of letters as described in the table below
# 12 Es but only 1 Z, it should be 12 times as likely for the user to draw an E as a Z

# Invoking this function should not change the pool of letters
# Imagine that the user returns their hand to the pool before drawing new letters'''
# cacatenate


def uses_available_letters(word, letter_bank):
    pass
    #users_word = str
    # amount of tiles that need to be dealt back = 10 letter - users_word
    # Has two parameters:
    #     word, the first parameter, describes some input word, and is a string

    #     letter_bank, the second parameter, describes an array of drawn letters in a hand. You can expect this to be an array of ten strings, with each string representing a letter

    #     Returns either True or False

    #     Returns True if every letter in the input word is available (in the right quantities) in the letter_bank

    #     Returns False if not; if there is a letter in input that is not present in the letter_bank or has too much of compared to the letter_bank

    # word=input("You're gonna have to spell it out for me: ")
    # if


def score_word(word):
    pass


def get_highest_word_score(word_list):
    pass
