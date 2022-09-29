from gzip import BadGzipFile
import random
from collections import Counter

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
    bag_of_letters = []
    letter_bank = []
    # based on the value add the letter n times to alphabet list
    for letter,value in LETTER_POOL.items():
        for i in range(value):
            bag_of_letters.append(letter)

    while len(letter_bank) != 10:
        draw = random.choice(bag_of_letters)
        letter_bank.append(draw)
        bag_of_letters.remove(draw)
    
    return letter_bank
    
    


def uses_available_letters(word, letter_bank):
    c = Counter(letter_bank)
    for char in word:
        c[char.upper()] -= 1
        if char.upper() not in letter_bank or c[char.upper()] < 0:
            return False
    return True


def score_word(word):
    point_value = [["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    ["D", "G"],
    ["B", "C", "M", "P"],
    ["F", "H", "V", "W", "Y"],
    ["K"],
    ["J", "X"],
    ["Q", "Z"]]

    if len(word) >= 7:
        total_points = 8
    else:
        total_points = 0
    #refactored above code
    #total_points = 8 if len(word) >= 7 else 0

    for letter in word.upper():
        if letter in point_value[0]:
            total_points += 1
        elif letter in point_value[1]:
            total_points += 2
        elif letter in point_value[2]:
            total_points += 3
        elif letter in point_value[3]:
            total_points += 4
        elif letter in point_value[4]:
            total_points += 5
        elif letter in point_value[5]:
            total_points += 8
        elif letter in point_value[6]:
            total_points += 10

    return total_points


def get_highest_word_score(word_list):
    highest_score = 0
    tuple_list = []
    #tie_list = []

    for word in word_list:
        tuple_list.append((word, score_word(word)))
    
    for item in tuple_list:
        if item[1] > highest_score:
            highest_score = item[1]
        if item[1] == highest_score:
            tie_list.append(item)
    
    test_length = 10
    shortest_word = ()
    for item in tie_list:
        if len(item[0]) == 10:
            return item
        elif len(item[0]) < 10:
            test_length == len(item[0])
            shortest_word = item

    for item in tuple_list:
        if tie_list:
            return shortest_word
        if item[1] == highest_score:
            return item