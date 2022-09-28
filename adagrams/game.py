import random
POOL_OF_LETTERS = {"A" : 9,
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
	"Z" : 1}

LETTER_POINTS= {
    "A": 1,
    "E" : 1, 
    "I" : 1,
    "O" : 1,
    "L" : 1,
    "N" : 1,
    "R" : 1,
    "S" : 1,
    "T" : 1,
    "D" : 2, 
    "G" : 2,
    "B" : 3,
    "C" : 3,
    "M" : 3,
    "P" : 3,
    "F" : 4,
    "H" : 4,
    "V" : 4,
    "W" : 4,
    "Y" : 4,
    "K" : 5,
    "J" : 8,
    "X" : 8,
    "Q" : 10,
    "Z" : 10,
    }
def draw_letters():    
    # make a copy of the dictionary so that original dictionary doesn't change
    pool_of_letters_copy = POOL_OF_LETTERS.copy()
    # taking just the keys of the dictionary (all the letters)
    just_letters = list(pool_of_letters_copy)
    # create an empty list to store the hand
    hand_list = []
    # length of the hand
    while len(hand_list) < 10:
        # use .choice to randomly select letters
        hand =random.choice(just_letters)
        # if the letter has a value more than 0 in the dictionary copy, append to the empty list
        # and decrement the value by 1 
        if pool_of_letters_copy[hand] >= 1:
            hand_list.append(hand)
            pool_of_letters_copy[hand] -= 1
    return hand_list

def uses_available_letters(word, letter_bank):
    # copy the letter bank so that original letter bank doesn't change
    letter_bank_copy =letter_bank.copy()
    # for each letter in the word (it should be uppercase so use ".upper")
    # if the letter is in the letter_bank_copy list, remove it from the letter_bank_copy
    # after checking all the letters in the word, if all the letters in the word are in the letter_bank_copy
    # return "True"
    for letter in word.upper():
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False    
    return True
    
def score_word(word):
    score = 0
    for letter in word:
        score += LETTER_POINTS[letter.upper()]
    if len(word) >= 7:
        score += 8
    return score

def get_highest_word_score(word_list):
    highest_score = 0
    highest_word = ()
    for word in word_list:
        if score_word(word) == highest_score:
            if len(highest_word) == 10:
                continue
            elif len(word) == 10 or len(word) < len(highest_word):
                highest_word = word
        else:         
            if score_word(word) > highest_score:
                highest_score = score_word(word)
                highest_word = word
            
    return (highest_word, highest_score) 