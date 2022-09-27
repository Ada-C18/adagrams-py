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
    letter_pool_list = []
    my_ten_letters = [] 

    for letter in LETTER_POOL:
        for num in range(0,(LETTER_POOL[letter])): #letter_pool[letter] accesses the integer values of each letter
            letter_pool_list.append(letter)

    while len(my_ten_letters) < 10: #loop will not stop until we have a ten letter string 
        for num in range(0,10):
            random_letter = random.choice(letter_pool_list) #selects a random letter from letter pool 
            my_ten_letters.append(random_letter) # adds the random letter to a list 
            my_string_count = my_ten_letters.count(random_letter) #counts how many times our random letter appears in our ten letter string
            word_pool_count = letter_pool_list.count(random_letter) # counts how many times our random letter appears in our letter pool
            if my_string_count > word_pool_count: # if the count for a letter in our ten letter strings exceeds the count for the same letter in letter pool we remove it. 
                my_ten_letters.remove(random_letter) 

    return my_ten_letters

def uses_available_letters(word, letter_bank):
    
    letter_results = [] 
    for letter in word:
        if letter not in letter_bank:
            letter_results.append("f") # "f" in my head stands for false 
            if "f" in letter_results:
                return False
            else:
                return True

    for letter in word:
        count_pool_letter = letter_bank.count(letter)
        count_word_letter = word.count(letter)
        if count_word_letter > count_pool_letter:
            return False
        else:
            return True
    
    #word_all_caps = word.upper() 
    #return word_all_caps 

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass