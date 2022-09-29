from audioop import add
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

SCORE_CHART = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
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



def draw_letters():
    letters = []

    while len(letters) < 10:
        random_letter = random.choice(list(LETTER_POOL.keys()))
        
        if letters.count(random_letter) < LETTER_POOL[random_letter]:
            letters.append(random_letter)

    return letters



def uses_available_letters(word, letter_bank):
    available_letters = letter_bank[:]
    upper_word = word.upper()

    for letter in upper_word:
        if letter not in available_letters:
            return False
        else:
            available_letters.remove(letter)

    return True



def score_word(word):
    score = 0
    upper_word = word.upper()

    for letter in upper_word:
        if letter in SCORE_CHART:
            score += SCORE_CHART[letter]

    if len(word) >= 7:
        score += 8

    return score



def get_highest_word_score(word_list):

    word_scores = {}
    highest_scoring = []

    for word in word_list:
        word_scores[word] = score_word(word)

    max_score = max(word_scores.values())
    print(f"MAX: {max_score}")
    for word, score in word_scores.items():
        if score == max_score:
            highest_scoring.append((word, score))

    highest_scoring.sort(key=lambda x: len(x[0]))

    for i in range(len(highest_scoring)):
        word = highest_scoring[i][0]

        if len(word) == 10:
            return highest_scoring[i]

    return highest_scoring[0]