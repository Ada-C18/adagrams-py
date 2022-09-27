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

# score_table = {
#     ("A","E","I","O","U","L","N","R","S","T"):1,
#     ("D","G"):2,
#     ("B","C","M","P"):3,
#     ("F","H","V","W","Y"):4,
#     ("K"):5,
#     ("J","X"):8,
#     ("Q","Z"):10
# }

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
        string = (letter * frequency)
        tiles = list(string)
        random_list += tiles
    return random.sample(random_list, 10)


def uses_available_letters(word, letter_bank):
    copy_letter_bank = copy.deepcopy(letter_bank)
    word = word.upper()
    for letter in word:
        if letter in copy_letter_bank:
            copy_letter_bank.remove(letter)
        else:
            return False
    return True


def score_word(word):
    total_score = 0
    word = word.upper()
    letter_count = dict(Counter(word))
    for letter in letter_count:
        for score, letters in score_table.items():
            if letter in letters:
                total_score += score*letter_count[letter]
    if len(word) >= 7:
        total_score += 8
    return total_score


print(score_word("dog"))
# if letter in letter_count in score_table.


# score_word("dogg")
# list(dogg) ['d','o','g', 'g']

# Iterate over the letters in word, match it with the score table dict
# Add up to the sum
# Also give bonus points for length of word 7, 8, 9, or 10, then the word += 8 points
# Return everything


def get_highest_word_score(word_list):
    pass
