import random

def draw_letters():
    """
    build a hand of 10 letters for the user
    """

    # Letter Pool could be better in global field to easily change game
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
    


def score_word(word):
    """
    function returns the score of a given word as defined by the Adagrams game
    """
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
    winning_word = ""
    winning_score = -1
    for word in word_list:
        score = score_word(word)
        if score > winning_score:
            winning_word = word
            winning_score = score
        elif score == winning_score and len(winning_word) != 10:
            if len(word) == 10 or len(word) < len(winning_word):
                winning_word = word           

    return (winning_word, winning_score)