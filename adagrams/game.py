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
    pool = LETTER_POOL.copy()
    hand = []

    while len(hand) < 10:
        random_letter = random.choice(list(pool))
        avail = pool.get(random_letter)

        if avail > 0:
            hand.append(random_letter)
            pool[random_letter] -= 1
    
    return hand

def uses_available_letters(word, letter_bank):
    pass
    # for i in word:
    #     if i in letter_bank:
    #         letter_bank.remove(i)
    #     else:
    #         return False
        


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass