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

def draw_letters():
    hand = []
    while len(hand) < 10 or not hand:
        letter = random.choice(list(LETTER_POOL))
        if hand.count(letter) < LETTER_POOL[letter]:
            hand.append(letter)

    return hand

def uses_available_letters(word, letter_bank):
    # get input from user = word (string)
    # letter_bank = draw_letters()
    # return True or False
    # TRUE: if letter in letter bank and available in right qty
    # FALSE: if not in letter bank and not right qty

    # make empty list to hold each element of word

    word_list = []
    letter_bank_copy = copy.deepcopy(letter_bank)

    for each in word:
        word_list.append(each.upper())

    check_list =[]

    for letter in range(len(word_list)):
        if word_list[letter] in letter_bank_copy:
            letter_bank_copy.remove(word_list[letter])
            check_list.append(True)
        else:
            check_list.append(False)

    return all(check_list)
    

def score_word(word):
    word_list = []
    word_score=0
    score_chart={'A':1,'E':1, 'I':1, 
                 'O':1, 'U':1,'L':1, 'N':1,
                 'R':1,'S':1,'T':1, 
                 'D':2, 'G':2,
                 'B':3,
                 'C':3,'M':3,'P':3,
                 'F':4,'H':4 ,'V':4,'W':4,'Y':4,
                'K':5,
                'J':8 , 'X':8,
                'Q':10 , 'Z':10}
    for each in word:
        word_list.append(each.upper())
    for k,v in score_chart.items():
        for i in word_list:
            if i==k:
                word_score+=score_chart[k]
    if 7<=len(word_list)<=10 :
        word_score+=8
    return word_score

def get_highest_word_score(word_list):
    pass



















