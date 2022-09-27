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
    point_dict = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F" : 4, "G": 2, "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10}

    score = 0 
    length_points = 8

    for char in word:
        if char in point_dict:
            score += point_dict[char]
    
    if len(word) >= 7:
        score += 8
    
    return score 



def get_highest_word_score(word_list):
    
    final_tuple = ()

    final_dict = {}

    for word in word_list:
        word = word.upper()
        word_score = score_word(word)
        print(f"the word is {word}, the score is {word_score}")
        final_dict[word] = word_score

    the_winner = ""
    winner_score = 0
    for word in final_dict:
        if len(word) == 10:
            the_winner = word
            winner_score = final_dict[word]
            break
        return the_winner, winner_score

    winner_score = max(final_dict.values())
    print("winner score is ", winner_score)
    winning_words = []

    for key in final_dict:
        if winner_score == final_dict[key]:
            print("winner score is", winner_score)
            print("final_dict[key] is", final_dict[key])
            winning_words.append(key)
            print(winning_words)

    current_length = 10 #len(winning_words[0])

    for word in winning_words:
        print("the word is ", word)
        
        # if len(word) == 10:
        #     the_winner = word
        # else:
        if len(word) < current_length:
            current_length = len(word)
            the_winner = word
    print("result: ", the_winner , winner_score)
    return the_winner , winner_score

words = ["X", "XX", "XXX", "XXXX"]

# Act
best_word = get_highest_word_score(words)