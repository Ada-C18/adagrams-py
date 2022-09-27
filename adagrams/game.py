import random
def draw_letters():
    POOL_OF_LETTERS = {"A" : 9,
    "B" : 2,
    "C" : 2, 
    "D" : 4, 
    "E" : 12, 
    "F" : 2, 
    "G" : 3,
    "H" : 2,
    "I" : 9,
    "J" : 1,
    "K" : 1,
    "L" : 4,
    "M" : 2,
    "N" : 6,
	"O" : 8,
	"P" : 2,
	"Q" : 1,
	"R" : 6,
	"S" : 4,
	"T" : 6,
	"U" : 4,
	"V" : 2,
	"W" : 2,
	"X" : 1,
	"Y" : 2,
	"Z" : 1}
    pool_of_letters_copy = POOL_OF_LETTERS.copy()
    just_letters = list(pool_of_letters_copy)
    hand_list = []
    while len(hand_list) < 10:
        hand = random.choice(just_letters)
        if pool_of_letters_copy[hand] >= 1:
            hand_list.append(hand)
            pool_of_letters_copy[hand] -= 1
    return hand_list

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass