import random
import copy

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

SCORE_DICT = {
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

def draw_letters():

    letter_bank = []
    temp_letter_pool = copy.deepcopy(LETTER_POOL)

    while len(letter_bank) < 10:        
        letter = random.choice(list(temp_letter_pool.keys()))
        if temp_letter_pool[letter] > 0:
            temp_letter_pool[letter] -= 1
            letter_bank.append(letter)
        else:
            continue

    return letter_bank

def uses_available_letters(word, letter_bank):
    temp_letter_bank = copy.deepcopy(letter_bank)

    for letter in word:
        if letter.upper() in temp_letter_bank:
            temp_letter_bank.remove(letter.upper())
        else:
            return False
    return True

def score_word(word):
    score = 0
    
    for letter in word:
        score += SCORE_DICT.get(letter.upper())
    
    if len(word) >= 7:
        score += 8
    
    return score

def get_highest_word_score(word_list):
    highest_score = 0
    highest_word = ""
    for word in word_list:
        score_of_word = score_word(word)
        if score_of_word > highest_score:
            highest_score = score_of_word
            highest_word = word
        elif score_of_word == highest_score:
            if len(word) == 10 and len(highest_word) !=10:
                highest_score = score_of_word
                highest_word = word
            elif len(word) <len(highest_word) and len(highest_word) != 10:
                highest_score = score_of_word
                highest_word = word
        print(score_of_word)
    return tuple([highest_word, highest_score])



def get_highest_word_score_lisa_play(word_list):
    list_scores = []

    # checking for empty word_list input
    if not word_list:
        return None
    
    for word in word_list:
        word_score_dict = {}
        score_of_word = int(score_word(word))
        # populating new dict with words and score
        word_score_dict["word"] = word
        word_score_dict["score"] = score_of_word
        word_score_dict["len"] = len(word_score_dict["word"])
        list_scores.append(word_score_dict)
                 
    # print(list_scores)    
    highest_word_score = max(list_scores, key = lambda word: word["score"])
        
    print(tuple([highest_word_score["word"], highest_word_score["score"]]))
    return tuple([highest_word_score["word"], highest_word_score["score"]])

get_highest_word_score_lisa_play(["XZ", "OOOOOOOOOO"])

""" Here's what I've been working on and trying to figure out: 

    highest_score_list = []

    for word in list_scores:
        if word['score'] == highest_score:
            highest_score_list.append(word)

    if len(highest_score_list) == 1:
        return highest_score_list
    else:
        for word in highest_score_list:
            if word['len'] == 10:
                print(word['word'], word['score'])
            else: 
                smallest_len = min(highest_score_list, key = lambda word: word["len"])
                print(smallest_len['word'])
                print(smallest_len['score'])
                #print(tuple([smallest_len["word"], smallest_len["score"]]))
    

get_highest_word_score_lisa_play(["CCX", "AAAA"])




    





"""