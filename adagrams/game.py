from operator import le
import random
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

def create_bag_of_letters():
    """
    Returns an array containing all the letters of the "LETTER_POOL" dictionary 
    according to the frequency associated with each letter.
    Ex: Since the value of 'A' is 9, the first 9 elements of this list will be 'A' 
    appearing 9 times, and so on.
    bag_of_letters = ['A', 'A', ..., 'B', ...]
    """
    bag_of_letters = []
    for letter in LETTER_POOL:
        number_of_letters = LETTER_POOL[letter]
        for i in range(number_of_letters):
            bag_of_letters.append(letter)
    return bag_of_letters

def draw_letters():
    hand_of_letters = [] # to be filled with 10 one-letter strings
    bag_of_letters = create_bag_of_letters()
   
    for i in range(10):
        #size_of_letter_bag = len(bag_of_letters)
        letter_picked = random.choice(bag_of_letters) 
        hand_of_letters.append(letter_picked)
        bag_of_letters.remove(letter_picked)

    return hand_of_letters

def uses_available_letters(word, letter_bank):
    copy_of_letter_bank = list(letter_bank)
    upper_case_word = word.upper()
    #We checked to make sure that removing wouldn't affect original letter_bank array here:
    # copy_of_letter_bank.remove('B')
    # print("letter bank:", letter_bank)
    #print("copy of letter bank:" , copy_of_letter_bank)
    
    for character in upper_case_word:
        if character in copy_of_letter_bank:
            copy_of_letter_bank.remove(character)
        else:
            return False
    
    return True


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass

#hand = ['S', 'B', 'E', 'T', 'R','E' , 'Z', 'A', 'L', 'M']
#uses_available_letters("TREE", hand)