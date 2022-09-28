import random

LETTER_POOL_W_VALUES = {
    'A': {
        'qty': 9, 
        'value': 1
    },
    'B': {
        'qty': 2,
        'value': 3
    },
    'C': {
        'qty': 2, 
        'value': 3
    },
    'D': {
        'qty': 4, 
        'value': 2
    },
    'E': {
        'qty': 12,
        'value': 1
    },
    'F': {
        'qty': 2, 
        'value': 4
    },
    'G': {
        'qty': 3, 
        'value': 2
    },
    'H': {
        'qty': 2, 
        'value': 4
    },
    'I': {
        'qty': 9,
        'value' :1
    },
    'J': {
        'qty': 1, 
        'value': 8
    },
    'K': {
        'qty': 1, 
        'value': 5
    },
    'L': {
        'qty': 4, 
        'value': 1
    },
    'M': {
        'qty': 2, 
        'value': 3
    },
    'N': {
        'qty': 6, 
        'value': 1
    },
    'O': {
        'qty': 8,
        'value': 1
    },
    'P': {
        'qty': 2, 
        'value': 3
    },
    'Q': {
        'qty': 1, 
        'value': 10
    },
    'R': {
        'qty': 6,
        'value': 1
    },
    'S': {
        'qty': 4, 
        'value': 1
    },
    'T': {
        'qty': 6, 
        'value': 1
    },
    'U': {
        'qty': 4, 
        'value': 1
    },
    'V': {
        'qty': 2, 
        'value': 4
    },
    'W': {
        'qty': 2, 
        'value': 4
    },
    'X': {
        'qty': 1, 
        'value': 8
    },
    'Y': {
        'qty': 2, 
        'value': 4
    },
    'Z': {
        'qty': 1,
        'value': 10
    }
}

def draw_letters():
    letters = []
    frequency_of_letters = []
    for letter, frequency in LETTER_POOL_W_VALUES.items():
        letters.append(letter)
        frequency_of_letters.append(frequency['qty'])
    # random.sample returns a new list containing elements from the population
    # while leaving the original population unchanged. counts controls the
    # probability of an element within the sample. in this case, the greater
    # the quantity of tiles for a letter, the higher probability that letter
    # will be part of the random sample.
    random_letters_list = random.sample(letters, counts =\
        frequency_of_letters, k = 10)
    return random_letters_list

def uses_available_letters(word, letter_bank):
    copy_letter_bank = letter_bank.copy()
    for letter in word.upper():
        if letter not in copy_letter_bank:
            return False
        else: 
            copy_letter_bank.remove(letter)
    return True

def score_word(word):
    score = 0
    for letter in word.upper():
        for k, v in LETTER_POOL_W_VALUES.items():
            if k == letter:
                score += v["value"]
    if 6 < len(word) < 11:
        score += 8
    return score

def get_highest_word_score(word_list):
    # list to store tuples
    word_tuple_list = []
    # make a tuple with word, score and length
    # append the tuples to word_tuple_list
    for word in word_list:
        score = score_word(word)
        length = len(word)
        word_tuple = (word, score, length)
        word_tuple_list.append(word_tuple)

    highest_score_tuple = (word_tuple_list[0])
    highest_score = word_tuple_list[0][1]
    shortest_word_length = word_tuple_list[0][2]

    # element[1] is score in each tuple
    # element[2] is len of each word in each tuple
    # determine highest tuple
    # loops over each tuple in word tuple list
    for element in word_tuple_list:
        if element[1] > highest_score:
            highest_score = element[1]
            highest_score_tuple = element
    # tie breaker
        elif element[1] == highest_score:
            if element[2] == 10:
                highest_score_tuple = element
                return highest_score_tuple
            elif element[2] < shortest_word_length:
                highest_score_tuple = element

    return highest_score_tuple