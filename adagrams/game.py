import random
LETTER_POOL = [{
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
}]
def draw_letters():
    letters = []
    remaining_letters_pool = {}
    
    if len(letters) < 11:
    #getting the remaining amount of letters in the letter pool
        for dict in LETTER_POOL:
            for key, value in dict.items():
                if key not in remaining_letters_pool and value > 0:
                 remaining_letters_pool[key] = value
    #adding random letter to the length of the letter list if it's less than ten
    while len(letters) < 10:
        random_letter = random.choice(list(remaining_letters_pool))
    ##Removing the used letter from the remaining letter pool  
        for letter in list(remaining_letters_pool):
            if remaining_letters_pool[letter] == 0:
                remaining_letters_pool.pop(letter)
            elif random_letter == letter:
                remaining_letters_pool[letter]-= 1
                letters.append(random_letter)            
    return letters


def uses_available_letters(word, letter_bank):
    dict_word={}
    word=word.upper()
    word_list=[]
    values_dict=[]
    #Creating a list of each letter that is a string
    for letter in word:
        word_list.append(letter)
    #Assigning a boolean to each letter if it appears in the list
    for letter in word_list:
        if letter in letter_bank:
            freq_letter=word_list.count(letter)
            freq_letter_bank=letter_bank.count(letter)
            if freq_letter == freq_letter_bank:
                dict_word[letter]=True
            elif freq_letter>freq_letter_bank:
                dict_word[letter]=False
            elif freq_letter<freq_letter_bank:
                dict_word[letter]=True
        else:
            dict_word[letter]=False
    #Adding all of the booleans values for the given word to a list
    for key,value in dict_word.items():
        values_dict.append(value)
    if False in values_dict:
    #if there are any False values in the dict then return False
        return False
    else:
        return True


def score_word(word):
    #creating a new dictionary assinging values to each letter
    letter_value={'A': 1, 
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
    'Z': 10,}

    total_sum=0
    #Test case sensitivity
    cap_word=word.upper()
    if len(word) > 6:
        total_sum=8
    for letter in cap_word:
        total_sum+=letter_value[letter]
    return total_sum

def get_highest_word_score(word_list):
    highest_score=0
    words=[]
    word_scored={}
    #Creating a dictionary for each word with the key pair value word and score
    for word in word_list:
        word_scored[word]=score_word(word)
    #Getting highest score
    for value in word_scored.values():
        if value > highest_score:
            highest_score=value
    
    #get words with highest_score        
    for word in word_list:
      if word_scored[word]==highest_score:
        words.append(word)
    
    #evaluate tie-breaks
    if len(words) > 1:
      shortest_word_len = 10
      shortest_word = ''
      for word in words:
        if len(word) == 10:
          return (word, highest_score)
        elif len(word) < shortest_word_len:
          shortest_word_len = len(word)
          shortest_word = word
      return (shortest_word, highest_score)    
    
    #only one winner   
    else:
      
      return (words[0], highest_score)