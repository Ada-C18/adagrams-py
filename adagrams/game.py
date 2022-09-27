import random

def draw_letters():
    # string == 1letter only
    # hand_letter == [ten strings]
    # draw_letters.random(LETTER_POOL)
    # return an array of hand_letter

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
    letters = []
    letter_frequency = {}
    for i in range(11):
        letter = random.choice(list(LETTER_POOL)) 
        if letter in letter_frequency:
            letter_frequency[letter] += 1
        else:
            letter_frequency[letter] = 1
        if letter_frequency[letter] <= LETTER_POOL[letter]:
            letters.append(letter)
    print(len(letters))
    return letters
    
    









def uses_available_letters(word, letter_bank):
    # check input word is anagram within drawn letters
    
    # player_input = input(word)
    for letter in word:
        if letter in letter_bank and len(letter):
            return True
        else:
            return False







def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass