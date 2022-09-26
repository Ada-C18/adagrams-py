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

LETTER_POINTS = {
    "A, E, I, O, U, L, N, R, S, T": 1,
    "D, G": 2,
    "B, C, M, P": 3,
    "F, H, V, W, Y": 4,
    "K": 5,
    "J, X": 8,
    "Q, Z": 10,
}


def draw_letters():
    from random import sample

    return sample(LETTER_POOL.keys(), counts=LETTER_POOL.values(), k=10)


def uses_available_letters(word, letter_bank):
    upper_word = word.upper()
    return all(
        [
            upper_word.count(letter) <= letter_bank.count(letter)
            for letter in set(upper_word)
        ]
    )


def score_word(word):
    total_score = 0
    word = word.upper()
    if len(word) > 6:
        total_score += 8
    for letter in word:
        for key, score in LETTER_POINTS.items():
            if letter in key:
                total_score += score
    return total_score


def break_tie(words):
    for word in words:
        if len(word) == 10:
            return word
    return min(words, key=len)


def get_highest_word_score(word_list):
    word_scores = {word: score_word(word) for word in word_list}
    # The tuple must contain the following elements:
    # index 0 ([0]): a string of a word
    # index 1 ([1]): the score of that word
    highest_score = max(word_scores.values())
    tied_words = [word for word, score in word_scores.items() if score == highest_score]
    return break_tie(tied_words), highest_score
