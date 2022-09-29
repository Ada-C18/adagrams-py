import random

def draw_letters():

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

    the_letters = []
    for key,value in LETTER_POOL.items():
        for i in range(value):
            the_letters.append(key)

    the_hand = random.sample(the_letters, 10)  
    return the_hand

def uses_available_letters(word, letter_bank):
    #copy letter_bank to track what letters are still available to use
    available_letters = [letter for letter in letter_bank]
    # check if each letter in the word is available
    for letter in word:
        # use .upper() to make sure lowercase input is still tracked
        if letter.upper() in available_letters:
            available_letters.remove(letter.upper())
        else:
            return False
    return True

def score_word(word):
    score = 0
    the_score_dict = { 1: ['A','E','I','O','U','L','N','R','S','T'],
    2 : ['D','G'],
    3 : ['B','C','M','P'],
    4: ['F','H','V','W','Y'],
    5: ['K'],
    8: ['J','X'],
    10: ['Q','Z']
    }
    
    for letter in word:
        for key, value in the_score_dict.items():
            if letter.upper() in value:
                score += key
    if len(word) >= 7:
        score += 8
    
    return score


def get_highest_word_score(word_list):
    highest_score = 0
    top_word = ""
    
    tie_list = []
    for word in word_list:
        score = score_word(word)
        if score > highest_score:
            highest_score = score
            top_word = word
    for word in word_list:
        score = score_word(word)
        if score == highest_score:
            tie_list.append(word)

    for word in tie_list:
        if len(word) == len(top_word):
            top_word = tie_list[0]
        elif len(word) == 10:
            top_word = word
        elif len(word) < len(top_word) and len(top_word) != 10:
            top_word = word

    the_winner = (top_word, highest_score)
    return the_winner

