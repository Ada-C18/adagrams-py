
import random
def draw_letters():
    distribution_of_letters = {"A" : 9, "N" : 6, "B" : 2, "O" : 8, "C" : 2, "P" : 2, "D" : 4 ,"Q" : 1, "E" : 12, "R" : 6, "F" : 2, "S" : 4, "G" : 3, "T" : 6, "H" : 2, "U" : 4, "I" : 9, "V" : 2, "J" : 1 , "W" : 2, "K" : 1, "X" : 1, "L" : 4, "Y" : 2, "M" : 2, "Z" : 1}
    letters = []
    while len(letters) < 10:
        userletters = random.choice(list(distribution_of_letters.items()))
        if userletters[1] > 0:
            letters.append(userletters[0])
            distribution_of_letters[userletters[0]]-=1
    return letters

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
    point_1_letters = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
    point_2_letters = ["D", "G"]
    point_3_letters = ["B", "C", "M", "P"]
    point_4_letters = ["F", "H", "V", "W", "Y"]
    point_5_letters = ["K"]
    point_8_letters = ["J", "X"]
    point_10_letters = ["Q", "Z"]
    
    # use map to store letter to score relationships
    score_chart = {
        1: point_1_letters,
        2: point_2_letters,
        3: point_3_letters,
        4: point_4_letters,
        5: point_5_letters,
        8: point_8_letters,
        10: point_10_letters
        }
    
    total_score = 0

    if len(word) != 0:
        special_length = [7, 8, 9, 10]

        # add additional 8 points for words with special length
        if len(word) in special_length:
            total_score += 8
        
        # find the score for each letter in word, and add score to total_score
        for point, letters in score_chart.items():
            for letter in word.upper():
                if letter in letters:
                    total_score += point

    return total_score

    
def get_highest_word_score(word_list):
    best_word = None

    # iterate through the word_list, and update best_word when current word is the best word
    for word in word_list: 
        score = score_word(word)

        # store the first word and score to the empty best_word
        if not best_word:
            best_word = (word, score)
        # update best_word with new value when current score is greater than previous best score
        elif score > best_word[1]:
            best_word = (word, score)
        # update best_word when there's a tie and the previous word length is not 10 and either current word length is 10 or shorter than previous word length
        elif score == best_word[1] and len(best_word[0]) != 10 and (len(word) == 10 or len(word) < len(best_word[0])):
            best_word = (word, score)
        
    return best_word
            
