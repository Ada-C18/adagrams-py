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
        "O ": 8,
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

        # Randomly select a letter
        random_letter = random.choice(string.ascii_uppercase)
        # print(f"Random letter: {random_letter}")

        if random_letter in hand:
            # POTENTIALLY: add dictionary with letters in hand and adding the count to the value as we go
            letter_count = hand.count(random_letter)
            # print(f"Hand letter qty: {letter_count}")

            # print(f"Pool[random_letter]: {pool[random_letter]}.")
            # print(f"Hand: {hand}")

            # Check pool letter count
            # If letter quantity less than number of letters in hand
            # FIX LOGIC HERE
            if letter_count < pool[random_letter]:
                # append letter to list
                hand.append(random_letter)
            else:
                continue
        else:
            hand.append(random_letter)

        # If not, pick a new letter

        # 5. Return list of lists
    # print(hand)
    return hand


# print(draw_letters())

# print(random.choice(string.ascii_uppercase))

# mylist = ["apple", "banana", "cherry"]
# print(random.choices(mylist, weights = [10, 1, 1], k = 14))

# WAVE 2


def uses_available_letters(word, letter_bank):
    pass


# WAVE 3
def score_word(word):
    pass


# WAVE 4
def get_highest_word_score(word_list):
    pass
