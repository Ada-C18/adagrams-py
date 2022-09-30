
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
    pool = LETTER_POOL.copy()
    hand = []

    while len(hand) < 10:
        choices = "".join([letter * pool[letter] for letter in pool])
        random_letter = random.choice(list(choices))
        avail = pool.get(random_letter)

        if avail > 0:
            hand.append(random_letter)
            pool[random_letter] -= 1

    return hand

def uses_available_letters(word, letter_bank):
    bank = letter_bank.copy()
    for letter in word.upper():
        if letter in bank:
            bank.remove(letter)
        else:
            return False

    return True
        

def score_word(word):
 
    score_chart = {
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
    score = 0
    for letter in word.upper():
        if letter in score_chart:
            score += score_chart.get(letter)
    if len(word) >= 7:
        score += 8
    return score




def get_highest_word_score(word_list):

    scores=[]
    score_dict = {}
    for word in word_list:
        score = score_word(word) #called in our score_word function 
        scores.append(score) #created a list of our scores
        score_dict[word] = score #made it to a dictionary. ex. {'X': 8, 'XX': 16, 'XXX': 24, 'XXXX': 32}

   
    max_score = scores[0]
    for i,score in enumerate(scores):
        if score > max_score:
            max_score = score 

    new_key = ""
    list_equal_points_and_len = []
    max_keys = [word for word, score in score_dict.items() if score == max(score_dict.values())] 
    new_key = min(max_keys, key = len) 
    for words_max_points in max_keys:
        if len(words_max_points) == 10:
            new_key = words_max_points
            list_equal_points_and_len.append(new_key)
            new_key = list_equal_points_and_len[0]

    return(new_key, max_score)



    




    


                
            
        
      
                
                
            

            
        
        
            
            
               

            

            
            
             
    


        



        
       


   


   