import random
# import string


random_letter = ['s', 't', 'o', 's', 't', 'o', 's', 't', 'o', 'm', 'p', 'u']
LETTER_POOL = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 
    'E': 12, 'F': 2, 'G': 3, 'H': 2, 
    'I': 9, 'J': 1, 'K': 1, 'L': 4, 
    'M': 2, 'N': 6, 'O': 8, 'P': 2, 
    'Q': 1, 'R': 6, 'S': 4, 'T': 6, 
    'U': 4, 'V': 2, 'W': 2, 'X': 1, 
    'Y': 2, 'Z': 1
}


def build_letter_pool_list():
    letter_pool_list = []
    for key, value in LETTER_POOL.items():
        letter_pool_list.extend(list(key * value))
    return letter_pool_list



def draw_letters():
    random_letter = build_letter_pool_list()
    letter = [] 
    while len(letter) < 10:
       random_index = random.randint(0, len(random_letter)-1)
       letter.append(random_letter.pop(random_index))

    return letter
    





# print(draw_letters(random_letter))
    







def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass