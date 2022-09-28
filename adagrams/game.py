import random

def draw_letters():
    """
    input: nothing
    output: 10 random tiles in a list randomly taken from alphabet dictionary.
    """
    allletters = []
    alphabet = {
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
    #expanded dictionary per numbers of letters
    for letter, number in alphabet.items():
        for i in range(number):
            allletters.append(letter)
    
    #picking 10 random letters from expanded dictionary
    gameletters = []
    for letter in range(10):
        number = random.randint(0, 27)
        random_letter = allletters[number]
        gameletters.append(random_letter)
        allletters.remove(random_letter)
        
    return gameletters



def uses_available_letters(word, letter_bank):
    """
    input: word, letter_bank
    output: True if word contains all letters in the letterbank, False if the word contains a letter not in the letterbank.
    """
    letter_bank_copy = letter_bank[:]
    for letter in word:
        letter = letter.capitalize()
        if letter not in letter_bank_copy:
            return False
        else:
            letter_bank_copy.remove(letter)
    return True

### Wave 3: score_word

def score_word(word):
    """
    input: word
    output: the calculated points per word.
    """
    points_dict = {
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
    total_points = 0
    for letter in word:
        letter = letter.capitalize()
        point_value = points_dict[letter]
        total_points += point_value
    if len(word) in range(7, 11):
        total_points += 8 
    return total_points

### Wave 4: get_highest_word_score
def get_highest_word_score(word_list):
    """
    This function takes in an input of word_list containing all the entered words. It calculates the score of each word
    using score_word() and then finds the highest score from all the scores. Finally it returns all of the words that
    equal to that highest score. If there is a tie with multiple highest-scoring words, then our function returns the first
    shortest word unless the length of the word is equal to 10 letters, than our functions returns that 10-letter word.

    input: word_list
    output: winning_words_list
    """
    winning_words_list = []
    maximum_score = 0
    for word in word_list:
        if int(score_word(word)) > maximum_score:
            maximum_score = int(score_word(word))
            winning_words_list = [word]
        elif int(score_word(word)) == maximum_score:
            winning_words_list.append(word)
   
    if len(winning_words_list) == 1:
        winning_words_list.append(maximum_score)
        return tuple(winning_words_list)
   
    else:
        length_word = 10
        for word in winning_words_list:
            if len(word) == 10:
                winning_words_list = [word]
                winning_words_list.append(maximum_score)
                return tuple(winning_words_list)
            elif len(word) < length_word:
                length_word = len(word)
                winning_words_list = [word]
                winning_words_list.append(maximum_score)
        return tuple(winning_words_list)

 
