##-----------------------------------------##
##-----------------WAVE 1------------------##
##-----------------------------------------##
"""
1. Your first task is to build a hand of 10 letters for the user. 
-No parameters
-Returns an array of ten strings
    -Each string should contain exactly one letter
    -These represent the hand of letters that the player has drawn
-The letters should be randomly drawn from a pool of letters
    -This letter pool should reflect the distribution of letters as described in the table below
    -There are only 2 available C letters, so draw_letters cannot ever return more than 2 Cs
    -Since there are 12 Es but only 1 Z, it should be 12 times as likely for the user to draw an E as a Z
-Invoking this function should not change the pool of letters
    -Imagine that the user returns their hand to the pool before drawing new letters
    reference: https://theprogrammingexpert.com/get-random-value-from-dictionary-python/
"""
import random

def draw_letters():
    # string == 1letter only
    # hand_letter == [ten strings]
    # draw_letters.random(LETTER_POOL)
    # return an array of hand_letter

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
    letters = []
    letter_frequency = {}
    for i in range(11):
        letter = random.choice(list(LETTER_POOL)) 
        if letter in letter_frequency:
            letter_frequency[letter] += 1
        else:
            letter_frequency[letter] = 1
        if letter_frequency[letter] <= LETTER_POOL[letter]:
            letters.append(letter)
    print(len(letters))
    return letters
    
    
##-----------------------------------------##
##-----------------WAVE 2------------------##
##-----------------------------------------##
"""
2. You need a way to check if an input word (a word a player submits) only uses characters that 
    are contained within a collection (or hand) of drawn letters
-Has two parameters:
    -word, the first parameter, describes some input word, and is a string
    -letter_bank, the second parameter, describes an array of drawn letters in a hand. You can expect this to be an array of ten strings,
    with each string representing a letter
-Returns either True or False
-Returns True if every letter in the input word is available (in the right quantities) in the letter_bank
-Returns False if not; if there is a letter in input that is not present in the letter_bank or has too much of compared to the letter_bank
reference: https://www.programiz.com/python-programming/methods/list/count
"""

def uses_available_letters(word, letter_bank):
<<<<<<< HEAD
    pass
#     # check input word is anagram within drawn letters   
#     for letter in word:
#         if letter in letter_bank:
#             return True
#         else:
#             return False
=======
    # ensure consistent case
    word = word.upper()
    # check input word is anagram within drawn letters
    #iterating over each letter in the word
    for letter in word:
        # check if that letter is in the letter bank
        if letter in letter_bank:
            word_count = word.count(letter)
            # if word_count is in the right quantities in the letter bank, continue checking next letter
            if word_count == letter_bank.count(letter):
                continue
            else:
                return False
        else:
            return False
>>>>>>> bfca547ebb57dced0447909d4b8a02fd2a993942

    return True







def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass