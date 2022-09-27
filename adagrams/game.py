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
    # make for loop 
    letters = []
    for letter in LETTER_POOL:
        for num in range(LETTER_POOL[letter]):
            letters.append(letter)
    letter_weights = list(LETTER_POOL.values())

    result = []
    for i in range(10):
        letter = random.choice(letters)
        result.append(letter)
        letters.remove(letter)

    return result


def uses_available_letters(word, letter_bank):
    word = word.upper()
    letter_bank_copy = []
    for letter in letter_bank:
        letter_bank_copy.append(letter)

    for letter in word: 
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False 
    return True


def score_word(word):
    LETTER_SCORE = {
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
    word = word.upper()
    if len(word) >= 7 and len(word) <= 10:
        score += 8

    for letter in word:
        if letter in list(LETTER_SCORE.keys()):
            score += LETTER_SCORE[letter]
        
        else: 
            score += 0

    return score

def get_highest_word_score(word_list):
    high_score = 0 
    high_score_word = None
    high_score_words = []
    for word in word_list:
        if high_score < score_word(word):
            high_score = score_word(word)
            high_score_word = word

    for word in word_list:
        if score_word(word) == high_score:
            high_score_words.append(word)
    highest_word_length = 0 

    for word in high_score_words:
        if len(word) == 10:
            high_score_word = word
            return "Winner"

    word_value_dic = {}
    for word in high_score_word:
        word[word] = len(word)
        if len(word) > high_score_words:
            min(word_value_dic.values())
                return word_value_dic
            
            


        return(high_score_word , high_score)
        
