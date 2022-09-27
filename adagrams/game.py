import random

def draw_letters():
    """
    build a hand of 10 letters for the user
    """
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
    letter_list =  []
    for letter, freq in LETTER_POOL.items():
        for i in range(freq):
            letter_list.append(letter)
    
    hand = []
    while len(hand) < 10:
        # drawn_letter = letter_list.pop()
        hand.append(letter_list.pop(random.randint(0,len(letter_list)-1)))
    return hand


def uses_available_letters(word, letter_bank):
    """
    Check if an input word (a word a player submits) only uses characters that are contained within a collection (or hand) of drawn letters
    """
    hand = letter_bank[:]
    word = word.upper()
    for letter in word:
        if letter not in hand:
            return False
        else:
            hand.remove(letter)
            
    return True
    # - for loop to check if letters in word are in the string of letter bank
    # - Remove  from letter bank if it is in there
    # -return false if it isn't in the letter bank
    


def score_word(word):
    """
    function returns the score of a given word as defined by the Adagrams game
    """
    # - make total variable
    # - if len(word) 7,8,9,10 add 8 to total
    # - inside if statement, put for loop through letter in word
    #   - we can do if else or do lists of letters as value and points as they key in dictionary
    # - add appropriate points
    # - return score
    point_values = {
        "AEIOULNRST" : 1,
        "DG": 2,
        "BCMP": 3, 
        "FHVWY": 4,
        "K": 5,
        "JX":8,
        "QZ": 10
    }
    word_upper = word.upper()
    total = 0

    for letter in word_upper:
        for key in point_values:
            if letter in key:
                total += point_values[key]
    
    if 6 < len(word) < 11:
        total += 8
    return total



def get_highest_word_score(word_list):
    """
    This function looks at the list of `word_list` 
    and calculates which of these words has the highest score,
    applies any tie-breaking logic, and returns the winning 
    word in a tuple.
    The tuple must contain the following elements:
    - index 0 ([0]): a string of a word
    - index 1 ([1]): the score of that word
    """
    # - create a list to store our tuples
    # - create a for loop to go through all of the words in word_list, len word_list
    #   - use helper function score word on each list. 
    #   - store word as 1st object in tuple and score in second
    # - use max to find the highest scores 
        # 
        #- if there are multiple highest then choose the len that is smaller
        #- if they have same len and score, return the one that comes first in word_list
    #- return the tuple of the winning word
    