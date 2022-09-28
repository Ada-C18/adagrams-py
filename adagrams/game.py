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
    """
    Letter pool is a dict containing the letters and each allowed occurence
    Draw 10 chars from the letter pool randomly. DONT change the dict
    The pool is reset with each draw. 
    return an array of ten chars"""

    """
    initialize letter pool dict (helper function?)
    initialize an empty hand
    initialize an empty letter count dict

    while the hand is less than 10 chars:
        pick a random number from 1-24
        if the letter corresponding to the number is not in the hand:
            add to the hand
            add letter to count dict, dict[letter] = 1
        else the letter corresponsing to the number IS in the hand:
            check the amount of that letter in the hand against the pool rules
            if the letter has reached the maximum allowed amount:
                continue loop
            else:
                add to hand
                add count to count dict, dict[letter] += 1
    
    return hand"""

    hand = []
    LETTER_POOL = build_letter_pool()
    available_letters = build_available_letters_list(LETTER_POOL)
    count_dict = {}
    
    while len(hand) < 10:
        random_letter = random.choice(available_letters)
        if random_letter not in hand:
            hand.append(random_letter)
            count_dict[random_letter] = 1
        else:
            if LETTER_POOL[random_letter] > count_dict[random_letter]:
                hand.append(random_letter)
                count_dict[random_letter] += 1
            else:
                continue

    return hand


def uses_available_letters(word, letter_bank):
    """compare the input word to the hand. cannot change the letter bank and ignores cases
    find if the letters in word are in the letter bank in the same quantities.
    initialize letter bank copy
    for letter in word.upper()
        if letter not in letter bank copy
            return false
        if letter in letter bank copy
            remove letter from letter bank copy
        ****TO DO: handle instances of multiple letters in the word not in the letter bank better

    """
    
    letter_bank_copy = letter_bank.copy()
    for letter in word.upper():
        if letter not in letter_bank_copy:
            return False
        else:
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
    """returns an int of points
    
    initialize score chart dict (helper function)
    initialize total score to 0
    If the length of the word is 7, 8, 9, or 10, then the word gets an additional 8 points
    for letters, points in score chart.items()
        for char in word
            if char in letters:
                total_score += points
    """
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
            # if they're the same length
            if len(current_word_score[0]) == len(highest_word_score[0]):
                continue

            #if one has a length of 10
            elif len(current_word_score[0]) == 10:
                highest_word_score = current_word_score
            
            elif len(highest_word_score[0]) == 10:
                continue

            # pick the word with the fewest letters
            else:
                if len(current_word_score[0]) < len(highest_word_score[0]):
                    highest_word_score = current_word_score
    
    return highest_word_score

print(get_highest_word_score(["AAAAAAAAAA", "BBBBBB"]))

"""- In the case of tie in scores, use these tie-breaking rules:
    - prefer the word with the fewest letters...
    - ...unless one word has 10 letters. If the top score is tied between multiple words and one is 10 letters long, choose the one with 10 letters over the one with fewer tiles
    - If the there are multiple words that are the same score and the same length, pick the first one in the supplied list"""
