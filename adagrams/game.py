import random
import copy
# LETTER_POOL = 

letter_dict = {
"A" : 9 , "N" : 6,
"B" : 2, "O" : 8, 
"C" : 2, "P" : 2,
"D" : 4,  "Q" : 1, 
"E" : 12, "R" : 6,
"F": 2, "S" : 4,
"G" : 3, "T" : 6, 
"H" : 2, "U" : 4,
"I" : 9, "V" : 2,
"J" : 1, "W" : 2,
"K" : 1, "X" : 1,
"L" : 4, "Y" : 2,
"M" : 2, "Z" : 1 
}


def draw_letters():
    player_hand = random.choices(list(letter_dict.keys()), weights=letter_dict.values(), k=10)       
    return player_hand
    
    # decrease the value 
    letter_bank = []
    
    while len(letter_bank)<10:
        random_letter=random.choice(letter_dict)
        letter_bank.append(letter_bank)
        letter_dict[random_letter] -= 1
        if letter_dict[random_letter] == 0:
            continue 


# different ideas

# print(letter_dict)
# letter_bank = []
# while len(letter_bank) < 10:
#         random_letter = random.choice(list(letter_dict))
#         letter_bank.append(random_letter)
#         letter_dict[random_letter] -= 1
#         if letter_dict[random_letter] == 0:
#             continue
# print(letter_bank)
# print(letter_dict)

    # letters=[]
    # letter_bank=[]
    # for letter in LETTER_POOL.items():
    #     letters.extend(repeat(letter[0],letter[1]))
   
    # while len(letter_bank)<10:
    #     random_letter=random.choice(letters)
    #     letter_bank.append(random_letter)
    #     letters.remove(random_letter)
    #     if len(letter_bank)==10:
    #         break



    # random.sample(population, k, *, counts=None)
#     return letter_bank
    # random_letter = random.choice(letters)
# pull letters one by one
# generate one letter. check and then pull it out


    # k = 10 draws all the counters in at the same time 
    # review chances of drawing same letters (review .choices method) (weighted may not fit) 
    # random.sample (without replacement) takes k and counts 
    # come back and complete longer version
    # Check for test 1.3 
def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank.copy()
    for letter in word:
        letter = letter.upper()
        if letter not in letter_bank_copy:
            return False
        else:
            letter_bank_copy.remove(letter)  
    return True 
 
# decrease quantity until letter gets to 0 don't check anymore
# check that all letters in word are in letter bank
# while len of letter bank is less than 10 
# dictionary with list 

def score_word(word):
    pass

def get_highest_word_score(word_list):
    print('1')