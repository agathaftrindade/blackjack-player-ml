from enum import Enum, auto
from random import shuffle
from collections import deque

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

def get_deck():
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
    shuffled = [card for sublist in cards for card in sublist]
    shuffle(shuffled)
    return deque(shuffled)