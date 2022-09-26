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
    pass
#wave 3
def score_word(word):
    pass
# Wave 4
def get_highest_word_score(word_list):
    pass