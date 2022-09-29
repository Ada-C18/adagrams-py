import copy

import random

tiles_org = ["A", "A", "A","A", "A", "A","A", "A", "A","B", "B", "C", "C", 'D', 'D', 'D', 'D', 'E', 'E','E', 'E', 'E','E', 'E', 'E','E', 'E', 'E','E', 'F', 'F', 'G', 'G', 'G', 'H', 'H', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'J', 'K', 'L', 'L', 'L', 'L', 'M', 'M', 'N', 'N', 'N', 'N', 'N', 'N', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'P', 'P', 'Q', 'R', 'R', 'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'T', 'T', 'U', 'U', 'U', 'U', 'V', 'V', 'W', 'W', 'X', 'Y', 'Y', 'Z']


def draw_letters():
    tiles = tiles_org.copy()
    hand = []

    for letter in range(10):
        tile = random.randint(0,len(tiles)-1)
        hand.append(tiles[tile])
        tiles.remove(tiles[tile])
    return hand

def uses_available_letters(word, letter_bank):
    correct_letters = []
    new_letter_bank = copy.deepcopy(letter_bank)
    word_case = word.upper() 
    for char in word_case:
        if char in new_letter_bank:
            correct_letters.append(char)
            new_letter_bank.remove(char)
        if len(word_case) == len(correct_letters):

            return True 
    else:
        return False


def score_word(word):
        tile_points = {
        'A': 1,
        'E': 1,
        'I': 1,
        'O': 1,
        'U': 1,
        'L': 1,
        'N': 1,
        'R': 1,
        'S': 1,
        'T': 1,
        'D': 2,
        'G': 2,
        'B': 3,
        'C': 3,
        'M': 3,
        'P': 3,
        'F': 4,
        'H': 4,
        'V': 4,
        'W': 4,
        'Y': 4,
        'K': 5,
        'J': 8,
        'X': 8,
        'Q': 10,
        'Z': 10
    }
        word_points = 0
        upper_word = word.upper()
        for letter in upper_word:
            if letter in tile_points:
                word_points += tile_points[letter]
        if len(upper_word) >= 7:
            word_points += 8
            
        return word_points        

def get_highest_word_score(word_list):

    score_list = []

    for word in word_list:
        score = score_word(word)
        score_list.append(score)

    highest_score_index = 0
    for index in range (len(word_list)):
        score = score_list[index]
        if score > score_list[highest_score_index]:
            highest_score_index = index

    for index in range (len(word_list)):
        score = score_list[index]
        current_word = word_list[index]
        high_score = score_list[highest_score_index]
        high_score_word = word_list[highest_score_index]
        if score == high_score and len(current_word) < len(high_score_word):
            highest_score_index = index 

    for index in range (len(word_list)):
        score = score_list[index]
        current_word = word_list[index]
        high_score = score_list[highest_score_index]
        high_score_word = word_list[highest_score_index]
        if score == high_score and len(current_word) == 10:
            highest_score_index = index

    for index in range (len(word_list)):
        score = score_list[index]
        current_word = word_list[index]
        high_score = score_list[highest_score_index]
        high_score_word = word_list[highest_score_index]
        if score == high_score and len(current_word) == len(high_score_word):
            highest_score_index = index
            word_list[0]
            break

    return [word_list[highest_score_index],score_list[highest_score_index]]
    

