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

# =========== WAVE ONE ===========
# ================================

def draw_letters():
    # takes in no parameter
    letters = [] # the "hand" with 10 letters that we return
    
    count = 0
    
    new_dict = LETTER_POOL.copy()

    # print("BEFORE: list of letters = ", letters)
    # print("BEFORE: dictionary = ", new_dict)

    # create a list that's 10 letters long
    # random drawing from letters in dictionary — import random module
    while len(letters) < 10:
        random_letter = random.choice(list(new_dict.keys()))

        # ... conditional statement ...
        for k, v in new_dict.items():
            if k == random_letter and v > 1:
                # print("BEFORE change ", k, v)
                letters.append(random_letter)
                v -= 1 # this creates a new value for v
                new_dict[k] = v # this syntax adds updates the value of the dictionary w/in the loop
                # print("AFTER change = ", k, v)
            else:
                continue
        count += 1 # we need to make this change to the dictionary
    # print("Letters list = ", letters)
    return letters


# =========== WAVE TWO ===========
# ================================


def uses_available_letters(word, letter_bank):

    # check input-word only uses letters in hand
    # word = "string"
    # letter_bank = ["list", "of", "strings", "ie letters"]

    word = word.upper()

    word_letters = list(word)
    print("List of letters from WORD = ", word_letters)
    print("Letter Bank = ", letter_bank)

    frequency = {}

    for letter in word_letters:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    print("Frequency of Letters in Word = ", frequency)

    frequency2 = {}

    for letter in letter_bank:
        if letter in frequency2:
            frequency2[letter] += 1
        else:
            frequency2[letter] = 1
    print("Frequency of letters in Bank = ", frequency2)

    # if every letter in word is in letter_bank
    # return True

    common = frequency.items() & frequency2.items() 

    if len(common) == len(frequency):
        return True
    # if every letter in word is NOT in letter_bank
    # return False
    else:
        return False
    
    print("Len of COMMON_key:values dict = ", len(common))
    print("Len of HAND dict = ",len(frequency))
    print("Len of LETTER_BANK dict = ", len(frequency2))



# =========== WAVE THREE ===========
# ==================================

def score_word(word):

    # GOAL: return the score of given word defined by Adagram
    # word = "string of characters"

    print("Word list = ", word, ",", type(word))

    sum = 0

    # if length of word is 7, 8, 9, or 10 -->
        # then the word gets 8 extra points
    if len(word) >= 7 and len(word) <= 10:
        sum += 8

    # each letter withing word has a point value
    # sum up the total number of points for the word

    

    # return an integer representing the number of points
    # return <int>



    # pass




# =========== WAVE FOUR ===========
# =================================

def get_highest_word_score(word_list):
    pass