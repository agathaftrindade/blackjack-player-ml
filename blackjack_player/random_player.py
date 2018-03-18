import random
from blackjack_engine.match import ACTION

class RandomPlayer:
    def play(self, match_state):
        return random.choice([ACTION.HIT, ACTION.STAND])