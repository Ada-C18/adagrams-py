import copy

LETTER_POOL = {
    'A': 10, 
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
    import random
    list_of_all_letter = []
    for key, value in LETTER_POOL.items():
        for i in range(value):
            list_of_all_letter.append(key)

    ten_letters = []
    for i in range(10):
        ten_letters.append(list_of_all_letter.pop(random.randrange(0, len(list_of_all_letter))))
    
    return ten_letters


def uses_available_letters(word, letter_bank):
    copy_bank = copy.deepcopy(letter_bank)
    word = word.upper()
    for char in word:
        if char in copy_bank:
            copy_bank.remove(char)
            
        else:
            return False
    return True

def score_word(word):
    word = word.upper()
    point_dict = {"A, E, I, O, U, L, N, R, S, T " : 1, 
        "D, G" : 2, 
        "B, C, M, P" : 3, 
        "F, H, V, W, Y" : 4, 
        "K" : 5, 
        "J, X" : 8, 
        "Q, Z" : 10}

    score = 0 

    for key in point_dict:
        for char in word:
            if char in key:
                score += point_dict[key]

    if len(word) >= 7:
        score += 8
    
    return score 
    


def get_highest_word_score(word_list):

    final_dict = {}

    for word in word_list:
        word = word.upper()
        word_score = score_word(word)
        final_dict[word] = word_score

    winner_score = max(final_dict.values())
    winning_words = []

    for key in final_dict:
        if winner_score == final_dict[key]:
            winning_words.append(key)

    current_length = 10 
    the_winner = ""
    winner_score = 0

    for word in winning_words:
        if len(word) == 10:
            the_winner = word
            winner_score = final_dict[word]
            return the_winner , winner_score
        else:
            if len(word) < current_length:
                current_length = len(word)
                the_winner = word
                winner_score = final_dict[word]

    return the_winner , winner_score
