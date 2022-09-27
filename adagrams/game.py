import random
import string
# from collections import Counter

def draw_letters():
    #create a pool for all the letters, using a list
    #import random
    # use random.choices to randomly generate 10 letters from the letter pool 
    
    # LETTER_POOL = ["A","A","A","A","A","A","A","A","A", "B","B", "C","C","D","D","D","D","E","E","E","E","E","E","E","E","E","E",
    # "E","E","F","F","G","G","G","H","H","I","I","I","I","I","I","I","I","I","J","K","L","L","L","L","M","M","N","N","N","N","N","N","O"
    # ,"O","O","O","O","O","O","O","O","P","P","Q","R","R","R","R","R","R","S","S","S","S","T","T","T","T","T","T","U","U","U","U","V","V","W","W","X","Y","Y","Z"]
    LETTER_POOL_COUNT = {
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
    hand = []
    while len(hand) < 11:
        random_letter = random.choice(string.ascii_uppercase)
        if hand.count(random_letter) < LETTER_POOL_COUNT[random_letter]:
            hand.append(random_letter)
        else:
            continue
            
    return hand

    # # random_letter = random.choice(string.ascii_uppercase)
    # random_letter = random.choice(LETTER_POOL_COUNT.keys())
    # # if random_letter in hand:
    # hand.append(random_letter)
    # if hand.count(draw_letters) > LETTER_POOL_COUNT[draw_letters]:
    #     hand.pop()

    # and hand.count(draw_letter) <= LETTER_POOL_COUNT[draw_letter]:
    #     draw_letter = random.choice(LETTER_POOL_COUNT.keys())
    #     hand.append(draw_letter)
    
    # return hand
    
    # letter_list = LETTER_POOL_COUNT.keys()
    
    # for letter in letter_list:
        
        
    #     for i in range (LETTER_POOL_COUNT[letter]):
    #         LETTER_POOL.append(letter)

    # return random.choices(LETTER_POOL_COUNT,k=10)
    
def uses_available_letters(word, letter_bank):
    word_case = word.capitalize()
    for letter in word_case:
        while letter in letter_bank:
            if word.count(letter) <= letter_bank.count(letter):
                return True
            return False
        return False


def score_word(word):
    pass
    # create the dictionary for letter in word (score_chart)
    # score is starting from 0
    # iterate over the word and add scores, value = dict["keys"]
    # check len(word) == 7, 8, 9, or 10, then score += 8 points

def get_highest_word_score(word_list):
    pass
    # word_list: stores all words user submitted
    # build a list/dict for all words & scores: {"word1" : score1; "word2" : score2; ... etc}
    # find the max value in the dict/list dict.values, append to winning_dict
    #     handling ties: len(word)==10 > smalles len(word) > len1==len2: word1 wins
    # return a tuple for the highest score words (word, score)