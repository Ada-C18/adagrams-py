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
    ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'): 1,
    ('D', 'G'): 2,
    ('B', 'C', 'M', 'P'): 3,
    ('F', 'H', 'V', 'W', 'Y'): 4,
    ('K'): 5,
    ('J', 'X'): 8,
    ('Q', 'Z'): 10
}

def draw_letters():
    letter_pool_list = []
    my_ten_letters = [] 

    for letter in LETTER_POOL:
        for num in range(0,(LETTER_POOL[letter])): 
            letter_pool_list.append(letter)

    #Claire's suggestion for a while loop 

    while len(my_ten_letters) < 10:  
        random_letter = random.choice(letter_pool_list)  
        my_ten_letters.append(random_letter)  
        letter_pool_list.remove(random_letter)
    return my_ten_letters

    #original solution 

    # while len(my_ten_letters) < 10:  
    #     for num in range(0,10):
    #         random_letter = random.choice(letter_pool_list)  
    #         my_ten_letters.append(random_letter)  
    #         my_string_count = my_ten_letters.count(random_letter) 
    #         word_pool_count = letter_pool_list.count(random_letter) 
    #         if my_string_count > word_pool_count: 
    #             my_ten_letters.remove(random_letter) 

def uses_available_letters(word, letter_bank):
    
    word = word.upper()
    # Claire's suggestion to combine the foor loops 
    for letter in word:
        count_pool_letter = letter_bank.count(letter)
        count_word_letter = word.count(letter)
        if letter not in letter_bank:
            return False
        if count_word_letter > count_pool_letter:
            return False 
        else: 
            continue 
    return True 

    # original for solution
    # word = word.upper()
    # letter_results = []
    # for letter in word:
    #     if letter not in letter_bank:
    #         letter_results.append("f") 
    #         if "f" in letter_results:
    #             return False
    #         else:
    #             return True

    # for letter in word:
    #     count_pool_letter = letter_bank.count(letter)
    #     count_word_letter = word.count(letter)
    #     if count_word_letter > count_pool_letter:
    #         return False
    #     else:
    #         return True



def score_word(word):

    if len(word) == 0:
        return 0

    word_score = 0
    word = word.upper()
    
    if len(word) in range(7, 11):
        word_score += 8
    
    for letter in word:
        for key in SCORE_CHART:
            if letter in key:
                word_score += SCORE_CHART.get(key)
    return word_score

def get_highest_word_score(word_list):

    score_dict = {}  
    for word in word_list:
        score = score_word(word) 
        score_dict[word] = score

    highest_score_value = max(score_dict.values())
    
    highest_scores = []

    #Claire's suggestion for more descriptive syntax
    for word, score in score_dict.items():
        if score == highest_score_value:
            highest_scores.append([word,score])

    # original solution
    # for dict in score_dict.items():
    #     if dict[1] == highest_score_value:
    #         highest_scores.append(dict)
            
    shortest_word_length = len(highest_scores[0][0])
    shortest_word = highest_scores[0][0] 
    
    if len(highest_scores) > 1:
        for word, score in highest_scores:
            if len(word) >= 10:
                shortest_word = word
                return (shortest_word, highest_score_value)
            elif len(word) < shortest_word_length:
                shortest_word_length = len(word)
                shortest_word = word
    return (shortest_word, highest_score_value)

