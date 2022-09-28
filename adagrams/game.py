import random

def draw_letters():
    letter_dict = {
                "A" : 9 , "N" : 6, "B" : 2, "O" : 8, "C" : 2, "P" : 2, "D" : 4, "Q" : 1,
                "E" : 12, "R" : 6, "F": 2, "S" : 4, "G" : 3, "T" : 6, "H" : 2, "U" : 4,
                "I" : 9, "V" : 2, "J" : 1, "W" : 2, "K" : 1, "X" : 1, "L" : 4, "Y" : 2,
                "M" : 2, "Z" : 1 
                }     
    letter_pool = []
    for letter in letter_dict:
        letter_pool += list(letter) * letter_dict[letter]
    
    player_hand = []
    while len(player_hand) < 10:
        letter = random.choice(letter_pool) 
        if player_hand.count(letter) < letter_pool.count(letter):
            player_hand += letter
    
    return player_hand

def uses_available_letters(word, letter_bank):
    letters = letter_bank.copy()
    for letter in word.upper():
        if letter not in letters:
            return False
        letters.remove(letter)
    return True          

def score_word(word):
    letter_scores = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1,
                     'R': 1, 'S': 1, 'T': 1, 'D': 2, 'G': 2, 'B': 3, 'C': 3,
                     'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
                     'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10
                     }
    total_points = 0
    for letter in word:
        points = letter_scores[letter]
        total_points = total_points + points
    
    return total_points

def get_highest_word_score(word_list):
    # scores = [(word, score_word(word)) for word in word_list]
    # return max(scores)[1]
