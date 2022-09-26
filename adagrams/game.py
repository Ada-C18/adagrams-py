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
    letter_list = []
    letter_count = {}
    while len(letter_list) <10:
        letter = random.choice(list(LETTER_POOL.keys())) 
        if letter not in letter_count:
            letter_count[letter] = 1
            print(letter)
            print(letter_count)
        else:
            letter_count[letter] +=1 
        if letter_count[letter] <= LETTER_POOL[letter]:
            letter_list.append(letter)
    return letter_list

def uses_available_letters(word, letter_bank):
    new_list = letter_bank.copy()
    word_upper = word.upper()
    try:
        for i in range(len(word)):
            if word_upper[i] in new_list:
                new_list.remove(word_upper[i])
            else:
                return False
            return True
    except KeyError:
        return False

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass