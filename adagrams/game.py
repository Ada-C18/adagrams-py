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

    # creates a list of individual letters to draw from
    for letter, number in letter_pool_amounts.items():
        for x in range(number):
            letter_pool.append(letter)
    # draws 10 random letters and returns them as a list
    for x in range(10):
        letter_index = random.randint(0, pool_count - 1)
        drawn_letters.append(letter_pool.pop(letter_index))
        pool_count -= 1
    return drawn_letters

def uses_available_letters(word, letter_bank):
    temp_letter_bank = letter_bank.copy()
    # checks each letter in the word
    # if it's in the letter bank, removes that letter from the bank to avoid duplicate checking
    for letter in word.upper():
        if letter in temp_letter_bank:
            temp_letter_bank.remove(letter)
        else:
            return False

    return True

def score_word(word):
    # initialize score = 0
    # initialize dictionary w/ each letter's value
    # make sure word is in all caps and remove non-alphabetic characters
    # if length of word >= 7 and <= 10
    # add 8 points to score
    # iterate through all letters in word
    # look each letter up in score dict
    # add each letter's value to score
    # return score
    pass

def get_highest_word_score(word_list):
    # highest score = -1
    # shortest length = 999
    # shortest words = []
    # iterate over words in word_list
    # get word's score using score_word()
    # if score > highest score
    # highest score = score
    # if length of word < shortest length
    # shortest length = length

    # iterate over word_list again
    # if a word's score == highest score and length == 10, it wins immediately
    # else if score == highest score and length == shortest length, add word to shortest words list
    # first entry in shortest words list wins
    pass
