import random
import copy
#from tkinter import E

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

#WAVE ONE
def dict_to_list(dict):
    '''
    Create a list using the key-value pairs from the inputted dictionary.
    1. Start with an empty list.
    2. Add each key-value pair, add the key to the list n times, with n being the associated value to the key. 
    3. Return the list.
    '''
    bag_of_letters = []
    for key, value in dict.items():
        new_letters = [key] * value
        bag_of_letters.extend(new_letters)
    
    return bag_of_letters

def draw_letters():
    bag_of_letters = dict_to_list(LETTER_POOL)
    hand_as_numbers = []
    hand_as_letters = []
    
    # 0(n)
    while len(hand_as_letters) < 10:
        index = random.randint(0,len(bag_of_letters)-1)
        if index not in hand_as_numbers: # 0(n)
            hand_as_numbers.append(index) # n(1)
            hand_as_letters.append(bag_of_letters[index]) # n(1)
    
    return hand_as_letters


#WAVE TWO
def uses_available_letters(word, letter_bank):
    '''
    Ariam
    '''
    copy_of_letter_bank = copy.deepcopy(letter_bank)
    word = word.upper()
    # 0(n * (2n)) = O(n^2) ****************************** WORK ON THIS ***************************
    for letter in word: # O(n)
        if letter not in copy_of_letter_bank: # O(n)
            return False
        else:
            copy_of_letter_bank.remove(letter) # O(n)
    return True


#WAVE THREE
# SCORING = {
#     1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
#     2: ['D', 'G'],
#     3: ['B', 'C', 'M', 'P'],
#     4: ['F', 'H', 'V', 'W', 'Y'],
#     5: ['K'],
#     8: ['J', 'X'],
#     10: ['Q', 'Z']
# }

SCORING = {
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

def score_word(word):
    '''
    Calculate the score of the word
    1. Iterate through each character in the word, adding the associated value of each letter per the SCORING dictionary
    2. If the length of the word is 7, 8, 9, or 10, add an additional 8 points to the score
    3. Return score
    '''
    score = 0
    for letter in word.upper():
        score += SCORING[letter]
        
    if 7 <= len(word) <= 10:
        score += 8
    
    return score

    # O(n^3) ****************************** WORK ON THIS ***************************
    # for letter in word:
    #     for key, value in SCORING.items():
    #         if letter in value:
    #             score += key

    # return score


#WAVE FOUR
def get_highest_word_score(word_list):
    '''
    Ariam
    '''
    words_and_scores = {}
    # O(n)
    for word in word_list:
        words_and_scores[word] = score_word(word)
    # O(n)
    highest_score = max(words_and_scores.values())

    highest_scores = []
    # O(n)
    for word, score in words_and_scores.items():
        if score == highest_score:
            highest_scores.append(word)

    winning_word = highest_scores[0]

    # worse case scenario: O(n + n + n + n) = O(4n) = O(n) ****************************** WORK ON THIS ***************************
    if len(highest_scores) != 1:
        # tie-handling: check if there is string with 10 characters, otherwise return string with fewest characters
        # O(n)
        words_with_10 = [word for word in highest_scores if len(word) == 10]
        # O(n)
        if words_with_10:
            target_length = 10
        else:
            # O(n)
            target_length = len(min(highest_scores, key=len))

        # O(n)
        for word in highest_scores:
            if len(word) == target_length:
                winning_word = word
                break 
    
    return (winning_word, words_and_scores[winning_word])