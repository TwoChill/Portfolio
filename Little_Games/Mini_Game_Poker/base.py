import os
import platform
import random
import time

# Source: Idea Inspiration: https://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards


class Cards(object):
    """ Everything to do with creating cards.

    Keeps track.
    """

    def __init__(self):
        self.card_nrs = [i for i in range(1, 15)]
        self.suits = {'Spades': '♠', 'Diamonds': '♦',
                      'Hearts': '♥', 'Clubs': '♣', 'Joker': '§'}
        self.all_card_combinations = {
            k: list(self.suits.keys()) for k in self.card_nrs for v in self.suits.items() if v != 'Joker'}
        # 4 Jokers Added
        self.all_card_combinations[len(
            self.card_nrs) + 1] = ['Joker' for i in range(len(self.suits))]
        self.winning_combinations = {
            # if player_combo[1][0] and  player_combo[1][1] etc == True)
            "Five of a Kind": (),
            "Royal Flush": (),
            "Straight Flush": (),
            "Four of a Kind": (),
            "Full House": (),
            "Flush": (),
            "Straight": (),
            "Three of a Kind": (),
            "Two Pair": (),
            "One Pair": ()
        }

    def create_cards(self, nr_of_cards, indx_cards_tuple=None):
        """Create Cards

        Creates card combinations and returns ASCII- type cards based on the given index
        """
        # Creates a list of list which will contain the lines of the card itself.
        card_index = [i for i in range(nr_of_cards)]
        lines = [[] for i in range(9)]
        random_result = {}
        ascii_cards = {}
        space = ' ' * 4

        for n in range(nr_of_cards):
            card_nr = random.randint(1, 14)
            suit_nr = random.randint(0, 3)

            # Renameing High-Cards
            if card_nr == 1:
                card_nr = 'A'
            elif card_nr == 11:
                card_nr = 'J'
            elif card_nr == 12:
                card_nr = 'Q'
            elif card_nr == 13:
                card_nr = 'K'
            elif card_nr == 14:
                card_nr = 'Joker'
            # Joker's special symbol index nr.
                suit_nr = 4
                space = ''

            # The 'Joker' card has differences in whitespaces and thus will use its own template.
            if card_nr == 'Joker':
                lines[0].append('╔═════════╗')
                lines[1].append('║{}    {}║'.format(card_nr, space))
                lines[2].append('║         ║')
                lines[3].append('║         ║')
                lines[4].append('║    {}    ║'.format(
                    list(self.suits.values())[suit_nr].upper()))
                lines[5].append('║         ║')
                lines[6].append('║         ║')
                lines[7].append('║{}    {}║'.format(space, card_nr))
                lines[8].append('╚═════════╝')
                space = ' ' * 4

            elif card_nr == 10:
                # '10' has two characters. There for diffrent whitespaces.
                space = ' ' * 3
                lines[0].append('╔═════════╗')
                lines[1].append('║{}    {}║'.format(card_nr, space))
                lines[2].append('║         ║')
                lines[3].append('║         ║')
                lines[4].append('║    {}    ║'.format(
                    list(self.suits.values())[suit_nr].upper()))
                lines[5].append('║         ║')
                lines[6].append('║         ║')
                lines[7].append('║{}    {}║'.format(space, card_nr))
                lines[8].append('╚═════════╝')
                space = ' ' * 4

            else:
                # The 'Other' cards are using this template.
                lines[0].append('╔═════════╗')
                lines[1].append('║{}    {}║'.format(card_nr, space))
                lines[2].append('║         ║')
                lines[3].append('║         ║')
                lines[4].append('║    {}    ║'.format(
                    list(self.suits.values())[suit_nr].upper()))
                lines[5].append('║         ║')
                lines[6].append('║         ║')
                lines[7].append('║{}    {}║'.format(space, card_nr))
                lines[8].append('╚═════════╝')

            # Dictionary of the random card combination
            random_result[card_nr] = suit_nr

            # Append key = index. v are the cards lines
            ascii_cards[card_index[n]] = lines

        return ascii_cards, random_result


class Dealer(object):
    """Everything to do with the dealing for the cards
    """

    def __init__(self):
        self.DoubleDown = False

    def deal_cards(self, ascii_cards):

        for i in range(9):
            for card in ascii_cards[1][i]:
                time.sleep(1)
                print(card)

    def check_combination(self, player_combination):
        """Check Card Combination

        Checks to see if the final combination is a winning combination.
        If so, returns the name of the combination with it's corresponding multiplier
        """
    pass


class DoubleDown(object):
    pass


class Select(object):
    pass


class Checker(object):
    pass


class Bet(object):
    pass


def sys_clear(OnScreen=None):
    ''' Clears terminal screen for diffrent OS's '''

    if 'linux' in platform.platform().lower():
        os.system('clear')
    elif 'windows' in platform.platform().lower():
        os.system('cls')
    else:
        print("Sorry, Your OS is not known to me yet.")

    if OnScreen is None:
        pass
    else:
        print(f'\n{OnScreen}')
