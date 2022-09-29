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
    '''
    pulls a random letter from LETTER_POOL and stores it
    in a list, returns list
    '''
    letter_list = generate_letter_list()
    user_hand = []

    while len(user_hand) < 10:
        random_letter = random.choice(letter_list)
        user_hand.append(random_letter)
        for letter in letter_list:
            if letter == random_letter:
                letter_list.remove(letter)

    return user_hand

def generate_letter_list():
    '''
    helper function - returns a list that contains every instance 
    of the letters in the LETTER_POOL dict, including duplicates
    '''
    letter_list = []

    for letter in LETTER_POOL:
        for i in range(LETTER_POOL[letter]):
            letter_list.append(letter)
    
    return letter_list


def uses_available_letters(word, letter_bank):
    '''
    takes 2 parameters word and letter_bank(the player's hand) 
    and checks that all letters in word are in letter_bank
    returns boolean value
    '''
    hand_dict = {}
    word = word.upper()

    for letter in letter_bank:
        if letter not in hand_dict.keys():
            hand_dict[letter] = 0
        hand_dict[letter] += 1

    for letter in word:
        if letter not in letter_bank or hand_dict[letter] == 0:
            return False
        hand_dict[letter] -= 1
    
    return True

def score_word(word):
    '''
    takes one argument, word, and finds the a final score
    based on the point value of all of the letters in that word
    adds 8 for any 7-10 letter word and returns final score
    '''
    points_dict = {
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"]
    }

    final_score = 0
    word = word.upper()

    if len(word) >= 7:
        final_score += 8

    for score, letter_list in points_dict.items():
        for letter in word:
            if letter in letter_list:
                final_score += score

    return final_score

def get_highest_word_score(word_list):
    '''
    returns a tuple that contains highest scoring word
    and its corresponding score. contains logic to 
    resolve ties
    '''
    word_score_list = get_high_score_tuple(word_list)
    score = 0
    final_word = ""
    final_score_list = []

    for score_tuple in word_score_list:
        # tie resolution
        if score_tuple[1] == score:
            if len(score_tuple[0]) == 10 and len(final_word) != 10:
                final_word = score_tuple[0]
                score = score_tuple[1]            
            elif len(score_tuple[0]) < len(final_word) and len(final_word) != 10:
                final_word = score_tuple[0]
                score = score_tuple[1]
        # updates final_word and score variables with highest scoring word and score
        elif score_tuple[1] > score:
                final_word = score_tuple[0]
                score = score_tuple[1]

    while len(final_score_list) < 2:
        final_score_list.append(final_word)
        final_score_list.append(score)
    
    return tuple(final_score_list)

def get_high_score_tuple(word_list):
    '''
    helper function - returns list of tuples, tuples contain word 
    from word_list and score of that word
    '''
    word_score_list = []

    for word in word_list:
        word_score = score_word(word)
        word_score_list.append((word, word_score))
    
    return word_score_list