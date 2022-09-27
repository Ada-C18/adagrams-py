import random

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

# def score_word(word): #Abby
#     score_values = []
#     score_dict = { 1: ["A","E", "I", "O", "U", "L", "N", "R", "S", "T"], 2: ["D", "G"], 3: ["B", "C", "M", "P"], 4: ["F","H", "V", "W", "Y"], 5: ["K"], 8: ["J", "X"], 10: ["Q", "Z"]}
#     word = word.upper()

#     if len(word) >= 7: 
#         score_values.append(8)
#     for character in word:
#         for letter_value, letters in score_dict.items():
#             for letter in letters:
#                 if letter == character: 
#                     score_values.append(letter_value)
    
#     return sum(score_values)

def get_highest_word_score(word_list):
    pass

#-----wave 03 ------------ #
     #LP's version (with coworking!)

def score_word(word):
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
        #look for the character in the keys of letter_scores.
        #add the associated value to score
        score += letter_scores[char]
        #print(char, word, score)
    if len(word) >= 7:
        score += 8
            
    return score

        
#-------------end wave 3---------



draw_letters()