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

# Jamie's pseudocode:
# def get_highest_word_score(word_list):
#     # sort word_list by str length
#     compare_words_list = []
#     for word in word_list:
#         word_score = score_word(word)
#         word_and_score_dict = {"word":word,"word_score":word_score}       
#         compare_words_list.append(word_and_score_dict)
        
#     winning_word = compare_words_list[0]
#     winning_word_list = []
#     for word in compare_words_list:
#         print(word)
#         if compare_words_list["word_score"]>winning_word['word_score']:
#             winning_word = word
#             winning_word_list.clear()
#             winning_word_list.append(word)
#         elif compare_words_list[word]==winning_word_list[0]:
#             winning_word_list.append(word)
# get_highest_word_score(['dog','zoo','dog','aaaaazqpoi'])

    # Emily's pseudo code:
    # So we want to look at the word_list
    # And then get the score of each word
    # Then choose the highest value
    # Also do some handling for ties
    # IF some words are tied, choose which has the shorter len
    # HOWEVER, if a word is 10 letters long, use that instead
    # If the words are the same len, then use whatever came first (maybe use index func)
# def get_highest_word_score(word_list):
#     highest_score = 0
#     winning_word = None
#     for word in word_list:
#         if score_word(word) > highest_score:
#             highest_score = score_word(word)
#             winning_word = word
#         elif score_word(word) == highest_score:
#             if (len(word) == len(winning_word)
#             or len(winning_word) == 10):
#                 continue
#             elif len(word) == 10:
#                 winning_word = word
#             elif len(word) < len(winning_word):
#                 winning_word = word
#     best_word = (winning_word, highest_score)
#     return best_word


# Bianca's notes:
# Emily's code passes all tests except one: test_get_highest_word_tie_prefers_ten_letters()
# I added line 116 ('or len(winning_word) == 10')  
# This correction helps us get past that last test