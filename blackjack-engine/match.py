from enum import Enum, auto

import game_params
from deck import CARD, create_deck, calculate_points

class ACTION(Enum):
    HIT = auto()
    STAND = auto()
    SURRENDER = auto()   

class Match():

    def __init__(self):
        
        self.deck = create_deck()
        self.player = {'cards': [], 'finished': False}
        self.dealer = {'cards': [], 'finished': False}
        self.player_surrendered = False
        self.game_finished = True
        
        for _ in range(2):
            self.player['cards'].append(self.draw_card())

        for _ in range(2):
            self.dealer['cards'].append(self.draw_card())

    def draw_card(self):
        #TODO handle empty deck
        return self.deck.popleft()

    def play_player_turn(self, action):
        if action == ACTION.HIT:
            self.player['cards'].append(self.draw_card())
        if action == ACTION.STAND:
            self.player['finished'] = True
        if action == ACTION.SURRENDER:
            self.player_surrendered = True

    def _play_dealer_turn(self, action):
        if action == ACTION.HIT:
            self.dealer['cards'].append(self.draw_card())
        if action == ACTION.STAND:
            self.dealer['finished'] = True

    def play_dealer_turn(self):
        action = ACTION.HIT
        if calculate_points(self.dealer['cards']) >= game_params.DEALER_HITS_UNTIL:
            action = ACTION.STAND

        self._play_dealer_turn(action)       
        return action

    def get_winner(self):
        #TODO Blackjack instant win

        #Surrender
        if self.player_surrendered:
            return 'dealer'
        
        player_points = calculate_points(self.player['cards'])
        dealer_points = calculate_points(self.dealer['cards'])

        #Player busted
        if player_points > game_params.MAX_POINTS:
            return 'dealer'

        #Dealer busted
        if dealer_points > game_params.MAX_POINTS:
            return 'player'
               
        if not self.player['finished'] or not self.dealer['finished']:
            return None

        # Score comparison after game finished
        if dealer_points > player_points:
            return 'dealer'
        if dealer_points == player_points:
            return 'draw'
        return 'player'
        
if __name__ == '__main__':
    print('-----New Match-----')
    match = Match()
    print('player_cards:', match.player['cards'], '=>', calculate_points(match.player['cards']))
    print('player_cards:', match.dealer['cards'], '=>', calculate_points(match.dealer['cards']))
    print()
    
    from random import choice

    winner = ''
    while not winner:
        if not match.player['finished']:
            act = choice([ACTION.HIT, ACTION.STAND])
            print('Player', 'hits' if act == ACTION.HIT else 'stands')
            match.play_player_turn(act)
        else:
            act = match.play_dealer_turn()
            print('Dealer', 'hits' if act == ACTION.HIT else 'stands')

        print('player_cards:', match.player['cards'], '=>', calculate_points(match.player['cards']))
        print('player_cards:', match.dealer['cards'], '=>', calculate_points(match.dealer['cards']))
        print()
        winner = match.get_winner()

    print('winner:', match.get_winner())
    print('-----Match Ended-----')