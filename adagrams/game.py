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

def letter_soup(letter_data):
  letter_soup = []

  for data in letter_data:
    runner = 0
    while runner < data['quantity']:
      letter_soup.append(data['letter'])
      runner += 1
  
  return letter_soup

todays_soup = letter_soup(alphabet_data_list)

def draw_letters():
  # letter_soup = []

  # for data in alphabet_data_list:
  #   runner = 0
  #   while runner < data['quantity']:
  #     letter_soup.append(data['letter'])
  #     runner += 1

  user_letter_pool = []
  
  while len(user_letter_pool) < 10:
    draw = random.randint(0, (len(todays_soup)-1))
    drawn_letter = todays_soup[draw]

    if user_letter_pool.count(drawn_letter) < todays_soup.count(drawn_letter):
      user_letter_pool.append(drawn_letter)

  return user_letter_pool

def uses_available_letters(word, letter_bank):
   # user_letter_dict = {}

    if len(word) > 10: 
     return False
    
    for letter in word.upper():
      if letter not in letter_bank: #using if not letter not in letter_bank passes 3
          return False
    return True

#add lower or upper so its not case sensitive #

    for letters in letter_bank:
      for used_letters in word:
        if letter_bank.count(letters) != word.count(letters):
          return False

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
      if data['letter'] == word_breakdown[i]:
        score += data['value']

  return score


def get_highest_word_score(word_list):
  #find max score of word_list

  winning_word = word_list[0]
  winning_score = 0

  tie_breaker = []

  for word in word_list:
    test_score = score_word(word) #all errors are referring to previous function score_word. Maybe because reusing variables, score already calculated
    if test_score < winning_score:
      test_score = winning_score
      word = winning_word
    if test_score == winning_score:
      tie_breaker.append(winning_word)
      tie_breaker.append(word)
 #list comprehension for above code block, zip lists
 # max_score =  max_score = max(word_list)
  #find max_score of multiple values (find ties)
  #tie_breaker = [t for t in word_list if word_list == max_score]
  
  #check length of tie_breaker list, if it has one value return a tuple of the list
  if len(tie_breaker) == 0:
    return tuple(winning_word)

  else: 
    if len(tie_breaker[0]) == 10 and len(tie_breaker[1]) != 10:
      return tuple(tie_breaker[0])
    if tie_breaker[1] == 10 and tie_breaker[0] != 10:
      return tuple(tie_breaker[1])
    if len(tie_breaker[0]) == len(tie_breaker[1]):
      return tuple(tie_breaker[0])

    




