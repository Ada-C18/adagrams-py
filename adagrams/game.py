import random

def draw_letters():
    pool_count = 98 # number of letters in pool overall
    drawn_letters = []
    letter_pool = [] # list of letters available draw from
    letter_pool_amounts = {
        'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12,
        'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1,
        'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8,
        'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6,
        'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
    }

    # iterate through letter_pool_amounts keys and values
    for letter, number in letter_pool_amounts.items():
    # for each key, add it [value] number of times to letter_pool list
        for value in range(number):
            letter_pool.append(letter)
    # use random.randint w/ index 10 times to draw 10 random letters
    for value in range(10):
        letter_index = random.randint(0, pool_count - 1)
        chosen_letter = letter_pool.pop(letter_index)
        drawn_letters.append(chosen_letter)
        pool_count -= 1
    return drawn_letters

def uses_available_letters(word, letter_bank):
    # make sure word is in all caps
    # make a copy of letter bank
    # iterate through letters in word
    # for each letter, check if it's in the letter bank
    # if so, remove that letter from the bank
    # if not, return false
    # after all letters have been checked, return true

def score_word(word):
    # initialize score = 0
    # initialize dictionary w/ each letter's value
    # make sure word is in all caps
    # remove non-alphabetic characters
    # iterate through all letters in word
    # look each letter up in score dict
    # add each letter's value to score
    # return score

def get_highest_word_score(word_list):
    pass
