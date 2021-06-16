import pytest
import part1
import inspect
import re
import os



def test_session6_function_name_had_cap_letter():
    """ 
    Test check to prohibit use capitalization in functions name.
    """
    functions = inspect.getmembers(part1, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"



####################################################### Validations for play_poker()######################################

def test_session6_play_poker_no_args():
    
    first_hand = [('spades', 'ace'), ('hearts', 'king'), ('diamonds', '10'), ('diamonds', '7'), ('diamonds', 'ace')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '7'), ('clubs', '2')]
    with pytest.raises(TypeError, match=r".*required positional argument*"):
        part1.play_poker()


def test_session6_play_poker_cards_in_hand_limit():
    
    first_hand = [('spades', 'ace'), ('hearts', 'king')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '7'), ('clubs', '2')]
    with pytest.raises(ValueError, match=r".*no of cards in a hand should be between 3 and 5 inclusive*"):
        part1.play_poker(first_hand, second_hand)


def test_session6_play_poker_cards_incorrect_suit():
    
    first_hand = [('SALESFORCE', 'ace'), ('hearts', 'king'), ('diamonds', '10'), ('diamonds', '7'), ('diamonds', 'ace')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '7'), ('clubs', '2')]
    with pytest.raises(ValueError, match=r".*suit should be one of these: spades , clubs , hearts , diamonds*"):
        part1.play_poker(first_hand, second_hand)


def test_session6_play_poker_cards_incorrect_vals():
    
    first_hand = [('spades', 'SRIGANGANAGAR'), ('hearts', 'king'), ('diamonds', '10'), ('diamonds', '7'), ('diamonds', 'ace')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '7'), ('clubs', '2')]
    with pytest.raises(ValueError, match=r".*Woah! Don't you know cards*"):
        part1.play_poker(first_hand, second_hand)



def test_session6_play_poker():
    '''  '''

    first_hand = [('spades', 'ace'), ('hearts', 'king'), ('diamonds', '10'), ('diamonds', '7'), ('diamonds', 'ace')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '7'), ('clubs', '2')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'one_pair', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == first_hand, "winner hand values are not correct"


    first_hand = [('spades', 'ace'), ('spades', 'king'), ('spades', '10'), ('spades', 'jack'), ('spades', 'queen')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '7'), ('clubs', '2')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'royal_flush', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == first_hand, "winner hand values are not correct"


    first_hand = [('spades', '9'), ('spades', 'king'), ('spades', '10'), ('spades', 'jack'), ('spades', 'queen')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '7'), ('clubs', '2')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'straight_flush', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == first_hand, "winner hand values are not correct"


    first_hand = [('spades', '9'), ('spades', '2'), ('spades', '10'), ('spades', 'jack'), ('spades', 'queen')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '5'), ('clubs', '2')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'flush', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == first_hand, "winner hand values are not correct"


    first_hand = [('spades', '9'), ('clubs', '9'), ('diamonds', '9'), ('hearts', '9'), ('spades', 'queen')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '5'), ('clubs', '2')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'four_of_a_kind', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == first_hand, "winner hand values are not correct"    


    first_hand = [('spades', '9'), ('clubs', '9'), ('diamonds', '9'), ('hearts', 'queen'), ('spades', 'queen')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '5'), ('clubs', '2')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'full_house', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == first_hand, "winner hand values are not correct"    


    first_hand = [('spades', '9'), ('clubs', '9'), ('diamonds', '9'), ('hearts', '5'), ('spades', 'queen')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '5'), ('clubs', '2')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'three_of_a_kind', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == first_hand, "winner hand values are not correct"        


    first_hand = [('spades', '9'), ('clubs', '9'), ('diamonds', '8'), ('hearts', 'queen'), ('spades', 'queen')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '5'), ('clubs', '2')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'two_pair', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == first_hand, "winner hand values are not correct"            


    first_hand = [('spades', '9'), ('clubs', '2'), ('diamonds', '7'), ('hearts', 'queen'), ('spades', 'ace')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '5'), ('clubs', '2')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'high_card', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == first_hand, "winner hand values are not correct"            


    first_hand = [('spades', '9'), ('clubs', '2'), ('diamonds', '7'), ('hearts', 'queen')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '5')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'high_card', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == first_hand, "winner hand values are not correct"    


    first_hand = [('spades', '9'), ('clubs', '2'), ('diamonds', '7')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'high_card', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == first_hand, "winner hand values are not correct"        


    first_hand = [('spades', 'ace'), ('spades', 'king'), ('spades', 'jack'), ('spades', 'queen')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '7')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'royal_flush', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == first_hand, "winner hand values are not correct"    


    first_hand = [('spades', 'ace'), ('spades', 'king'), ('spades', 'queen')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'royal_flush', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == first_hand, "winner hand values are not correct"       


    first_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '5')]
    second_hand = [('spades', '9'), ('clubs', '9'), ('diamonds', '9'), ('hearts', '5')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'three_of_a_kind', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == second_hand, "winner hand values are not correct"

    first_hand = [('spades', '8'), ('clubs', 'queen'), ('diamonds', 'jack'), ('hearts', '5')]
    second_hand = [('hearts', 'king'), ('spades', '7'), ('spades', '8'), ('clubs', '7')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'one_pair', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == second_hand, "winner hand values are not correct"

    first_hand = [('spades', '8'), ('spades', 'queen'), ('spades', 'jack'), ('spades', '5')]
    second_hand = [('hearts', 'king'), ('spades', '7'), ('spades', '8'), ('clubs', '7')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'flush', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == first_hand, "winner hand values are not correct"