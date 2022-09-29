import random
LETTER_POOL = list("A"*9 + "B"*2 + "C"*2 + "D"*4 + "E"*12 + "F"*2 + "G"*3 + "H"*2 + "I"*9 + "J"*1 + "K"*1 + "L"*4 + "M"*2 + "N"*6 + "O"*8 + "P"*2 + "Q"*1 + "R"*6 + "S"*4 + "T"*6 + "U"*4 + "V"*2 + "W"*2 + "X"*1 + "Y"*2 + "Z"*1)
SCORE_DICT = { 'A': 1, 
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
'Z': 10}

def draw_letters():
    adjusted_letter_pool=LETTER_POOL.copy()
    hand_list = []
    
    #Appends 10 random letters to the hand
    for _ in range(10):
        current_letter = random.choice(adjusted_letter_pool)
        adjusted_letter_pool.remove(current_letter)
        hand_list.append(current_letter)

    return hand_list

def uppercase_letter_list(letter_bank):
    hand=[]

    #Converts each letter in the letter bank to uppercase
    for letter in letter_bank:
        upper_letter = letter.upper()
        hand.append(upper_letter)

    return hand

def uses_available_letters(word, letter_bank):
    players_letters_list = list(word.upper())
    hand = uppercase_letter_list(letter_bank)
    hand_dict = {}

    #Generates a counter dictionary for letters in the hand
    for hand_letter in hand:
        # lowercase_hand_letter = hand_letter.upper()
        if hand_letter in hand_dict:
            hand_dict[hand_letter] += 1
        else:
            hand_dict[hand_letter] = 1

    #Checks validity of user's word letters against the counter dictionary
    for player_letter in players_letters_list:
        if player_letter not in hand_dict:
            return False

        if hand_dict[player_letter] == 0:
            return False
        else:
            hand_dict[player_letter] -= 1
    #Assumes a valid word if the function does not return False
    return True

def score_word(word):    
    players_letters_list=list(word.upper())
    letter_count=len(players_letters_list)
    players_word_score = 0

    #Adds each letter's points to the word score 
    for player_letter in players_letters_list:
        players_word_score += SCORE_DICT[player_letter]
    
    #Adds 8 points to the word score if the word is 7 letters or longer
    if letter_count >= 7:
        players_word_score += 8
        
    return players_word_score

def get_highest_word_score(word_list):
    max_words = []
    letter_counts = []
    
    #assigns an initial max score
    max_score = score_word(word_list[0])
    
    # compares current score against previously stored max score 
    # and appends (1) the word and (2) number of letters in the word to lists
    for word in word_list:
        current_score = score_word(word)
        if current_score > max_score:
            max_score = current_score
            max_words = [word]
            letter_counts = [len(word)]
        elif current_score == max_score:
            max_words.append(word)
            letter_counts.append(len(word))

    min_letter_count = min(letter_counts)
    
    # checks if letter count equals to 10 and returns the winning tuple
    for index,lett_count in enumerate(letter_counts):
        if lett_count == 10:
            winner_word = max_words[index]
            return winner_word, max_score
        
    # checks if letter count equals to the minimum letter count and returns winning tuple
    for index,lett_count in enumerate(letter_counts):
        if lett_count == min_letter_count:
            winner_word = max_words[index]
            return winner_word, max_score

