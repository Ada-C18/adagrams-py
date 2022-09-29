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
    word_data_list = []
    # created a dictionary to access the data keep score and word
    for word in word_list:
        word_dic = {}
        word_dic["word"] = word
        word_dic["score"] = score_word(word)
        word_dic["length"] = len(word)
        word_data_list.append(word_dic)

    highest_score = 0 
    highest_score_words = []
    # Iterated over the dictionary to compare each string in the dictionary 
    for word_dic in word_data_list: 
        if word_dic["score"] > highest_score:
            highest_score = word_dic["score"]
            highest_score_words = [word_dic]
        elif word_dic["score"] == highest_score:
            highest_score_words.append(word_dic)
    
    if len(highest_score_words) == 1:
        return (highest_score_words[0]["word"],highest_score)
    else: 
        fewest_length = highest_score_words[0]["length"]
        fewest_length_words = []
        for dic in highest_score_words:
            if dic["length"] == 10:
                high_score_word = dic["word"]
                break
            else:
                # compare the dictionarys, length of word
                for word_dic in highest_score_words:
                    if word_dic['length'] < fewest_length:
                        fewest_length = word_dic["length"]
                        fewest_length_words = [word_dic]
                    elif word_dic["length"] == fewest_length:
                        fewest_length_words.append(word_dic)
                high_score_word = fewest_length_words[0]["word"]


        return(high_score_word, highest_score)
        
