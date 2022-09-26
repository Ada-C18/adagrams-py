# NOTE from Dainiz: I changed this variable name so I could use letter_pool in
# draw_letters() but we can change things up if another way makes more sense to you!
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

def draw_letters():
    letter_pool = []
    for letter, count in LETTER_DISTRIBUTION.items():
        for i in range(count):
            letter_pool.append(letter)
    pass

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass