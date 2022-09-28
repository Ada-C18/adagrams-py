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


score_chart = {
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


def draw_letters():
    letter_pool_copy = LETTER_POOL.copy()
    hand = []
    while len(hand) < 10:
        # letter = random.choice(list(LETTER_POOL.keys()))
        # find out why code work with random.choices with weighted avg and random.choice.what is happening behind those scence.is there an advantage to using random.choice over .choices
        letter = random.choices(list(LETTER_POOL.keys()), weights=[
                                9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1], k=1)[0]

        if letter_pool_copy[letter] > 0:

            hand.append(letter)
            letter_pool_copy[letter] -= 1
    return hand


def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank.copy()
    if len(word) > len(letter_bank_copy):
        return False
    for letter in word.upper():
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False

    return True


def score_word(word):

    score = 0
    if 7 <= len(word) <= 10:
        score += 8
    for letter in word.upper():
        if letter.isalpha():
            score += score_chart.get(letter)
    return score


def get_highest_word_score(word_list):
    pass
