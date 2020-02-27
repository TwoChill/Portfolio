import base as clss
import time

# Show 'PayOut' on screen.
clss.sys_clear(OnScreen=clss.payout)

card_nrs = [i for i in range(1, 15)]
suits = {'Spades': '♠', 'Diamonds': '♦', 'Hearts': '♥', 'Clubs': '♣', 'Joker': '§'}
suits.pop('Joker')

all_card_combinations = {k: list(suits.keys()) for k in card_nrs}
all_card_combinations[len(card_nrs) + 1] = ['Joker' for i in range(len(suits))]
suits['Joker'] = '§'

NR_OF_CARDS = 5

# Objects
cards = clss.Cards(NR_OF_CARDS, suits, all_card_combinations)
dealer = clss.Dealer(NR_OF_CARDS, suits, all_card_combinations)
the_flop = dealer.shuffles_cards(cards.create_cards(NR_OF_CARDS), NR_OF_CARDS)

dealer.deals_cards(the_flop, NR_OF_CARDS)
