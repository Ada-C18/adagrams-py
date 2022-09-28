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


def draw_letters():
    hand = []
    letters = []

    for k, v in LETTER_POOL.items():
        while v > 0:
            letters.append(k)
            v -= 1

    for i in range(10):
        letter = ""

        while not letter:
            index = random.randint(0, 97)
            letter = letters[index]

        hand.append(letter)
        letters[index] = ""

    return hand


def uses_available_letters(word, letter_bank):

    word = word.upper()
    letter_bank_dict = {}

    for letter in letter_bank:
        if letter in letter_bank_dict:
            letter_bank_dict[letter.upper()] += 1
        else:
            letter_bank_dict[letter.upper()] = 1

    for letter in word:
        if letter not in letter_bank_dict:
            return False
        elif letter_bank_dict[letter] == 0:
            return False
        else:
            letter_bank_dict[letter] -= 1

    return True


def score_word(word):

    letters_dict = {
        'A': 1,
        'B': 3,
        'C': 3,
        'D': 2,
        'E': 1,
        'F': 4,
        'G': 2,
        'H': 4,
        'I': 1,
        'J': 9,
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
    sum = 0

    for letter in word:
        value = letters_dict[letter.upper()]
        sum += value

    if len(word) > 6:
        sum += 8

    return sum


def get_highest_word_score(word_list):

    winner_arr = [{"word": word_list[0], "score": score_word(word_list[0])}]

# changed to word_list[1:] so that we can skip the first element in the array
    for word in word_list[1:]:
        word_score = score_word(word)
        if word_score > winner_arr[0]["score"]:
            winner_arr = [{"word": word, "score": word_score}]
        elif word_score == winner_arr[0]["score"]:
            # error was here
            winner_arr.append({"word": word, "score": word_score})

    if len(winner_arr) == 1:
        return (winner_arr[0]["word"], winner_arr[0]["score"])

    winner = (winner_arr[0]["word"], winner_arr[0]["score"])

    for word in winner_arr:
        if len(word["word"]) == 10:
            return (word["word"], word["score"])
        elif len(word["word"]) < len(winner[0]):
            winner = (word["word"], word["score"])
            print(f"updated loop winner: {winner}")

    return winner


# alternate implementation
# def get_highest_word_score(word_list):

#     words_dict = {}

#     for word in word_list:
#         words_dict[word] = score_word(word)

#     winner = (word_list[0], words_dict[word_list[0]])

#     for k, v in words_dict.items():
#         if v > winner[1]:
#             winner = (k, v)
#         if v == winner[1] and len(winner[0]) < 10:
#             if len(k) == 10:
#                 winner = (k, v)
#             elif len(k) < len(winner[0]):
#                 winner = (k, v)

#     return winner
