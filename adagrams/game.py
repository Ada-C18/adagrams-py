import random
def draw_letters():
    '''
    input: a list of letters 
    output: a list of 10 letters of strings
    ''' 
    # make letter pool which is a list of dictionaries
    # make an editable copy of the letter pool
    # set up an empty list that will hold the hand for the player
    # loop through the range 1-10
        # make a varaible that holds a random integer (1-26)
        # go into the index of editable copy of list
        # make a random integer between (1-the value) held within previous dictionary index
        # append the letter however many times that random integer dictates
    # return list 

    letter_pool = [{"A" : 9}, {"N" : 6}, {"B" : 2}, {"O" : 8}, {"C" : 2}, {"P" : 2}, {"D" : 4}, {"Q" : 1}, {"E" : 12}, {"R" : 6}, {"F" : 2}, {"S" : 4}, {"G": 3}, {"T" : 6}, {"H" : 2}, {"U" : 4}, {"I" : 9},  {"V" : 2}, {"J" : 1}, {"W" : 2}, {"K" : 1}, {"X" : 1}, {"L" : 4}, {"Y" : 2}, {"M" : 2}, {"Z" : 1}]
    letter_pool_copy = letter_pool[:]
    hand_list = []

    for i in (range(10)):
        rand_num = random.randint(0, 25)
        letter_dict = letter_pool_copy[rand_num] #maybe we need to extract the value and save it into another variable?  
        key = list(letter_dict.keys())[0]
        val = list(letter_dict.values())[0]
        # rand_freq = random.randint(1, val)
        if val != 0: 
            hand_list.append(key)
            letter_dict[key] -= 1 
        # hand_list.extend([key for i in range(rand_freq)])
        # print(rand_num)
        # print(val)
        # print(rand_freq)
    return hand_list


def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass