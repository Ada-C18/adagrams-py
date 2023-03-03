import random

def draw_letters():

    letter_distribution = {
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
    ten_rand_letters = []

    while len(ten_rand_letters) < 10:
        random_letter =random.choice(list(letter_distribution.keys()))   
        
        if ten_rand_letters.count(random_letter) < letter_distribution[random_letter]:
            ten_rand_letters.append(random_letter)
    return ten_rand_letters

def uses_available_letters(word, letter_bank):

    upper_word = word.upper()
    
    for letter in upper_word:
        if letter not in letter_bank or letter_bank.count(letter) < upper_word.count(letter):
            return False
        else:
            continue
    return True

def score_word(word):

    score = 0
    letter_values = {
            ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T") : 1, 
            ("D", "G") : 2,
            ("B", "C", "M", "P") : 3,
            ("F", "H", "V", "W", "Y") :4,
            ("K") : 5,
            ("J", "X") : 8,
            ("Q", "Z") : 10
            }
    
    upper_word = word.upper()
    for letter in upper_word:
        for key in letter_values.keys():
            if letter in key:
                score += letter_values[key]

    if 7 <= len(word) <= 10:
        score += 8
    
    return score

def get_highest_word_score(word_list):
    
    highest_scoring_word = word_list[0]
    highest_score = score_word(highest_scoring_word)
    
    for word in word_list:
        word_score = score_word(word)
        if word_score < highest_score:
            continue
        elif word_score > highest_score:
            highest_scoring_word = word
            highest_score = word_score
        elif word_score == highest_score and len(highest_scoring_word) != len(word):
            if len(highest_scoring_word) == 10:
                continue
            elif len(word) == 10:
                highest_scoring_word = word
                highest_score = word_score
            elif len(word) < len(highest_scoring_word):
                highest_scoring_word = word
                highest_score = word_score

    return (highest_scoring_word, highest_score)