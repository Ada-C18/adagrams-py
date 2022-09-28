import random

# letters with point value and distribution
LETTERS = {
    "A" : [1, 9],
    "B" : [3, 2],
    "C" : [3, 2],
    "D" : [2, 4],
    "E" : [1, 12],
    "F" : [4, 2],
    "G" : [2, 3],
    "H" : [4, 2],
    "I" : [1, 9],
    "J" : [8, 1],
    "K" : [5, 1],
    "L" : [1, 4],
    "M" : [3, 2],
    "N" : [1, 6],
    "O" : [1, 8],
    "P" : [3, 2],
    "Q" : [10, 1],
    "R" : [1, 6],
    "S" : [1, 4],
    "T" : [1, 6],
    "U" : [1, 4],
    "V" : [4, 2],
    "W" : [4, 2],
    "X" : [8, 1],
    "Y" : [4, 2],
    "Z" : [10, 1]
}


def draw_letters():

    # creates a pool of letters given distribution
    letter_pool = []
    for letter, stats in LETTERS.items():
        letter_distribution = stats[1]
        letter_pool += letter * letter_distribution
    
    # selects 10 letters from pool
    user_letters = random.sample(letter_pool, k=10)

    return user_letters
    

def uses_available_letters(word, letter_bank):

    # create a dictionary counting available letters
    available_letters = {}
    for letter in letter_bank:
        available_letters[letter] = available_letters.get(letter, 0) + 1

    for letter in word.upper():
        # if letter is not available in bank, return False
        if letter not in letter_bank or available_letters[letter] == 0:
            return False
        # if letter still available, subtract 1 from letter count
        elif available_letters[letter] != 0:
            available_letters[letter] -= 1

    # return True if all used letters were available
    return True


def score_word(word):

    score = 0
    for letter in word.upper():
        letter_value = LETTERS[letter][0]
        score += letter_value

    if len(word) >= 7:
        score += 8
        
    return score


def get_highest_word_score(word_list):
    word_scores = {}
    top_scores = []
    
    # build a dictionary with word scores
    for word in word_list:
        word_scores[word] = score_word(word)
    
    # create a list of words that have the highest score
    highest_score = max(word_scores.values())
    for word in word_scores:
        if word_scores[word] == highest_score:
            top_scores.append(word)
    
    # if there's one highest word, return it
    if len(top_scores) == 1:
        return top_scores[0], highest_score
    
    # in case of a tie...
    elif len(top_scores) > 1:
        # return the first word with length 10
        for word in top_scores:
            if len(word) == 10:
                return word, highest_score
        # return the first word with shortest length
        shortest_word = min(top_scores, key=len)
        return shortest_word, highest_score

