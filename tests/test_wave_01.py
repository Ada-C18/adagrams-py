import pytest
from scipy import stats as stats
from pprint import pprint
from collections import Counter

from adagrams.game import draw_letters

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

def test_draw_letters_draws_ten():
    # Arrange/Act
    letters = draw_letters()

    # Assert
    assert len(letters) == 10

def test_draw_letters_is_list_of_letter_strings():
    # Arrange/Act
    letters = draw_letters()

    # Assert
    assert len(letters) == 10

    for elem in letters:
        assert type(elem) == str
        assert len(elem) == 1

def test_letter_not_selected_too_many_times():

    for i in range(1000):
        # Arrange/Act
        letters = draw_letters()

        letter_freq = {}
        for letter in letters:
            if letter in letter_freq:
                letter_freq[letter] += 1
            else:
                letter_freq[letter] = 1
        
        # Assert
        for letter in letters:
            assert letter_freq[letter] <= LETTER_POOL[letter]

def test_chi_square_frequencies():

    # this *should* work 
    # technique adapted from 
    # http://practicalcryptography.com/cryptanalysis/text-characterisation/chi-squared-statistic/
    # TODO: get someone with better stats experience to 
    # double-check this

    # arrange/act


    # normalize LETTER_POOL frequencies
    pool_sum = sum(LETTER_POOL.values())
    pool_freqs = {}
    for letter, value in LETTER_POOL.items():
        pool_freqs[letter] = value / pool_sum
    

    # collect our sample
    sample_counter = Counter()
    for i in range (500): 
        letters = draw_letters()
        for letter in letters:
            sample_counter[letter] += 1

    # organize our expected and sample
    # into parallel lists
    expected = []
    sample = []
    total = sample_counter.total()
    for letter, freq in pool_freqs.items():
        expected.append(freq * total)
        sample.append(sample_counter[letter])
    
    # pprint(sample)
    # pprint(expected)
    # pprint(sum(expected))
    chi  = stats.chisquare(sample, expected)
    pprint(chi.pvalue)

    assert chi.pvalue > 0.05
        

        






