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
    bank = letter_bank.copy()
    for letter in word.upper():
        if letter in bank:
            bank.remove(letter)
        else:
            return False

    return True

    
        
        


def score_word(word):

# we have a dictionary of letters corresponding to point values. 




    score_chart = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}
    score = 0
    for letter in word.upper():
        if letter in score_chart:
            score += score_chart.get(letter) #get method returns the value of specified key, values() would return a list of values
    if len(word) >= 7:
        score += 8
    return score








def get_highest_word_score(word_list):
    pass