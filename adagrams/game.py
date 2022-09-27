from collections import Counter
import random

<<<<<<< HEAD
    # return an array of ten strings
        # each str should contain exactly 1 letter
        # these represent the hand of letters that the player has drawn
    # the letters should be randomly drawn from LETTER_POOL
        # This letter pool should reflect the distribution of letters as described in the table below
        # There are only 2 available C letters, so draw_letters cannot ever return more than 2 Cs
        # Since there are 12 Es but only 1 Z, it should be 12 times as likely for the user to draw an 
        # E as a Z
    # Invoking this function should not change the pool of letters
        # Imagine that the user returns their hand to the pool before drawing new letters
=======
>>>>>>> 964e28e3cceb1c5502fb750f77eff9a68b0e2727
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
    'Z': 1,
}

LETTER_VALUES = {"A": 1,
                 "B": 3,
                 "C": 3,
                 "D": 2,
                 "E": 1,
                 "F": 4,
                 "G": 2,
                 "H": 4,
                 "I": 1,
                 "J": 1,
                 "K": 5,
                 "L": 1,
                 "M": 3,
                 "N": 1,
                 "O": 1,
                 "P": 3,
                 "Q": 10,
                 "R": 1,
                 "S": 1,
                 "T": 1,
                 "U": 1,
                 "V": 4,
                 "W": 4,
                 "X": 8,
                 "Y": 4,
                 "Z": 10,
                 "#": 0,
}


def draw_letters() -> list:
    """
    Returns a list with ten letters chosen randomly from LETTER_POOL
    """
    letter_pool_copy = LETTER_POOL.copy()
    hand = []
    while len(hand) < 10:
        letter = random.choice(list(letter_pool_copy.keys()))
        if letter_pool_copy[letter] > 0:
            hand.append(letter)
            letter_pool_copy[letter] =- 1

    return hand

