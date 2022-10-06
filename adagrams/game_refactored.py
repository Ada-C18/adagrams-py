import random
from operator import itemgetter

def build_letter_pool(): # wave 1
    
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

    letter_pool = []

    for letter, frequency in LETTER_POOL.items():
        for num in range(frequency):
            letter_pool.append(letter)
    # print(letter_pool)
    return letter_pool
    

def draw_letters(): #wave 1
    letter_pool = build_letter_pool()
    letters = random.sample(letter_pool, 10)
    # print(letters)
    return letters
    # pass

def uses_available_letters(word, letter_bank): #wave 2
    result = True
    letter_bank_dict = {}
    
    for letter in letter_bank: 
        letter_bank_dict[letter] = letter_bank.count(letter)
    
    word = word.upper()
    
    for character in word: 
        if character in letter_bank_dict:
            if letter_bank_dict[character] == 0:
                result = False
            letter_bank_dict[character] -= 1
        else:
            result = False
    return result
    # pass


#-----wave 03 ------------ #
    #LP's version (with coworking!)

def score_word(word):#THIS IS MAKING THE DICTIONARY FOR EVERY WORD.  MAKE THIS A GLOBAL VARIABLE INSTEAD, AND JUST CALL THE FUNCTION ONCE.
    letter_scores = make_score_dict()
    score = get_score(word.upper(), letter_scores)
    return score
    
#challenge: compare words to an imported dictionary to see if it's a word!
#I would do this, but I don't know how to install packages here. I don't think it'll work in this window.

def make_score_dict():
    #set up dictionary of score values
    #we want the form letter are keys and scores are the values

    letter_scores = {}
    point1 = (1, ["A", "E", "I", 'O', 'U', 'L', 'N', 'R', 'S', 'T'])
    point2 = (2, ['D', 'G'])
    point3 = (3, ['B', 'C', 'M', 'P']) 
    point4 = (4, ['F', 'H', 'V', 'W', 'Y'])
    point5 = (5, ['K']) 
    point8 = (8, ['J', 'X'])
    point10 = (10, ['Q', 'Z'])
    point_info = [point1, point2, point3, point4, point5, point8, point10]
    
    for point_group in point_info:
        for letter in point_group[1]:
            letter_scores[letter] = point_group[0]
            
    return letter_scores
    
def get_score(word, letter_scores):
    #loop through the word, adding up the value associated with the letter (key) of the dict!
    score = 0
    for char in word:
        char = char.upper()
        #look for the character in the keys of letter_scores.
        #add the associated value to score
        score += letter_scores[char]
        #print(char, word, score)
    if len(word) >= 7:
        score += 8
            
    return score

#--------------- New code from class --------------- 10/7/22 ---------
#testing
# letter_scores = make_score_dict()
# print(get_score("za", letter_scores))

# def max_with_ties_for_score(data):  #my function below should work for this as well. 
#     best = []
#     best_score = None
#     for item in data:
#         score = score_word(item)
#         if best_score == None or score > best_score:
#             best = [item] #throw out the old list!  start a new list.
#             best_score = score
#         elif score == best_score:
#             best.append(item)
#     return best

#testing
# words = ['hello', 'za', 'today', 'qi']
# print(max_with_ties_for_score(words))

# def max_with_ties_for_len(data):  #let's change a few things to make this about length. 
#     best = []
#     best_score = None
#     for item in data:
#         score = len(item)  #this is the only line that has changed so far!
#         if best_score == None or score > best_score:
#             best = [item] #throw out the old list!  start a new list.
#             best_score = score
#         elif score == best_score:
#             best.append(item)
#     return best

#testing
# words = ['hello', 'za', 'today', 'qi']
# print(max_with_ties_for_len(words))

#note : THE FUNCTIONS ABOVE ARE DUPLICATES OF EACH OTHER!!  TOO BUSY!!  le'ts get it together. 
#let's replace this with higher order function!!
#WE CAN USE THE FOLLOWING FUNCTION IN A LOT OF DIFFERENT CONTEXTS, JUST USING HIGHER ORDER FUNCTIONS.
#this code is much more flexible. :) 

#this behaves a lot like python's max.  Max is also flexible because it has an optional key argument.
def max_with_ties(data, scorer):  #we'll pass in a function called scorer. #do all the logic with this function. 
    best = []
    best_score = None
    for item in data:
        score = scorer(item)  #this is the only line that has changed so far!
        if best_score == None or score > best_score:
            best = [item] #throw out the old list!  start a new list.
            best_score = score
        elif score == best_score:
            best.append(item)
    return best

words = ['hello', 'za', 'today', 'qi']
print(max_with_ties(words, score_word))  #notice: we don't put () following the name of the function.
print(max_with_ties(words, len))
#-------------end wave 3---------


#------ Begin Wave 4------------


def get_highest_word_score(word_list):
    """
    This gets the word with the highest score. 
    This will be a list of tuples (word, score) of type (str, int)
    """
    words_scores_list = []
    
    for word in word_list: 
        words_scores_list.append((word, score_word(word)))
    sorted_words_scores_list = sorted(words_scores_list, key=itemgetter(1), reverse=True)

    max_score = sorted_words_scores_list[0][1]
    #we find the max score
    potential_winners = []
    # set up a list of all the things that have the best score. 
    for word, score in sorted_words_scores_list:
        if score == max_score:
            potential_winners.append((word, score, len(word)))
    
    if len(potential_winners) == 1:
        return potential_winners[0]

    sorted_winners = sorted(potential_winners, key = itemgetter(2),reverse=True)
    min_length = sorted_winners[-1][2]
    
    for word, score, length in sorted_winners:
        if length == 10: 
            return word, score
        elif length == min_length:
            return word, score
