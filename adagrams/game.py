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
    letter_list = list(LETTER_POOL.keys())
    letter_count = list(LETTER_POOL.values())

    hand = random.sample(letter_list, k = 10, counts = letter_count)

    return hand

def uses_available_letters(word, letter_bank):
    letter_frequency={}
    
    for letter in word:
        #if letter.upper() or letter.lower():
            if letter in letter_frequency:
                letter_frequency[letter]+=1
            else:
                letter_frequency[letter]=1
    if letter_frequency[letter] <= letter_bank.count(letter):
        return True
    else:
        return False



def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass