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
    
    









def uses_available_letters(word, letter_bank):
    # check input word is anagram within drawn letters
    
    # player_input = input(word)
    for letter in word:
        if letter in letter_bank and len(letter):
            return True
        else:
            return False







def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass