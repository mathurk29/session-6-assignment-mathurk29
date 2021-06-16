import random
import poker
#1

deck = [{x:y} for x in [ 'spades' , 'clubs' , 'hearts' , 'diamonds' ] for y in [ 'ace', '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'jack' , 'queen' , 'king' ]  ]
len(deck)

#2

def create_deck_of_cards_forloops() -> list:
    ''' This function returns a list of tuples that represents the 52 cards in a deck of cards. '''

    vals = [ 'ace', '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'jack' , 'queen' , 'king' ]

    suits = [ 'spades' , 'clubs' , 'hearts' , 'diamonds' ]
    
    deck = []
    for v in vals:
        for s in suits:
            deck.append({s:v})
    return deck

len(create_deck_of_cards_forloops())


