import os
import platform
import random
import time
# Between lines 31/28

payout = f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Payout ━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃\t\t\t\t\t\t\t\t  ┃
┃\tFive of a Kind\tx 100\t\tFlush\t\tx 7\t  ┃
┃ \tRoyal Flush\tx 50\t\tStraight\tx 5\t  ┃
┃ \tStraight Flush\tx 20\t\tThree of a Kind\tx 3\t  ┃ 
┃ \tFour of a Kind\tx 10\t\tTwo Pair\tx 2\t  ┃
┃ \tFull House\tx 8\t\tOne Pair\tx 1\t  ┃
┃\t\t\t\t\t\t\t\t  ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
"""

# Source: Idea Inspiration: https://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards


class Cards(object):
    """ Everything to do with creating cards.

    Keeps track.
    """
    # These comprihansions should be calculated only when needed. Does noting but take up resources

    def __init__(self, NR_OF_CARDS, suits, all_card_combinations):
        self.NR_OF_CARDS = NR_OF_CARDS
        self.MARGIN_BETWEEN = ' ' * 2
        self.MARGIN_LEFT = ' ' * 2
        self.set_cards_suits = set()
        self.suits = suits
        self.all_card_combinations = all_card_combinations

    def create_cards(self, NR_OF_CARDS):
        """Create Cards

        Creates card combinations and returns ASCII- type cards based on the given index

        """
        # Creates a list of list which will contain the lines of the card itself.
        card_index = [i for i in range(NR_OF_CARDS)]
        lines = [[] for _ in range(9)]
        front_ascii_cards = {}
        space = ' ' * 4
<<<<<<< HEAD
        set_cards_suits = set()

        for line_index in range(NR_OF_CARDS):
            card_nr = random.randint(1, 14)
            suit_sym = random.randint(0, 3)             # MAX: 3

            # Renaming High-Cards
=======

        for random_card_values in range(NR_OF_CARDS):
            card_nr = random.randint(1, 14)
            suit_sym = random.randint(0, 3)             # MAX: 3

            # Renameing High-Cards
>>>>>>> master
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

<<<<<<< HEAD
            if f'{(card_nr, suit_sym)}' in set_cards_suits:
                # Discard Multiple Card Combinations
                set_cards_suits.remove((card_nr, suit_sym))

            # Add Card Combinations to a Set
            set_cards_suits.update((card_nr, suit_sym))
=======
            if f'{(card_nr, suit_sym)}' in SETS_CARDS_SUITS:
                # Discard Multiple Card Combinations
                SETS_CARDS_SUITS.remove((card_nr, suit_sym))

            # Add Card Combinations to a Set
            SETS_CARDS_SUITS.update((card_nr, suit_sym))
>>>>>>> master

            # Append key = index. v are the cards lines
            front_ascii_cards[card_index[line_index]] = lines

        return front_ascii_cards


class Dealer(Cards):
    """Everything to do with the dealing for the cards
    """

    def __init__(self, NR_OF_CARDS, suits, all_card_combinations):
        Cards.__init__(self, NR_OF_CARDS, suits, all_card_combinations)
        self.DoubleDown = False
        self.winning_multipliers = {
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

<<<<<<< HEAD
    def shuffles_cards(self, front_ascii_cards, NR_OF_CARDS):
        """Dealer deals the flop"""

        start_line = 5
        end_line = 6
        start_cardNr = 1
        end_cardNr = 2
        the_colored_flop = []
        ascii_lines = []

        # The cards are printed on 9 lines.
        for lines_down in range(9):
            ascii_lines.append(self.MARGIN_BETWEEN.join(
                front_ascii_cards[0][lines_down]))

        # append each line to a set or list to return as a whole
        # Changes Color of cards based on the suit
        for line in ascii_lines:
            # Change AND to OR and all colors disapears. Good to know when building function to turn of color
            if line != ascii_lines[1] and line != ascii_lines[4] and line != ascii_lines[7]:
                the_colored_flop.append(f'{self.MARGIN_LEFT}{line}')
            else:
                # Color for the upper card numbers
                if line == ascii_lines[1]:
                    for nr_of_card in range(NR_OF_CARDS):

                        # Change 'Clubs' and 'Spades' to color BLACK
                        if self.suits['Clubs'] in ascii_lines[4][start_line:end_line] or self.suits['Spades'] in ascii_lines[4][start_line:end_line]:
                            startLine = line[:start_cardNr]
                            colorLine = bcolors.GREY + \
                                line[start_cardNr:end_cardNr] + \
                                bcolors.ENDC
                            if '10' in line[start_cardNr:(end_cardNr + 1)]:
                                end_cardNr += 1
                                colorLine = bcolors.GREY + \
                                    line[start_cardNr:end_cardNr] + \
                                    bcolors.ENDC
                            endLine = line[end_cardNr:]
                            line = startLine + colorLine + endLine

                        # Change 'Heart' and 'Diamonds' to color RED
                        elif self.suits['Hearts'] in ascii_lines[4][start_line:end_line] or self.suits['Diamonds'] in ascii_lines[4][start_line:end_line]:
                            startLine = line[:start_cardNr]
                            colorLine = bcolors.RED + \
                                line[start_cardNr:end_cardNr] + \
                                bcolors.ENDC
                            if '10' in line[start_cardNr:(end_cardNr + 1)]:
                                end_cardNr += 1
                                colorLine = bcolors.RED + \
                                    line[start_cardNr:end_cardNr] + \
                                    bcolors.ENDC
                            endLine = line[end_cardNr:]
                            line = startLine + colorLine + endLine

                        # If Joker, change them all to 1 color
                        elif self.suits['Joker'] in ascii_lines[4] and 'mJoker' not in line:
                            line = line.replace(
                                'Joker', bcolors.ORANGE + 'Joker' + bcolors.ENDC)

                        start_line += 13
                        end_line += 13
                        start_cardNr += 22
                        end_cardNr += 22

                    the_colored_flop.append(f'{self.MARGIN_LEFT}{line}')

                if line == ascii_lines[4]:

                    for suit_name in [k for k, v in self.suits.items()]:
                        if 'Clubs' in suit_name or 'Spades' in suit_name:
                            line = line.replace(
                                self.suits[f'{suit_name}'], bcolors.GREY + self.suits[f'{suit_name}'] + bcolors.ENDC)
                        elif 'Hearts' in suit_name or 'Diamonds' in suit_name:
                            line = line.replace(
                                self.suits[f'{suit_name}'], bcolors.RED + self.suits[f'{suit_name}'] + bcolors.ENDC)
                        else:  # Make ELIF
                            line = line.replace(
                                self.suits[f'{suit_name}'], bcolors.ORANGE + self.suits[f'{suit_name}'] + bcolors.ENDC)
                    the_colored_flop.append(f'{self.MARGIN_LEFT}{line}')

                if line == ascii_lines[7]:
                    # Resetting values of these variables for the last line in the card
                    start = 5
                    end = 6
                    start_cardNr = 9
                    end_cardNr = 10

                    for nr_of_card in range(NR_OF_CARDS):

                        # Change 'Clubs' and 'Spades' to color BLACK
                        if self.suits['Clubs'] in ascii_lines[4][start_line:end_line] or self.suits['Spades'] in ascii_lines[4][start_line:end_line]:
                            startLine = line[:(start_cardNr - 1)]
                            colorLine = bcolors.GREY + \
                                line[start_cardNr - 1:end_cardNr] + \
                                bcolors.ENDC
                            if '10' in line[start_cardNr:(end_cardNr + 1)]:
                                end_cardNr += 1
                                colorLine = bcolors.GREY + \
                                    line[start_cardNr:end_cardNr] + \
                                    bcolors.ENDC
                            endLine = line[end_cardNr:]
                            line = startLine + colorLine + endLine

                        # Change 'Heart' and 'Diamonds' to color RED
                        elif self.suits['Hearts'] in ascii_lines[4][start_line:end_line] or self.suits['Diamonds'] in ascii_lines[4][start_line:end_line]:
                            startLine = line[:(start_cardNr - 1)]
                            colorLine = bcolors.RED + \
                                line[(start_cardNr - 1):end_cardNr] + \
                                bcolors.ENDC
                            if '10' in line[start_cardNr:(end_cardNr + 1)]:
                                end_cardNr += 1
                                colorLine = bcolors.RED + \
                                    line[start_cardNr:end_cardNr] + \
                                    bcolors.ENDC
                            endLine = line[end_cardNr:]
                            line = startLine + colorLine + endLine

                        # If Joker on the Turn, change them all to 1 color
                        elif self.suits['Joker'] in ascii_lines[4] and 'mJoker' not in line:
                            line = line.replace(
                                'Joker', bcolors.ORANGE + 'Joker' + bcolors.ENDC)

                        start += 13
                        end += 13
                        start_cardNr += 22
                        end_cardNr += 22
                    the_colored_flop.append(f'{self.MARGIN_LEFT}{line}')

        return the_colored_flop

    def deals_cards(self, ascii_lines, NR_OF_CARDS):
        """Prints The ASCII Cards
        Prints the backcover of the cards, then the individual cards
        """
=======
    def deal_flop(self, ascii_cards):
        """Dealer deals the flop"""
>>>>>>> master

        # Prints empty  as standard
        back_ascii_cards = ['╔═════════╗'] + ['║' + bcolors.RED +
                                              '░░░░░░░░░' + bcolors.ENDC + '║'] * 2 + ['║' + bcolors.RED + '░░░░X░░░░' + bcolors.ENDC + '║'] * 3 + ['║' + bcolors.RED + '░░░░░░░░░' + bcolors.ENDC + '║'] * 2 + ['╚═════════╝']

        # Prints back of cards side for side
        time.sleep(1.5)
        for nr in range(1, (NR_OF_CARDS + 1)):
            time.sleep(0.2)
            sys_clear(OnScreen=payout)
            for line in back_ascii_cards:
                print(f'{self.MARGIN_LEFT}' + (line + f'{self.MARGIN_BETWEEN}') * nr, end='\n', flush=True)
        time.sleep(2)

        
        # copy backascii card to change and print without changing the original
        # for x in range(nr of cards)
        # for loop nr of lines (9)
        
        # string slice first card
        # print na elke line(9)
        # add certain amout to sliceing
        # add time delay

        # String slice first lines of first card
        # Replace those with front cards
        # Print whole list
        # Repeate Nr of card times
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
    # gebruik variable 'set_cards_suits'
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
