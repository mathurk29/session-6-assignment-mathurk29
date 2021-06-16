import pytest
import part1
import inspect
import re
import os
from part1 import create_deck_of_cards

####################################################################Validations for README.md####################################################################


README_CONTENT_CHECK_FOR = [
    'play_poker',
    'find_hand_type',
    'Validations',
    'compare_hands'
]


def test_session6_readme_exists():
    """ 
    checks for the existence of README.md
    """
    assert os.path.isfile('README.md'), "README.md file is missing"


def test_session6_readme_500_words():
    """
    Verifies that the README.md has at least 500 words!
    """
    readme_words = [word for line in open(
        'README.md', 'r', encoding='utf-8') for word in line.split()]
    assert len(
        readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_session6_readme_proper_description():
    """ 
    Verifies whether the README.md explains all the functions which are present in session6.py. 
    """
    READMELOOKSGOOD = True
    f = open('README.md', 'r', encoding='utf-8')
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            print(f'{c}')
            READMELOOKSGOOD = False
            break
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_session6_readme_file_for_more_than_10_hashes():
    """ 
    Checks whether the README.md is properly formatted by counting the number of headings. 
    """
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_session6_indentations_part1():
    """
    Verifies if the part1.py file follows the PEP8 guidelines. 
    """
    lines = inspect.getsource(part1)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        print(space)
        print(f'len of space {len(space)}')
        print('done')
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(
            r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_session6_function_name_had_cap_letter():
    """ 
    Test check to prohibit use capitalization in functions name.
    """
    functions = inspect.getmembers(part1, inspect.isfunction)
    for function in functions:
        assert len(re.findall(
            '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"






##################################################### Validations for 1 and 2######################################

manual_deck = [
    {'spades': 'ace'}, {'spades': '2'}, {'spades': '3'}, {'spades': '4'}, {'spades': '5'}, {'spades': '6'}, {'spades': '7'}, {'spades': '8'}, {'spades': '9'}, {'spades': '10'}, {'spades': 'jack'}, {'spades': 'queen'}, {'spades': 'king'},
    {'clubs': 'ace'}, {'clubs': '2'}, {'clubs': '3'}, {'clubs': '4'}, {'clubs': '5'}, {'clubs': '6'}, {'clubs': '7'}, {'clubs': '8'}, {'clubs': '9'}, {'clubs': '10'}, {'clubs': 'jack'}, {'clubs': 'queen'}, {'clubs': 'king'}, 
    {'hearts': 'ace'}, {'hearts': '2'}, {'hearts': '3'}, {'hearts': '4'}, {'hearts': '5'}, {'hearts': '6'}, {'hearts': '7'}, {'hearts': '8'}, {'hearts': '9'}, {'hearts': '10'}, {'hearts': 'jack'}, {'hearts': 'queen'}, {'hearts': 'king'}, 
    {'diamonds': 'ace'}, {'diamonds': '2'}, {'diamonds': '3'}, {'diamonds': '4'}, {'diamonds': '5'}, {'diamonds': '6'}, {'diamonds': '7'}, {'diamonds': '8'}, {'diamonds': '9'}, {'diamonds': '10'}, {'diamonds': 'jack'}, {'diamonds': 'queen'}, {'diamonds': 'king'}

]

def test_single_exp():
    assert part1.single_exp_generate_deck == manual_deck, 'Single expression for generating deck is incorrect!'


def test_create_deck_of_cards():
    assert create_deck_of_cards() == manual_deck, "function create_deck_of_cards is not functioning properly"






##################################################### Validations for play_poker()######################################

def test_session6_part1_no_args():

    first_hand = [('spades', 'ace'), ('hearts', 'king'),
                  ('diamonds', '10'), ('diamonds', '7'), ('diamonds', 'ace')]
    second_hand = [('hearts', '4'), ('spades', '7'),
                   ('spades', '8'), ('clubs', '7'), ('clubs', '2')]
    with pytest.raises(TypeError, match=r".*required positional argument*"):
        part1.play_poker()


def test_session6_part1_incorrect_suit():

    first_hand = [('SALESFORCE', 'ace'), ('hearts', 'king'),
                  ('diamonds', '10'), ('diamonds', '7'), ('diamonds', 'ace')]
    second_hand = [('hearts', '4'), ('spades', '7'),
                   ('spades', '8'), ('clubs', '7'), ('clubs', '2')]
    with pytest.raises(ValueError, match=r".*suit should be one of these: spades , clubs , hearts , diamonds*"):
        part1.play_poker(first_hand, second_hand)


def test_session6_part1_incorrect_vals():

    first_hand = [('spades', 'SRIGANGANAGAR'), ('hearts', 'king'),
                  ('diamonds', '10'), ('diamonds', '7'), ('diamonds', 'ace')]
    second_hand = [('hearts', '4'), ('spades', '7'),
                   ('spades', '8'), ('clubs', '7'), ('clubs', '2')]
    with pytest.raises(ValueError, match=r".*Provide card ranks as strings*"):
        part1.play_poker(first_hand, second_hand)


def test_session6_part1_check_duplicate_cards():
    pass
    first_hand = [('spades', 'ace'), ('hearts', 'king'),
                  ('diamonds', '10'),  ('clubs', '7'), ('diamonds', 'ace')]
    second_hand = [('hearts', '4'), ('spades', '7'),
                   ('spades', '8'), ('clubs', '7'), ('clubs', '2')]
    with pytest.raises(ValueError, match=r".*Same card present in both hands*"):
        part1.play_poker(first_hand, second_hand)


def test_session6_play_poker():
    ''' Comparing 10 hands with each other '''

    # Comparing the 10 types of hands with each other one by one.
    # i.e.
    # 'Royal Flush' to 'Straight Flush', then 'Straight Flush' to 'Four of a Kind', 'Four of a Kind' to 'Full House'
    # and so on...

    first_hand = [('hearts', 'ace'), ('hearts', 'king'),
                  ('hearts', 'queen'), ('hearts', 'jack'), ('hearts', '10')]
    second_hand = [('spades', '10'), ('spades', '9'),
                   ('spades', '8'), ('spades', '7'), ('spades', '6')]
    assert part1.play_poker(first_hand, second_hand)[
        0] == 'royal_flush', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[
        1] == first_hand, "winner hand values are not correct"

    first_hand = [('spades', '10'), ('spades', '9'),
                  ('spades', '8'), ('spades', '7'), ('spades', '6')]
    second_hand = [('diamonds', 'queen'), ('clubs', 'queen'),
                   ('spades', 'queen'), ('hearts', 'queen'), ('spades', '5')]
    assert part1.play_poker(first_hand, second_hand)[
        0] == 'straight_flush', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[
        1] == first_hand, "winner hand values are not correct"

    first_hand = [('diamonds', 'queen'), ('clubs', 'queen'),
                  ('spades', 'queen'), ('hearts', 'queen'), ('spades', '5')]
    second_hand = [('hearts', 'ace'), ('spades', 'ace'),
                   ('clubs', 'ace'), ('spades', 'king'), ('hearts', 'king')]
    assert part1.play_poker(first_hand, second_hand)[
        0] == 'four_of_a_kind', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[
        1] == first_hand, "winner hand values are not correct"

    first_hand = [('hearts', 'ace'), ('spades', 'ace'),
                  ('clubs', 'ace'), ('spades', 'king'), ('hearts', 'king')]
    second_hand = [('hearts', 'queen'), ('hearts', '8'),
                   ('hearts', '6'), ('hearts', '4'), ('hearts', '2')]
    assert part1.play_poker(first_hand, second_hand)[
        0] == 'full_house', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[
        1] == first_hand, "winner hand values are not correct"

    first_hand = [('hearts', 'king'), ('hearts', '8'),
                  ('hearts', '6'), ('hearts', '4'), ('hearts', '2')]
    second_hand = [('clubs', '8'), ('spades', '7'),
                   ('clubs', '6'), ('spades', '5'), ('diamonds', '4')]
    assert part1.play_poker(first_hand, second_hand)[
        0] == 'flush', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[
        1] == first_hand, "winner hand values are not correct"

    first_hand = [('clubs', '8'), ('spades', '7'),
                  ('clubs', '6'), ('spades', '5'), ('diamonds', '4')]
    second_hand = [('hearts', 'queen'), ('diamonds', 'queen'),
                   ('spades', 'queen'), ('hearts', '7'), ('spades', '2')]
    assert part1.play_poker(first_hand, second_hand)[
        0] == 'straight', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[
        1] == first_hand, "winner hand values are not correct"

    first_hand = [('hearts', 'queen'), ('diamonds', 'queen'),
                  ('spades', 'queen'), ('hearts', '7'), ('spades', '2')]
    second_hand = [('hearts', 'jack'), ('clubs', 'jack'),
                   ('diamonds', '9'), ('spades', '9'), ('clubs', '5')]
    assert part1.play_poker(first_hand, second_hand)[
        0] == 'three_of_a_kind', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[
        1] == first_hand, "winner hand values are not correct"

    first_hand = [('hearts', 'jack'), ('clubs', 'jack'),
                  ('diamonds', '9'), ('spades', '9'), ('clubs', '5')]
    second_hand = [('hearts', 'king'), ('spades', 'king'),
                   ('clubs', '9'), ('clubs', '8'), ('hearts', '4')]
    assert part1.play_poker(first_hand, second_hand)[
        0] == 'two_pair', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[
        1] == first_hand, "winner hand values are not correct"

    first_hand = [('hearts', 'king'), ('spades', 'king'),
                  ('clubs', '9'), ('clubs', '8'), ('hearts', '4')]
    second_hand = [('hearts', 'ace'), ('clubs', 'queen'),
                   ('diamonds', '6'), ('spades', '4'), ('clubs', '2')]
    assert part1.play_poker(first_hand, second_hand)[
        0] == 'one_pair', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[
        1] == first_hand, "winner hand values are not correct"

    # Comparing two hands of same type and determine which has higher ranking card

    # Skipping Royal Flush as two royal flush will only result in deuce.

    first_hand = [('spades', '10'), ('spades', '9'),
                  ('spades', '8'), ('spades', '7'), ('spades', 'jack')]
    second_hand = [('spades', '6'), ('spades', '5'),
                   ('spades', '4'), ('spades', '3'), ('spades', '2')]
    assert part1.play_poker(first_hand, second_hand)[
        0] == 'straight_flush', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[
        1] == first_hand, "winner hand values are not correct"

    first_hand = [('diamonds', 'queen'), ('clubs', 'queen'),
                  ('spades', 'queen'), ('hearts', 'queen'), ('spades', '5')]
    second_hand = [('diamonds', 'jack'), ('clubs', 'jack'),
                   ('spades', 'jack'), ('hearts', 'jack'), ('spades', '6')]
    assert part1.play_poker(first_hand, second_hand)[
        0] == 'four_of_a_kind', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[
        1] == first_hand, "winner hand values are not correct"

    first_hand = [('hearts', 'ace'), ('spades', 'ace'),
                  ('clubs', 'ace'), ('spades', 'king'), ('clubs', 'king')]
    second_hand = [('hearts', 'jack'), ('spades', 'jack'),
                   ('clubs', 'jack'), ('diamonds', 'king'), ('hearts', 'king')]
    assert part1.play_poker(first_hand, second_hand)[
        0] == 'full_house', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[
        1] == first_hand, "winner hand values are not correct"

    first_hand = [('hearts', 'king'), ('hearts', '8'),
                  ('hearts', '6'), ('hearts', '4'), ('hearts', '2')]
    second_hand = [('diamonds', 'queen'), ('diamonds', '8'),
                   ('diamonds', '6'), ('diamonds', '4'), ('diamonds', '2')]
    assert part1.play_poker(first_hand, second_hand)[
        0] == 'flush', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[
        1] == first_hand, "winner hand values are not correct"

    first_hand = [('clubs', '8'), ('spades', '7'),
                  ('clubs', '6'), ('spades', '5'), ('diamonds', '4')]
    second_hand = [('clubs', '7'), ('diamonds', '6'),
                   ('clubs', '5'), ('clubs', '4'), ('spades', '3')]
    assert part1.play_poker(first_hand, second_hand)[
        0] == 'straight', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[
        1] == first_hand, "winner hand values are not correct"

    first_hand = [('hearts', 'queen'), ('diamonds', 'queen'),
                  ('spades', 'queen'), ('hearts', '7'), ('spades', '2')]
    second_hand = [('hearts', 'jack'), ('diamonds', 'jack'),
                   ('spades', 'jack'), ('hearts', '8'), ('spades', '3')]
    assert part1.play_poker(first_hand, second_hand)[
        0] == 'three_of_a_kind', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[
        1] == first_hand, "winner hand values are not correct"

    first_hand = [('hearts', 'jack'), ('clubs', 'jack'),
                  ('diamonds', '9'), ('spades', '9'), ('clubs', '5')]
    second_hand = [('hearts', '10'), ('clubs', '10'),
                   ('diamonds', '4'), ('spades', '4'), ('clubs', '2')]
    assert part1.play_poker(first_hand, second_hand)[
        0] == 'two_pair', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[
        1] == first_hand, "winner hand values are not correct"

    first_hand = [('hearts', 'jack'), ('clubs', 'jack'),
                  ('diamonds', '10'), ('spades', '10'), ('clubs', '5')]
    second_hand = [('diamonds', 'jack'), ('diamonds', 'jack'),
                   ('diamonds', '9'), ('spades', '9'), ('clubs', '6')]
    assert part1.play_poker(first_hand, second_hand)[
        0] == 'two_pair', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[
        1] == first_hand, "winner hand values are not correct"

    first_hand = [('hearts', 'king'), ('spades', 'king'),
                  ('clubs', '9'), ('clubs', '8'), ('hearts', '4')]
    second_hand = [('hearts', 'queen'), ('spades', 'queen'),
                   ('clubs', '5'), ('clubs', '4'), ('hearts', '2')]
    assert part1.play_poker(first_hand, second_hand)[
        0] == 'one_pair', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[
        1] == first_hand, "winner hand values are not correct"
