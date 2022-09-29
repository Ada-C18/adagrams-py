import random

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
    letter_list = list(LETTER_POOL.keys())
    letter_count = list(LETTER_POOL.values())

    hand = random.sample(letter_list, k = 10, counts = letter_count)

    return hand

def uses_available_letters(word, letter_bank):
    word = word.upper()
    letter_frequency={}
    
    for letter in word:
        if letter in letter_frequency:
            letter_frequency[letter]+=1
        else:
            letter_frequency[letter]=1
    if letter_frequency[letter] <= letter_bank.count(letter):
        return True
    else:
        return False


def score_word(word):
    letter_vals_dict={
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}
    score=0
    word=word.upper()
    for letter in word:
        if letter in letter_vals_dict.keys():
            score+= letter_vals_dict[letter]
    if len(word)>=7:
        score+=8
            
    return score


def get_highest_word_score(word_list):
    winning_word=["", 0]
    for word in word_list:
        score= score_word(word)
        if score > winning_word[1]:
            winning_word[0]=word
            winning_word[1]=score
        elif score == winning_word[1]:
            if len(winning_word[0])==10:
                pass
            elif len(word) == 10 or len(word) < len(winning_word[0]):
                winning_word[0]= word
                winning_word[1]= score
    
    return tuple(winning_word)
            