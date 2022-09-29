import random
import copy

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

#WAVE ONE
def dict_to_list(dict):
    '''
    Create a list using the key-value pairs from the inputted dictionary.
    1. Start with an empty list.
    2. Iterate through each key-value pair, adding the key to the list n times, with n being the associated value to the key. 
    3. Return the list.
    '''
    bag_of_letters = []
    for key, value in dict.items(): 
        new_letters = [key] * value 
        bag_of_letters.extend(new_letters) 
    
    return bag_of_letters

def draw_letters():
    '''
    Return a list of ten randomized letters, drawn from the bag_of_letters.
    1. Create a bag_of_letters list with appropriate distribution by passing through LETTER_POOL dictionary.
    2. Use the random.randint generator to select a unique integer, which represents the index of the letter 
    to be drawn from the bag_of_letters list.
    3. Repeat step #2 until 10 letters have been randomized.
    4. Return the ten letters in a list format.
    '''
    bag_of_letters = dict_to_list(LETTER_POOL)
    hand_as_numbers = []
    hand_as_letters = []

    while len(hand_as_letters) < 10: 
        index = random.randint(0,len(bag_of_letters)-1) 
        if index not in hand_as_numbers: 
            hand_as_numbers.append(index) 
            hand_as_letters.append(bag_of_letters[index]) 
    
    return hand_as_letters


#WAVE TWO
def uses_available_letters(word, letter_bank):
    '''
    Check if the word is an anagram of some or all of the given letters in the hand
    1. Iterate through every letter in word to check if every letter in the `input` word is available in the letter_bank.
    2. Return False if there is a letter in `input` that is not present in the `letter_bank` 
    or has too much of compared to the letter_bank. Otherwise, return True.
    '''
    copy_of_letter_bank = copy.deepcopy(letter_bank)
    word = word.upper()

    for letter in word: 
        try:
            copy_of_letter_bank.remove(letter) 
        except:
            return False 
    return True


#WAVE THREE
SCORING = {
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
    'Z': 10
}

def score_word(word):
    '''
    Calculate the score of the word
    1. Iterate through each character in the word, adding the associated value of each letter per the SCORING dictionary.
    2. If the length of the word is 7, 8, 9, or 10, add an additional 8 points to the score.
    3. Return score.
    '''
    score = 0
    for letter in word.upper(): 
        score += SCORING[letter] 
        
    if 7 <= len(word) <= 10: 
        score += 8 
    
    return score


#WAVE FOUR
def get_highest_word_score(word_list):
    '''
    Find the highest scoring word
    1. Create a dictionary words_and_scores. Populate it with the key being every word in word_list and value being the associated score.
    2. Calculate the highest score, and create a list highest_scoring_words with words that have the highest score.
    3. In the case of no ties, assign winning_word as the first and only item in the highest_scoring_words.
    2. In the case of tie in scores, check if there is string with 10 characters, otherwise assign the 
    winning_word as that with fewest characters.
    3. Return a tuple that represents the data of a winning_word and its score.
    '''
    words_and_scores = {}
    for word in word_list:
        words_and_scores[word] = score_word(word) 
    
    highest_score = max(words_and_scores.values()) 
    highest_scoring_words = [word for word, score in words_and_scores.items() if score == highest_score] 
    winning_word = highest_scoring_words[0] 

    if len(highest_scoring_words) != 1:
        words_with_10 = [word for word in highest_scoring_words if len(word) == 10] 
        try:
            winning_word = words_with_10[0] 
        except:
            winning_word = min(highest_scoring_words, key=len) 
    
    return (winning_word, words_and_scores[winning_word])