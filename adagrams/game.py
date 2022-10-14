
import random
import copy
POOL_OF_LETTERS = {"A" : 9, "N" : 6, "B" : 2, "O" : 8, "C" : 2, "P" : 2, "D" : 4 ,"Q" : 1, "E" : 12, "R" : 6, "F" : 2, "S" : 4, "G" : 3, "T" : 6, "H" : 2, "U" : 4, "I" : 9, "V" : 2, "J" : 1 , "W" : 2, "K" : 1, "X" : 1, "L" : 4, "Y" : 2, "M" : 2, "Z" : 1}

def draw_letters():
    distribution_of_letters = copy.deepcopy(POOL_OF_LETTERS)
    letters = []
    while len(letters) < 10:
        userletters = random.choice(list(distribution_of_letters.items()))
        if userletters[1] > 0:
            letters.append(userletters[0])
            distribution_of_letters[userletters[0]]-=1
    return letters
# solution 2(try random.sample)
    # letter_list = list(distribution_of_letters.keys())
    # letter_count = list(distribution_of_letters.values())
    # letters = random.sample(letter_list, k = 10, counts = letter_count)
    # return letters

def uses_available_letters(word, letter_bank):
    counter = {}
    for letter in letter_bank:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
    
    for ch in word.upper():
            if ch in counter and counter[ch] > 0:
                counter[ch] -= 1
            else:
                return False
    return True

def score_word(word):
    # use map to store letter to score relationships
    score_chart = {
        "AEIOULNRST": 1,
        "DG": 2,
        "BCMP": 3,
        "FHVWY": 4,
        "K": 5,
        "JX": 8,
        "QZ": 10
        }
    
    total_score = 0
    # add additional 8 points for words with special length
    if len(word) > 6 and len(word) < 11:
        total_score += 8
    # find the score for each letter in word, and add score to total_score
    for letter, value in score_chart.items(): 
        for ch in word.upper():
            if ch in letter:
                total_score += value

    return total_score

    
def get_highest_word_score(word_list):
    # Function iterate through the word_list, and update best_word when current word is the best word
    # store the first word and score to the empty best_word
    # update best_word with new value when current score is greater than previous best score
    # update best_word when there's a tie and the previous word length is not 10 and either current word length is 10 or shorter than previous word length
    best_word = None
    
    for word in word_list: 
        score = score_word(word)

        if not best_word:
            best_word = (word, score)
        
        elif score > best_word[1]:
            best_word = (word, score)
        
        elif score == best_word[1] and len(best_word[0]) != 10 and (len(word) == 10 or len(word) < len(best_word[0])):
            best_word = (word, score)
          
    return best_word
            
