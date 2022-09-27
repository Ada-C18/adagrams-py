import random
import string

# WAVE 1
def draw_letters():
    # 1. Create empty list variable
    hand = []
    # 2. Create dictionary of letter pool
    pool = {
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

    # 3. Use loop to keep track of # of letters in hand
    while len(hand) < 10:

        # 4. Randomly select a letter
        random_letter = random.choice(string.ascii_uppercase)

        if random_letter in hand:
            letter_count = hand.count(random_letter)
            # Check pool letter count
            # If letter quantity less than number of letters in hand
            if letter_count < pool[random_letter]:
                # append letter to list
                hand.append(random_letter)
            else:
                continue
        else:
            hand.append(random_letter)

        # If not, pick a new letter

    # 5. Return list of lists

    return hand

# WAVE 2


def uses_available_letters(word, letter_bank):
    pass


# WAVE 3
def score_word(word):
    pass


# WAVE 4
def get_highest_word_score(word_list):
    pass
