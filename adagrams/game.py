import random
from collections import Counter
# import string


random_letter = ['s', 't', 'o', 's', 't', 'o', 's', 't', 'o', 'm', 'p', 'u']
LETTER_POOL = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 
    'E': 12, 'F': 2, 'G': 3, 'H': 2, 
    'I': 9, 'J': 1, 'K': 1, 'L': 4, 
    'M': 2, 'N': 6, 'O': 8, 'P': 2, 
    'Q': 1, 'R': 6, 'S': 4, 'T': 6, 
    'U': 4, 'V': 2, 'W': 2, 'X': 1, 
    'Y': 2, 'Z': 1
}

###### wave 1 ########
def build_letter_pool_list():
    letter_pool_list = []
    for key, value in LETTER_POOL.items():
        letter_pool_list.extend(list(key * value))
    return letter_pool_list



def draw_letters():
    random_letter = build_letter_pool_list()
    letter = [] 
    while len(letter) < 10:
       random_index = random.randint(0, len(random_letter)-1)
       letter.append(random_letter.pop(random_index))

    return letter
    

    
###### wave 2 ########

def uses_available_letters(word, letter_bank):

    '''
- Has two parameters:
   - `word`, the first parameter, describes some input word, and is a string
   - `letter_bank`, the second parameter, describes an array of drawn letters in a hand. 
      You can expect this to be an array of ten strings, with each string representing a letter
- Returns either `True` or `False`
- Returns `True` if every letter in the `input` word is available 
  (in the right quantities) in the `letter_bank`
- Returns `False` if not; if there is a letter in `input` that is not 
present in the `letter_bank` or has too much of compared to the `letter_bank`
    '''
    word = word.upper()

    letter_bank_dict = {element: letter_bank.count(element) for element in letter_bank}
    word_dict = {element: word.count(element) for element in word}

    for letter,num in word_dict.items():
        if letter not in letter_bank_dict.keys():
            return False
        elif letter in letter_bank_dict:
            letter_bank_dict[letter] -= num
            if letter_bank_dict[letter] < 0:
                return False
        # else:
        #     return False
        
        
    return True

            




    # print(letter_bank_dict)
    print(word_dict)




def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass