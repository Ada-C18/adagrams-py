import random
from symbol import pass_stmt

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
    # initialize sum
    # if len(word) > 6: sum += 8
    # return sum
    pass


def get_highest_word_score(word_list):
    # return tuple with winning word and its score
    # iterate over words, calculate score using helper function
    # set winners_ arr = [first element]
    # if each element score is > score first element, update array.
    # if equal, append

    # if winners array is length of 1, return first element

    # winner = None
    # if score tie:
    # check if any has 10 letters, return the first that has 10 letters
    # else: return the one with the fewest letters

    # #     prefer the word with the fewest letters...
    # ...unless one word has 10 letters. If the top score is tied between multiple words and one is 10 letters long, choose the one with 10 letters over the one with fewer tiles
    # If the there are multiple words that are the same score and the same length, pick the first one in the supplied list

    pass
