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
    2. Iterating through each key-value pair, adding the key to the list n times, with n being the associated value to the key. 
    3. Return the list.
    '''
    bag_of_letters = []
    for key, value in dict.items(): # O(k), where k = len(dict)
        new_letters = [key] * value # O(1)
        bag_of_letters.extend(new_letters) # O(n), where n = len(bag_of_letters)
    
    return bag_of_letters

def draw_letters():
    '''
    Return a list of ten randomized letters, drawn from the bag_of_letters.
    1. Create a bag_of_letters list with appropriate distribution by passing through LETTER_POOL dictionary
    2. Use the random.randint generator to select a unique integer, which represents the index of the letter to be drawn from the bag_of_letters list
    3. Repeat step #2 until, 10 letters have been randomized.
    4. Return the ten letters in a list format.
    '''
    bag_of_letters = dict_to_list(LETTER_POOL)
    hand_as_numbers = []
    hand_as_letters = []

    while len(hand_as_letters) < 10: # O(1)
        index = random.randint(0,len(bag_of_letters)-1) # O(1)
        if index not in hand_as_numbers: # O(n)
            hand_as_numbers.append(index) # O(1)
            hand_as_letters.append(bag_of_letters[index]) # O(1)
    
    return hand_as_letters


#WAVE TWO
def uses_available_letters(word, letter_bank):
    '''
    Check if the word is an anagram of some or all of the given letters in the hand
    1.Returns `True` if every letter in the `input` word is available in the `letter_bank`
    2.Returns `False` if not; if there is a letter in `input` that is not present in the `letter_bank` 
    or has too much of compared to the `letter_bank`
  
    '''
    copy_of_letter_bank = copy.deepcopy(letter_bank)
    word = word.upper()
    # O(n * k) = n? ****************************** WORK ON THIS ***************************
    for letter in word: # O(n), where n = len(word)
        try:
            copy_of_letter_bank.remove(letter) # O(k), where k = len(copy_of_letter_bank)
        except:
            return False 
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
    for letter in word.upper(): # O(n)
        score += SCORING[letter] # O(1)
        
    if 7 <= len(word) <= 10: # O(1)
        score += 8 # O(1)
    
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
    Find the highest scoring word
    1.Function looks at the list of `word_list` and calculates which of these words has the highest score.
    2.In the case of tie in scores,check if there is string with 10 characters, 
    otherwise return string with fewest characters.
    -prefer the word with the fewest letters if tie in scores 
    3.Returns a tuple that represents the data of a winning word and it's score

    '''
    words_and_scores = {}
    for word in word_list: # O(n)
        words_and_scores[word] = score_word(word) # O(1) ?
    
    highest_score = max(words_and_scores.values()) # O(n)
    highest_scoring_words = [word for word, score in words_and_scores.items() if score == highest_score] # O(n)
    winning_word = highest_scoring_words[0] # O(1)

    # worse case scenario: O(n + n + n) = O(3n) = O(n) ****************************** WORK ON THIS ***************************
    if len(highest_scoring_words) != 1:
        words_with_10 = [word for word in highest_scoring_words if len(word) == 10] # O(n)
        try:
            winning_word = words_with_10[0] # O(1)
        except:
            winning_word = min(highest_scoring_words, key=len) # O(n)
    
    return (winning_word, words_and_scores[winning_word])