import random
def draw_letters():
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N","O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ]
    gameletters = []
    for letter in range(10):
        number = random.randint(0, 27)
        random_letter = alphabet[number]
        gameletters.append(random_letter)
    return gameletters

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass