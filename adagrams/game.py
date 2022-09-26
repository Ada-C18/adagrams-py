import random
import string
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
SCORE_CHART = {
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

def draw_letters():
    count_dict = {}
    letter_list = []
    while len(letter_list) < 10:
        new_letter = (random.choice(string.ascii_uppercase))
        if new_letter in count_dict and count_dict[new_letter] < LETTER_POOL[new_letter]:
            count_dict[new_letter] += 1
            letter_list.append(new_letter)
        elif new_letter not in count_dict:
            count_dict[new_letter] = 1
            letter_list.append(new_letter)
        else:
            continue
    return letter_list

def uses_available_letters(word, letter_bank):
    upper_case_word = word.upper()
    letter_bank_count = Counter(letter_bank)
    for letter in upper_case_word:
        if letter in letter_bank_count and letter_bank_count[letter] > 0:
            letter_bank_count[letter] -= 1
            continue
        else:
            return False
    return True

def score_word(word):
    upper_case_word = word.upper()
    score_total = 0
    if len(upper_case_word) >= 7:
        score_total += 8
    for letter in upper_case_word:
        for key in SCORE_CHART:
            if letter == key:
                score_total += SCORE_CHART[key]
    return score_total
def get_highest_word_score(word_list):
    best_word = []
    for i in range(len(word_list)):
        score = score_word(word_list[i])
        if len(best_word) == 0:
            best_word.append(word_list[i])
            best_word.append(score)
        elif score > best_word[1]:
            best_word[0] = word_list[i]
            best_word[1] = score
        elif score == best_word[1]:  
            if len(best_word[0]) == len(word_list[i]) or len(best_word[0]) == 10:
                continue    
            elif len(best_word[0]) > len(word_list[i]) or len(word_list[i]) == 10:  
                best_word[0] = word_list[i] 
            elif len(best_word[0]) < len(word_list[i]):
                continue
     

    return best_word
    