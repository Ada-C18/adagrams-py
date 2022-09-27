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
    "A": 1,
    "N": 1,
    "B": 3,
    "O": 1,
    "C": 3,
    "P": 3,
    "D": 2,
    "Q": 10,
    "E": 1,
    "R": 1,
    "F": 4,
    "S": 1,
    "G": 2,
    "T": 1,
    "H": 4,
    "U": 1,
    "I": 1,
    "V": 4,
    "J": 8,
    "W": 4,
    "K": 5,
    "X": 8,
    "L": 1,
    "Y": 4,
    "M": 3,
    "Z": 10,
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
    total_score = sum([LETTER_POINTS.get(letter, 0) for letter in word.upper()])
    if len(word) > 6:
        total_score += 8
    return total_score


# The tuple must contain the following elements:
# index 0 ([0]): a string of a word
# index 1 ([1]): the score of that word


def break_tie(words):
    # key lambda returns 0 "length" to win if word uses all 10 letters
    return min(words, key=lambda w: 0 if len(w) == 10 else len(w))


def get_highest_word_score(word_list):
    word_scores = {word: score_word(word) for word in word_list}
    highest_score = max(word_scores.values())
    tied_words = [word for word, score in word_scores.items() if score == highest_score]
    return break_tie(tied_words), highest_score
