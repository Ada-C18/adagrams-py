def mystery(numbers):
    index = 0
    while index < len(numbers):
        numbers[index] *= 2
        index += 1
    
    return numbers

nums = [1, 2, 3, 4, 5]
mystery(nums)

print(nums[3])






# def get_fire_students(students):
#     '''
#     INPUT: A list of dictionaries with the "name" and "class" key-value pairs.
#     Example:  get_fire_students([{ "name": "Ada", "class": "fire"}, { "name": "Taylor", "class": "earth" }])
#     RETURN VALUE: A list of dictionaries with **only** the students in the "fire" class.
#     '''
#     temp = []
#     students = students.copy() 
#     
#     while students:
#         student = students.pop()
#         if student["class"] == "fire":
#             temp.append(student)
# # 
# #     while temp:
# #         students.append(temp.pop())
#     print(students)
#     return students
# 
# 
# get_fire_students([{ "name": "Ada", "class": "fire"}, { "name": "Taylor", "class": "earth" }])

    cur_score = score_word(word)
    word_len = -len(word)
    has_10 = word_len == -10 # True if word length is 10.

# def hamming_distance(strand1, strand2):
#     count_of_differences = 0
#     index = 0
#     
# 
#     if len(strand1) == 0 or len(strand2) == 0:
#         raise ValueError("One of your inputs is invalid, please try again.")
#         
#       
#     for letter in strand2:
# #       if letter[index] not in strand2[index]: 
#         count_of_differences += 1
#         index += 1  
#         
#             
#     return count_of_differences  
# 
# print(hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"))
# print(hamming_distance("GAG", "GAG"))
# print(hamming_distance("GAG", ""))


# def score(word):  
# 
#     point_system = {
#       ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"): 1,
#       ("D", "G"): 2,
#       ("B", "C", "M", "P"): 3,
#       ("F", "H", "V", "W", "Y"): 4,
#       "K": 5,
#       ("J", "X"): 8,
#       ("Q", "Z"): 10
#     }
#     
#     total_score = 0
# 
#     try: 
#         word = word.upper()
#     except AttributeError as err:
#         return "You've entered a number, please enter a letter and try again."
#     except Exception:
#         print("You've entered a number, please enter a letter and try again.")
#         raise 
#     
#     letters_of_word = list(word)
#     
#     if len(letters_of_word) == 0:
#         return None
#     
#     else:
#         for letter in letters_of_word:
#             for key,value in point_system.items():
#                 if letter in key:
#                     total_score += value
#     return total_score
# 
# 
# # print(score("Dog"))
# # print(score(123))
# print(score("supercalifragilisticexpialidocious"))
# print(score(''))


# example input 1: "supercalifragilisticexpialidocious"
# expected output 1: 56

# example input 2: "Français"
# expected output 2:
# 
# def test_ridiculous_words():
#     # arrange
#     word = "supercalifragilisticexpialidocious"
#     # act
#     result = score(word)
#     # assert
#     assert result = 56
# 
# def test_letter_not_in_English():
#     # arrange
#     word = "Français"
#     # act
#     result = score(word)
#     # assert
#     result = 