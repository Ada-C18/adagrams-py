import random, string


def draw_letters():
    english_letters = list(string.ascii_uppercase)
    letters_frequency = [9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1]
    num_of_letters_draw = 10
    letter_bank = random.sample(english_letters, counts=letters_frequency, k=num_of_letters_draw)
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
    score_chart_dict = {
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"]
    }
    score = 0
    word_in_upper = word.upper()
    for letter in word_in_upper:
        for key, value in score_chart_dict.items():
            if letter in value:
                score += key
    if len(word_in_upper) > 6 and len(word_in_upper) < 11:
        score += 8
    
    return score


def get_highest_word_score(word_list):
    words_dict = {}
    max_score_words_list= []
    for word in word_list:
        score = score_word(word)
        words_dict[word] = score
    max_score = max(words_dict.values())
    for word, score in words_dict.items():
        if score == max_score:
            if len(word) == 10:
                return (word, score)
            max_score_words_list.append(word)
    sorted_max_score_words = sorted(max_score_words_list, key=len)
    return (sorted_max_score_words[0], max_score)

