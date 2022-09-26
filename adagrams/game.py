from random import sample

LETTER_POOL = {
    "A": 9,
    "N": 6,
    "B": 2,
    "O": 8,
    "C": 2,
    "P": 2,
    "D": 4,
    "Q": 1,
    "E": 12,
    "R": 6,
    "F": 2,
    "S": 4,
    "G": 3,
    "T": 6,
    "H": 2,
    "U": 4,
    "I": 9,
    "V": 2,
    "J": 1,
    "W": 2,
    "K": 1,
    "X": 1,
    "L": 4,
    "Y": 2,
    "M": 2,
    "Z": 1,
}


def draw_letters():
    # draw ten random letters from the letter pool
    # append them to an array and return

    # pool = ""
    # for letter, count in letter_pool.items():
    #     pool += letter * count

    draw = sample(LETTER_POOL.keys(), counts=LETTER_POOL.values(), k=10)
    return draw


def uses_available_letters(word, letter_bank):
    word = word.upper()
    for letter in set(word):
        letter_freq = word.count(letter)
        if letter_freq > letter_bank.count(letter):
            return False
    return True


def score_word(word):
    pass


def get_highest_word_score(word_list):
    pass
