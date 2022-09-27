import random
import string


# WAVE 1
def draw_letters():
    hand = []

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

    while len(hand) < 10:
        random_letter = random.choice(string.ascii_uppercase)

        if random_letter in hand:
            letter_count = hand.count(random_letter)

            if letter_count < pool[random_letter]:
                # append letter to list
                hand.append(random_letter)
            else:
                continue
        else:
            hand.append(random_letter)
    return hand


# WAVE 2
def uses_available_letters(word, letter_bank):
    # 1. Turn letter_bank into a dict (letter: frq)
    word_dict = {}
    letter_bank_dict = {}

    for letter in letter_bank:
        letter_bank_dict[letter] = letter_bank.count(letter)

    # 2. Turn word into dict (letter: frq)
    word = word.upper()

    for letter in word:
        word_dict[letter] = word.count(letter)
        if letter not in letter_bank_dict:
            return False

    # 3. Create a for loop to compare freq
    for letter, freq in word_dict.items():
        if freq <= letter_bank_dict[letter]:
            return True
        else:
            return False


# WAVE 3
def score_word(word):
    pass


# WAVE 4
def get_highest_word_score(word_list):
    pass
