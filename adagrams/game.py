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
    # takes in no parameter
    letters = [] # the "hand" with 10 letters that we return
    
    count = 0
    
    new_dict = LETTER_POOL.copy()

    # print("BEFORE: list of letters = ", letters)
    # print("BEFORE: dictionary = ", new_dict)

    # create a list that's 10 letters long
    # random drawing from letters in dictionary — import random module
    while len(letters) < 10:
        random_letter = random.choice(list(new_dict.keys()))

        # ... conditional statement ...
        for k, v in new_dict.items():
            if k == random_letter and v > 1:
                # print("BEFORE change ", k, v)
                letters.append(random_letter)
                v -= 1 # this creates a new value for v
                new_dict[k] = v # this syntax adds updates the value of the dictionary w/in the loop
                # print("AFTER change = ", k, v)
            else:
                continue
        count += 1 # we need to make this change to the dictionary
    # print("Letters list = ", letters)
    return letters


# =========== WAVE TWO ===========
# ================================


def uses_available_letters(word, letter_bank):

    # check input-word only uses letters in hand
    # word = "string"
    # letter_bank = ["list", "of", "strings", "ie letters"]

    word = word.upper()

    word_letters = list(word)
    print("List of letters from WORD = ", word_letters)
    print("Letter Bank = ", letter_bank)

    frequency = {}

    for letter in word_letters:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    print("Frequency of Letters in Word = ", frequency)

    frequency2 = {}

    for letter in letter_bank:
        if letter in frequency2:
            frequency2[letter] += 1
        else:
            frequency2[letter] = 1
    print("Frequency of letters in Bank = ", frequency2)
    
    # REFACTOR: can we refactor these two loops into one?

    # if every letter in word is in letter_bank
    # return True

    common = frequency.items() & frequency2.items() 
    print("Len of COMMON_key:values dict = ", len(common))
    print("Len of HAND dict = ",len(frequency))
    print("Len of LETTER_BANK dict = ", len(frequency2))

    if len(common) == len(frequency):
        return True
    # if every letter in word is NOT in letter_bank
    # return False
    else:
        return False



# =========== WAVE THREE ===========
# ==================================


def score_word(word):

    # POINTS
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

    # GOAL: return the score of given word defined by Adagram
    # word = "string of characters"
    word = word.upper()
    # print("Word list = ", word, ",", type(word), len(word))
    # if the word is 1 letter, return the point

    sum = 0
    # print("Sum = ", sum)

    # if length of word is 7, 8, 9, or 10 -->
        # then the word gets 8 extra points
    if len(word) >= 7 and len(word) <= 10:
        sum += 8

    # each letter within word has a point value
    # sum up the total number of points for the word

    for letter in word:
        if letter in score_chart.keys():
            # print("BEFORE: sum changes", sum)
            sum += score_chart[letter]
            # print("The letter's value = ", letter, score_chart[letter])
            # print("AFTER: sum changes", sum)
    # return an integer representing the number of points
    # return <int>
    return sum
    # print("Total after iteration = ", sum)



# =========== WAVE FOUR ===========
# =================================

# I think I want to rename the variables in this project for consistency :)

def get_highest_word_score(word_list):
    
    # print(word_list)

    # # score_list = []
    score_dict = {}

    for word in word_list:
        word_score = score_word(word)
        # score_list.append((word, word_score))
        score_dict[word] = word_score
    print("Score Dict = ", score_dict)
    # print(score_list)

    max_score = max(score_dict.values())
    print("Max Score = ", max_score)


    tied_scores = []
    for k, v in score_dict.items():
        if v == max_score:
            best_word = (k, v)
            # return best_word
            tied_scores.append(best_word)
    # print(tied_scores)

    sort_ties = sorted(tied_scores)
    print("Shorted List = ", sort_ties)
    shortest = max(sort_ties) # this is kind of confusing me??
    highest = min(sort_ties)
    print("Shorest Char Score = ", shortest)
    print("Highest Char Score = ", highest)


    for scores in sort_ties:

        if len(scores[0]) == 10:
            print(scores)
            return scores

        elif scores == shortest:
            print(scores)
            return scores