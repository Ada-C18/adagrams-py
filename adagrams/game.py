from audioop import add
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
    # find way to use range in for loop to iterate 10 times
    letters = []
        
    for i in range(11):
        random_letter = random.choice(list(LETTER_POOL.keys()))
        # print(f"RL: {random_letter}")
        
        if letters.count(random_letter) < LETTER_POOL[random_letter]:
            letters.append(random_letter)
            # print("letter count: ", letters.count(random_letter), "\n")

    return letters



def uses_available_letters(word, letter_bank):
    pass

#   Check if word is in random 10 letter list (Helper Funct)
#       - it ignores letter case
#   Make sure that each letter is only used as many times as
#       it appears on the list of random letters.

#   Returns True or False



def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass