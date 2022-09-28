from ctypes.wintypes import WORD
from operator import mul
import random

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

LETTER_VALUES = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10 
}
def draw_letters():
    letters = []
    while len(letters) < 10:
        letter = random.choice(list(LETTER_POOL.keys()))
        if letters.count(letter) < LETTER_POOL[letter]:
            letters.append(letter)
    return letters

def uses_available_letters(word, letter_bank):
    '''
    (1) read letter from word (in list) from user
    (2) read letter_bank from the output of draw_letters()
    (3) check if each letter in the letter_bank
    '''

    letters = letter_bank.copy()
    word = word.upper()
    for letter in word:
        if letter in letters:
            letters.remove(letter)
            continue
        else:
            return False
    return True

def score_word(word):
    '''
    (1) letter in word
    (2) get the value from LETTER_VALUES (in dict)
    (3) add each value to score
    '''

    score = 0
    word = word.upper()
    for letter in word:
        score += LETTER_VALUES[letter]
        
    if len(word) > 6:
        score += 8

    return score

def get_highest_word_score(word_list):
    words_with_scores = {}
    for word in word_list:
        score = score_word(word)
        words_with_scores[word] = score
    
    highest_score_word = max(words_with_scores,key=words_with_scores.get)
    high_score = words_with_scores[highest_score_word]
    print(high_score)
    # print(max_score)
    max_score_tuple = (highest_score_word, words_with_scores[highest_score_word])
    

    multiple_max_score_words = []
    for key in words_with_scores:
        if high_score == words_with_scores[key]:
            multiple_max_score_words.append(key)
    print(f"{multiple_max_score_words=}")

    if len(multiple_max_score_words) == 1:
        current_winner = max_score_tuple
    else:

        for i in range(0, len(multiple_max_score_words)):
            print((multiple_max_score_words[i]))
            print(len(multiple_max_score_words[i]))
            if len(multiple_max_score_words[i]) == 10:
                return (multiple_max_score_words[i], words_with_scores[multiple_max_score_words[i]])
                print(len(multiple_max_score_words[i]))  

            elif len(multiple_max_score_words[i-1]) < len(multiple_max_score_words[i]):
                current_winner = (multiple_max_score_words[i-1], words_with_scores[multiple_max_score_words[i-1]]) 

            else:
                current_winner = (multiple_max_score_words[i], words_with_scores[multiple_max_score_words[i]])

    return current_winner   



    # if len(multiple_max_score_words) < 2:
    #     return max_score_word
    # else:
    #     return multiple_max_score_words
    






# ### Wave 4: get_highest_word_score

# After several hands have been drawn, words have been submitted, checked, 
# scored, and played, you need a way to find the highest scoring word. This 
# function looks at the list of `word_list` and calculates which of these 
# words has the highest score, applies any tie-breaking logic, and returns 
# the winning word in a special data structure.

# Implement a function called `get_highest_word_score` in `game.py`. This method 
# should have the following properties:

# - Has one parameter: `word_list`, which is a list of strings
# - Returns a tuple that represents the data of a winning word and it's score.  
# The tuple must contain the following elements:
#   - index 0 ([0]): a string of a word
#   - index 1 ([1]): the score of that word
# - In the case of tie in scores, use these tie-breaking rules:
#     - prefer the word with the fewest letters...
#     - ...unless one word has 10 letters. If the top score is tied between 
# multiple words and one is 10 letters long, choose the one with 10 letters 
# over the one with fewer tiles
#     - If the there are multiple words that are the same score and the same 
# length, pick the first one in the supplied list


