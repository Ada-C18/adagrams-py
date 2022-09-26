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
    letter_pool_list = []
    my_ten_letters = [] 

    for letter in LETTER_POOL:
        for num in range(0,(LETTER_POOL[letter])):
            letter_pool_list.append(letter)

    while len(my_ten_letters) < 10: 
        for num in range(0,10):
            random_letter = random.choice(letter_pool_list)
            my_ten_letters.append(random_letter)
            my_string_count = my_ten_letters.count(random_letter)
            word_pool_count = letter_pool_list.count(random_letter) 
            if my_string_count > word_pool_count:
                my_ten_letters.remove(random_letter) 

    return my_ten_letters

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass