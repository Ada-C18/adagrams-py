import random
import string
from collections import Counter

def draw_letters():
    #create a pool for all the letters, using a list
    #import random
    # use random.choices to randomly generate 10 letters from the letter pool 
    LETTER_POOL_COUNT = {
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
    hand = []
    while len(hand) < 10:
        random_letter = random.choice(string.ascii_uppercase)
        if hand.count(random_letter) < LETTER_POOL_COUNT[random_letter]:
            hand.append(random_letter)
            continue
        else:
            continue
            
    return hand
    
def uses_available_letters(word, letter_bank):
    word_case = word.upper()
    letter_count_dict = Counter(letter_bank)
    for letter in word_case:
        if letter in letter_count_dict and letter_count_dict[letter] > 0:
            letter_count_dict[letter] -= 1
            continue
        else:
            return False
        
            
    return True


def score_word(word):
    pass
    # create the dictionary for letter in word (score_chart)
    # score is starting from 0
    # iterate over the word and add scores, value = dict["keys"]
    # check len(word) == 7, 8, 9, or 10, then score += 8 points

def get_highest_word_score(word_list):
    pass
    # word_list: stores all words user submitted
    # build a list/dict for all words & scores: {"word1" : score1; "word2" : score2; ... etc}
    # find the max value in the dict/list dict.values, append to winning_dict
    #     handling ties: len(word)==10 > smalles len(word) > len1==len2: word1 wins
    # return a tuple for the highest score words (word, score)