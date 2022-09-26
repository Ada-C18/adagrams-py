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