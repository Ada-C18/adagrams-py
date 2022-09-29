
def draw_letters():
    pass

def uses_available_letters(word, letter_bank):
    pass

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
            for letter in str.upper(word):
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
            
