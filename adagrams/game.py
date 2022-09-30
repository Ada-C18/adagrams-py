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
    'Z': 10,
}
def draw_letters():
    letter_list = []
    hand = []

    for letter in LETTER_POOL.keys():
        for num in range(LETTER_POOL[letter]):
            letter_list.append(letter)
    
    for draw in range(10):
        index = random.randint(0, (len(letter_list) -1))
        hand.append(letter_list[index])
        letter_list.pop(index)

    return hand

def uses_available_letters(word, letter_bank):
    formatted_word = word.upper()
    for letter in formatted_word:
        if formatted_word.count(letter) > letter_bank.count(letter):
            return False
        if letter not in letter_bank:
            return False
    return True

def score_word(word):
    formatted_word = word.upper()
    score = 0

    for letter in formatted_word:
        score += SCORE_CHART[letter]
    
    if len(word) >= 7:
        score += 8
    
    return score

def get_highest_word_score(word_list):
    pass