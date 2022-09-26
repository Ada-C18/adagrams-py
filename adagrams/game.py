import random
letter_dict = {
"A" : 9 , "N" : 6,
"B" : 2, "O" : 8, 
"C" : 2, "P" : 2,
"D" : 4,  "Q" : 1, 
"E" : 12, "R" : 6,
"F": 2, "S" : 4,
"G" : 3, "T" : 6, 
"H" : 2, "U" : 4,
"I" : 9, "V" : 2,
"J" : 1, "W" : 2,
"K" : 1, "X" : 1,
"L" : 4, "Y" : 2,
"M" : 2, "Z" : 1 
}


def draw_letters():
    player_hand = random.choices(list(letter_dict.keys()), weights=letter_dict.values(), k=10)       
    return player_hand
    # come back and complete longer version

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    print('1')