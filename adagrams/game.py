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

#Takes the two inputs and stores them in one dictionary 
def generate_alphabet_data_list(quantity_data, value_data):
  all_letters = string.ascii_uppercase
  results = [] #dictionaries stored in results
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
#makes a list that generates the numbers of letters so its proportionate to the probability of getting a certain letter
def letter_soup(letter_data):
  letter_soup = []

  for data in letter_data:
    runner = 0
    while runner < data['quantity']:
      letter_soup.append(data['letter'])
      runner += 1
  
  return letter_soup

todays_soup = letter_soup(alphabet_data_list)
#Returns letters to user
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

# Checks that letters being used in words are letters in a users letter bank
def uses_available_letters(word, letter_bank):

    letter_count = {}
  
# loop through word, convert all letters to uppercase, add count to letter_count
    for l in word:
      letter = l.upper()
      if letter not in letter_count:
        letter_count[letter] = 0
     
      letter_count[letter] += 1
      l_count = letter_count[letter] 

      if l_count > letter_bank.count(letter):
        return False
  
    return True

# Scores each user word
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

# Finds highest score in list of words 
def get_highest_word_score(word_list):

  if (len(word_list)) == 0:
    return None

  winning_words = []
  winning_score = 0

  for word in (word_list):
    value_of_word = score_word(word) 
    
    if value_of_word == winning_score: # if its a tie append it to list winning_words
      winning_words.append(word)

    elif value_of_word > winning_score:
        winning_score = value_of_word 
        winning_words = [word]

  # if length of word is one than no tie breaker neede
  if (len(winning_words)) == 1:
    return (winning_words[0], winning_score)
  
  shortest_word = None 
  shortest_length = None 
  
  for word_2 in winning_words:  
    word_length = len(word_2) #determine each words length

    # If word is 10 letters return it as the winner, will return first item in list
    if word_length == 10:
      return word_2, winning_score

    # Find which word has shortest length, initialize shortest length == None
    if shortest_length == None: 
      shortest_length = word_length
      shortest_word = word_2
    else:
      if word_length < shortest_length: 
        shortest_length = word_length
        shortest_word = word_2 
    
  return shortest_word, winning_score 
