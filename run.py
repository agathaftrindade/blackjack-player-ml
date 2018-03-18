from blackjack_engine.match import Match, ACTION
from blackjack_engine.deck import calculate_points

from blackjack_player.random_player import RandomPlayer

MAX_ITERATIONS = 1000

def play_match(player):
    # print('-----New Match-----')

    match = Match()
    # print('player_cards:', match.player['cards'], '=>', calculate_points(match.player['cards']))
    # print('player_cards:', match.dealer['cards'], '=>', calculate_points(match.dealer['cards']))
    # print()
    winner = ''
    while not winner:
        if not match.player['finished']:
            match_state = {
                'player_cards': match.player['cards'],
                'dealer_cards': match.dealer['cards'][0]
            }
            act = player.play(match_state)
            # print('Player', 'hits' if act == ACTION.HIT else 'stands')
            match.play_player_turn(act)
        else:
            act = match.play_dealer_turn()
            # print('Dealer', 'hits' if act == ACTION.HIT else 'stands')
        # print('player_cards:', match.player['cards'], '=>', calculate_points(match.player['cards']))
        # print('player_cards:', match.dealer['cards'], '=>', calculate_points(match.dealer['cards']))
        # print()
        winner = match.get_winner()
    # print('winner:', match.get_winner())
    # print('-----Match Ended-----')
    return winner

def test_player(player):
    stats = {}
    for i in range(MAX_ITERATIONS):
        r = play_match(player)

        stats[r] = stats.get(r, 0)
        stats[r] = stats[r] + 1
    return stats

def print_stats(stats):
    print('dealer win rate:', stats['dealer'] / (stats['dealer'] + stats['player'] + stats['draw']))
    print('player win rate:', stats['player'] / (stats['dealer'] + stats['player'] + stats['draw']))
    print('draw rate:', stats['draw'] / (stats['dealer'] + stats['player'] + stats['draw']))

if __name__ == '__main__':
    print('Testing RandomPlayer')
    stats = test_player(RandomPlayer)
    print_stats(stats)
