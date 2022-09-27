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
    hand = []  # renamed res to hand
    letters = []

    for k, v in LETTER_POOL.items():
        while v > 0:
            letters.append(k)
            v -= 1

    for i in range(10):  # do code below 10 times
        letter = ""  # set letter to be empty so while loop runs

        while not letter:  # check if index in our letters is used/empty, if not, get another random integer
            # hoping to get a random integer between 0 and 97
            index = random.randint(0, 97)
            letter = letters[index]

        hand.append(letter)
        letters[index] = ""

    return hand


def uses_available_letters(word, letter_bank):

    word = word.upper()
    # make dictionary of letter_bank
    letter_bank_dict = {}

# ["a", "b", "c"]
    for letter in letter_bank:
        if letter in letter_bank_dict:
            letter_bank_dict[letter.upper()] += 1
        else:
            letter_bank_dict[letter.upper()] = 1
# "banana"
    for letter in word:
        if letter not in letter_bank_dict:
            return False
        elif letter_bank_dict[letter] == 0:
            return False
        else:
            letter_bank_dict[letter] -= 1

    return True


def score_word(word):
    # PSE 2
    # dict of letters
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
    # initialize sum
    sum = 0

    for letter in word:
        value = letters_dict[letter.upper()]
        sum += value

    if len(word) > 6:
        sum += 8
    # if len(word) > 6: sum += 8
    return sum


def get_highest_word_score(word_list):
    # word_ list = ["apple", "banana", "orange"]

    # winner_arr = []
    # {word: "apple", score: 5}
    # iterate over words, calculate score using score_word
    # set winners_ arr = [first element]
    # if each element score is > score first element, update array.
    # if equal, append
    # [{word: "apple", score: 5}, {word: "banana", score: 5}]

    # if len(winner_arr) == 1:
    # return as tuple

    # if more than 1 element in winner_arr:
    # check if any has 10 letters, return the first that has 10 letters

    # winner variable
    # else: return the one with the fewest letters
