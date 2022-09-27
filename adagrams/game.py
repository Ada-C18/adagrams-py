import random

DICT = {
    "A": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "B": [10, 11],
    "C": [12, 13],
    "D": [14, 15, 16, 17],
    "E": [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
    "F": [30, 31],
    "G": [32, 33, 34],
    "H": [35, 36],
    "I": [37, 38, 39, 40, 41, 42, 43, 44, 45],
    "J": [46],
    "K": [47],
    "L": [48, 49, 50, 51],
    "M": [52, 53],
    "N": [54, 55, 56, 57, 58, 59],
    "0": [60, 61, 62, 63, 64, 65, 66, 67],
    "P": [68, 69],
    "Q": [70],
    "R": [71, 72, 73, 74, 75, 76],
    "S": [77, 78, 79, 80],
    "T": [81, 82, 83, 84, 85, 86],
    "U": [87, 88, 89, 90],
    "V": [91, 92],
    "W": [93, 94],
    "X": [95],
    "Y": [96, 97],
    "Z": [98]
}


# WEIGHTED_LETTER_DICT = {
#     "qty 1": ["J", "K", "Q", "X", "Z"],
#     "qty 2": ["B", "C", "F", "H", "M", "P", "V", "W", "Y"],
#     "qty 3": ["G"],
#     "qty 4": ["D", "L", "S", "U"],
#     "qty 6": ["N", "R", "T"],
#     "qty 8": ["O"],
#     "qty 9": ["A", "I"],
#     "qty 12": ["E"]
#     }

    # weights = [6, 18, 3, 16, 18, 8, 18, 13]

def draw_letters():
    # pick 10 letters randomly from weighted list of letters
    # letters_avail_to_draw = dict.copy(LETTER_POOL) # shallow copy of mutable object (make sure to understand shallow vs deep copy)
    # random.choices(population, weights=None, *, cum_weights=None, k=1)
    
    ten_letter_hand = []
    ten_random_nums = random.sample(range(1, 99), 10)
    for num in ten_random_nums:
        for k, v in DICT.items():
            if num in v:
                ten_letter_hand.append(k)
    return ten_letter_hand


def uses_available_letters(word, letter_bank):
    word = word.upper()
    for letter in word:
        if letter not in letter_bank:
            return False
    letter_freq_in_bank = {}
    for letter in letter_bank:
        if letter not in letter_freq_in_bank:
            letter_freq_in_bank[letter] = 1
        else:
            letter_freq_in_bank[letter] += 1
    letter_freq_in_word = {}
    for letter in word:
        if letter not in letter_freq_in_word:
            letter_freq_in_word[letter] = 1
        else:
            letter_freq_in_word[letter] += 1
    for letter, freq in letter_freq_in_word.items():
        if freq > letter_freq_in_bank[letter]:
            return False
    return True

def score_word(word):
    # can we combine this dict with the contacts dict?
    LETTER_VALUE_DICT = {
        "value 1 letters": {
            "value": 1,
            "letters": ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
        },
        "value 2 letters": {
            "value": 2,
            "letters" :["D", "G"]
        },
        "value 3 letters": {
            "value": 3,
            "letters": ["B", "C", "M", "P"]
        },
        "value 4 letters": {
            "value": 4,
            "letters": ["F", "H", "V", "W", "Y"]
        },
        "value 5 letters": {
            "value": 5,
            "letters": ["K"]
        },
        "value 8 letters": {
            "value": 8,
            "letters": ["J", "X"]
        },
        "value 10 letters": {
            "value": 10,
            "letters": ["Q", "Z"],
        }
    }
    word = word.upper()
    score = 0
    for letter in word:
        for k, v in LETTER_VALUE_DICT.items():
            if letter in v["letters"]:
                score += v["value"]
    if 6 < len(word) < 11:
        score += 8
    return score



def get_highest_word_score(word_list):
    pass