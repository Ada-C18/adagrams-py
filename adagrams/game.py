# from tests.test_wave_01 import LETTER_POOL


# Wave 1
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
def draw_letters():
    """Function to build a hand of 10 letters for the user
    Input: Letter pool which include all the letters and their frequency
    Output: Return 10 random letters from the letter pool
    """
    list_1= [k*v for k,v in LETTER_POOL.items()]
    letter_pool_list=[]
    for string in list_1:
        for letter in string:
            letter_pool_list.append(letter)
    
    
    print(letter_pool_list)
    user_hand= (random.sample(letter_pool_list,10))

    return user_hand 
    


def uses_available_letters(word, letter_bank):
    """ Function to check if the word the user provided is in the the letter bank
    Input: user's word and letter bank
    Output: True (if all the letter in the word is in the letter bank with the right counts of letter) or False (if any letter in the word is NOT in the letter bank or if the user uses more than allowed)
    """
    word = word.upper()
    word_list = [letter for letter in word]
    print(word_list)
    for character in word:
        for string in letter_bank:
            if character not in letter_bank:
                return False
            elif character in letter_bank: #and character == string:
                if word.count(character) > letter_bank.count(string):
                    # print('False')
                    return False
    # print('True')
    return True

def score_word(word):
    """ Function to return the score of the word that the user input
    Input: user's word and the score chart
    Output: the score of user's word
    """
    SCORE_CHART = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}
    word=word.upper()
    word_list=[letter for letter in word]
    score=0
    if len(word_list)<7:
        score=0
        
    else:
        score += 8
    
    for letter in word_list:
        if letter in SCORE_CHART:
            score+= SCORE_CHART[letter]
    
    return score
            

def get_highest_word_score(word_list):
    """ Function that chooses the word with the highest score, or highest score with fewest letter or with 10 letters
    Input: word_list
    Output: word and score in tuple type
    """
    highest_score=0
    highest_score_list= []
    for word in word_list:
        score= score_word(word) 
        if score > highest_score:
            highest_score= score
            highest_score_list.clear()
            highest_score_list.append(word)
        elif score == highest_score:
            highest_score_list.append(word)

    fewest_letter = highest_score_list[0]
    len_fewest_letter= len(highest_score_list[0])

    for word in highest_score_list:
        if len(word)== 10:
            return (word,highest_score)
        elif len(word)< len_fewest_letter:
            fewest_letter = word
            len_fewest_letter = len(word)

    return (fewest_letter,highest_score)
