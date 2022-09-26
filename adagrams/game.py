def draw_letters():
    pass
    letter_pool_list = []
    hand_of_ten_letters = []

    for key, value in LETTER_POOL.items():
        for i in range(value):
            letter_pool_list.append(key)

    while len(hand_of_ten_letters) < 10:
        random_letter = random.choice(letter_pool_list)
        count = hand_of_ten_letters.count(random_letter)
        if count < LETTER_POOL[random_letter]:
            # print(random_letter)
            # print(count)
            # print(LETTER_POOL[random_letter])
            # print()
            hand_of_ten_letters.append(random_letter)
    return(hand_of_ten_letters)

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass