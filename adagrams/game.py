import random
def draw_letters():
    allletters = []
    alphabet = {
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
    for letter, number in alphabet.items():
        for i in range(number):
            allletters.append(letter)
    

    gameletters = []
    for letter in range(10):
        number = random.randint(0, 27)
        random_letter = allletters[number]
        gameletters.append(random_letter)
    return gameletters

def uses_available_letters(word, letter_bank):
    new_list = []
    for letter in letter_bank:
        if letter in word:
            new_list.append(letter)
            return True 
        else:
            return False
        

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass