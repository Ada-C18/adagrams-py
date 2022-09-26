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
    pass

def get_highest_word_score(word_list):
    pass