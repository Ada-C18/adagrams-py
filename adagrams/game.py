import random
import copy
from collections import Counter

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


score_table = {
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"]
}


def draw_letters():
    random_list = []
    for letter, frequency in LETTER_POOL.items():
        random_list += list(letter * frequency)
    return random.sample(random_list, 10)


def uses_available_letters(word, letter_bank):
    letter_bank_copy = copy.deepcopy(letter_bank)
    for letter in word.upper():
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
    return True


def score_word(word):
    total_score = 0
    letter_freq = dict(Counter(word.upper()))
    for letter in letter_freq:
        for score, letters in score_table.items():
            if letter in letters:
                total_score += score * letter_freq[letter]
    if len(word) >= 7:
        total_score += 8
    return total_score


def get_highest_word_score(word_list):
    highest_score = 0
    winning_word = None
    for word in word_list:
        if score_word(word) > highest_score:
            highest_score = score_word(word)
            winning_word = word
        elif score_word(word) == highest_score:
            if (len(word) == len(winning_word)
            or len(winning_word) == 10):
                continue
            elif len(word) == 10:
                winning_word = word
            elif len(word) < len(winning_word):
                winning_word = word
    best_word = (winning_word, highest_score)
    return best_word