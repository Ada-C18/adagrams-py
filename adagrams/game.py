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

# =========== WAVE ONE ===========
# ================================

def draw_letters():
    
    letters = []
    
    count = 0
    
    new_letter_dict = LETTER_POOL.copy()

    while len(letters) < 10:
        random_letter = random.choice(list(new_letter_dict.keys()))
        for letter, points in new_letter_dict.items():
            if letter == random_letter and points > 1:
                letters.append(random_letter)
                points -= 1
                new_letter_dict[letter] = points
            else:
                continue
        count += 1 
    
    return letters

# =========== WAVE TWO ===========
# ================================

def uses_available_letters(word, letter_bank):

    word = word.upper()

    list_of_words = list(word)

    frequency_in_word = {}

    for letter in list_of_words:
        if letter in frequency_in_word:
            frequency_in_word[letter] += 1
        else:
            frequency_in_word[letter] = 1

    frequency_in_bank = {}

    for letter in letter_bank:
        if letter in frequency_in_bank:
            frequency_in_bank[letter] += 1
        else:
            frequency_in_bank[letter] = 1


    common = frequency_in_word.items() & frequency_in_bank.items() 

    if len(common) == len(frequency_in_word):
        return True
    else:
        return False

# =========== WAVE THREE ===========
# ==================================

def score_word(word):

    score_chart = {
    'A': 1,
    'E': 1,
    'I': 1,
    'O': 1,
    'U': 1,
    'L': 1,
    'N': 1,
    'R': 1,
    'S': 1,
    'T': 1,
    'D': 2,
    'G': 2,
    'B': 3,
    'C': 3,
    'M': 3,
    'P': 3,
    'F': 4, 
    'H': 4,
    'V': 4,
    'W': 4,
    'Y': 4,
    'K': 5,
    'J': 8,
    'X': 8,
    'Q': 10,
    'Z': 10,
    }

    word = word.upper()
    
    sum = 0

    if len(word) >= 7 and len(word) <= 10:
        sum += 8

    for letter in word:
        if letter in score_chart.keys():
            sum += score_chart[letter]
    return sum

# =========== WAVE FOUR ===========
# =================================

def get_highest_word_score(word_list):
    
    scores_dict = {}

    for word in word_list:
        score_of_word = score_word(word)
        scores_dict[word] = score_of_word

    max_score = max(scores_dict.values())

    highest_tied_scores = []
    for word, score in scores_dict.items():
        if score == max_score:
            best_word = (word, score)
            highest_tied_scores.append(best_word)

    sorted_highest_tied_scores = sorted(highest_tied_scores)

    # longest = max(sorted_highest_tied_scores, key=lambda scores: len(scores[0]))
    shortest = min(sorted_highest_tied_scores, key=lambda scores: len(scores[0]))

    for scores in sorted_highest_tied_scores:
        if len(scores[0]) == 10:
            return scores
        elif scores == shortest:
            return scores