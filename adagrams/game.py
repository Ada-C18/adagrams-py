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

def uses_available_letters(word, letter_bank):
    word = word.upper()
    word_dict = {}
    letter_count = 0
    is_valid = False

    for letter in word:
        if letter in letter_bank and word.count(letter) <= letter_bank.count(letter):
            word_dict[letter] = True
            letter_count += 1
            is_valid = True
        elif not letter in letter_bank:
            word_dict[letter] = False
            is_valid = False
    return is_valid

### Wave 3: score_word

# Now you need a function returns the score of a given word as defined by the Adagrams game.

# Implement the function `score_word` in `game.py`. This method should have the following properties:

# - Has one parameter: `word`, which is a string of characters
# - Returns an integer representing the number of points
# - Each letter within `word` has a point value. The number of points of each letter is summed up to represent the total score of `word`
# - Each letter's point value is described in the table below
# - If the length of the word is 7, 8, 9, or 10, then the word gets an additional 8 points

# #### Score chart

# |Letter                        | Value|
# |:----------------------------:|:----:|
# |A, E, I, O, U, L, N, R, S, T  |   1  |
# |D, G                          |   2  |
# |B, C, M, P                    |   3  |
# |F, H, V, W, Y                 |   4  |
# |K                             |   5  |
# |J, X                          |   8  |
# |Q, Z                          |   10 |

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass