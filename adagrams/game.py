# from tests.test_wave_01 import LETTER_POOL
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

SCORE_CHART = {
    'A': 1,
    'E': 1, 
    'I': 1, 
    'O': 1, 
    'U': 1, 
    'L': 1, 
    'N': 1, 
    'R': 1, 
    'S': 1, 
    'T': 1,
    'D': 2, 
    'G': 2,
    'B': 3, 
    'C': 3, 
    'M': 3, 
    'P': 3,
    'F': 4, 
    'H': 4, 
    'V': 4, 
    'W': 4, 
    'Y': 4,
    'K': 5,
    'J': 8, 
    'X': 8,
    'Q': 10, 
    'Z': 10
}

def create_letter_pool_list(LETTER_POOL):
    letter_pool_list = []
    for key, value in LETTER_POOL.items():
        for i in range(value):
            letter_pool_list.append(key)
    return letter_pool_list

def draw_letters():
    hand_of_ten_letters = []
    letter_pool_list = create_letter_pool_list(LETTER_POOL)
    while len(hand_of_ten_letters) < 10:
        random_letter = random.choice(letter_pool_list)
        count = hand_of_ten_letters.count(random_letter)
        if count < LETTER_POOL[random_letter]:
            hand_of_ten_letters.append(random_letter)
    return(hand_of_ten_letters)


def uses_available_letters(word, hand_of_ten_letters):
    word = word.upper()
    for char in word:
        if word.count(char) is not hand_of_ten_letters.count(char):
            return False
    return True

def score_word(word):
    word = word.upper()
    score = 0
    for letter in word:
        score += (SCORE_CHART[letter])
    if len(word) >= 7:
        score += 8
    return(score)

def get_highest_word_score(word_list):
    pass