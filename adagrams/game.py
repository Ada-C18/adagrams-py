import random

def draw_letters():
    letter_dict={
        'A' : 9, 'N' : 6,
        'B' : 2, 'O' : 8,
        'C' : 2, 'P' : 2,
        'D' : 4, 'Q' : 1,
        'E' : 12, 'R' : 6,
        'F' : 2, 'S' : 4,
        'G' : 3, 'T' : 6,
        'H' : 2, 'U' : 4,
        'I' : 9, 'V' : 2,
        'J' : 1, 'W' : 2,
        'K' : 1, 'X' : 1,
        'L' : 4, 'Y' : 2,
        'M' : 2, 'Z' : 1 }
    representative_letter_list=[]
    for letter,value in letter_dict.items():
        for counter in range(value):
            representative_letter_list.append(letter)
    return_list=random.sample(representative_letter_list,k=10)
    return return_list

def uses_available_letters(word, letter_bank):
    word = word.upper()
    letter_bank_copy = letter_bank.copy()
    for letter in word:
        try:
            letter_bank_copy.remove(letter)
        except ValueError:
            return False
    return True

def score_word(word):
    letter_dict={
        'D':2,
        'G':2,
        'B':3,
        'C':3, 
        'M':3, 
        'P':3,
        'F':4,
        'H':4, 
        'V':4, 
        'W':4, 
        'Y':4,
        'K':5,
        'J':8, 
        'X':8,
        'Q':10,
        'Z':10
    }
    total=0
    word=word.upper()
    for letter in word:
        if letter >= "A" and letter <= "Z":
            if letter in letter_dict.keys():
                total+=letter_dict[letter]
            else:
                total+=1
    if len(word)>6:
        total+=8
    return total


def get_highest_word_score(word_list):
    highest_word_score = ("", 0)
    for word in word_list:
        word_score = score_word(word)
        if word_score > highest_word_score[1]:
            highest_word_score = (word, word_score)
        elif word_score == highest_word_score[1] and len(highest_word_score[0]) != 10:
            if len(word) == 10:
                highest_word_score = (word, word_score)
            elif len(word) < len(highest_word_score[0]):
                highest_word_score = (word, word_score)
    return highest_word_score 

