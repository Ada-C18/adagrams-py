import random
from collections import Counter
LETTER_POOL20 = {
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
def random_selection():
    values = list(LETTER_POOL20.values())
    keys = list(LETTER_POOL20.keys())
    percentages= []
    for num in values:
        percentages.append(num)
    tup = tuple(percentages)
    random_l = random.choices(keys , weights = tup)
    return ''.join(random_l)
    
def check_available(random, players_hand, LETTER_POOL20):
    if random in LETTER_POOL20:  
        if LETTER_POOL20[random] == 0:     
            return False
        else:
            LETTER_POOL20[random] -=1   
            players_hand.append(random)
            return True
def draw_letters():
    players_hand = []            
    i=0
    if all(LETTER_POOL20.values()) == 0:
        return []
    random_selection()
    available = True
    while available and len(players_hand)<10 and i <26:
        letter = random_selection()
        check_available(letter, players_hand,LETTER_POOL20)
        i +=1
    return players_hand
    

def uses_available_letters(word, letter_bank):
    list_bool = []
    word = word.upper()
    amount_bank = Counter(letter_bank)
    for letter in word:
        if letter in letter_bank and amount_bank[letter] > 0 :
            amount_bank[letter] -= 1
            list_bool.append(True)
        else:
            list_bool.append(False)
    if False in list_bool:
        return False
    else:
        return True


def score_word(word):
    point_system = {
        ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T") : 1,
        ("D","G"): 2,
        ("B", "C", "M", "P"):3,
        ("F", "H", "V", "W", "Y"):4,
        ("K"): 5,
        ("J","X"):8,
        ("Q","Z"):10
    }
    word = word.upper()
    score = 0
    for letter in word:
        for key, point in point_system.items():
            if letter in key:
                score += point
    if 6 < len(word) <= 10:
        score+=8
    return score

def get_highest_word_score(word_list):
    score_sheet = []
    high_score = 0
    top_players_tie=[]
    top_player = ("",0)

    for word in word_list:
        score = score_word(word)
        score_info = (word,score)
        score_sheet.append(score_info)
        if score > high_score:
            high_score = score
    for player in score_sheet:
        if player[1] == high_score:
            top_players_tie.append(player)
            top_player = player

    if len(top_players_tie)>1:
        for player in top_players_tie:
            if len(player[0]) == len(top_player[0]) and player is not top_player:
                return top_players_tie[0]
            elif len(player[0]) == 10:
                top_player = player
                return top_player
                
            elif len(player[0]) < len(top_player[0]):
                top_player = player

    
    return top_player

