import random

def draw_letters():
    hand_letters = []
    letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O','P','Q','R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']
    for i in range(10):
        b=random.randint(0,26)
        hand_letters.append(letters[b])
    
    return hand_letters



def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass

print(draw_letters())