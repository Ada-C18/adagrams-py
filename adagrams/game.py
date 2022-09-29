import random
def draw_letters():
    LETTER_POOL = {"A": 9, "B": 2, "C": 2, "D": 4, "E": 12, "F": 2, "G": 3, "H": 2, "I": 9, "J": 1, 
                    "K": 1, "L": 4, "M": 2, "N": 6, "O": 8, "P": 2, "Q": 1, "R": 6, "S": 4, "T": 6,
                    "U": 4, "V": 2, "W": 2, "X": 1, "Y": 2, "Z": 1}
    
    available_letters = []
    letter_list = []

    for letter,amount in LETTER_POOL.items():
        available_letters.extend(letter for _ in range(amount))

    while len(letter_list) < 10:
        used = random.choice(available_letters)
        letter_list.append(used)
        available_letters.remove(used)
    
    return letter_list



def uses_available_letters(word, letter_bank):
    letter_list = letter_bank.copy()

    for letter in word.upper():
        if letter not in letter_list:
            return False
        else:
            letter_list.remove(letter)

    return True          

def score_word(word):  # sourcery skip: collection-into-set
    score_dict = {"A":1, "E":1, "I":1, "O":1, "U":1, "L":1, "N":1, "R":1, "S":1, "T":1, "D":2,
                    "G":2, "B":3, "C":3, "M":3, "P":3, "F":4, "H":4, "V":4, "W":4, "Y":4, "K":5, 
                    "J":8, "X":8, "Q":10, "Z":10}
    score = 0

    for letter in word:
        points = score_dict[letter.upper()]
        if letter.isalpha() == False: 
            continue
        else:
            score += points

    if len(word) in [7, 8, 9, 10]:
        score += 8

    return score


def get_highest_word_score(word_list):
    score =0
    temp = []

    for word in word_list:
        word_score = score_word(word)
        if word_score > score:
            temp = []
            score =word_score
            temp.append(word)
        elif word_score == score:
            temp.append(word)

    word = temp[0]
    if len(temp)>1:
        for i in temp:
            if len(i)==10:
                word=i
                break
            else:
                word = min(temp, key=len)

    score=score_word(word)
    return word,score
