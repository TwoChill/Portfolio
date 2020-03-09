import os
import base as clss
import time

# Show 'PayOut' on screen.
clss.sys_clear(OnScreen=clss.payout)

card_nrs = [i for i in range(1, 15)]
suits = {'Spades': '♠', 'Diamonds': '♦',
         'Hearts': '♥', 'Clubs': '♣', 'Joker': '§'}
suits.pop('Joker')

# Dictionary of per card nr and there suits. Exclude the joker which is appended on the last line 4 times.
all_card_combinations = {k: list(suits.keys()) for k in card_nrs}
all_card_combinations[len(card_nrs) + 1] = ['Joker' for i in range(len(suits))]
suits['Joker'] = '§'

NR_OF_CARDS = 5

# Create instance of cards
cards = clss.Cards(NR_OF_CARDS, suits, all_card_combinations)

# Creates the Flop (Front Acsii-Cards)
dealer = clss.Dealer(NR_OF_CARDS, suits, all_card_combinations)
front_ascii_cards, set_cards_suits = cards.create_cards(NR_OF_CARDS)
the_flop = dealer.shuffles(front_ascii_cards, NR_OF_CARDS)

print(set_cards_suits)

# Deals the Flop
dealer.deals_cards(the_flop, NR_OF_CARDS)


# Player select cards
player = clss.Select(the_flop, NR_OF_CARDS, suits, all_card_combinations)
player.color_selects(the_flop)
