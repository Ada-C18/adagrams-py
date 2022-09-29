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
    SCORE_CHART= {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1,  
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}
    score = 0
    for letter in word.upper():
        score += SCORE_CHART[letter]
    if len(word) > 6:
        score += 8
    return score

def get_highest_word_score(word_list):
    """
    input:word_list, which is a list of strings
    output: dictionary of word and scores
    """
    words_score = {}
    for word in word_list:
        score = score_word(word)
        words_score[word] = score

    highest_score = max(words_score.values())

    tie_dictionary = {}
    for key, value in words_score.items():
        if value == highest_score:
            tie_dictionary[key] = len(key)
    
    most_letters = max(tie_dictionary.values())
    fewest_letters = min(tie_dictionary.values())

    if most_letters == 10:
        for word in tie_dictionary.keys():
            if tie_dictionary[word]== 10:
                return(word, words_score[word])
    else:
        for word in tie_dictionary.keys():
            if tie_dictionary[word] == fewest_letters:
                return(word, words_score[word])