import random

def draw_letters():
    #available letters should be in a dictionary
    available_letters = { 
        "A": 9, "B": 2, "C": 2, 
        "D" : 4, "E": 12, "F": 2,        
        "G": 3, "H": 2, "I": 9,
        "J": 1, "K": 1, "L":4,
        "M": 2, "N": 6, "O": 8,
        "P": 2, "Q": 1, "R": 6,
        "S": 4, "T": 6, "U": 4,
        "V": 2, "W":2, "X": 1,
        "Y": 2, "Z": 1
        }
    # start with an empty list of available letters to use
    hand_available = []
    # maybe the selection of the random word can go here?
    # selection = random.choice(list(available_letters.keys()))

    # iterate through the length of dictionary of letters/quantity available (key:value)
    for letter, quantity in available_letters.items():
    # randomly choose a letter in the dictionary using keys
        # selection = random.choice(list(available_letters.keys()))
        selection = random.choice(letter)
    # if the user list has < 10 letters
        if len(hand_available) < 10:
    # if the quantity of the letter is not 0 (value)
            if quantity != 0:
    # add the letter to the empty list 
                hand_available.append(selection)
    # subtract that number from the amounts available
                quantity -= 1

    return hand_available


def uses_available_letters(word, letter_bank):
    for letter in word:
        if letter in letter_bank:
            return True
        elif letter not in letter_bank or len(word) > len(letter_bank):
            return False
    
    # if every letter in the word is not in the letter_bank or
    # exceedes the len() of the letter_bank:
    # if every letter in the word is found in the letter_bank:
    # return True
    # if every letter in the word is not in the letter_bank or
    # exceedes the len() of the letter_bank:
    # return False

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass