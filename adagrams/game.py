LETTER_POOL = {
    'A': 9, 'B': 2, 'C': 2,'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 
    'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2,  'Q': 1, 'R': 6, 
    'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
}

def draw_letters():
    letters_not_drawn = list(LETTER_POOL.keys())
    letters_drawn = []
    letter_count = 0

    for letter in letters_not_drawn:
        if letter not in letters_drawn and len(letters_drawn) < 10:
            letters_drawn.append(letter)
            letter_count += 1
    return letters_drawn

### Wave 2: use_available_letters

# Next, you need a way to check if an input word (a word a player submits) only uses characters that are contained within a collection (or hand) of drawn letters. Essentially, you need a way to check if the word is an anagram of some or all of the given letters in the hand.

# To do so, implement the function called `uses_available_letters` in `game.py`. This function should have the following properties:

# - Has two parameters:
#    - `word`, the first parameter, describes some input word, and is a string
#    - `letter_bank`, the second parameter, describes an array of drawn letters in a hand. You can expect this to be an array of ten strings, with each string representing a letter
# - Returns either `True` or `False`
# - Returns `True` if every letter in the `input` word is available (in the right quantities) in the `letter_bank`
# - Returns `False` if not; if there is a letter in `input` that is not present in the `letter_bank` or has too much of compared to the `letter_bank`


def uses_available_letters(word, letter_bank):
    # word = word.upper()
    word_dict = {}
    letter_count = 0
    is_valid = False

    for letter in word:
        if letter in letter_bank and letter_count <= LETTER_POOL[letter]:
            word_dict[letter] = True
            letter_count += 1
            is_valid = True
        elif not letter in letter_bank:
            word_dict[letter] = False
            is_valid = False
    return is_valid
        # else:
        #     return True

    # def build_word_dict(snowman_word):
    # """This function takes snowman_word as input and returns 
    # a dictionary with a key-value pair for each letter in 
    # snowman_word where the key is the letter and the value is `False`.
    # """
    # snowman_word_dict = {}
    # for letter in snowman_word:
    #     snowman_word_dict[letter] = False
    # return snowman_word_dict

    # if not snowman_dict[letter] 


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass