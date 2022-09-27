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
    random_letters_list = random.sample(letters, counts=frequency_of_letters, k=10)
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
    word = word.upper()
    score = 0
    for letter in word:
        for k, v in LETTER_POOL_W_VALUES.items():
            if k == letter:
                score += v["value"]
    if 6 < len(word) < 11:
        score += 8
    return score






def get_highest_word_score(word_list):
    word_tuple_list = []
    highest_score = word_tuple_list[0][1]
    for word in word_list:
        score = score_word(word)
        length = len(word)
        tuple = (word, score, length)
        word_tuple_list.append(tuple)
        if tuple[1] > highest_score:
            highest_score = tuple[1]

# work in progress *******
def get_highest_word_score(word_list):
    word_tuple_list = []
    highest_score_tuple = ()

    # highest_score = word_tuple_list[0][1]

    for word in word_list:
        score = score_word(word)
        length = len(word)
        tuple = (word, score, length)
        word_tuple_list.append(tuple)
        # highest_score_tuple = tuple
        highest_score = word_tuple_list[0][1]
        if tuple[1] > highest_score:
          highest_score_tuple = tuple
          highest_score = tuple[1]
        elif tuple[1] == highest_score:
            if tuple[2] < highest_score_tuple[2]:
              highest_score_tuple = tuple
              highest_score = tuple[1]
              
    print(highest_score)
    print(highest_score_tuple)