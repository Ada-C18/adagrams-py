from multiprocessing import pool
import random

def build_letter_pool():
    LETTER_POOL = {
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

    return LETTER_POOL


def build_available_letters_list(LETTER_POOL):
    available_letters = []

    for letter,frequency in LETTER_POOL.items():
        for i in range(frequency):
            available_letters.append(letter)

    return available_letters


def draw_letters():
    hand = []
    LETTER_POOL = build_letter_pool()
    available_letters = build_available_letters_list(LETTER_POOL)
    count_dict = {}
    
    while len(hand) < 10:
        random_letter = random.choice(available_letters)
        
        if random_letter not in hand:
            hand.append(random_letter)
            count_dict[random_letter] = 1
        elif LETTER_POOL[random_letter] > count_dict[random_letter]:
            hand.append(random_letter)
            count_dict[random_letter] += 1

    return hand


def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank.copy()
    for letter in word.upper():
        if letter not in letter_bank_copy:
            return False
        
        letter_bank_copy.remove(letter)
    
    return True


def build_score_chart():
    """
    |Letter                        | Value|
    |:----------------------------:|:----:|
    |A, E, I, O, U, L, N, R, S, T  |   1  |
    |D, G                          |   2  |
    |B, C, M, P                    |   3  |
    |F, H, V, W, Y                 |   4  |
    |K                             |   5  |
    |J, X                          |   8  |
    |Q, Z                          |   10 |
    """

    score_chart = {
        ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"): 1,
        ("D", "G"): 2,
        ("B", "C", "M", "P"): 3,
        ("F", "H", "V", "W", "Y"): 4,
        ("K"): 5,
        ("J", "X"): 8,
        ("Q", "Z"): 10
        }

    return score_chart


def score_word(word):
    score_chart = build_score_chart()
    score = 0

    if 7 <= len(word) <= 10:
        score += 8

    for letters, points in score_chart.items():
        for char in word.upper():
            if char in letters:
                score += points

    return score


def get_highest_word_score(word_list):
    highest_word_score = ("", 0)
    
    for word in word_list:
        current_word_score = (word, score_word(word))
        if current_word_score[1] > highest_word_score[1]:
            highest_word_score = current_word_score
        
        # tie breakers
        if current_word_score[1] == highest_word_score[1]:
            # if they're the same length pick the first word
            if len(current_word_score[0]) == len(highest_word_score[0]):
                continue

            # or pick the word with a length of 10
            elif len(current_word_score[0]) == 10:
                highest_word_score = current_word_score
            
            elif len(highest_word_score[0]) == 10:
                continue

            # or pick the word with the fewest letters
            elif len(current_word_score[0]) < len(highest_word_score[0]):
                highest_word_score = current_word_score
    
    return highest_word_score

