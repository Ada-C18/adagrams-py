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


    num_letters = []
    random_hands = []

    for letter in LETTER_POOL:
        if letter not in num_letters:
            num_letters = list(LETTER_POOL.keys())
            
    for i in range(0, len(num_letters)):
        num_letters.extend(num_letters[i] * LETTER_POOL[num_letters[i]])
    del num_letters[:26]

    # for i in range(0,10):
    #     if len(random_hands) < 10:
    #         random_letter = random.choice(num_letters)
    #         random_hands.append(random_letter)
    
    return (random.sample(num_letters,10))


def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass