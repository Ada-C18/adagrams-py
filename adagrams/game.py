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
    letters = []
    letter_pool_dict = LETTER_POOL.copy()
    while len(letters) < 10:
        letter = random.choice(list(letter_pool_dict.keys()))
        for key in letter_pool_dict:
            if key == letter and letter_pool_dict[key] > 0:
                letters.append(letter)
                letter_pool_dict[key] -= 1
    return letters

def uses_available_letters(word, letter_bank):
    word_list = list(word.upper())
    letter_bank_copy = letter_bank.copy()
    return_list = []
    for letter in word_list:
        if letter in letter_bank_copy:
            return_list.append(letter)
            letter_bank_copy.remove(letter)

    if word_list == return_list:
        return True
    else:
        return False

def score_word(word):
    my_dict = {
        ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'): 1,
        ('D', 'G'): 2,
        ('B', 'C', 'M', 'P'): 3,
        ('F', 'H', 'V', 'W', 'Y'): 4,
        ('K'): 5,
        ('J', 'X'): 8,
        ('Q', 'Z'): 10
    }

    word_list = list(word.upper())
    score_counter = 0

    for letter in word_list:
        for key, value in my_dict.items():
            if letter in key:
                score_counter += value
        
    if len(word_list) >= 7 and len(word_list) <= 10:
        score_counter += 8

    return score_counter

def get_highest_word_score(word_list):
    word_score_dict = {}
    for word in word_list:
        score = score_word(word)
        word_score_dict[word] = score
    highest_score = max(word_score_dict.values())
    highest_dict = {}
    for word in word_score_dict:
        if word_score_dict[word] == highest_score:
            highest_dict[word] = word_score_dict[word]
    min_len_word = min(list(highest_dict.keys()), key=len)
    for k, v in highest_dict.items():
        if len(k) == 10:
            return k, v
    for k, v in highest_dict.items():
        if k == min_len_word:
            return k, v

print(get_highest_word_score(["BBBBBB", "AAAAAAAAAA"]))