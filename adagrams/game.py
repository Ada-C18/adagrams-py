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

    while len(hand_list) < 10:
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


def score_word(word):
    #create 7 lists of points
    #for each letter in the word, use a conditional to find corresponding point
    #   make a score variable and add to it as we loop through the char of the word
    # if len of word >= 7 add 8 more points
    # return score 

    list_1 = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
    list_2 = ["D", "G"]
    list_3 = ["B", "C", "M", "P"]
    list_4 = ["F", "H", "V", "W", "Y"]
    list_5 = ["K"]
    list_8 = ["J", "X"]
    list_10 = ["Q", "Z"]
    
    score = 0 
    
    for char in word.upper():
        if char in list_1:
            score += 1
        elif char in list_2:
            score += 2
        elif char in list_3:
            score += 3
        elif char in list_4:
            score += 4
        elif char in list_5:
            score += 5
        elif char in list_8:
            score += 8
        elif char in list_10:
            score += 10
    if len(word) >= 7:
        score += 8
    return score

def get_highest_word_score(word_list):
    #set up an empty string that holds the higherst score word
    #have a highest score variable starting at zero
    #loop through the word_list and for each word we call the function above to get score
        # compare it to the higheset_score_var and it's replaced if it is higher
        # add the highest score word to the string var
        # as we loop through replace them using conditionals
            # if tie compare len of words with len of highest word place holder (if its less than highest word it replaces current one)
                # if len(word) > len(string_var) and len(strint_var) is not 10 then replace with new word
                #elif len(word) == len(string_var) then string_var will remain
        # return tuple 
    highest_score = 0
    highest_str = ""
    
    for word in word_list:
        word_score = score_word(word)
        if word_score > highest_score:
            highest_score = word_score 
            highest_str = word
        elif word_score == highest_score:
            if len(word) < len(highest_str) and len(highest_str) != 10:
                highest_str = word
            elif len(word) == 10 and len(highest_str) != 10:
                highest_str = word
 
    return (highest_str, highest_score)

        

