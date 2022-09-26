import random

def draw_letters():
    
    LETTER_DISTRIBUTION = {
        "A" : 9,
        "B" : 2,
        "C" : 2,
        "D" : 4,
        "E" : 12,
        "F" : 2,
        "G" : 3,
        "H" : 2,
        "I" : 9,
        "J" : 1,
        "K" : 1,
        "L" : 4,
        "M" : 2,
        "N" : 6,
        "O" : 8,
        "P" : 2,
        "Q" : 1,
        "R" : 6,
        "S" : 4,
        "T" : 6,
        "U" : 4,
        "V" : 2,
        "W" : 2,
        "X" : 1,
        "Y" : 2,
        "Z" : 1
    }

    letter_pool = []

    for key, value in LETTER_DISTRIBUTION.items():
        letter_pool += key * value
    
    user_letters = random.sample(letter_pool, k=10)

    return user_letters
    


def uses_available_letters(word, letter_bank):
    available_letters = {}

    for letter in letter_bank:
        available_letters[letter] = available_letters.get(letter, 0) + 1

    for letter in word.upper():
        if letter not in letter_bank or available_letters[letter] == 0:
            return False
        elif available_letters[letter] != 0:
            available_letters[letter] -= 1

    return True

def score_word(word):
    
    score_chart = {
        1 : ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2 : ["D", "G"],
        3 : ["B", "C", "M", "P"],
        4 : ["F", "H", "V", "W", "Y"],
        5 : ["K"],
        8 : ["J", "X"],
        10 : ["Q", "Z"]
    }

    score = 0
    for letter in word.upper():
        for key, value in score_chart.items():
            if letter in value:
                score += key

    if len(word) >= 7:
        score += 8
        
    return score

def get_highest_word_score(word_list):
    word_scores = {}
    top_scores = []
    
    for word in word_list:
        word_scores[word] = score_word(word)
    
    highest_score = max(word_scores.values())

    for word in word_scores:
        if word_scores[word] == highest_score:
            top_scores.append(word)
    
    if len(top_scores) == 1:
        return top_scores[0], highest_score
    elif len(top_scores) > 1:
        for word in top_scores:
            if len(word) == 10:
                return word, highest_score
        
        shortest_word = min(top_scores, key=len)
        return shortest_word, highest_score

