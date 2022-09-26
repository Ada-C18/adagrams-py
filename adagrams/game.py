import random
from collections import Counter
def draw_letters():
    user_letter_list = []
    #changed from a constant 
    pool_of_letters = {
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
    for num in range(10):
        choice = random.choice(list(pool_of_letters.keys()))
        if pool_of_letters[choice] != 0:
            user_letter_list.append(choice)
            pool_of_letters[choice] -= 1
            if pool_of_letters[choice] == 0:
                del pool_of_letters[choice]

    return user_letter_list
    

def uses_available_letters(word, letter_bank):
    uppercase_word = word.upper()
    letter_list = [letter for letter in uppercase_word]
    freq_map = {}

    for letter in letter_bank:
        if letter in freq_map:
            freq_map[letter] += 1
        else: 
            freq_map[letter] = 1

    
    for ele in letter_list:
        if ele not in freq_map:
            return False
        if freq_map[ele] == 0:
            return False
        if ele in letter_bank:
            freq_map[ele] -= 1 
            is_word_valid = True
        else:
            return False

    return is_word_valid


def score_word(word):
    word_points = 0
    adagrams_dict = {
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
          
    word_upper = word.upper()
    letter_list = [letter for letter in word_upper]
  
    for ele in letter_list:
        if ele in adagrams_dict:
            word_points += adagrams_dict[ele]
        else:
            word_points += 0
    if len(word_upper) >= 7:
        word_points += 8

    return word_points
       

def get_highest_word_score(word_list):
    word_points = {}
    for word in word_list:
        word_points[word] = score_word(word)
    winner = max(word_points.values())
    
    # for word in word_points:
    #     if winner.count > 1:
    #         winner = min (len(word_points.key()))

    
    for key, value in word_points.items():
        if winner == value:
            return (key,value)
 

