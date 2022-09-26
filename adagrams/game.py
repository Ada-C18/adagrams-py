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
    # Draw 10 letters
    # From the letter pool, we want to select 10 random letters
    # However, not each letter has the same chance of being pulled
    # Need to figure out a way to do letter : qty
    # random_list = []
    # for letter in LETTER_POOL
    # for frequency in letter:
    # random_list.append(letter)
    # then do a random and select from the list. Pop from the pool list and add to player_hand_list?

    # OR, do a rand from 1 - 12
    # Get all the keys that have a value equal to the rand
    # then randomly select if more than 1 key, that's your letter
    # Hmm but then how do we keep track of how many times a letter is used? Maybe update a copy of the dict
    random_list = []
    user_hand = []
    for letter in LETTER_POOL:
        for frequency in letter:
            random_list.append(letter)
    pass

def uses_available_letters(word, letter_bank):
    # We aren't here yet
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass