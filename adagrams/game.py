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
    for keys, values in data.items():
      runner = 0
      while runner < data['quantity']:
        letter_soup.append(data['letter'])
        runner += 1

  max_range = len(letter_soup) - 1
  user_letter_pool = []
  
  for r in range(0,9):
    draw = random.randint(0, max_range)
    drawn_letter = letter_soup[draw]

    if user_letter_pool.count(drawn_letter) == letter_soup.count(drawn_letter):
      pass
    else:
      user_letter_pool.append(drawn_letter)

  return user_letter_pool

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
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

def get_highest_word_score(word_list):
    pass