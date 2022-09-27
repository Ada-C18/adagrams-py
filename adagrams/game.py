import random
from collections import Counter
LETTER_POOL20 = {
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
def random_selection():
    values = list(LETTER_POOL20.values())
    keys = list(LETTER_POOL20.keys())
    percentages= []
    for num in values:
        percentages.append(num)
    tup = tuple(percentages)
    random_l = random.choices(keys , weights = tup)
    return ''.join(random_l)
    
def check_available(random, players_hand, LETTER_POOL20):
    if random in LETTER_POOL20:  
        if LETTER_POOL20[random] == 0:     
            return False
        else:
            LETTER_POOL20[random] -=1   
            players_hand.append(random)
            return True
def draw_letters():
    players_hand = []            
    i=0
    if all(LETTER_POOL20.values()) == 0:
        return []
    random_selection()
    available = True
    while available and len(players_hand)<10 and i <26:
        letter = random_selection()
        check_available(letter, players_hand,LETTER_POOL20)
        i +=1
    return players_hand
    

def uses_available_letters(word, letter_bank):
    list_bool = []
    word = word.upper()
    amount_bank = Counter(letter_bank)
    for letter in word:
        if letter in letter_bank and amount_bank[letter] > 0 :
            amount_bank[letter] -= 1
            list_bool.append(True)
        else:
            list_bool.append(False)
    if False in list_bool:
        return False
    else:
        return True


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass