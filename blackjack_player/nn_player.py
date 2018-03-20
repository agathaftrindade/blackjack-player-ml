from blackjack_engine.match import Match, ACTION
from blackjack_engine.deck import CARD

import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import plot_model

def card_count(deck, card_type):
    return len([card for card in deck if card == card_type])

class ReinforcementLearningPlayer:
    def train(self):
        self.model = Sequential()
        self.model.add(Dense(units=13, input_dim=13))
        self.model.add(Dense(units=13, activation='relu'))
        self.model.add(Dense(units=1, activation='sigmoid'))

        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        plot_model(self.model, to_file='model.png')

    def play(self, match_state):
        # a = np.array([1] * 14).reshape(1,14)
        nn_input = np.array([
            card_count(match_state['player_cards'], CARD.ACE),
            card_count(match_state['player_cards'], CARD.TWO),
            card_count(match_state['player_cards'], CARD.THREE),
            card_count(match_state['player_cards'], CARD.FOUR),
            card_count(match_state['player_cards'], CARD.FIVE),
            card_count(match_state['player_cards'], CARD.SIX),
            card_count(match_state['player_cards'], CARD.SEVEN),
            card_count(match_state['player_cards'], CARD.EIGHT),
            card_count(match_state['player_cards'], CARD.NINE),
            card_count(match_state['player_cards'], CARD.TEN),
            card_count(match_state['player_cards'], CARD.KING),
            card_count(match_state['player_cards'], CARD.QUEEN),
            card_count(match_state['player_cards'], CARD.JACK)
        ]).reshape((1, 13))

        # import random; return random.choice([ACTION.STAND, ACTION.HIT])
        y_pred = self.model.predict(nn_input)
        if y_pred > 0.5:
            return ACTION.HIT
        return ACTION.STAND