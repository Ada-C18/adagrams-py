def draw_letters():
    letter_pool = []
    letter_pool_amounts = {
        'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12,
        'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1,
        'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8,
        'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6,
        'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
    }

    # iterate through letter_pool_amounts keys and values
    for letter, number in letter_pool_amounts.items():
    # for each key, add it [value] number of times to letter_pool list
        for value in range(number):
            letter_pool.append(letter)

    # use random.randint w/ index 10 times to draw 10 random letters

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass