import random

letter_dict = { 
                'A': {'frequency': 9, 'score': 1}, 
                'B': {'frequency': 2, 'score': 3}, 
                'C': {'frequency': 2, 'score': 3}, 
                'D': {'frequency': 4, 'score': 2}, 
                'E': {'frequency': 12, 'score': 1}, 
                'F': {'frequency': 2, 'score': 4}, 
                'G': {'frequency': 3, 'score': 2}, 
                'H': {'frequency': 2, 'score': 4}, 
                'I': {'frequency': 9, 'score': 1}, 
                'J': {'frequency': 1, 'score': 8}, 
                'K': {'frequency': 1, 'score': 5}, 
                'L': {'frequency': 4, 'score': 1}, 
                'M': {'frequency': 2, 'score': 3}, 
                'N': {'frequency': 6, 'score': 1},
                'O': {'frequency': 8, 'score': 1}, 
                'P': {'frequency': 2, 'score': 3}, 
                'Q': {'frequency': 1, 'score': 10}, 
                'R': {'frequency': 6, 'score': 1}, 
                'S': {'frequency': 4, 'score': 1}, 
                'T': {'frequency': 6, 'score': 1}, 
                'U': {'frequency': 4, 'score': 1}, 
                'V': {'frequency': 2, 'score': 4}, 
                'W': {'frequency': 2, 'score': 4}, 
                'X': {'frequency': 1, 'score': 8}, 
                'Y': {'frequency': 2, 'score': 4}, 
                'Z': {'frequency': 1, 'score': 10}
                }
    
def draw_letters():  
    letter_pool = []
    for letter in letter_dict:
        letter_pool += list(letter) * letter_dict[letter]['frequency']
    
    player_hand = []
    while len(player_hand) < 10:
        letter = random.choice(letter_pool) 
        if player_hand.count(letter) < letter_pool.count(letter):
            player_hand += letter
    
    return player_hand

def uses_available_letters(word, letter_bank):
    letters = letter_bank.copy()
    for letter in word.upper():
        if letter not in letters:
            return False
        letters.remove(letter)
    return True          

def score_word(word):
    total_points = sum([letter_dict[letter]['score'] for letter in word.upper()])
    
    if len(word) >= 7:
        total_points += 8
    
    return total_points

def get_highest_word_score(word_list):
    scores = [(word, score_word(word)) for word in word_list]
    
    highest_score = scores[0]
    for score in scores: 
        if score[1] > highest_score[1]:
            highest_score = score

        if score[1] == highest_score[1]:
            if len(highest_score[0]) < 10 and (len(score[0]) == 10 or len(score[0]) < len(highest_score[0])):
                highest_score = score
                
    return highest_score