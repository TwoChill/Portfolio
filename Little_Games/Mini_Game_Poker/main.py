import base as clss
import time
# Show 'PayOut' on screen.
clss.sys_clear(OnScreen=clss.payout)

<<<<<<< HEAD
card_nrs = [i for i in range(1, 15)]
suits = {'Spades': '♠', 'Diamonds': '♦',
         'Hearts': '♥', 'Clubs': '♣', 'Joker': '§'}

suits.pop('Joker')
all_card_combinations = {k: list(suits.keys()) for k in card_nrs}
# Adds 4 Jokers as the last set of cards
all_card_combinations[len(card_nrs) + 1] = ['Joker' for i in range(len(suits))]
suits['Joker'] = '§'
=======
# Objects
cards = clss.Cards()
dealer = clss.Dealer()

# TWEAKER VARIABLES
NR_OF_CARDS = 5
MARGIN_LEFT = ' ' * 1
MARGIN_BETWEEN = ' ' * 2

ascii_cards, SETS_CARDS_SUITS = cards.create_cards(NR_OF_CARDS)
suit_names, suit_symbols_dict = cards.get_all_combinations()
card_lines = []
combi_card_list = []
start = 5
end = 6
start_cardNr = 1
end_cardNr = 2

# TEST VARIABLES #
print('\t\t', SETS_CARDS_SUITS)

# The cards are printed on 9 lines.
for lines_down in range(9):
    card_lines.append(MARGIN_BETWEEN.join(ascii_cards[(NR_OF_CARDS - 1)][lines_down]))

# Changes Color of cards barsed on the suit
for line in card_lines:
    # Change AND to OR and all colors disapears. Good to know when building function to turn of color
    if line != card_lines[1] and line != card_lines[4] and line != card_lines[7]:
        print(MARGIN_LEFT, line)
    else:
        # Color for the upper card numbers
        if line == card_lines[1]:
            for nr_of_card in range(NR_OF_CARDS):
>>>>>>> master


NR_OF_CARDS = 5

# Objects
cards = clss.Cards(NR_OF_CARDS, suits, all_card_combinations)
dealer = clss.Dealer(NR_OF_CARDS, suits, all_card_combinations)
# color card 1 function
# line 24 returns only set card suit to use later for combination check


the_flop = dealer.shuffles_cards(cards.create_cards(NR_OF_CARDS), NR_OF_CARDS)


dealer.deals_cards(the_flop, NR_OF_CARDS)