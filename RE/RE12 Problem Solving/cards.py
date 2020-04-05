"""
First, write an auxiliary Python function card_value(card) that, given a card, returns its value. The values of the cards correspond to their numerical value from 2-10, all face cards (Jack, Queen, King) count 10 and the Ace counts 11. If the suits are black (clubs and spades) the value of the card doubles. 🂡 🃑

Then re-write a new Python function play(seed) that returns a string with the winners of the game (for example, "P1 P4"). 
""" 

import cards
import random

def card_value(card):
    figs = {'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    if card[1] in figs:
        val = int(figs[card[1]])
    else:
        val = int(card[1])
    if card[0] == '♠' or card[0] == '♣':
        return val*2
    else:
        return val


def play(seed):
    result = ''
    random.seed(seed)
    deck = cards.create_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, cards.deal_hands(deck))}
    print(hands['P1'])
    row_points = {'P1': 0, 'P2': 0, 'P3': 0, 'P4': 0}
    start_player = cards.choose(names)
    turn_order = cards.player_order(names, start=start_player)
    final_pont = {'P1': 0, 'P2': 0, 'P3':0, 'P4': 0}
    while hands[start_player]:
        row_points = {'P1': 0, 'P2': 0, 'P3': 0, 'P4': 0}
        for name in turn_order:
            card = cards.choose(hands[name])
            print(name)
            row_points[name] += card_value(card)
            hands[name].remove(card)
            print(row_points)
        points_sort = sorted(row_points.items(), key = lambda x: x[1], reverse=True)
        max_pont = points_sort[0][1]
        for k, v in row_points.items():
            if v == max_pont:
                final_pont[k] += 1
    final_sort = sorted(final_pont.items(), key = lambda x: x[1], reverse=True)
    max_pont = final_sort[0][1]
    for k, v in final_pont.items():
        if v == max_pont:
            result += k + ' '
    return result.strip()

print(play(123))
print(play(35791113))
print(play(580))
print(play(98765432))
print(play(999))
print(play(31))
print(play(72))
print(play(19))
