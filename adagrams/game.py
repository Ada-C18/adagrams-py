import random
LETTERS = {
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
letter_value =[
{"A,E, I, O, U, L, N, R, S, T":1},
{"D, G": 2},
{"B, C, M, P": 3},
{"F, H, V, W, Y": 4},
{"K": 5},
{"J, X": 8},
{"Q, Z": 10}
]

def draw_letters():
    letter_list = []
    freq_dict = {}
    count = 0
    while count < 10:
        letter = chr(random.randint(ord('A'), ord('Z')))
        freq_dict[letter] = freq_dict.get(letter,0)+1
    
        if freq_dict[letter] > LETTERS[letter]:
            continue
        else:
            letter_list.append(letter)
        count += 1
    return letter_list    
def uses_available_letters(word, letter_bank):
    flag =0
    char_list=[]
    for char in word.upper():
        for letter in letter_bank:
            if char==letter and char not in char_list:
                char_list.append(char)
                flag+=1
    if flag ==len(word) :
        return True
    return False                

def score_word(word):
    score =0
    
    if len(word)>=7 and len(word)<=10:
        score+=8
    for letter in letter_value:
        for key,value in letter.items():
            for char in word.upper():
                if char in key:
                    score+=value
    return score                         

def get_highest_word_score(word_list):
    score =0
    temp =[]
    for word in word_list:
        word_score = score_word(word)
        if word_score > score:
            temp =[]
            score =word_score
            temp.append(word)
        elif word_score == score:
            temp.append(word)
        
    word = temp[0]
        
    if len(temp)>1:
        for i in temp:
            if len(i)==10:
                word=i
                break 
            else:   
                word = min(temp, key=len) 
    score=score_word(word)            
    return word,score



