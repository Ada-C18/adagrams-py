from random import randint

def draw_letters():
    letter_dict = {}
    for key, value in LETTER_POOL.items():
        letter_dict[key] = value
    letter_list = []
    for k, v in LETTER_POOL.items():
        for num in range(0, LETTER_POOL[k]):
            letter_list.append(k)
    output_list = []
    while len(output_list) < 10:
        index = randint(0, len(letter_list)-1)   
        if letter_dict[letter_list[index]] == 0:
            continue
        else:
            output_list.append(letter_list[index])
            letter_dict[letter_list[index]] -= 1
    return output_list

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass

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