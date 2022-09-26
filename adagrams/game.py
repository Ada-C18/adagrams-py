import random
import string

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
    letter_list=[letter for letter in string.ascii_uppercase]
    representative_letter_list=[]
    for chara in letter_list:
        for counter in range(letter_dict[chara]):
            representative_letter_list.append(chara)
    return_list=[]
    for count in range(10):
        return_list.append(representative_letter_list.pop(random.randint(0,len(representative_letter_list)-1)))
    return return_list

def uses_available_letters(word, letter_bank):
    pass

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
    for chara in word:
        if ord(chara)>64 and ord(chara)<91:
            try:
                total+=letter_dict[chara]
            except:
                total+=1
        else:
            continue
    if len(word)>6:
        total+=8
    return total

def get_highest_word_score(word_list):
    pass