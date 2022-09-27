# Wave 1 
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

def draw_letters():
    letters = []
    all_letter_pool = []
    for letter in LETTER_POOL:
        letter_freq = LETTER_POOL[letter]
        all_letter_pool += letter * letter_freq

    for i in range(10):
        letter_choice = random.choice(all_letter_pool)
    # print(letter_choice)
        letters.append(letter_choice)
        all_letter_pool.remove(letter_choice)
    return letters

#wave 2
def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank[:]
    for letter in word.upper():
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
    if len(letter_bank) - len(word) == len(letter_bank_copy):
        return True
    return False

#wave 3
def score_word(word):
    value_1 = 1
    value_2 = 2
    value_3 = 3
    value_4 = 4
    value_5 = 5
    value_8 = 8
    value_10 = 10
    d1 = {k:value_1 for k in 'AEIOULNRST'}
    d2 = {k:value_2 for k in 'DG'}
    d3 = {k:value_3 for k in 'BCMP'}
    d4 = {k:value_4 for k in 'FHVWY'}
    d5 = {k:value_5 for k in 'K'}
    d8 = {k:value_8 for k in 'JX'}
    d10 = {k:value_10 for k in 'QZ'}
    d1.update(d2)
    d1.update(d3)
    d1.update(d4)
    d1.update(d5)
    d1.update(d8)
    d1.update(d10)
    score = 0
    for letter in word.upper():
        score += d1[letter]
    if len(word) >=7:
        score += 8
    return score

# Wave 4
def get_highest_word_score(word_list):
    scores = []
    for word in word_list:
        score = score_word(word)
        scores.append(score)
    result = list(zip(word_list, scores))
    sorted_scores_list = sorted(result, reverse = True)
    
    length_list = []
    if sorted_scores_list[0][1] == sorted_scores_list[1][1]:
        for word in word_list:
            length_list.append(len(word))
    if 10 in length_list:
        return result[length_list.index(10)]

    return sorted_scores_list[0]