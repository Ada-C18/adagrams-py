import random

def draw_letters():
    letter_distribution = {
        "A" : 9, 	"N" : 6,
        "B" : 2, 	"O" : 8,
        "C" : 2, 	"P" : 2,
        "D" : 4, 	"Q" : 1,
        "E" : 12,	"R" : 6,
        "F" : 2, 	"S" : 4,
        "G" : 3, 	"T" : 6,
        "H" : 2, 	"U" : 4,
        "I" : 9, 	"V" : 2,
        "J" : 1, 	"W" : 2,
        "K" : 1, 	"X" : 1,
        "L" : 4, 	"Y" : 2,
        "M" : 2, 	"Z" : 1, 
    }
    all_letters = []
    
    for letter in letter_distribution:
        for i in range(letter_distribution[letter]):
            all_letters.append(letter)
    random_letters = []
    for i in range(10):
        random_letter = random.choice(all_letters)
        all_letters.remove(random_letter)
        random_letters.append(random_letter)


    return random_letters
    
    
    




def uses_available_letters(word, letter_bank):
    copy_bank = letter_bank.copy()
    for letter in word:
        letter = letter.upper()
        try:
            copy_bank.remove(letter)
        except:
            return False
    return True
    

def score_word(word):
    letter_score = {
        "A" : 1, 	"N" : 1,
        "B" : 3, 	"O" : 1,
        "C" : 3, 	"P" : 3,
        "D" : 2, 	"Q" : 10,
        "E" : 1,	"R" : 1,
        "F" : 4, 	"S" : 1,
        "G" : 2, 	"T" : 1,
        "H" : 4, 	"U" : 1,
        "I" : 1, 	"V" : 4,
        "J" : 8, 	"W" : 4,
        "K" : 5, 	"X" : 8,
        "L" : 1, 	"Y" : 4,
        "M" : 3, 	"Z" : 10, 
    }
    total = 0
    for letter in word:
        letter = letter.upper()
        total += letter_score[letter]
    if len(word) == 0:
            return total
    elif len(word) >= 7 and len(word) <= 10:
        total += 8
    return total
   
        
    

def get_highest_word_score(word_list):
    words_with_scores = []
    highest_score = 0
    for word in word_list:
        if score_word(word) > highest_score:
            highest_score = score_word(word)
            words_with_scores.append(word)
            if len(word) == 10:
                return ([word,highest_score])

    return ([word,highest_score])
    