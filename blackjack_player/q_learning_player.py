from blackjack_engine.match import Match, ACTION
from blackjack_engine.deck import CARD

import numpy as np

def card_count(deck, card_type):
    return len([card for card in deck if card == card_type])

def preprocess_deck(deck):
    return (
        card_count(deck, CARD.ACE),
        card_count(deck, CARD.TWO),
        card_count(deck, CARD.THREE),
        card_count(deck, CARD.FOUR),
        card_count(deck, CARD.FIVE),
        card_count(deck, CARD.SIX),
        card_count(deck, CARD.SEVEN),
        card_count(deck, CARD.EIGHT),
        card_count(deck, CARD.NINE),
        card_count(deck, CARD.TEN),
        card_count(deck, CARD.KING),
        card_count(deck, CARD.QUEEN),
        card_count(deck, CARD.JACK)
    )

class QLearningPlayer:
    
    EXPLORATION_PROBABILITY = 0.2
    
    def __init__(self):
        self.q_table = {}
    
    def train(self):
        learn_rate = 1
        discount_factor = 0.9

        INTERATIONS = 10000
        for _ in range(INTERATIONS):
            match = Match()
            winner = ''
            visited_states = []
            while not winner:
                if not match.player['finished']:

                    player_cards = preprocess_deck(match.player['cards'])

                    act = self.play({
                        'player_cards': player_cards,
                    }, explore=True)
                    visited_states.append((player_cards, act))

                    match.play_player_turn(act)
                else:
                    act = match.play_dealer_turn()
                winner = match.get_winner()
                
            reward = -1
            if winner == 'player':
                reward = 1
            if winner == 'draw':
                reward = 0.5

            for i, (state, action) in enumerate(visited_states[::-1]):
                self.q_table[state] = self.q_table.get(state, {})
                self.q_table[state][action] = self.q_table[state].get(action, np.random.random())
                self.q_table[state][action] += reward * (discount_factor ** (i + 1))

        print('Q_table: ')
        for k, v in self.q_table.items():
            print(k, v)
        print()

    def play(self, match_state, explore=False):
        player_cards = preprocess_deck(match_state['player_cards'])

        reward_action_hit = self.q_table.get(player_cards, {}).get(ACTION.HIT, np.random.random())
        reward_action_stand = self.q_table.get(player_cards, {}).get(ACTION.STAND, np.random.random())

        action = ACTION.STAND
        if reward_action_hit > reward_action_stand:
            action =  ACTION.HIT

        exploration_move = ACTION.HIT if action == ACTION.STAND else ACTION.STAND
        if explore and np.random.random() < self.EXPLORATION_PROBABILITY:
            return exploration_move

        return action