from enum import Enum, auto
from random import shuffle
from collections import deque

from blackjack_engine import game_params

class CARD(Enum):
    ACE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()

def create_deck():
    cards = [
        [CARD.ACE] * 4,
        [CARD.TWO] * 4,
        [CARD.THREE] * 4,
        [CARD.FOUR] * 4,
        [CARD.FIVE] * 4,
        [CARD.SIX] * 4,
        [CARD.SEVEN] * 4,
        [CARD.EIGHT] * 4,
        [CARD.NINE] * 4,
        [CARD.TEN] * 4,
        [CARD.JACK] * 4,
        [CARD.QUEEN] * 4,
        [CARD.KING] * 4
    ]
    deck = [card for sublist in cards for card in sublist]
    shuffle(deck)
    return deque(deck)

def _get_points_for_card(card):
    if card == CARD.ACE: return (1, 11)
    if card == CARD.TWO: return 2
    if card == CARD.THREE: return 3
    if card == CARD.FOUR: return 4
    if card == CARD.FIVE: return 5
    if card == CARD.SIX: return 6
    if card == CARD.SEVEN: return 7
    if card == CARD.EIGHT: return 8
    if card == CARD.NINE: return 9
    if card == CARD.TEN: return 10
    if card == CARD.JACK: return 10
    if card == CARD.QUEEN: return 10
    if card == CARD.KING: return 10

def calculate_points(deck):
    normal_cards = [card for card in deck if card != CARD.ACE]
    aces = [card for card in deck if card == CARD.ACE]

    points = 0
    for card in normal_cards:
        points += _get_points_for_card(card)
    
    possible_points = [points]
    for ace in aces:
        possible_points = [p + ace_point for p in possible_points for ace_point in _get_points_for_card(ace)]

    possible_points.sort(reverse=True)

    # Return biggest possible point calculation that doesn't bust.
    # If not possible, return minimum possible value
    for p in possible_points[:-1]:
        if p <= game_params.MAX_POINTS:
            return p
    return possible_points[-1]