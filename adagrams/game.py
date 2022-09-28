import random

def draw_letters():
    pool_count = 98 # number of letters in pool overall
    drawn_letters = []
    letter_pool = [] # list of letters available draw from
    letter_pool_amounts = {
        'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12,
        'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1,
        'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8,
        'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6,
        'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
    }

    # creates a list of individual letters to draw from
    for letter, number in letter_pool_amounts.items():
        for x in range(number):
            letter_pool.append(letter)
    # draws 10 random letters and returns them as a list
    for x in range(10):
        letter_index = random.randint(0, pool_count - 1)
        drawn_letters.append(letter_pool.pop(letter_index))
        pool_count -= 1
    return drawn_letters

def uses_available_letters(word, letter_bank):
    temp_letter_bank = letter_bank.copy()
    # checks each letter in the word
    # if it's in the letter bank, removes that letter from the bank to avoid duplicate checking
    for letter in word.upper():
        if letter in temp_letter_bank:
            temp_letter_bank.remove(letter)
        else:
            return False

    return True

def score_word(word):
    # initialize dictionary w/ each letter's value
    score = 0
    LETTER_VALUES = {
        'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1,
        'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
        'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1,
        'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
        'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
    }
    # make sure word is in all caps and remove non-alphabetic characters
    formatted_word = ""
    for letter in word:
        if letter.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            formatted_word += letter.upper()
            
    # look each letter up in score dict and add each letter's value to score
    for letter in formatted_word:
        score += LETTER_VALUES[letter]

    if len(formatted_word) >= 7: 
        score += 8
    return score

def get_highest_word_score(word_list):
    highest_score = -1
    shortest_length = 999
    winning_words = []

    for word in word_list:
        word_score = score_word(word)
        # gets the highest score out of all words
        if word_score > highest_score:
            highest_score = word_score
        # gets the shortest length out of all words
        if len(word) < shortest_length:
            shortest_length = len(word)

    for word in word_list:
        if score_word(word) == highest_score and len(word) == 10:
            return (word, score_word(word)) #automatic win condition

        # adds highest scoring words to list of winning words
        elif score_word(word) == highest_score:
            winning_words.append(word)

    # if there is more than one winning word, pick the first one with the fewest characters
    if len(winning_words) > 1:
        for word in winning_words:
            if len(word) == shortest_length:
                return (word, score_word(word))
    # otherwise, return the winner
    else:
        return (winning_words[0], score_word(winning_words[0]))
