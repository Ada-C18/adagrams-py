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

SCORE_CHART = {
    'A':1,
    'E':1,
    'I':1,
    'O':1,
    'U':1,
    'L':1,
    'N':1,
    'R':1,
    'S':1,
    'T':1,
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
def draw_letters():

    random_hand = []

    for letter in LETTER_POOL:
        for _ in range(LETTER_POOL[letter]):
            random_hand += letter
    
    return (random.sample(random_hand,10))

def uses_available_letters(word, letter_bank):

    word_1 = word.upper()

    for letter in word_1:
        for i in letter_bank:
            if letter not in letter_bank or word_1.count(letter) > letter_bank.count(i):
                return False
    return True 

def score_word(word):
    
    # score = 0 
    word_1 = word.upper()
    total_score = 0
    scored_letter = 0 

    for letter in word_1:
        scored_letter = SCORE_CHART[letter]
        total_score += scored_letter
    if len(word_1) >= 7:
        total_score += 8
    return total_score
            
def get_highest_word_score(word_list):
    
    scored_words = {}
    for word in word_list:
        score_calculated = score_word(word)
        scored_words[word] = score_calculated

    for scores in scored_words:     
        winning_word = max(scored_words, key = scored_words.get)
        winning_score = scored_words.get(winning_word)

    tie_list=[]
    for word, score in scored_words.items():
        if winning_score == score:
            tie_list.append(word)
        
    #if we have a tie, apply tie_breaker logic
    if len(tie_list)>1:
        
        max_tie_word=max(tie_list, key=len)
        min_tie_word=min(tie_list, key=len)

        if len(max_tie_word)==len(min_tie_word):
            winning_word=tie_list[0]
        elif len(max_tie_word)==10:
            winning_word=max_tie_word
        else:
            winning_word=min_tie_word
    
    winner=(winning_word, winning_score)
    return winner