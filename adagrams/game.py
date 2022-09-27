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
    hand = []  # renamed res to hand
    letters = []

    for k, v in LETTER_POOL.items():
        while v > 0:
            letters.append(k)
            v -= 1

    for i in range(10):  # do code below 10 times
        letter = ""  # set letter to be empty so while loop runs

        while not letter:  # check if index in our letters is used/empty, if not, get another random integer
            # hoping to get a random integer between 0 and 97
            index = random.randint(0, 97)
            letter = letters[index]

        hand.append(letter)
        letters[index] = ""

    return hand


def uses_available_letters(word, letter_bank):
    
    
    pass


def score_word(word):
    pass


def get_highest_word_score(word_list):
    pass
