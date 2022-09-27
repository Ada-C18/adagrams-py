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
    scores_dict = {}
    for word in word_list:
        score = score_word(word)
        scores_dict[word] = score

    max_score = max(scores_dict.values())
    words_with_max_score_list = []

    for word, score in scores_dict.items():
        if score == max_score:
            words_with_max_score_list.append(word)
    
    if len(words_with_max_score_list) == 1:
        return (words_with_max_score_list[0], max_score)
    elif len(words_with_max_score_list) > 1:
        longest_word = max(words_with_max_score_list, key=len)
        print(f"longest word: {longest_word}")
        shortest_word = min(words_with_max_score_list, key=len)
        print(f"shortest word: {shortest_word}")
        if len(longest_word) == 10:
            return (longest_word, max_score)
        elif len(longest_word) < 10:
            return (shortest_word, max_score)
        else:
            return (words_with_max_score_list[0], max_score)
            # for word in word_list:
            #     for max_score_word in words_with_max_score_list:
            #         if max_score_word == word:
            #             return (max_score_word, max_score)
    # print("!!!!!!!!!!!")
    # print(scores_dict)
    # print(max_score)