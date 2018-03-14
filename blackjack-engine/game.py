from deck import CARD, get_deck
from enum import Enum, auto

class ACTION(Enum):
    HIT = auto()
    STAND = auto()

class ACTION(Enum):
    HIT = auto()
    STAND = auto()
    SURRENDER = auto()   

def create_game():
    game_state = {
        'deck': get_deck(),
        'dealer': {'cards': []},
        'player': {'cards': []},
        'finished': False,
        'winner': None
    }

    game_state['dealer']['cards'].append(game_state['deck'].popleft())

    for _ in range(2):
        game_state['player']['cards'].append(game_state['deck'].popleft())

    return game_state

def play_turn(game_state, who, action):
    if action == ACTION.HIT:
        game_state[who]['cards'].append(game_state['deck'].popleft())
    if action == ACTION.STAND:
        pass
    if action == ACTION.SURRENDER:
        game_state[who]['surrendered'] = True
        pass

    game_state = check_winner(game_state)

    return game_state

def check_winner(game_state):
    for p in ['player', 'dealer']:
        pass   

if __name__ == '__main__':
    game = create_game()
    game = play_turn(game, 'player', ACTION.HIT)
    print(game)