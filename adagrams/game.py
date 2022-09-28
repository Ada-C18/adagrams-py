import copy
def draw_letters():
    pass 

def uses_available_letters(word, letter_bank):
    correct_letters = []
    new_letter_bank = copy.deepcopy(letter_bank)
    word_case = word.upper() 
    for char in word_case:
        if char in new_letter_bank:
            correct_letters.append(char)
            new_letter_bank.remove(char)
        if len(word_case) == len(correct_letters):

            return True 
    else:
        return False


    
    

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass