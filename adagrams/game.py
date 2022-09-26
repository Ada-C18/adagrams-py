import random
def draw_letters():
    user_letter_list = []
    #changed from a constant 
    pool_of_letters = {
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
    for num in range(10):
        choice = random.choice(list(pool_of_letters.keys()))
        if pool_of_letters[choice] != 0:
            user_letter_list.append(choice)
            pool_of_letters[choice] -= 1
            if pool_of_letters[choice] == 0:
                del pool_of_letters[choice]
        
                
    return user_letter_list
    

def uses_available_letters(word, letter_bank):
    uppercase_word = word.upper()
    is_word_valid = False
    letter_list = []
    for letter in uppercase_word:
        letter_list.append(letter)
    for ele in letter_list:
        if ele in letter_bank:
            is_word_valid = True
        else:
            is_word_valid = False
            # delete the letter from the list... but what if the letter is there twice?
            # all test should pass once fixed 
    return is_word_valid


    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass