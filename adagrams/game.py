<<<<<<< HEAD
import sys
from adagrams.ui_helper import *
from adagrams.game import draw_letters, uses_available_letters, score_word, get_highest_word_score
import random

from tests.test_wave_01 import LETTER_POOL
import random

def draw_letters():
    p=[]
    g=[]
    for key, value in LETTER_POOL.items():
        t=key*value
        g.append(t)
    #print(g)
    for i in range(len(g)):
        for j in g[i]:
            p.append(g[i][0])
    #print(p)
    draw_letters=(random.sample(p,10))
    
    return draw_letters   
    
=======
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
    # hand = ["B", "B"]
    hand = []
    while len(hand) < 10 or not hand:
        letter = random.choice(list(LETTER_POOL))
        # letter = 'B'
        if hand.count(letter) < LETTER_POOL[letter]:
            hand.append(letter)

    return hand
>>>>>>> 787b57a1f7b9a9f6d5e5d079e1cda7e9cd722d84

def uses_available_letters(word, letter_bank):
    letter_bank=draw_letters()
    word_list=[]
    for each in word:
        alphas=each
        word_list.append(alphas)
    
    if all(item in word_list for item in letter_bank ):
        return True
    else:
        return False
    
    
    
    
    
    

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass