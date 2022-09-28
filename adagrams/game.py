import random

def draw_letters():

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

    the_letters = []
    for key,value in LETTER_POOL.items():
        for i in range(value):
            the_letters.append(key)

    # use random to pick an index of the length of the_letters 
    # the element is in the list then remove it -- add it to the hand and remove it from letters

    #the_hand = [random.choice(list(the_letters)) for i in range(10)]
    # where in the letters list we are going to pull from
    the_hand = []
    for i in range(10):
        random_letter_index = random.randint(0,len(the_letters)-1)
        the_hand.append(the_letters[random_letter_index])
        the_letters.remove(the_letters[random_letter_index])
    # use random in my owm words----  
    # create a dict 
    
    
    return the_hand



def uses_available_letters(word, letter_bank):
    #copy letter_bank to track what letters are still available to use
    available_letters = [letter for letter in letter_bank]
    # check if each letter in the word is available
    for letter in word:
        # use .upper() to make sure lowercase input is still tracked
        if letter.upper() in available_letters:
            available_letters.remove(letter.upper())
        else:
            return False
    return True



def score_word(word):

    ''' word is a str of characters
    returns an int representing the number of points
    each letter within word has a point value..
    total score = number of points of all words
    if len(word) == 7,8,9,19 then score additional 8 points
    '''

# dict 
    score = 0
    the_score_dict = { 1: ['A','E','I','O','U','L','N','R','S','T'],
    2 : ['D','G'],
    3 : ['B','C','M','P'],
    4: ['F','H','V','W','Y'],
    5: ['K'],
    8: ['J','X'],
    10: ['Q','Z']
    }
    
    for letter in word:
        for key, value in the_score_dict.items():
            if letter.upper() in value:
                score += key
    if len(word) >= 7:
        score += 8
    
    return score


def get_highest_word_score(word_list):
    ''' reads a word_list and scores each word
    finds highest scoring word
    returns tuple of word and score
    tie breakers:
        word with fewest letters OR
        word with 10 letters OR
        first one in list for multiple
    '''
    highest_score = 0
    top_word = ""
    tie_list = []
    for word in word_list:
        score = score_word(word)
        if score > highest_score:
            highest_score = score
            top_word = word
        if score == highest_score:
            tie_list.append(word)

    the_winner = (top_word, highest_score)
    return the_winner