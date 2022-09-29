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
    LETTER_SCORE = {'A': 1,'B': 3,'C': 3,'D': 2,'E': 1,'F': 4,'G': 2,'H': 4,'I': 1,'J': 8,'K': 5, 
    'L': 1,'M': 3,'N': 1,'O': 1,'P': 3,'Q': 10,'R': 1,'S': 1,'T': 1,'U': 1,'V': 4,'W': 4,'X': 8,'Y': 4,'Z':10}
    word_upper = word.upper()
    score = 0
        
    for letter in word_upper:
        if letter in LETTER_SCORE:
            score += LETTER_SCORE[letter]
    if len(word_upper) >= 7 and len(word_upper) <= 10:
            score += 8
    return score

def get_highest_word_score(word_list):
    sorted_word_list = sorted(word_list, key=len)
    score_list = []
    word_score_dict = {}
    for word in sorted_word_list:
        word_score = score_word(word)
        score_list.append(word_score)
        word_score_dict[word] = word_score

    highest_word_score = max(set(score_list))
    highest_word_dict = {}
    for word, score in word_score_dict.items():
        if score == highest_word_score:
            highest_word_dict[word] = score
    for word, score in highest_word_dict.items():
        if len(word) == 10:
            winning_tuple = (word, score)
            break
        else:
            winning_tuple = list(highest_word_dict.items())[0]
    return winning_tuple

# def get_highest_word_score(word_list):
#     word_to_score_dict = {}
#     for word in word_list:
#         word_score = score_word(word)
#         word_to_score_dict[word] = word_score
    
#     highest_scoring_word = ()

#     for word, word_score in word_to_score_dict.items():
#         highest_scoring_word = (word, word_score)
#         # by putting [1] i am accessing the score 0
#         if word_score > highest_scoring_word[1]:
#             highest_scoring_word = (word, word_score)
#             return (highest_scoring_word)
#         elif word_score == highest_scoring_word[1]:
#             if len(highest_scoring_word[0]) == 10:
#                 return highest_scoring_word
#             elif len(word) == 10:
#                 highest_scoring_word = (word, word_to_score_dict[word])
#                 return highest_scoring_word
#             elif len(highest_scoring_word[0]) <= len(word):
#                 return highest_scoring_word
#             elif len(highest_scoring_word[0]) > len(word):
#                 highest_scoring_word = (word, word_to_score_dict[word])
#                 return highest_scoring_word
#         else:
#             continue


    
    

    
