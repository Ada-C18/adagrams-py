import random
def draw_letters():
    distribution_of_letters = {"A" : 9, "N" : 6, "B" : 2, "O" : 8, "C" : 2, "P" : 2, "D" : 4 ,"Q" : 1, "E" : 12, "R" : 6, "F" : 2, "S" : 4, "G" : 3, "T" : 6, "H" : 2, "U" : 4, "I" : 9, "V" : 2, "J" : 1 , "W" : 2, "K" : 1, "X" : 1, "L" : 4, "Y" : 2, "M" : 2, "Z" : 1}
    letters = []
    while len(letters) < 10:
        userletters = random.choice(list(distribution_of_letters.items()))
        if userletters[1] > 0:
            letters.append(userletters[0])
            distribution_of_letters[userletters[0]]-=1
    return letters

def uses_available_letters(word, letter_bank):
    available = True
    counter = 0
    for letter in word:
        for lb in letter_bank:
            if letter == lb: 
                counter += 1
                #letter_bank.remove(lb)
    if len(word) == counter: 
            return True
    else: 
    	return False

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass