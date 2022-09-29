import random
def draw_letters():
    LETTER_POOL = {
        "A": 9,
        "B": 2,
        "C": 2,
        "D": 4,
        "E": 12,
        "F": 2,
        "G": 3,
        "H": 2,
        "I": 9,
        "J": 1,
        "K": 1,
        "L": 4,
        "M": 2,
        "N": 6,
        "O": 8,
        "P": 2,
        "Q": 1,
        "R": 6,
        "S": 4,
        "T": 6,
        "U": 4,
        "V": 2,
        "W": 2,
        "X": 1,
        "Y": 2,
        "Z": 1,
    }
    letter_list = []
    pool_list = []
    i = 0
    for letter in LETTER_POOL.keys():
        for i in range(LETTER_POOL[letter]):
            pool_list.append(letter)
    letter_list = random.sample(pool_list, 10)
    return letter_list

def uses_available_letters(word, letter_bank):
    pass
    letter_bank_copy = letter_bank.copy()
    word = word.upper()
    for letter in word:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False 
    return True

def score_word(word):
    pass

    SCORE_CHART = {
        "A": 1,
        "B": 3,
        "C": 3,
        "D": 2,
        "E": 1,
        "F": 4,
        "G": 2,
        "H": 4,
        "I": 1,
        "J": 8,
        "K": 5,
        "L": 1,
        "M": 3,
        "N": 1,
        "O": 1,
        "P": 3,
        "Q": 10,
        "R": 1,
        "S": 1,
        "T": 1,
        "U": 1,
        "V": 4,
        "W": 4,
        "X": 8,
        "Y": 4,
        "Z": 10,
    }
    word = word.upper()
    score = 0

    if len(word) >=7 and len(word)<=10:
            score += 8  
    for letter in word:
         for key in SCORE_CHART:
                if letter == key:
                    score += SCORE_CHART[key]
    return score

def get_highest_word_score(word_list):
    
    score_dict = {}
    for word in word_list:
        score_dict[word.upper()] = score_word(word)
    #list comprehension to score max keys to a list
    max_keys = [key for key, value in score_dict.items() if value == max(score_dict.values())]
   
    if len(max_keys)>1:#if there's a tie 
            for word in max_keys: #loop through to check length
                if len(word)==10: #if word has 10 letters
                    return word,score_dict[word] #return word with 10 letters
            return min(max_keys, key=len),score_dict[min(max_keys, key=len)] #return shortest word
    return max_keys[0], score_dict[max_keys[0]]