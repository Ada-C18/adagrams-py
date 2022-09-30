import random

def draw_letters():
    # Import random - assign the randomized number to the index
    # "bag" of letters will be a dictionary as shown below
    # hand will be a list
# | A : 9  | N : 6 |
# | B : 2  | O : 8 |
# | C : 2  | P : 2 |
# | D : 4  | Q : 1 |
# | E : 12 | R : 6 |
# | F : 2  | S : 4 |
# | G : 3  | T : 6 |
# | H : 2  | U : 4 |
# | I : 9  | V : 2 |
# | J : 1  | W : 2 |
# | K : 1  | X : 1 |
# | L : 4  | Y : 2 |
# | M : 2  | Z : 1 |
    bag_of_letters_dict = {
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
    bag_of_letters_list = []
    for key, value in bag_of_letters_dict.items():
        for letter in range(value):
            bag_of_letters_list.append(key)

    hand = []

    while len(hand) < 10:
        for letter in bag_of_letters_list:
            hand.append(letter)
            letter_of_index = bag_of_letters_list.index(letter)
            bag_of_letters_list.pop(letter_of_index)
            break
    return hand

def uses_available_letters(word, letter_bank):
    true_false = []
    word = word.upper()
    word_list = []

    for letter in word:
        word_list.append(letter)
        if letter in letter_bank and word_list.count(letter) == letter_bank.count(letter):
            true_false.append(True)
        else:
            true_false.append(False)
    if False in true_false:
        return False
    else:
        return True

def score_word(word):
    scoreboard = {
        1 : "A, E, I, O, U, L, N, R, S, T",
        2 : "D, G",
        3 : "B, C, M, P",
        4 : "F, H, V, W, Y",
        5 : "K",
        8 : "J, X",
        10 : "Q, Z"
    }
    word = word.upper()
    #- If the length of the word is 7, 8, 9, or 10, 
    # then the word gets an additional 8 points
    score = 0
    for letter in word:
        for key, value in scoreboard.items():
            if letter in value:
                score += key
    if len(word) > 6:
        score += 8
    return score



def get_highest_word_score(word_list):
    tuple = ()
    winner_score = 0
    word_score = {}
    winner_word = ''
    for word in word_list:
        word_score[word] = score_word(word)
    for key, value in word_score.items():
        if value > winner_score:
            winner_score = value
            winner_word = key
        if value == winner_score:
            if len(key) < len(winner_word):
                winner_word = key

        tuple = (winner_word, winner_score)
    return tuple
    # winner = ()
    # word_score = {}
    # for word in word_list:
    #     word_score[word] = score_word(word)
    # for key, value in word_score.items():
    #     winner + max(value),key
    # return winner
