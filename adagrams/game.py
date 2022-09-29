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
    #empty list to hold keys
    all_letters =[]
    #empty list to hole random letter
    letter_bank =[]
    
    for key, value in LETTER_POOL.items():
        for i in range(value):
            all_letters.append(key)
    while len(letter_bank) < 10:
        letter = random.choice(all_letters)
        letter_bank.append(letter)
        all_letters.remove(letter)
    return letter_bank
    

def uses_available_letters(word, letter_bank):
    #word is string describes some input word
#letter_bank is list of drawn leters in hand(10 string)
#if every letter in input is avilable in letter_bank return Tru
#if not letter in input in letter bank or has to much compare to letter bank return False
    upper_letter = word.upper()
    dict = {}
    for letter in letter_bank:
        # print(letter)
        if letter in dict:
            dict[letter]+=1
        dict[letter]=1
    
    for letter in upper_letter:
        if letter in dict and dict[letter] > 0:
            dict[letter] -=1
            continue
        else:
            return False

    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass