import random

def draw_letters():

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

    the_letters = []
    for key,value in LETTER_POOL.items():
        for i in range(value):
            the_letters.append(key)

    # use random to pick an index of the length of the_letters 
    # the element is in the list then remove it -- add it to the hand and remove it from letters

    #the_hand = [random.choice(list(the_letters)) for i in range(10)]
    # where in the letters list we are going to pull from
    the_hand = []
    for i in range(10):
        random_letter_index = random.randint(0,len(the_letters)-1)
        the_hand.append(the_letters[random_letter_index])
        the_letters.remove(the_letters[random_letter_index])


    # use random in my owm words----  
    # create a dict 
    
    
    return the_hand



def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass