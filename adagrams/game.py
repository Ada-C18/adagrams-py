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

def dict_to_list(dict):
    bag_of_letters = []
    for key, value in dict.items():
        new_letters = [key] * value
        bag_of_letters.extend(new_letters)
    
    return bag_of_letters

def draw_letters():
    bag_of_letters = dict_to_list(LETTER_POOL)
    hand_as_numbers = []
    hand_as_letters = []
    
    while len(hand_as_letters) < 10:
        index = random.randint(0,len(bag_of_letters)-1)
        if index not in hand_as_numbers:
            hand_as_numbers.append(index)
            hand_as_letters.append(bag_of_letters[index])
    
    return hand_as_letters



#WAVE TWO
def uses_available_letters(word, letter_bank):
    copy_of_letter_bank = copy.deepcopy(letter_bank)
    word = word.upper()
    for letter in word:
        if letter not in copy_of_letter_bank:
            return False
        else:
            copy_of_letter_bank.remove(letter)
    return True


#WAVE THREE

SCORING = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X'],
    10: ['Q', 'Z']
}

def score_word(word):
    score = 0
    word = word.upper()

    if len(word) >= 7:
        score += 8

    for letter in word:
        for key, value in SCORING.items():
            if letter in value:
                score += key

    return score

def get_highest_word_score(word_list):
    words_and_scores = {}

    for word in word_list:
        words_and_scores[word] = score_word(word)
    highest_score = max(words_and_scores.values())

    words_with_highest_scores = []

    for word,score in words_and_scores.items():
        if score == highest_score:
            words_with_highest_scores.append(word)

    winning_word = words_with_highest_scores[0]
    target_length = len(min(words_with_highest_scores, key = len))
    words_with_10 = [word for word in words_with_highest_scores if len(word) == 10]
    if words_with_10:
        target_length = 10 

    if len(words_with_highest_scores) != 1:
        for word in words_with_highest_scores:
            if len(word) == target_length:
                winning_word = word
                break 
    return (winning_word,words_and_scores[winning_word])    




    pass