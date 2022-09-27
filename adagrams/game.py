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
        letter_dict = letter_pool_copy[rand_num] 
        key = list(letter_dict.keys())[0]
        val = list(letter_dict.values())[0]

        if val != 0: 
            hand_list.append(key)
            letter_dict[key] -= 1 
    return hand_list


def uses_available_letters(word, letter_bank):
    #loop through the letters in the word and check if its in the letter bank
    #if its not in the letter bank, return false
    #potentially write a helper function
    #initialize a list to hold all present letters from the letter_bank 
    #if the letter is in the bank, add it to the new list and remove it from the letter bank
    #if the len of new list == len word return true else false 
<<<<<<< HEAD
    pass
=======
    available_letters = []
    letter_bank_copy = letter_bank[:]
    for char in word.upper():
        if char not in letter_bank_copy:
            return False
        else:
            available_letters.append(char)
            letter_bank_copy.remove(char)
            if len(available_letters) == len(word):
                return True

>>>>>>> bd739cbbbd72fa3da27884c92bd5d040725d5534

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass