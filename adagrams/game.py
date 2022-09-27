import random

def draw_letters():
    allletters = []
    alphabet = {
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
    #expanded dictionary per numbers of letters
    for letter, number in alphabet.items():
        for i in range(number):
            allletters.append(letter)
<<<<<<< HEAD

=======
    
    #picking 10 random letters from expanded dictionary
>>>>>>> 4ce1b22f209d98b0bd4915516b9c1b862c64ebe4
    gameletters = []
    for letter in range(10):
        number = random.randint(0, 27)
        random_letter = allletters[number]
        gameletters.append(random_letter)
        allletters.remove(random_letter)
        
    return gameletters



def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank[:]
    for letter in word:
        letter = letter.capitalize()
        if letter not in letter_bank_copy:
            return False
        else:
            letter_bank_copy.remove(letter)
    return True


def score_word(word):
    points_dict = {
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
    total_points = 0
    for letter in word:
        letter = letter.capitalize()
        point_value = points_dict[letter]
        total_points += point_value
    if len(word) in range(7, 11):
        total_points += 8 
    return total_points

def get_highest_word_score(word_list):
    list_scoring = []
    winning_words_list = []

    
    for word in word_list:
        # print('word', word)
        list_scoring.append(word)
        list_scoring.append(int(score_word(word)))
    
    highest_score = max(list_scoring[1::2])

                

    print('list', list_scoring)

    
    
    index_of_highest = list_scoring.index(highest_score)
    index_word_of_highest_score = index_of_highest - 1
    word_of_highest_score = list_scoring[index_word_of_highest_score]
    winning_words_list.append(word_of_highest_score)
    winning_words_list.append(highest_score)
    
    tiebreaker_list = []
    print('type', type(winning_words_list))
    print('len', len(winning_words_list))
    print('list', winning_words_list)

    if len(winning_words_list) > 2:

        highest_score_tie = min(len(winning_words_list[0::2]))
        print('>>>', highest_score_tie)
        for word in winning_words_list:
            if len(word) == highest_score_tie:
                tiebreaker_list.append(word)
                tiebreaker_list.append(highest_score)
        return tiebreaker_list

    else: 
        return tuple(winning_words_list)
    
    #list_tuple =tuple(list_scoring)
