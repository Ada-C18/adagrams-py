import random

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
    letter_pool_list = []
    for letter, number in LETTER_POOL.items():
        letter_pool_list.extend([letter]*number)
    hand_list = []
    while len(hand_list) < 10:
        random.shuffle(letter_pool_list)
        hand_list.append(letter_pool_list.pop())
    return hand_list

def uses_available_letters(word, letter_bank):
    word = word.upper()
    new_letter_bank = []
    new_letter_bank.extend(letter_bank)
    for letter in word:
        if letter in new_letter_bank:
            new_letter_bank.remove(letter)
        else:
            return False
    return True


def score_word(word):
    word = word.upper()
    score_chart_dict = {
        "A": 1,
        "B": 3,
        "C": 3,
        "D": 2, 
        "E": 1,
        "F": 4,
        "G": 2,
        "H": 4,
        "I": 1,
        "J": 8,
        "K": 5,
        "L": 1,
        "M": 3,
        "N": 1,
        "O": 1,
        "P": 3,
        "Q": 10,
        "R": 1,
        "S": 1,
        "T": 1,
        "U": 1,
        "V": 4,
        "W": 4,
        "X": 8,
        "Y": 4,
        "Z": 10,
    }
    sum = 0
    if len(word) >= 7:
        sum += 8
    for letter in word:
        sum += score_chart_dict[letter]
    return sum

def get_highest_word_score(word_list):
    highest_score = 0
    highest_score_word = ""

    for word in word_list:
        score = score_word(word)
        if score > highest_score:
            highest_score = score
            highest_score_word = word 
        elif score == highest_score:
            if len(highest_score_word) == 10 and len(word) < len(highest_score_word):
                continue
            elif len(word) < len(highest_score_word):
                highest_score_word = word
            elif len(word) == 10:
                highest_score_word = word
    
    return (highest_score_word, highest_score)