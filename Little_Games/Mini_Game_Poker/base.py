import os
import platform
import random
import time

payout = f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Payout ━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃\t\t\t\t\t\t\t\t  ┃
┃\tFive of a Kind\tx 100\t\tFlush\t\tx 7\t  ┃
┃ \tRoyal Flush\tx 50\t\tStraight\tx 5\t  ┃
┃ \tStraight Flush\tx 20\t\tThree of a Kind\tx 3\t  ┃ 
┃ \tFour of a Kind\tx 10\t\tTwo Pair\tx 2\t  ┃
┃ \tFull House\tx 8\t\tOne Pair\tx 1\t  ┃
┃\t\t\t\t\t\t\t\t  ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩"""

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
        self.multiplier_winning_combination = {
            "Five of a Kind": 100,
            "Royal Flush": 50,
            "Straight Flush": 30,
            "Four of a Kind": 20,
            "Full House": 10,
            "Flush": 8,
            "Straight": 7,
            "Three of a Kind": 5,
            "Two Pair": 3,
            "One Pair": 1
        }

    def create_cards(self, NR_OF_CARDS, card_position=None):
        """Create Cards

        Creates card combinations and returns ASCII- type cards based on the given index
        """
        # Creates a list of list which will contain the lines of the card itself.
        card_index = [i for i in range(NR_OF_CARDS)]
        lines = [[] for i in range(9)]
        SETS_CARDS_SUITS = set()
        ascii_cards = {}
        space = ' ' * 4

        # While duplicate card is made, makes another diffrent one
        while len(SETS_CARDS_SUITS) < NR_OF_CARDS:
            for random_card_values in range(NR_OF_CARDS):
                card_nr = random.randint(1, 14)
                suit_sym = random.randint(0, 3)                          # MAX: 3

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
                    suit_sym = 4
                    space = ''

                # The 'Joker' card has differences in whitespaces and thus will use its own template.
                if card_nr == 'Joker':
                    lines[0].append('╔═════════╗')
                    lines[1].append('║{}    {}║'.format(card_nr, space))
                    lines[2].append('║         ║')
                    lines[3].append('║         ║')
                    lines[4].append('║    {}    ║'.format(
                        list(self.suits.values())[suit_sym].upper()))
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
                        list(self.suits.values())[suit_sym].upper()))
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
                        list(self.suits.values())[suit_sym].upper()))
                    lines[5].append('║         ║')
                    lines[6].append('║         ║')
                    lines[7].append('║{}    {}║'.format(space, card_nr))
                    lines[8].append('╚═════════╝')

                # Add to set (no duplicates allowed)
                SETS_CARDS_SUITS.add((card_nr, suit_sym))


                

            # Append key = index. v are the cards lines
            ascii_cards[card_index[random_card_values]] = lines

        return ascii_cards, SETS_CARDS_SUITS

    def get_all_combinations(self):
        """Get All Card Combinations
        Maybe there is a way to NOT use a methode ..
        Returns a dictionary of the card combinations
        """

        suit_names = []
        for k, v in self.all_card_combinations.items():
            suit_names.append(v)

        return suit_names[1], self.suits


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


class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'
    BLACK = '\033[30m'
    GREY = '\33[90m'
    BLINK1 = '\33[5m'
    BLINK2 = '\33[6m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def sys_clear(OnScreen=None):
    ''' Clears terminal screen for diffrent OS's '''
    if 'ipad' in platform.platform().lower():
        import console
        console.clear()
    elif 'linux' or 'Darwin' in platform.platform().lower():
        os.system('clear')
    elif 'windows' in platform.platform().lower():
        os.system('cls')
    else:
        print(f"Sorry, OS: {platform.platform()} is not known to me yet.")

    if OnScreen is not None:
        print(f'{OnScreen}')
