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
        letters.append(letter_choice)
        all_letter_pool.remove(letter_choice)
    return letters

#wave 2
def uses_available_letters(word, letter_bank):
    # create a copy of letter bank
    copy_bank = letter_bank[:]
    letters_used = []
    # for each letter in word, if letter is in 
    # letter bank, append letter to an empty list and 
    # remove from letter bank copy
    for letter in word.upper():
        letters_used.append(letter)
        if letter in copy_bank:
            copy_bank.remove(letter)
    # this checks that letters weren't reused 
    if len(copy_bank) == len(letter_bank) - (len(letters_used)):
        # this evaluates whether all letters used are in the letter bank
        return True
        # return all(i in letter_bank for i in letters_used)
    return False

#wave 3
def score_word(word):
    # wave 3
    d1 = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1, 'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10}

# dict = {1:'AEIOULNRST'}

# word_list = ["AAAAAAAAAA", "BBBBBB"]
# scores = []
# for word in word_list:
#     score = 0
    score = 0 
    for letter in word.upper():
        score += d1[letter]
        if len(word) >=7:
            score += 8
        
    return score
# Wave 4
def get_highest_word_score(word_list):
    pass