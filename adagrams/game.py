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

SCORE_CHART = {
    'A': 1, 
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
    'Z': 10
}


##    Main Function #1    ##
def draw_letters():
    letters = []

    while len(letters) < 10:
        random_letter = random.choice(list(LETTER_POOL.keys()))
        
        if letters.count(random_letter) < LETTER_POOL[random_letter]:
            letters.append(random_letter)

    return letters




# # Helper Function
# def convert_to_ignore_case(word, letter_bank):
#     # convert all letters in word and letter_bank to ignore case
#     # use casefold() method to remove all distinctions in string (similar to .lower() but more "aggresive")
#     # use list comprehensions to use casefold() on each letter in letter_bank
    
#     # print(f"word before converting: {word}")
#     # print(f"letter_bank before converting: {letter_bank}, \n")

#     word = word.casefold()
#     letter_bank = [letter.casefold() for letter in letter_bank]

#     # print(f"word after converting: {word}")
#     # print(f"letter_bank after converting: {letter_bank}, \n")
    
#     return word, letter_bank



# # Helper Function: 
# def check_word_in_letter_bank(word, letter_bank):
#     # check each letter in word if it is in letter bank
#     # create variable to count each time letter is found in letter bank
#     # compare count to len(word)
#     # if count and len(word) are equal return True
#     # if not equal, return False

#     word, letter_bank = convert_to_ignore_case(word, letter_bank)

#     print(f"word is: {word}")
#     print(f"letter bank is: {letter_bank}")

#     letter_count = 0

#     for letter in word:
#         if letter in letter_bank:
#             letter_count +=1

#     print(f"letter count: {letter_count}")
#     print(f"word lenth: {len(word)}")

#     if letter_count == len(word):
#         return True

#     return False





##    Main Function #2   ##
def uses_available_letters(word, letter_bank):
    available_letters = letter_bank[:]
    upper_word = word.upper()

    for letter in upper_word:
        if letter not in available_letters:
            return False
        else:
            available_letters.remove(letter)

    return True


def score_word(word):
#   word = string of characters
#   each letter has a point value based on the table
#   if length of word is 7+, the total adds 8 additiona points
#   returns an integer w/ number of points

def get_highest_word_score(word_list):
    pass