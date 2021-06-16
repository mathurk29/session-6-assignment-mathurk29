from collections import Counter
# 1

deck = [{x: y} for x in ['spades', 'clubs', 'hearts', 'diamonds'] for y in [
    'ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']]
len(deck)

# 2


def create_deck_of_cards() -> list:
    ''' This function returns a list of tuples that represents the 52 cards in a deck of cards. '''

    vals = ['ace', '2', '3', '4', '5', '6', '7',
            '8', '9', '10', 'jack', 'queen', 'king']

    suits = ['spades', 'clubs', 'hearts', 'diamonds']

    deck = []
    for v in vals:
        for s in suits:
            deck.append({s: v})
    return deck


len(create_deck_of_cards())


# 3


def convert_faces_to_numbers(hand):
    result = []
    for x, y in hand:
        if y == 'jack':
            y = 11
        elif y == 'queen':
            y = 12
        elif y == 'king':
            y = 13
        elif y == 'ace':
            y = 14
        else:
            y = int(y)
        result.append((x, y))

    # converted faces to numbers
    return result


def find_hand_type(hand, val_int, sizeof_hand):

    # sorted hand to manipulate values in hand
    sorted_hand = sorted([y for x, y in hand])

    # check for hands where all cards belong to same suit
    if len(set([x for x, y in hand])) == 1:

        # check for royal flush

        if sum([y for x, y in hand]) == sum(val_int[-sizeof_hand:]):
            return "royal_flush"
        # check for straight_flush
        elif sorted_hand == list(range(min(sorted_hand), max(sorted_hand)+1)):
            return "straight_flush"
        else:
            return "flush"

    occurrences = Counter([y for x, y in hand])

    # how many distinct values exist
    unique_values = len(occurrences)

    most_common_values = occurrences.most_common(unique_values)

    # first most common count
    mostcommon_first = most_common_values[0][1]
    # second most common count if it exists
    if unique_values > 1:
        mostcommon_second = most_common_values[1][1]

    if sizeof_hand == 5 and mostcommon_first == 3 and mostcommon_second == 2:
        return "full_house"

    if sizeof_hand in [4, 5] and mostcommon_first == 4:
        return "four_of_a_kind"

    if mostcommon_first == 3:
        return "three_of_a_kind"

    if sizeof_hand in [4, 5] and mostcommon_first == 2 and mostcommon_second == 2:
        return "two_pair"

    if (len(set([x for x, y in hand])) > 1) and (sorted_hand == list(range(min(sorted_hand), max(sorted_hand)+1))):
        return "straight"

    if mostcommon_first == 2:
        return "one_pair"
    else:
        return "high_card"


def find_winner(poker_hands, modified_hand_1, type_1, modified_hand_2, type_2):

    if type_1 != type_2:
        if poker_hands[type_1] > poker_hands[type_2]:
            return modified_hand_1
        else:
            return modified_hand_2
    else:
        if type_1 in ['royal_flush', 'straight_flush', 'flush', 'straight']:
            return modified_hand_2 if sum([y for x, y in modified_hand_1]) > sum([y for x, y in modified_hand_2]) else modified_hand_2
        elif type_1 in ['four_of_a_kind', 'three_of_a_kind']:
            list_1 = [y for x, y in modified_hand_1]
            list_2 = [y for x, y in modified_hand_2]
            return modified_hand_1 if max(set(list_1), key=list_1.count) > max(set(list_2), key=list_2.count) else modified_hand_2
        elif type_1 == 'full_house':
            return modified_hand_1 if sum(set([y for x, y in modified_hand_1])) > sum(set([y for x, y in modified_hand_2])) else modified_hand_2
        elif type_1 in ["two_pair", "one_pair"]:
            list_1 = [y for x, y in modified_hand_1]
            set_1 = set(list_1)
            list_2 = [y for x, y in modified_hand_2]
            set_2 = set(list_2)
            return modified_hand_1 if sum([x for x in set_1 if list_1.count(x) == 2]) > sum([x for x in set_2 if list_2.count(x) == 2]) else modified_hand_2
        elif type_1 == "high_card":
            return modified_hand_1 if max([y for x, y in modified_hand_1]) > max([y for x, y in modified_hand_2]) else modified_hand_2


def play_poker(first_hand, second_hand):

    vals = ['2', '3', '4', '5', '6', '7', '8',
            '9', '10', 'jack', 'queen', 'king', 'ace']
    suits = ['spades', 'clubs', 'hearts', 'diamonds']

    val_int = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    poker_hands = {"royal_flush": 10, "straight_flush": 9, "four_of_a_kind": 8, "full_house": 7,
                   "flush": 6, "straight": 5, "three_of_a_kind": 4, "two_pair": 3, "one_pair": 2, "high_card": 1}

    length_hand = len(first_hand)

    # Validations

    if not (3 <= length_hand <= 5):
        raise ValueError(
            "no of cards in a hand should be between 3 and 5 inclusive")

    for suit, _ in first_hand:
        if suit not in ['spades', 'clubs', 'hearts', 'diamonds']:
            raise ValueError(
                "suit should be one of these: spades , clubs , hearts , diamonds")
    for suit, _ in second_hand:
        if suit not in ['spades', 'clubs', 'hearts', 'diamonds']:
            raise ValueError(
                "suit should be one of these: spades , clubs , hearts , diamonds")

    for _, val in first_hand:
        if val not in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']:
            raise ValueError("Woah! Don't you know cards?")
    for _, val in second_hand:
        if val not in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']:
            raise ValueError("Woah! Don't you know cards?")

    # get the modified hands for the input hands
    mod_player1 = convert_faces_to_numbers(first_hand)
    mod_player2 = convert_faces_to_numbers(second_hand)

    # find the type of each hand
    type_1 = find_hand_type(mod_player1, val_int, length_hand)
    type_2 = find_hand_type(mod_player2, val_int, length_hand)

    # find the winner hand
    winner_hand = find_winner(poker_hands, mod_player1,
                        type_1, mod_player2, type_2)

    # return the original winner hand
    return [type_1, first_hand] if winner_hand == mod_player1 else [type_2, second_hand]
