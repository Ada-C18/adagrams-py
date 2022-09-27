import random, string

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
    # english_letters = list(string.ascii_uppercase)
    # letters_frequency = [9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1]
    # num_of_letters_draw = 10
    # letter_bank = random.choices(english_letters, weights=letters_frequency, k=num_of_letters_draw)
    # return letter_bank

    letter_pool_dict = LETTER_POOL.copy()
    hand_of_letters = []

    while len(hand_of_letters) < 10:
        random_letter = random.choice(list(letter_pool_dict.keys()))
        if letter_pool_dict[random_letter] > 0:
            hand_of_letters.append(random_letter)
            letter_pool_dict[random_letter] -= 1

    return hand_of_letters


def uses_available_letters(word, letter_bank):
    upper_case_word = word.upper()
    input_letter_bank = letter_bank.copy()

    for character in upper_case_word:
        if character not in input_letter_bank:
            return False
        elif character in input_letter_bank:
            input_letter_bank.remove(character)

    return True

def score_word(word):
    score_chart_dict = {
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"]
    }
    score = 0
    word_in_upper = word.upper()
    for letter in word_in_upper:
        for key, value in score_chart_dict.items():
            if letter in value:
                score += key
    if len(word_in_upper) > 6 and len(word_in_upper) < 11:
        score += 8
    
    return score

def get_highest_word_score(word_list):
    scores_dict = {}
    for word in word_list:
        score = score_word(word)
        scores_dict[word] = score
    max_score = max(scores_dict.values())
    for word, score in scores_dict.items():
        if score == max_score:
            return (word, score)
    # print("!!!!!!!!!!!")
    # print(scores_dict)
    # print(max_score)