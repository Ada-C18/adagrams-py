import random


def draw_letters():

    # Create empty list
    # Create empty counter dictionary
    # Use for loop i in range(10)
    # Use a built in funciton to draw random letter random.choice()
    #
    # Use if statement to check if random letter is not drawn more
    # than dict value comparing values from counter dict
    # Append to empty list
    # Return list of 10 letters(strings)
    LETTER_POOL = {
        "A": 9,
        "B": 2,
        "C": 2,
        "D": 4,
        "E": 12,
        "F": 2,
        "G": 3,
        "H": 2,
        "I": 9,
        "J": 1,
        "K": 1,
        "L": 4,
        "M": 2,
        "N": 6,
        "O": 8,
        "P": 2,
        "Q": 1,
        "R": 6,
        "S": 4,
        "T": 6,
        "U": 4,
        "V": 2,
        "W": 2,
        "X": 1,
        "Y": 2,
        "Z": 1,
    }
    letter_list = []
    pool_list = []
    i = 0
    for letter in LETTER_POOL.keys():
        for i in range(LETTER_POOL[letter]):
            pool_list.append(letter)
    letter_list = random.sample(pool_list, 10)
    print(letter_list)

    return letter_list


def uses_available_letters(word, letter_bank):
    pass


def score_word(word):
    pass


def get_highest_word_score(word_list):
    pass
