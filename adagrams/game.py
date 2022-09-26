def draw_letters():
    pass

def uses_available_letters(word, letter_bank):
    word_list = list(word.upper())
    letter_bank_copy = letter_bank.copy()
    return_list = []
    for letter in word_list:
        if letter in letter_bank_copy:
            return_list.append(letter)
            letter_bank_copy.remove(letter)

    if word_list == return_list:
        return True
    else:
        return False

def score_word(word):
    value_1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']
    value_2 = ['D', 'G']
    value_3 = ['B', 'C', 'M', 'P']
    value_4 = ['F', 'H', 'V', 'W', 'Y']
    value_5 = ['K']
    value_8 = ['J', 'X']
    value_10 = ['Q', 'Z']

def get_highest_word_score(word_list):
    pass