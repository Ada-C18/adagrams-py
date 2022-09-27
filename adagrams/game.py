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

def draw_letters():
    # takes in no parameter
    letters = [] # the "hand" with 10 letters that we return

    # random drawing from letters in dictionary — random module***
    """ 
    STEPS:
    begin to pull letters, randomly
        iterate through dict, key:value pair
        as we iterate, update the value
        update a list of letters, .append()
    return the hand
    """
    # Our thoughts on making a loop
    """
    LOOP:
    random get a key from —> calls the value
    return an updated value
    """

    # get a random letter
    # random_letter = random.choice(list(LETTER_POOL.keys()))
    # # player_choice = list(LETTER_POOL.values()) # random piece of code we were thinking about using LOL
    # print("Here's your letter = ", random_letter)

    # # create a list with the letters chosen
    # letters.append(random_letter)
    # print("Here's your current hand =", letters)

    # create a list that's 10 letters long
    count = 0
    
    new_dict = LETTER_POOL.copy()

    # print("BEFORE: list of letters = ", letters)
    # print("BEFORE: dictionary = ", new_dict)

    while len(letters) < 10:
        random_letter = random.choice(list(new_dict.keys()))

        # ... conditional statement ...
        for k, v in new_dict.items():
            if k == random_letter and v > 1:
                # print("BEFORE change ", k, v)
                letters.append(random_letter)
                v -= 1 # this creates a new value for v, but how do we get it back to the dictionary?
                new_dict[k] = v
                # print("AFTER change = ", k, v)
            else:
                continue
        count += 1 # we need to make this change to the dictionary
    return letters

    # print("Count = ", count)
    # print("AFTER: list of letters = ", letters)
    # print("AFTER: dictionary = ", new_dict)
    
    # psuedocode the the next loop
    # for letter in letters:
    #     if that letter is in LETTER_POOL.items(): # I want to grab the key and value
    #         for k, v in letter:
    #             i want to update the value ---> v -= 1
    #             return v

    # iterate through the list of letters being randomly pulled for the hand
    # for letter in range(len(letters)):
    #     print(letter)

    # for-loop updates the dictionary
        # for letter, value in LETTER_POOL.items():
        #     # print(letter, value)
        #     if letter == random_letter:
        #         print(letter, value)
        #         value -= 1
        # print(letter, value)
        # return value
        # return the value—so update the dictionary           


    # returns array of 10 strings - testing for len(letters) == 10
    return letters
    
    # pass

# =========== WAVE TWO ===========

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
    print(common)

    if len(common) == len(frequency):
        return True
    # if every letter in word is NOT in letter_bank
    # return False
    else:
        return False
    
    print("Len of COMMON_key:values dict = ", len(common))
    print("Len of HAND dict = ",len(frequency))
    print("Len of LETTER_BANK dict = ", len(frequency2))



# ---WAVE THREE---

def score_word(word):
    pass

# ---WAVE FOUR---

def get_highest_word_score(word_list):
    pass