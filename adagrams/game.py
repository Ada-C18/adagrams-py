from random import randint

def draw_letters():
    letter_dict = {}
    for key, value in LETTER_POOL.items():
        letter_dict[key] = value
    letter_list = []
    for k, v in LETTER_POOL.items():
        for num in range(0, LETTER_POOL[k]):
            letter_list.append(k)
    output_list = []
    while len(output_list) < 10:
        index = randint(0, len(letter_list)-1)   
        if letter_dict[letter_list[index]] == 0:
            continue
        else:
            output_list.append(letter_list[index])
            letter_dict[letter_list[index]] -= 1
    return output_list

def uses_available_letters(word, letter_bank):
    letter_dict = {}
    for letter in letter_bank:
        if letter in letter_dict.keys():
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    
    for letter in word:
        letter = letter.upper()
        if letter not in letter_bank or letter_dict[letter] == 0:
            return False
        else:
            letter_dict[letter] -= 1
    return True

def score_word(word):
    value_dic = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }
    sum = 0
    for letter in word:
        sum += value_dic[letter.upper()]
    if 7 <= len(word) <= 10:
        sum += 8
    return sum

def get_highest_word_score(word_list):
    highest_score = 0
    highest_scoring_words = []
    for word in word_list:
        score = score_word(word)
        if score > highest_score:
            highest_scoring_words.clear()
            highest_score = score
            highest_scoring_words.append(word)
        elif score == highest_score:
            highest_scoring_words.append(word)
    
    shortest_word_len = len(highest_scoring_words[0])
    shortest_word = highest_scoring_words[0]
    for word in highest_scoring_words:
        if (len(word) == 10):
            return (word, score_word(word))
        else:
            if len(word) < shortest_word_len:
                shortest_word_len = len(word)
                shortest_word = word
    return (shortest_word, score_word(shortest_word))    

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