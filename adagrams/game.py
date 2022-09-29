import random

POOL_OF_LETTERS = {
    "A" : 9,
    "B": 2,
    "C" : 2, 
    "D" : 4,
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
    "Z":1
}

def draw_letters():
    '''
    Returns a list of strings, each string contains one letter
    '''
    letter_bank = []
    all_the_letters = []
    for key,value in POOL_OF_LETTERS.items():
        for count in range(value):
            all_the_letters.append(key)
    
    while len(letter_bank) < 10:
        letter = random.choice(all_the_letters)
        letter_bank.append(letter)
        all_the_letters.remove(letter)
    return letter_bank

def uses_available_letters(word, letter_bank):
    '''
    Input: Word is user input of a word. letter_bank is a list of 10 strings (each a letter)
    Output: Returns True or False if word contains letters within letter_bank
    '''
    letter_bank_copy = letter_bank[:]
    for letter in word.upper() :
        if letter not in letter_bank_copy :
            return False
        else :
            letter_bank_copy.remove(letter)
    return True


def score_word(word):
    score_chart = {
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

    score = 0
    for letter in word.upper():
        score += score_chart[letter]

    if len(word) > 6 :
        score += 8

    return score


def get_word_score_dictionary(word_list):
    '''
    Input: word_list, which is a list of strings
    Output: dictionary of word and scores
    '''
    

def find_high_score_word_length(words_score):
    '''
    Input: dictionary of word and scores
    Output: A dictionary of all the words as keys and their length as values
    '''

def get_highest_word_score(word_list):
    '''
    Input: word_list, which is a list of strings
    Output: tuple of highest scoring word (word, score)
    '''

    words_score = {}
    return_word = []
    highest_score = 0

    for word in word_list:
        score = score_word(word)
        words_score[word] = score
    
    for word,score in words_score.items():
        if not highest_score:
            return_word = word
            highest_score = score
        elif score > highest_score:
            return_word = word
            highest_score = score
        elif score == highest_score and len(word) < len(return_word) and len(return_word) != 10:
            return_word = word
            highest_score = score
        elif score == highest_score and len(word) == 10 and len(word) != len(return_word):
            return_word = word
            highest_score = score
    return (return_word, highest_score)
    
    # highest_score = 0
    # tie_words = []
    # for word in word_list:
    #     if highest_score < score_word(word):
    #         highest_score = score_word(word)
    
    # for word in word_list:
    #     if score_word(word) == highest_score:
    #         if len(word) == 10:
    #             return (word,score_word(word))

    #         elif 
    
            

    # tie_dict = {}
    # for key,value in words_score.items():
    #     if value == highest_score:
    #         tie_dict[key] = len(key)
    # most_letters = max(tie_dict.values())
    # fewest_letters = min(tie_dict.values())

    # if most_letters == 10 :
    #     for word in tie_dict.keys():
    #         if tie_dict[word] == 10 :
    #             return (word, words_score[word])   
    # else:
    #     for word in tie_dict.keys():
    #         if tie_dict[word] == fewest_letters:
    #             return (word, words_score[word])
    # # words_score = {}
    # # for word in word_list:
    # #     score = score_word(word)
    # #     words_score[word] = score

    # # highest_score = max(words_score.values())

    # # tie_dict = {}
    # # for key,value in words_score.items():
    # #     if value == highest_score:
    # #         tie_dict[key] = len(key)
    # # print(tie_dict)
    # # most_letters = max(tie_dict.values())
    # # fewest_letters = min(tie_dict.values())

    # # if most_letters == 10 :
    # #     for word in tie_dict.keys():
    # #         if tie_dict[word] == 10 :
    # #             return (word, words_score[word])   
    # # else:
    # #     for word in tie_dict.keys():
    # #         if tie_dict[word] == fewest_letters:
    # #             return (word, words_score[word])

        
    
    
