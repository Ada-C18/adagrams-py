import random

def create_letter_list():
    #put the helper function here
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
    letter_pool = []
    for letter in LETTER_POOL:
        for i in range(LETTER_POOL[letter]):
            letter_pool.append(letter)
    return letter_pool

def draw_letters():
    #convert LETTER_POOL dict to list--helper function?
    letter_pool = create_letter_list()
    hand = []
    for i in range(10):
        rand_index = random.randint(0, len(letter_pool) - 1)
        hand.append(letter_pool.pop(rand_index))
    return hand

def uses_available_letters(word, letter_bank):
    word = word.upper()
    hand_copy = letter_bank[:]
    # print(hand_copy)
    for letter in word:
        if letter not in hand_copy:
            hand_copy = letter_bank[:]
            return False
        hand_copy.remove(letter)
        # print(hand_copy)
    return True

def score_word(word):
    score_dict = {
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
    word = word.upper()
    word_score = 0
    for letter in word:
        word_score += score_dict[letter]
    if 7 <= len(word) <= 10:
        word_score += 8
    return word_score


def get_highest_word_score(word_list):
    # print(word_list)
    word_scores = []
    for word in word_list:
        word_scores.append((word, score_word(word)))
    high_score = 0
    for i in range(len(word_scores)):
        if word_scores[i][1] > high_score:
            winner = word_scores[i]
            high_score = winner[1]
        elif word_scores[i][1] == high_score:
            if len(winner[0]) == 10:
                break
            elif len(word_scores[i][0]) < len(winner[0]) or len(word_scores[i][0]) == 10:
                winner = word_scores[i]
                high_score = winner[1]
            
    return winner