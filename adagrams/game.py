def draw_letters():
    pass

def uses_available_letters(word, letter_bank):
    upper_case_word = word.upper()
    input_letter_bank = letter_bank.copy()

    for character in upper_case_word:
        if character not in input_letter_bank:
            return False
        elif character in input_letter_bank:
            input_letter_bank.remove(character)

    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass