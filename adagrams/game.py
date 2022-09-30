from operator import le
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
SCORE_CHART =  {
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
def create_bag_of_letters():
    """
    Returns an array containing all the letters of the "LETTER_POOL" dictionary 
    according to the frequency associated with each letter.
    Ex: Since the value of 'A' is 9, the first 9 elements of this list will be 'A' 
    appearing 9 times, and so on.
    bag_of_letters = ['A', 'A', ..., 'B', ...]
    """
    bag_of_letters = []
    for letter in LETTER_POOL:
        number_of_letters = LETTER_POOL[letter]
        for i in range(number_of_letters):
            bag_of_letters.append(letter)
    return bag_of_letters

def draw_letters():
    hand_of_letters = [] # to be filled with 10 one-letter strings
    bag_of_letters = create_bag_of_letters()
   
    for i in range(10):
        #size_of_letter_bag = len(bag_of_letters)
        letter_picked = random.choice(bag_of_letters) 
        hand_of_letters.append(letter_picked)
        bag_of_letters.remove(letter_picked)

    return hand_of_letters

def uses_available_letters(word, letter_bank):
    copy_of_letter_bank = list(letter_bank)
    upper_case_word = word.upper()
    #We checked to make sure that removing wouldn't affect original letter_bank array here:
    # copy_of_letter_bank.remove('B')
    # print("letter bank:", letter_bank)
    #print("copy of letter bank:" , copy_of_letter_bank)
    
    for character in upper_case_word:
        if character in copy_of_letter_bank:
            copy_of_letter_bank.remove(character)
        else:
            return False
    
    return True


def score_word(word):
    final_score = 0
    upper_case_word = word.upper()
    for char in upper_case_word:
        final_score += SCORE_CHART[char]
    if len(word) > 6 and len(word) < 11:
        final_score += 8
    return final_score
    

def get_highest_word_score(word_list):
    word_info = []
    for word in word_list:
        word_dict = {}
        word_dict["word"] = word
        word_dict["score"] = score_word(word)
        word_dict["length"] = len(word)
        word_info.append(word_dict)
    
    max_words = []
    max_score = 0

    for word_dict in word_info:
        if word_dict["score"] ==  max_score:
            max_words.append(word_dict["word"])
        elif word_dict["score"] > max_score: 
            max_score =  word_dict["score"]
            max_words.clear()
            max_words.append(word_dict["word"])
# CASE 1
    if len(max_words) == 1:
        return (max_words[0], score_word(max_words[0]))

# CASE 2

    min_letter_count = 10
    shortest_word = None

    for word in max_words:
        if len(word) == 10:
            return (word, score_word(word))
        elif len(word) < min_letter_count:
            min_letter_count = len(word)
            shortest_word = word
    return (shortest_word, score_word(shortest_word))

# word_info:
# {“word”: word,
# “Score”: score_word(word),
# “Length”: len(word)
# }

#hand = ['S', 'B', 'E', 'T', 'R','E' , 'Z', 'A', 'L', 'M']
#uses_available_letters("TREE", hand)