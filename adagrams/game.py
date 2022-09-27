from audioop import add
import random

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

def draw_letters():
    letters = []
        
    for i in range(11):
        random_letter = random.choice(list(LETTER_POOL.keys()))
        # print(f"RL: {random_letter}")
        
        if letters.count(random_letter) < LETTER_POOL[random_letter]:
            letters.append(random_letter)
            # print("letter count: ", letters.count(random_letter), "\n")

    return letters


def convert_to_ignore_case(word, letter_bank):
    # convert all letters in word and letter_bank to ignore case
    # use casefold() method to remove all distinctions in string (similar to .lower() but more "aggresive")
    # use list comprehensions to use casefold() on each letter in letter_bank
    
    # print(f"word before converting: {word}")
    # print(f"letter_bank before converting: {letter_bank}, \n")

    word = word.casefold()
    letter_bank = [letter.casefold() for letter in letter_bank]

    # print(f"word after converting: {word}")
    # print(f"letter_bank after converting: {letter_bank}, \n")
    
    return word, letter_bank

def check_word_in_letter_bank(word, letter_bank):
    # check each letter in word if it is in letter bank
    # create variable to count each time letter is found in letter bank
    # compare count to len(word)
    # if count and len(word) are equal return True
    # if not equal, return False

    word, letter_bank = convert_to_ignore_case(word, letter_bank)

    print(f"word is: {word}")
    print(f"letter bank is: {letter_bank}")

    letter_count = 0

    for letter in word:
        if letter in letter_bank:
            letter_count +=1

    print(f"letter count: {letter_count}")
    print(f"word lenth: {len(word)}")

    if letter_count == len(word):
        return True

    return False

# print(check_word_in_letter_bank("DOGF", ["D", "O", "G", "X", "X", "X", "X", "X", "X", "X"]))

def uses_available_letters(word, letter_bank):
    pass

#   Check if word is in random 10 letter list (Helper Funct)
#       - it ignores letter case
#   Make sure that each letter is only used as many times as
#       it appears on the list of random letters.

#   Returns True or False



def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass