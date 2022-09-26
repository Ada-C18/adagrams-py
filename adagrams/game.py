import random

def draw_letters():
    # return an array of ten strings
        # each str should contain exactly 1 letter
        # these represent the hand of letters that the player has drawn
    # the letters should be randomly drawn from LETTER_POOL
        # This letter pool should reflect the distribution of letters as described in the table below
        # There are only 2 available C letters, so draw_letters cannot ever return more than 2 Cs
        # Since there are 12 Es but only 1 Z, it should be 12 times as likely for the user to draw an 
        # E as a Z
    # Invoking this function should not change the pool of letters
        # Imagine that the user returns their hand to the pool before drawing new letters
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
    letters = []
    for i in range(10):
        letters.append(random.choice(list(LETTER_POOL.keys())))

    dict_letters = {}
    for letter in letters: 
        dict_letters[letter] = dict_letters.get(letter, 0) + 1
        
    for letter, counts in dict_letters.items():
        if counts > LETTER_POOL[letter]:
            print(f"not enough letters {letter}")

    return letters

def uses_available_letters(word, letter_bank):
    print("testing git")

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass