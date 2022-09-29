from tests.test_wave_01 import LETTER_POOL
import random


def draw_letters():
    #returns: ["a", "b", "c", ...] player's hand
    #letter doesn't change
    #can't have more than the alloted number of a letter

    #initialize empty list
    result_list = []
    #set up dictionary of letter pool
    character, frequency = random.choice(list(LETTER_POOL.items()))
    print(character, frequency)



    #a loop to check if len is under 10
        #if not
         #return result_list
draw_letters()