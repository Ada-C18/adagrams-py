
import random

tiles_org = ["A", "A", "A","A", "A", "A","A", "A", "A","B", "B", "C", "C", 'D', 'D', 'D', 'D', 'E', 'E','E', 'E', 'E','E', 'E', 'E','E', 'E', 'E','E', 'F', 'F', 'G', 'G', 'G', 'H', 'H', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'J', 'K', 'L', 'L', 'L', 'L', 'M', 'M', 'N', 'N', 'N', 'N', 'N', 'N', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'P', 'P', 'Q', 'R', 'R', 'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'T', 'T', 'U', 'U', 'U', 'U', 'V', 'V', 'W', 'W', 'X', 'Y', 'Y', 'Z']


def draw_letters():
    tiles=tiles_org.copy()
    hand = []

    for letter in range(10):
        tile = random.randint(0,len(tiles)-1)
        hand.append(tiles[tile])
        tiles.remove(tiles[tile])
    return hand

# def uses_available_letters(word, letter_bank):
#     pass

# def score_word(word):
#     pass

# def get_highest_word_score(word_list):
#     pass

#this is a message