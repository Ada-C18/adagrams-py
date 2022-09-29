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


##    Main Function #1    ##
def draw_letters():
    letters = []

    while len(letters) < 10:
        random_letter = random.choice(list(LETTER_POOL.keys()))
        
        if letters.count(random_letter) < LETTER_POOL[random_letter]:
            letters.append(random_letter)

    return letters



##    Main Function #2   ##
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
#   word_list = list of strings
#   Which word in word_list has highest score?
#   Apply tie-breaking logic:
#       - prefer word with fewest letters (unless it has 10 letters)
#       - if tied words have same score and length, pick first appearance in word_list.
#   return tuple ('winning_word', score)

    word_scores = {}
    highest_scoring = []

    # fills dictionary with word and its score.
    for word in word_list:
        word_scores[word] = score_word(word)

    # takes word with highest score from dictionary and
    #       appends it to highest_scoring as a tuple.
    max_value = max(word_scores.values())
    print(f"MAX: {max_value}")
    for key, value in word_scores.items():
        if value == max_value:
            highest_scoring.append((key, value))

# NEED TO BREAK TIES!
# NEED TO RETURN A SINGLE TUPLE

    return highest_scoring


# for programmers testing use
print(get_highest_word_score(["X", "XX", "JJH", "XXW", "QQ"]))