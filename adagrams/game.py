import random

LETTER_DISTRIBUTION = {
    "A": 9,
    "B": 2,
    "C": 2,
    "D": 4,
    "E": 12,
    "F": 2,
    "G": 3,
    "H": 2,
    "I": 9,
    "J": 1,
    "K": 1,
    "L": 4,
    "M": 2,
    "N": 6,
    "O": 8,
    "P": 2,
    "Q": 1,
    "R": 6,
    "S": 4,
    "T": 6,
    "U": 4,
    "V": 2,
    "W": 2,
    "X": 1,
    "Y": 2,
    "Z": 1
}

SCORE_CHART = {
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],  
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"]
}

def draw_letters():
    letter_pool = []
    letter_bank = []
    for letter, count in LETTER_DISTRIBUTION.items():
        for i in range(count):
            letter_pool.append(letter)
    # NOTE: can we rewrite 45-47 with list comprehension? or move to helper function?:
    # letter_pool = [[letter] * count for letter, count in LETTER_DISTRIBUTION.items()]
    for letter in range(10):
        random_letter = random.choice(letter_pool)
        letter_bank.append(random_letter)
        letter_pool.remove(random_letter)
    return letter_bank

def uses_available_letters(word, letter_bank):
    bank_dict = {}
    # NOTE: I think we can rewrite this using dictionary comprehension?
    for item in letter_bank:
        if item not in bank_dict:
            bank_dict[item] = 1
        else:
            bank_dict[item] += 1
    for letter in word.upper():
        if letter not in bank_dict.keys():
            return False
        elif letter in bank_dict.keys():
            bank_dict[letter] -= 1
        
        if bank_dict[letter] < 0:
            return False
    return True

def score_word(word):
    total_score = 0
    for character in word.upper():
        for tally, letters in SCORE_CHART.items():
            if character in letters:
                total_score += tally
    if len(word) >= 7:
        total_score += 8
    return total_score

def get_highest_word_score(word_list):
    word_info = [{"word": word, "score": score_word(word), "length": len(word)}
                for word in word_list]
    print(word_info)    

    highest_score = max(word_info, key=lambda word_info: word_info["score"])
    
    word_info = list(filter(lambda word_dict: word_dict["score"]
                            == highest_score["score"], word_info))
    # We also came up with this implementation for line 91-92:
    # for word_dict in word_info:
    #     print("the score is:")
    #     print(word_dict["score"])
    #     if word_dict["score"] != highest_score["score"]:
    #         word_info.remove(word_dict)
    
    smallest_length = min(word_info, key=lambda word_info: word_info["length"])

    for word_dict in word_info:
        if word_dict["length"] == 10:
            return word_dict["word"], word_dict["score"]

    for word_dict in word_info:
        if word_dict["length"] == smallest_length["length"]:
            return word_dict["word"], word_dict["score"]

get_highest_word_score(["MMMM", "WWW"])