from random import sample
from collections import Counter
import pprint


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

SCORE_CHART = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}

def draw_letters():
    # use random.sample to draw 10 letters from the 
    # letter bank.

    # get the lists of letter and count for each letter
    # as list (preferred by random.sample)
    letter_list = list(LETTER_POOL.keys())
    letter_count = list(LETTER_POOL.values())

    # sample draws k items from the list using counts 
    # to determine the frequency of each item. 
    # https://docs.python.org/3/library/random.html#random.sample
    # requires python version 3.9 or greater 
    this_hand = sample(letter_list, k=10, counts=letter_count)

    # print('-----------------')
    # print(this_hand)
    # print('-----------------')


    return this_hand

def uses_available_letters(word, letter_bank):
    word = word.upper()

    # create a counter for letter_bank
    letter_bank_counts = Counter()

    for letter in letter_bank:
        letter_bank_counts[letter] += 1
    # print("Loaded counter: ", letter_bank_counts)

    for letter in list(word):
        if letter_bank_counts[letter] == 0:
            return False
        else:
            letter_bank_counts[letter] -= 1
    
    return True


# print(uses_available_letters)

def score_word(word):
    score_total = 0
    extra_points = 8
    length_of_word = len(word)
    word = word.upper()

    letters_from_word = list(word)

    if 7 <= length_of_word <= 10:    
        score_total += extra_points

    for letter in letters_from_word: 
        if letter in SCORE_CHART.keys():
            score_total += SCORE_CHART[letter]

    print(score_total)

    return(score_total)
    

def get_highest_word_score(word_list):
    # iterate over the wordlist
    #   calculate score
    #   create a tuple
    #   track highest score
    #   save touples with highest score to a list

    highest_scoring_words = [(word_list[0], score_word(word_list[0]))]

    for word in word_list:
        current_score = score_word(word)
        if current_score > highest_scoring_words[0][1]:
            highest_scoring_words = [(word, current_score)]
        elif current_score == highest_scoring_words[0][1]:
            highest_scoring_words.append( (word, current_score) )


    #############################
    # Tiebreaker logic 
    #############################





    