def draw_letters():
    import random
    # create letter pool
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
    # create temporary letter pool for selection process
    draw_pool = []
    for letter, frequency in LETTER_POOL.items():
        for i in range(frequency):
          draw_pool.append(letter)
    # randomly draw 10 from temp letter pool and assign to hand 
    hand = []
    for i in range(10):
        piece = random.randint(0,len(draw_pool)-1)
        selection = draw_pool[piece]
        hand.append(selection)
        draw_pool.remove(selection)
    return hand

def uses_available_letters(word, letter_bank):
 
    new_word = word.upper()
    copy_bank = letter_bank.copy()
    
    for letter in new_word:
        
      if letter in copy_bank:
        copy_bank.remove(letter)
      else: 
        return False
    return True





def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass 
