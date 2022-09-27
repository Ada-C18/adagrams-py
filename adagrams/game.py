import random
import copy

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
# Helper Functions --- Start ------

def create_word_list(word):
    word_list =[]
    for each in word:
        word_list.append(each.upper())
    return word_list

# Helper Functions --- End --------

def draw_letters():
    hand = []
    while len(hand) < 10 or not hand:
        letter = random.choice(list(LETTER_POOL))
        if hand.count(letter) < LETTER_POOL[letter]:
            hand.append(letter)

    return hand

def uses_available_letters(word, letter_bank):
    word_list = create_word_list(word)
    letter_bank_copy = copy.deepcopy(letter_bank)

    # for each in word:
    #     word_list.append(each.upper())

    check_list =[]

    for letter in range(len(word_list)):
        if word_list[letter] in letter_bank_copy:
            letter_bank_copy.remove(word_list[letter])
            check_list.append(True)
        else:
            check_list.append(False)

    return all(check_list)

SCORE_CHART = {
    "A": 1,
    "B": 3,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 4,
    "G": 2,
    "H": 4,
    "I": 1,
    "J": 8,
    "K": 5,
    "L": 1,
    "M": 3,
    "N": 1,
    "O": 1,
    "P": 3,
    "Q": 10,
    "R": 1,
    "S": 1,
    "T": 1,
    "U": 1,
    "V": 4,
    "W": 4,
    "X": 8,
    "Y": 4,
    "Z": 10
}

def score_word(word):
    word_list = create_word_list(word)
    score = 0

    # for each in word:
    #     word_list.append(each.upper())
    
    for letter in range(len(word_list)):
        if word_list[letter] in SCORE_CHART:
            score += SCORE_CHART[word_list[letter]]
    
    if len(word) > 6:
        score += 8
    
    return score

def get_highest_word_score(word_list):
    best_word_and_score = [] # did not start with tuple because tuples are immutable
    words_and_scores = {}

    # populate dictionary with word string as keys and score as value
    for word in range(len(word_list)):
        score = score_word(word_list[word])
        words_and_scores[word_list[word]] = score
    
    # iterate through words_and_scores dictionary to determine best word and score and put into list
    # called best_word_and_score
    
    for word, score in words_and_scores.items():
        if not best_word_and_score:
            best_word_and_score.append(word)
            best_word_and_score.append(score)
        elif score > best_word_and_score[1]:
            best_word_and_score[1] = score
            best_word_and_score[0] = word

            # TIEBREAKER RULES: 
            # 1. Prefer the first 10 letter word that was used
            # 2. 10 letter word over fewest letter word
            # 3. Fewest letter word, unless letter is 10 words

        elif score == best_word_and_score[1] and len(word) < len(best_word_and_score[0]) and len(best_word_and_score[0]) != 10:
            best_word_and_score[1] = score
            best_word_and_score[0] = word
        elif score == best_word_and_score[1] and len(word) == 10 and len(word) != len(best_word_and_score[0]):
            best_word_and_score[1] = score
            best_word_and_score[0] = word

    return tuple(best_word_and_score)
        
