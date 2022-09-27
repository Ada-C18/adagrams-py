import random, string


def draw_letters():
    english_letters = list(string.ascii_uppercase)
    letters_frequency = [9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1]
    num_of_letters_draw = 10
    letter_bank = random.choices(english_letters, weights=letters_frequency, k=num_of_letters_draw)
    return letter_bank


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