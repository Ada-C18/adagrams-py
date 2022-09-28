import random
from collections import defaultdict

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

def draw_letters():

    letter_list = []
    letter_freq = defaultdict(int)

    while len(letter_list) < 10:
        letter = random.choice(list(LETTER_POOL.keys()))
        if letter_freq[letter] < LETTER_POOL[letter]:
            letter_list.append(letter)

            if letter in letter_freq:
                letter_freq[letter] += 1
            else:
                letter_freq[letter] = 1

    return letter_list

def uses_available_letters(word, letter_bank):
    is_anagram = True

    copy_letter_bank = letter_bank[:]

    word = word.upper()

    for letter in word:
        if letter not in copy_letter_bank:
            is_anagram = False
        else:
            copy_letter_bank.remove(letter)
    return is_anagram

def score_word(word):
    score = 0
    word = word.upper()

    score_chart = {
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"]
    }

    for letter in word:
        for key in score_chart:
            if letter in score_chart[key]:
                score += key

    if len(word) >= 7:
        score += 8

    return score


def get_highest_word_score(word_list):
    # word_scores = []
    # for word in word_list:
    #     word_scores.append(score_word(word))
    # words_and_scores = zip(word_list, word_scores)

    word_scores_dict = {}
    max_scores_dict = {}

    for word in word_list:
        word_scores_dict[word] = score_word(word)
    
    highest_score = max(word_scores_dict.values())

    for word, score in word_scores_dict.items():
        if score == highest_score:
            max_scores_dict[word] = score

    if len(max_scores_dict) <= 1:
        for key, value in max_scores_dict.items(): 
            return key, value

    max_scores_dict_lengths = []
    for word in max_scores_dict.keys():
        max_scores_dict_lengths.append(len(word))
    shortest_max_score_word = min(max_scores_dict_lengths)

    for key, value in max_scores_dict.items(): 
        if len(key) == 10:
            return key, value

    for key, value in max_scores_dict.items():
        if len(key) == shortest_max_score_word:
                return key, value

    
