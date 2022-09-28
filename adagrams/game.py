import random
import string


# WAVE 1
def draw_letters():
    hand = []

    pool = {
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
        "Z": 1,
    }

    while len(hand) < 10:
        random_letter = random.choice(string.ascii_uppercase)

        if random_letter in hand:
            letter_count = hand.count(random_letter)
            if letter_count < pool[random_letter]:
                hand.append(random_letter)
            else:
                continue
        else:
            hand.append(random_letter)
    return hand


# WAVE 2
def uses_available_letters(word, letter_bank):
    word_dict = {}
    letter_bank_dict = {}

    for letter in letter_bank:
        letter_bank_dict[letter] = letter_bank.count(letter)

    word = word.upper()

    for letter in word:
        word_dict[letter] = word.count(letter)
        if letter not in letter_bank_dict:
            return False

    for letter, freq in word_dict.items():
        if freq <= letter_bank_dict[letter]:
            return True
        else:
            return False


# WAVE 3
def score_word(word):
    score_chart = {
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"],
    }

    points = 0

    word = word.upper()
    for letter in word:
        for point, letter_list in score_chart.items():
            if letter in letter_list:
                points += point

    if len(word) > 6 and len(word) < 11:
        points += 8

    return points


# WAVE 4
def get_highest_word_score(word_list):
    ''' 
    Input: list of strings
    Output: a tuple with (word str, score of that word)
    '''

    word_score_dict = {}

    for word in word_list:
        score = score_word(word)
        word_score_dict[word] = score

    highest_score = 0
    highest_score_words = []

    for word, score in word_score_dict.items():
        if score > highest_score:
            highest_score = score
            highest_score_words = [word]
        elif score == highest_score:
            highest_score_words.append(word)

    if len(highest_score_words) == 1:
        return (highest_score_words[0], highest_score)
    elif len(highest_score_words) == 0:
        return None
    else:
        first_highest = highest_score_words[0]
        second_highest = highest_score_words[1]

        if len(first_highest) == len(second_highest):
            return (first_highest, highest_score)
        else:
            if len(first_highest) == 10:
                return (first_highest, highest_score)
            elif len(second_highest) == 10:
                return (second_highest, highest_score)

        if len(first_highest) < len(second_highest):
            return (first_highest, highest_score)
        elif len(second_highest) < len(first_highest):
            return (second_highest, highest_score)