def draw_letters():
    pass

def uses_available_letters(word, letter_bank):
 
    new_word = word.upper()
    copy_bank = letter_bank.copy()
    
    for letter in new_word:
        
      if letter in copy_bank:
        copy_bank.remove(letter)
      else: 
        return False
    return True





def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass 
