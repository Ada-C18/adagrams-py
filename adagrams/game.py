import random
from collections import defaultdict

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

    letter_list = []
    letter_freq = defaultdict(int)

    while len(letter_list) < 10:
        letter = random.choice(list(LETTER_POOL.keys()))
        if letter_freq[letter] < LETTER_POOL[letter]:
            letter_list.append(letter)

            if letter in letter_freq:
                letter_freq[letter] += 1
            else:
                letter_freq[letter] = 1

    return letter_list

def uses_available_letters(word, letter_bank):
    is_anagram = True

    copy_letter_bank = letter_bank[:]

    word = word.upper()

    for letter in word:
        if letter not in copy_letter_bank:
            is_anagram = False
        else:
            copy_letter_bank.remove(letter)
    return is_anagram

def score_word(word):
    pass

def get_highest_word_score(word_list):
