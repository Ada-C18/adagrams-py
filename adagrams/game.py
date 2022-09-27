import random

# DICT = {
#     "A": [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     "B": [10, 11],
#     "C": [12, 13],
#     "D": [14, 15, 16, 17],
#     "E": [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
#     "F": [30, 31],
#     "G": [32, 33, 34],
#     "H": [35, 36],
#     "I": [37, 38, 39, 40, 41, 42, 43, 44, 45],
#     "J": [46],
#     "K": [47],
#     "L": [48, 49, 50, 51],
#     "M": [52, 53],
#     "N": [54, 55, 56, 57, 58, 59],
#     "0": [60, 61, 62, 63, 64, 65, 66, 67],
#     "P": [68, 69],
#     "Q": [70],
#     "R": [71, 72, 73, 74, 75, 76],
#     "S": [77, 78, 79, 80],
#     "T": [81, 82, 83, 84, 85, 86],
#     "U": [87, 88, 89, 90],
#     "V": [91, 92],
#     "W": [93, 94],
#     "X": [95],
#     "Y": [96, 97],
#     "Z": [98]
# }


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

# def draw_letters():
#     # pick 10 letters randomly from weighted list of letters
#     # letters_avail_to_draw = dict.copy(LETTER_POOL) # shallow copy of mutable object (make sure to understand shallow vs deep copy)
#     # random.choices(population, weights=None, *, cum_weights=None, k=1)
    
#     ten_letter_hand = []
#     ten_random_nums = random.sample(range(1, 99), 10)
#     for num in ten_random_nums:
#         for k, v in DICT.items():
#             if num in v:
#                 ten_letter_hand.append(k)
#     return ten_letter_hand


# # def uses_available_letters(word, letter_bank):
#     word = word.upper()
#     for letter in word:
#         if letter not in letter_bank:
#             return False
#     letter_freq_in_bank = {}
#     for letter in letter_bank:
#         if letter not in letter_freq_in_bank:
#             letter_freq_in_bank[letter] = 1
#         else:
#             letter_freq_in_bank[letter] += 1
#     letter_freq_in_word = {}
#     for letter in word:
#         if letter not in letter_freq_in_word:
#             letter_freq_in_word[letter] = 1
#         else:
#             letter_freq_in_word[letter] += 1
#     for letter, freq in letter_freq_in_word.items():
#         if freq > letter_freq_in_bank[letter]:
#             return False
# from tests.test_wave_01 import LETTER_POOL
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

LETTER_POOL_W_VALUES = {
    'A': {
        'qty': 9, 
        'value': 1
    },
    'B': {
        'qty': 2,
        'value': 3
    },
    'C': {
        'qty': 2, 
        'value': 3
    },
    'D': {
        'qty': 4, 
        'value': 2
    },
    'E': {
        'qty': 12,
        'value': 1
    },
    'F': {
        'qty': 2, 
        'value': 4
    },
    'G': {
        'qty': 3, 
        'value': 2
    },
    'H': {
        'qty': 2, 
        'value': 4
    },
    'I': {
        'qty': 9,
        'value' :1
    },
    'J': {
        'qty': 1, 
        'value': 8
    },
    'K': {
        'qty': 1, 
        'value': 5
    },
    'L': {
        'qty': 4, 
        'value': 1
    },
    'M': {
        'qty': 2, 
        'value': 3
    },
    'N': {
        'qty': 6, 
        'value': 1
    },
    'O': {
        'qty': 8,
        'value': 1
    },
    'P': {
        'qty': 2, 
        'value': 3
    },
    'Q': {
        'qty': 1, 
        'value': 10
    },
    'R': {
        'qty': 6,
        'value': 1
    },
    'S': {
        'qty': 4, 
        'value': 1
    },
    'T': {
        'qty': 6, 
        'value': 1
    },
    'U': {
        'qty': 4, 
        'value': 1
    },
    'V': {
        'qty': 2, 
        'value': 4
    },
    'W': {
        'qty': 2, 
        'value': 4
    },
    'X': {
        'qty': 1, 
        'value': 8
    },
    'Y': {
        'qty': 2, 
        'value': 4
    },
    'Z': {
        'qty': 1,
        'value': 10
    }
}


def draw_letters():
    # aria *********
    # add letter and frequency to their own lists
    letters = []
    frequency_of_letters = []
    for letter, frequency in LETTER_POOL_W_VALUES.items():
        letters.append(letter)
        # for letter['qty']
        frequency_of_letters.append(frequency['qty'])
    # return list of 10 random letters using random.sample
    random_letters_list = random.sample(letters, counts=frequency_of_letters, k=10)
    return random_letters_list



def uses_available_letters(word, letter_bank):
    # aria *********
    # copy letter bank list
    copy_letter_bank = letter_bank.copy()
    # make string all upper
    # check to see if letter in word is in letter bank
    for letter in word.upper():
        # if letter is not in letter bank, return false
        if letter not in copy_letter_bank:
            return False
    # if letter is in letter bank, remove from letter bank 
        else: 
            copy_letter_bank.remove(letter)
    # if loop finishes and doesn't return false, all the letters are in word, return true
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
        for v in LETTER_VALUE_DICT.values():
            if letter in v["letters"]:
                score += v["value"]
    if 6 < len(word) < 11:
        score += 8
    return score






def get_highest_word_score(word_list):
    pass