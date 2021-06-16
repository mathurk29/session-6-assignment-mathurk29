from collections import Counter
###################### 1.1 ######################

single_exp_generate_deck = [{x: y} for x in ['spades', 'clubs', 'hearts', 'diamonds'] for y in [
    'ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']]


####################### 1.2 ######################

def create_deck_of_cards() -> list:
    '''This function returns a list of tuples that represents the 52 cards in a deck of cards'''

    vals = ['ace', '2', '3', '4', '5', '6', '7',
            '8', '9', '10', 'jack', 'queen', 'king']

    suits = ['spades', 'clubs', 'hearts', 'diamonds']

    deck = []
    for s in suits:
        for v in vals:
            deck.append({s: v})
    return deck


####################### 1.3 ######################

def convert_faces_to_numbers(hand):
    '''  modify cards of input hands to integral values for easy computation of their comparisons '''
    result = []
    for x, y in hand:
        if y == 'jack':
            y = int(11)
        elif y == 'queen':
            y = int(12)
        elif y == 'king':
            y = int(13)
        # Marking Ace as 14 as it is superior to King(13) in Poker
        elif y == 'ace':
            y = int(14)
        else:
            y = int(y)
        result.append((x, y))

    return result


def find_hand_type(hand: list):
    ''' Returns the type of hand'''

    # sorting hand for easy calculations
    sorted_hand = sorted([y for x, y in hand])

    # check if all cards of the hand belong to same suit
    if len(set([x for x, y in hand])) == 1:

        # 10 to Ace, all of same suit
        if sum([y for x, y in hand]) == sum(range(10, 15)[-len(hand):]):
            return "royal_flush"

        # consecutive ranks, all of same suit
        elif sorted_hand == list(range(min(sorted_hand), max(sorted_hand)+1)):
            return "straight_flush"

        # inconsecutive ranks but all of same suit
        else:
            return "flush"

    frequency = Counter([y for x, y in hand])
    length_of_unique_ranks = len(frequency)
    most_common_ranks = frequency.most_common()

    # first most common
    mostcommon_first = most_common_ranks[0][1]
    if length_of_unique_ranks > 1:
        mostcommon_second = most_common_ranks[1][1]

    # three cards of same rank and two cards of some other rank
    if len(hand) == 5 and mostcommon_first == 3 and mostcommon_second == 2:
        return "full_house"

    # four cards of one rank
    if len(hand) >= 4 and mostcommon_first == 4:
        return "four_of_a_kind"

    # three cards of one rank
    if mostcommon_first == 3:
        return "three_of_a_kind"

    # two cards of one rank and two cards of another rank
    if len(hand) >= 4 and mostcommon_first == 2 and mostcommon_second == 2:
        return "two_pair"

    #  sequential ranks and not all of same suit
    if (sorted_hand == list(range(min(sorted_hand), max(sorted_hand)+1))) and (len(set([x for x, y in hand])) > 1):
        return "straight"

    # two cards of one rank
    if mostcommon_first == 2:
        return "one_pair"

    # no matching ranks among cards
    else:
        return "high_card"


def compare_hands(modified_first_hand: list, type_first_hand: str, modified_second_hand, type_second_hand: str):

    hands_rank_dict = \
        {
            "high_card": 1,
            "one_pair": 2,
            "two_pair": 3,
            "three_of_a_kind": 4,
            "straight": 5,
            "flush": 6,
            "full_house": 7,
            "four_of_a_kind": 8,
            "straight_flush": 9,
            "royal_flush": 10,
        }

    if type_first_hand != type_second_hand:

        return modified_first_hand if hands_rank_dict[type_first_hand] > hands_rank_dict[type_second_hand] else modified_second_hand

    else:
        ranks_hand1 = [y for x, y in modified_first_hand]
        ranks_hand2 = [y for x, y in modified_second_hand]

        if type_first_hand in ['royal_flush', 'straight_flush', 'flush', 'straight']:
            return modified_first_hand if max(ranks_hand1) > max(ranks_hand2) else modified_second_hand

        elif type_first_hand in ['four_of_a_kind', 'three_of_a_kind']:
            # compare the highest card of the quad/triplet
            return modified_first_hand if max(set(ranks_hand1), key=ranks_hand1.count) > max(set(ranks_hand2), key=ranks_hand2.count) else modified_second_hand

        elif type_first_hand == 'full_house':
            # first compare the triplets
            if max(set(ranks_hand1)) > max(set(ranks_hand2)):
                return modified_first_hand
            # triplets are deuce, so now compare pairs
            if min(set(ranks_hand1)) > min(set(ranks_hand2)):
                return modified_first_hand
            else:
                return modified_second_hand

        elif type_first_hand in ["two_pair", "one_pair"]:
            # compare the pair of higher rank
            if max([x for x in ranks_hand1 if ranks_hand1.count(x) == 2]) > max([x for x in ranks_hand2 if ranks_hand2.count(x) == 2]):
                return modified_first_hand
            # compare the rank of other only for two_pair case
            if type_first_hand == "two_pair" and min([x for x in ranks_hand1 if ranks_hand1.count(x) == 2]) > min([x for x in ranks_hand2 if ranks_hand2.count(x) == 2]):
                return modified_first_hand
            # compare kickers
            else:
                return modified_first_hand if [x for x in ranks_hand1 if ranks_hand1.count(x) == 1][0] > [x for x in ranks_hand2 if ranks_hand2.count(x) == 1][0] else modified_second_hand

        elif type_first_hand == "high_card":
            return modified_first_hand if max(ranks_hand1) > max(ranks_hand2) else modified_second_hand

        else:
            raise Exception(
                "There is problem either in the input validation or hand comparisons.")


def play_poker(first_hand: list, second_hand: list) -> tuple:
    ''' Wrapper function which validate, transform and compare hands. Returns the winner hand. '''

    # Validations
    for suit, _ in first_hand:
        if suit not in ['spades', 'clubs', 'hearts', 'diamonds']:
            raise ValueError(
                "suit should be one of these: spades , clubs , hearts , diamonds")
    for suit, _ in second_hand:
        if suit not in ['spades', 'clubs', 'hearts', 'diamonds']:
            raise ValueError(
                "suit should be one of these: spades , clubs , hearts , diamonds but I found " + suit)
    for _, val in first_hand:
        if val not in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']:
            raise ValueError(
                "Provide card ranks as strings. For face values, supply lowercase strings. For first hand I got: " + val)
    for _, val in second_hand:
        if val not in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']:
            raise ValueError(
                "Provide card ranks as strings. For face values, supply lowercase strings. For second hand I got: " + val)
    if len(first_hand) not in (3, 4, 5) or len(second_hand) not in (3, 4, 5):
        raise ValueError(
            'Length of a hand is either less than 3 or greater than 5')
    if set(first_hand).intersection(set(second_hand)) != set():
        raise ValueError(
            "Same card present in both hands. Casino Security on the way!")

    # convert cards of input hands to integral values for easy computation of their comparisons
    modified_first_hand = convert_faces_to_numbers(first_hand)
    modified_second_hand = convert_faces_to_numbers(second_hand)

    # find the type of each hand
    type_first_hand = find_hand_type(modified_first_hand)
    type_second_hand = find_hand_type(modified_second_hand)

    # find the winner hand
    wining_hand = compare_hands(
        modified_first_hand, type_first_hand, modified_second_hand, type_second_hand)

    # return the winning hand with it's type
    return [type_first_hand, first_hand] if wining_hand == modified_first_hand else [type_second_hand, second_hand]
