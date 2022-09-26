import random
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
def picletterrandom():
    x = list(LETTER_POOL20.keys())
    random_element =random.choice(x)
    return random_element
def check_to_see_avail(random,LETTER_POOL20):
    for letter_key, value in LETTER_POOL20.items():
        if random == letter_key:
            if value == 0:
                return False
            else:
                LETTER_POOL20[letter_key] -= 1
                return True
def draw_letters():
    players_hand = []            

    for num in range(10):
        check = False
        while not check:
            random_letter = picletterrandom()
            
            check = check_to_see_avail(random_letter, LETTER_POOL20)
            
        players_hand.append(random_letter)
    return players_hand
    

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass