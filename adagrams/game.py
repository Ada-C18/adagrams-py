#Maggie T adagrams project 
# Billie Betts adagram project

import string
import random

quantity_data = {1: ['Z', 'X', 'K', 'Q', 'J'],
                  2: ['B','C','F','H','M', 'P','V','W','Y'],
                  3: ['G'],
                  4: ['D', 'L', 'S', 'U'],
                  6: ['N', 'R', 'T'],
                  8: ['O'],
                  9: ['A', 'I'],
                  12: ['E']}

value_data = {1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
              2: ['D','G'],
              3: ['B', 'C', 'M', 'P'],
              4: ['F', 'H', 'V', 'W', 'Y'],
              5: ['K'],
              8: ['J', 'X'],
              10: ['Q', 'Z']}


def generate_alphabet_data_list(quantity_data, value_data):
  all_letters = string.ascii_uppercase
  results = []
  for letter in range(len(all_letters)):
    generate_dict = {}
    generate_dict['letter'] = all_letters[letter]

    for key, value in quantity_data.items():
      if all_letters[letter] in value:
        generate_dict['quantity'] = key

    for key, value in value_data.items():
      if all_letters[letter] in value:
        generate_dict['value'] = key
  
    results.append(generate_dict)

  return results
  

alphabet_data_list = generate_alphabet_data_list(quantity_data, value_data)

def draw_letters():
  letter_soup = []

  for data in alphabet_data_list:
    runner = 0
    while runner < data['quantity']:
      letter_soup.append(data['letter'])
      runner += 1

  user_letter_pool = []
  
  for r in range(0,10):
    draw = random.randint(0, (len(letter_soup)-1))
    drawn_letter = letter_soup[draw]

    for letter in alphabet_data_list:
      if letter['letter'] == drawn_letter:
        max_count = letter['quantity']

    if user_letter_pool.count(drawn_letter) < max_count:
      user_letter_pool.append(drawn_letter)

  return user_letter_pool

def uses_available_letters(word, letter_bank):
    letter_count = {}
    # word_uppercase = word.upper()
      
    for l in word:
      letter = l.upper()
      if letter not in letter_count:
        letter_count[letter] = 0

      letter_count[letter] += 1
      ct = letter_count[letter]

      if ct > letter_bank.count(letter):
        return False
  
    return True







   #  letter_count[letter] + 1
    


    # if len(word) > 10:
    #   return False

   
      


    # for letter in word.upper():
    #   if letter in letter_bank: #using if not letter not in letter_bank passes 3
    #     letter_bank.remove(letter)
    #   if letter not in letter_bank:
    #     return False
   
        
    #     return False
    # return True
  
    # for letters in letter_bank:
    #   for new_word in word.upper():
    #     if letter_bank.count(letters) == word.count(new_word):
    #       return True
    #     if letter_bank.count(letters) != word.count(new_word):
    #       return False
    #     # if letter_bank.count(letters) == word.count(letters):
    #     #   return True
      
     


    # for letter in word.upper():
    #   if letter not in letter_bank: #using if not letter not in letter_bank passes 3
    #     return False
    # return True










    # for letters in letter_bank:
    #   for new_word_letters in word:
    #     if letter_bank.count(letters) != word.count(letters):
    #       return False

  

#add lower or upper so its not case sensitive
def score_word(word):
  if type(word) is not str:
    return 0
  
  score = 0
  if len(word) > 6:
    score += 8

  word_breakdown = []

  for l in range(len(word)):
    word_breakdown.append(word[l].upper())

  for i in range(len(word_breakdown)):
    for data in alphabet_data_list:
      for keys, values in data.items():
        if data['letter'] == word_breakdown[i]:
          add_it = data['value']
    score += add_it

  return score


# given word_list, a list of strings
# foo, bar, baz
def get_highest_word_score(word_list):

  # highest_word = None
  # highest_word_score = 0

  # for word in word_list:
  #   score = score_word(word)
  #   if score >= highest_word_score:
  #     highest_word_score = score
  #     highest_word = word



  





























  #find max score of word_list

  winning_words = []
  winning_score = 0

  #for word in range(len(word_list)):
  for word in word_list:
    value_of_word = score_word(word) #all errors are referring to previous function score_word. Maybe because reusing variables, score already calculate
    print(word_list)
    if value_of_word == winning_score: # if its a tie append it to list winning_words
      winning_words.append(word)
    else:
      if value_of_word > winning_score: # encountered a new highest score
        winning_score = value_of_word 
        winning_words = [word]

  for i in winning_words:
    if len(i) == 1:
      winner = winning_words[word]



#function to print out winner/winners in tuple format
# def print_highest_score(winning_words, winning_score):

#     highest_word = winning_words
#     highest_score = winning_score

#     return (highest_word, highest_score)

  




  
  

   




















   

  #check length of tie_breaker list, if it has one value return a tuple of the list
  # if len(tie_breaker) == 1:
  #   return tuple(tie_breaker)

  # else: 
  #   if len(tie_breaker[0]) == 10 and len(tie_breaker[1]) != 10:
  #     return tuple(tie_breaker[0])
  #   if tie_breaker[1] == 10 and tie_breaker[0] != 10:
  #     return tuple(tie_breaker[1])
  #   if len(tie_breaker[0]) == len(tie_breaker[1]):
  #     return tuple(tie_breaker[0])

    




