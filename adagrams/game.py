def draw_letters():

    # Create empty list
    # Create empty counter dictionary
    # Use for loop i in range(10)
    # Use a built in funciton to draw random letter random.choice()
    #
    # Use if statement to check if random letter is not drawn more
    # than dict value comparing values from counter dict
    # Append to empty list
    # Return list of 10 letters(strings)
    LETTER_POOL = {
        "A": 9,
        "B": 2,
        "C": 2,
        "D": 4,
        "E": 12,
        "F": 2,
        "G": 3,
        "H": 2,
        "I": 9,
        "J": 1,
        "K": 1,
        "L": 4,
        "M": 2,
        "N": 6,
        "O": 8,
        "P": 2,
        "Q": 1,
        "R": 6,
        "S": 4,
        "T": 6,
        "U": 4,
        "V": 2,
        "W": 2,
        "X": 1,
        "Y": 2,
        "Z": 1,
    }
    letter_list = []
    pool_list = []
    i = 0
    for letter in LETTER_POOL.keys():
        for i in range(LETTER_POOL[letter]):
            pool_list.append(letter)
    letter_list = random.sample(pool_list, 10)
    print(letter_list)


def uses_available_letters(word, letter_bank):
    word_dict = {}
    for letter in word:
        word_dict[letter.upper()] = (
            word_dict.get(letter, 0) + 1
        )  # using .get to make dict
    for letter in word_dict.keys():
        if word_dict[letter] > letter_bank.count(letter):
            return False
    return True


def score_word(word):
    score_chart = {
        "A": 1,
        "E": 1,
        "I": 1,
        "O": 1,
        "U": 1,
        "L": 1,
        "N": 1,
        "R": 1,
        "S": 1,
        "T": 1,
        "D": 2,
        "G": 2,
        "B": 3,
        "C": 3,
        "M": 3,
        "P": 3,
        "F": 4,
        "H": 4,
        "V": 4,
        "W": 4,
        "Y": 4,
        "K": 5,
        "J": 8,
        "X": 8,
        "Q": 10,
        "Z": 10,
    }
    score = 0
    for letter in word:
        if not letter.isalpha():  # if it's special characters
            score += 0  # skip and add 0 to score
        else:
            score += score_chart[letter.upper()]
    if len(word) in [7, 8, 9, 10]:
        score += 8
    return score


def get_highest_word_score(word_list):
    # create a dictionary score_dict={}
    # for every word in word_list, get score by using score_word()
    # put word:score pair in score_dict={word1:score1, word2:score2...}
    # find max score and store it in a list;
    # if len(max_scores)==1, return tuple at end of function
    # else, if a word = len(10), return that tuple
    # if no word has 10 letters, return the shortest one
    # return word,score
    score_dict = {}
    for word in word_list:
        score_dict[word.upper()] = score_word(word)


# get_highest_word_score(["X", "XX", "XXX", "XXXX"])
