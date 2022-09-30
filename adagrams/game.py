from random import randint
from copy import deepcopy

def draw_letters():
    """
    Returns an array of ten strings from LETTER_POOL.
    """
    # Create a deep copy of LETTER_POOL dictionary to be able to update the quantity as letters are drawn
    letter_dict = deepcopy(LETTER_POOL)
    
    # Create a letter_list to store the pool of letters at individual index
    letter_list = []
    for k, v in LETTER_POOL.items():
        for num in range(v):
            letter_list.append(k)
    
    # Initialize an output list and append letters drawn
    output_list = []
    while len(output_list) < 10:

        # Generate a random index between 0 and length of the letter_list - 1 (both inclusive)
        index = randint(0, len(letter_list)-1)

        # If we have already used up this letter in the LETTER_POOL, we skip to the next drawing   
        if letter_dict[letter_list[index]] == 0:
            continue
        
        # If a letter can be drawn successfully, we append the letter to the output_list
        # and subtract one from its value in the letter_dict
        else:
            output_list.append(letter_list[index])
            letter_dict[letter_list[index]] -= 1
    return output_list

def uses_available_letters(word, letter_bank):
    """ 
    Returns True if every letter in the (input string) "word" is available 
    (in the right quantities) in the "letter_bank" (list).
    Returns False if there is a letter in input that is not present in the
    letter_bank or has too much of compared to the letter_bank.
    """
    # create a dictionary to calculate the quantity 
    # of each letter in the given letter_bank.
    letter_dict = {}
    for letter in letter_bank:
        if letter in letter_dict.keys():
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    
    # iterate through each letter in the given word.
    # returns True if all letters are in the letter_bank within correct quantity
    # returns False otherwise 

    for letter in word:
        letter = letter.upper()
        if letter not in letter_bank or letter_dict[letter] == 0:
            return False
        else:
            letter_dict[letter] -= 1
    return True

def score_word(word):
    """
    Returns the score of a given word as defined by the Adagrams game.
    """
    value_dic = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }

    # Initialize a variable called sum at 0
    sum = 0

    # Iterate over each letter in the given word and add its corresponding score to the sum
    for letter in word:
        sum += value_dic[letter.upper()]
    
    # If the word length is 7, 8, 9 or 10, add an addtional 8 score to the sum
    if 7 <= len(word) <= 10:
        sum += 8
    return sum

def get_highest_word_score(word_list):
    """
    Looks at the list of word_list and calculates which of these words has 
    the highest score, applies any tie-breaking logic, 
    and returns the winning word in a tuple.
    """

    # initializing a variable "highest_score" to track highest score 
    # and a list "highest_scoring_words" to track highest_scoring words.

    highest_score = 0
    highest_scoring_words = []

    # iterate over each word inside word_list to 
    # compute that word's score and update the highest_score variable
    # and highest_scoring_words list 
    for word in word_list:
        score = score_word(word)
        if score > highest_score:
            highest_scoring_words.clear()
            highest_score = score
            highest_scoring_words.append(word)
        elif score == highest_score:
            highest_scoring_words.append(word)
    
    # initialize the variables "shortest_word_length" and "shortest_word" 
    # to track highest-scoring word with shortest length for applying 
    # tie-breaker rules (Winning word is the first spotted 10-letter word. 
    # If there is no 10 letter word, the shortest word wins.)

    shortest_word_len = len(highest_scoring_words[0])
    shortest_word = highest_scoring_words[0]
    for word in highest_scoring_words:
        if (len(word) == 10):
            return (word, score_word(word))
        elif len(word) < shortest_word_len:
            shortest_word_len = len(word)
            shortest_word = word
    return (shortest_word, score_word(shortest_word))    

#***==================================================***
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