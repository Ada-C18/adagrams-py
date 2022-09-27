# NOTE from Dainiz: I changed this variable name so I could use letter_pool in
# draw_letters() but we can change things up if another way makes more sense to you!
import random

LETTER_DISTRIBUTION = {
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
    "Z": 1
}

SCORE_CHART = {
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],  
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"]
}

def draw_letters():
    letter_pool = []
    letter_bank = []
    for letter, count in LETTER_DISTRIBUTION.items():
        for i in range(count):
            letter_pool.append(letter)
    for letter in range(10):
        random_letter = random.choice(letter_pool)
        letter_bank.append(random_letter)
        letter_pool.remove(random_letter)
    return letter_bank

def uses_available_letters(word, letter_bank):
    bank_dict = {}
    for item in letter_bank:
        if item not in bank_dict:
            bank_dict[item] = 1
        else:
            bank_dict[item] += 1
    for letter in word.upper():
        if letter not in bank_dict.keys():
            return False
        elif letter in bank_dict.keys():
            bank_dict[letter] -= 1
        
        if bank_dict[letter] < 0:
            return False
    return True

def score_word(word):
    score = 0
    for letter in word.upper():
        # if letter in SCORE_CHART:
            # find the key that matches the letter
            # add the key to the score
        pass
    if len(word) >= 7:
        score += 8
    return score

def get_highest_word_score(word_list):
    pass