def draw_letters():
    pass

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