from pynput import keyboard
import copy
import platform
import random
import time
import os
if __name__ == "__main__":
    import main
# Between lines 31/28

payout = f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Payout ━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
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
    # These comprehensions should be calculated only when needed. Does noting but take up resources

    def __init__(self, NR_OF_CARDS, suits, all_card_combinations):
        self.NR_OF_CARDS = NR_OF_CARDS
        self.MARGIN_BETWEEN = ' ' * 2
        self.MARGIN_LEFT = ' ' * 2
        self.MARGIN_HITME = ' ' * \
            ((len(payout[payout.find('┏'):payout.find('┓')])) // 6)
        self.suits = suits
        self.set_cards_suits = set()
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
        set_cards_suits = set()

        for line_index in range(NR_OF_CARDS):
            while len(set_cards_suits) < NR_OF_CARDS or len(lines[8]) < len(set_cards_suits):
                card_nr = random.randint(1, 14)
                suit_sym = random.randint(0, 3)             # MAX: 3

                if (card_nr, suit_sym) in set_cards_suits:
                    # Discard Multiple Card Combinations
                    set_cards_suits.remove((card_nr, suit_sym))
                    continue

                # Add Card Combinations to a Set
                set_cards_suits.add((card_nr, suit_sym))

                if len(lines[8]) == 5:
                    break

                # Renaming High-Cards
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

            # Append key = index. v are the cards lines

            front_ascii_cards[card_index[line_index]] = lines

        return front_ascii_cards, set_cards_suits


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

    def shuffles(self, front_ascii_cards, NR_OF_CARDS):
        """Colors the cards"""

        start_line = 5
        end_line = 6
        start_cardNr = 1
        end_cardNr = 2
        the_flop = []
        ascii_lines = []

        # The cards are printed on 9 lines.
        for lines_down in range(9):
            ascii_lines.append(self.MARGIN_BETWEEN.join(
                front_ascii_cards[4][lines_down]))

        # append each line to a set or list to return as a whole
        # Changes Color of cards based on the suit
        for line in ascii_lines:
            # Change AND to OR and all colors disapears. Good to know when building function to turn of color
            if line != ascii_lines[1] and line != ascii_lines[4] and line != ascii_lines[7]:
                the_flop.append(line)
            else:
                # Color for the upper card numbers
                if line == ascii_lines[1]:
                    for _ in range(NR_OF_CARDS):

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

                    the_flop.append(line)

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
                    the_flop.append(line)

                if line == ascii_lines[7]:
                    # Resetting values of these variables for the last line in the card
                    start_line = 5
                    end_line = 6
                    start_cardNr = 9
                    end_cardNr = 10

                    for _ in range(NR_OF_CARDS):

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

                        start_line += 13
                        end_line += 13
                        start_cardNr += 22
                        end_cardNr += 22

                    the_flop.append(line)

        return the_flop

    def deals_cards(self, the_flop, NR_OF_CARDS):
        """Prints The ASCII Cards
        Prints the backcover of the cards, then the individual cards
        """

        hit_me = f"""{self.MARGIN_HITME}""" + bcolors.RED + f"""
{self.MARGIN_HITME}██╗  ██╗██╗████████╗    ███╗   ███╗███████╗
{self.MARGIN_HITME}██║  ██║██║╚══██╔══╝    ████╗ ████║██╔════╝
{self.MARGIN_HITME}███████║██║   ██║       ██╔████╔██║█████╗
{self.MARGIN_HITME}██╔══██║██║   ██║       ██║╚██╔╝██║██╔══╝
{self.MARGIN_HITME}██║  ██║██║   ██║       ██║ ╚═╝ ██║███████╗
{self.MARGIN_HITME}╚═╝  ╚═╝╚═╝   ╚═╝       ╚═╝     ╚═╝╚══════╝""" + bcolors.ENDC + f"""

{self.MARGIN_HITME}{self.MARGIN_HITME}    """ + bcolors.UNDERLINE + 'Press Enter' + bcolors.ENDC + """
"""
        # Prints empty as standard
        back_ascii_cards = ['╔═════════╗'] + ['║' + bcolors.RED +
                                              '░░░░░░░░░' + bcolors.ENDC + '║'] * 2 + ['║' + bcolors.RED + '░░░░X░░░░' + bcolors.ENDC + '║'] * 3 + ['║' + bcolors.RED + '░░░░░░░░░' + bcolors.ENDC + '║'] * 2 + ['╚═════════╝']
        input(f'{hit_me}')

        for nr in range(1, (NR_OF_CARDS + 1)):
            time.sleep(0.09)
            sys_clear(OnScreen=payout)
            for line in back_ascii_cards:
                print(f'{self.MARGIN_LEFT}' +
                      (line + f'{self.MARGIN_BETWEEN}') * nr)

        # Time to wait before the flop is shown to the player.
        time.sleep(2)
        sys_clear(OnScreen=payout)

        # The flop is being shown to the player
        for line in the_flop:
            print(f'{self.MARGIN_LEFT}' + line)

        # Time to wait before the player can select one or more cards
        time.sleep(1.5)


class DoubleDown(object):
    pass


class Select(Cards):

    def __init__(self, the_flop, NR_OF_CARDS, suits, all_card_combinations):
        Cards.__init__(self, NR_OF_CARDS, suits, all_card_combinations)
        self.the_flop = the_flop
        self.the_flop_copy = copy.deepcopy(the_flop)

    def highlight_card(self, the_flop):
        """Select cards to swap
        Player can choose and select/highlight cards to swap"""
        
        global start_a, end_a, start_b, end_b, end_c, index_line, card_position
        start_a = 0
        end_a = 11
        start_b = 0
        end_b = 1
        end_c = 19
        index_line = 0
        card_position = 1           # First card is highlighted automatically

        # Places a 'selective' color around a card
        while True:
            sys_clear(OnScreen=payout)
            for line in the_flop:
                # # Might be usefull later on if numbers try to go negative.
                # if start_a < 0:
                #     start_a = 0
                #     end_a = 11

                # The FIRST cardline
                if line[start_a:end_a] == the_flop[0][start_a:end_a]:
                    self.the_flop_copy.remove(self.the_flop_copy[0])
                    line = bcolors.BLUE + \
                        line[start_a:end_a] + bcolors.ENDC + line[end_a:]
                    if card_position >= 2:
                        line = the_flop[0][:start_a] + line
                    self.the_flop_copy.insert(0, line)

                # The LAST cardline
                elif line[start_a:end_a] == the_flop[8][start_a:end_a]:
                    self.the_flop_copy.remove(self.the_flop_copy[8])
                    line = bcolors.BLUE + \
                        line[start_a:end_a] + bcolors.ENDC + line[end_a:]
                    if card_position >= 2:
                        line = the_flop[8][:start_a] + line
                    self.the_flop_copy.insert(8, line)

                # The UPPER CARDNR Line
                elif line[start_b:(end_c + 1)] == the_flop[1][start_b:(end_c + 1)]:
                    self.the_flop_copy.remove(self.the_flop_copy[1])
                    line = bcolors.BLUE + line[start_b:end_b] + bcolors.ENDC + line[end_b:end_c] + \
                        bcolors.BLUE + \
                        line[end_c:(end_c + 1)] + bcolors.ENDC + \
                        line[(end_c + 1):]
                    if card_position >= 2:
                        line = the_flop[1][:start_b] + line
                    self.the_flop_copy.insert(1, line)

                # The MIDDEL CARDSUITT Line
                elif line[start_b:(end_c + 1)] == the_flop[4][start_b:(end_c + 1)]:
                    self.the_flop_copy.remove(self.the_flop_copy[4])
                    line = bcolors.BLUE + line[start_b:end_b] + bcolors.ENDC + line[end_b:end_c] + \
                        bcolors.BLUE + \
                        line[end_c:(end_c + 1)] + bcolors.ENDC + \
                        line[(end_c + 1):]
                    if card_position >= 2:
                        line = the_flop[4][:start_b] + line
                    self.the_flop_copy.insert(4, line)

                # The BOTTOM CARDNR Line
                elif line[start_b:(end_c + 1)] == the_flop[7][start_b:(end_c + 1)]:
                    self.the_flop_copy.remove(self.the_flop_copy[7])
                    line = bcolors.BLUE + line[start_b:end_b] + bcolors.ENDC + line[end_b:end_c] + \
                        bcolors.BLUE + \
                        line[end_c:(end_c + 1)] + bcolors.ENDC + \
                        line[(end_c + 1):]
                    if card_position >= 2:
                        line = the_flop[7][:start_b] + line
                    self.the_flop_copy.insert(7, line)

                # LINES IN BETWEEN
                else:
                    # Very Ugly solution (Get index of the normal lines)
                    if index_line == 0:
                        index_line = 2
                    elif index_line == 2:
                        index_line = 3
                    elif index_line == 3:
                        index_line = 5
                    elif index_line == 5:
                        index_line = 6

                    self.the_flop_copy.remove(self.the_flop_copy[index_line])
                    line = bcolors.BLUE + \
                        line[start_a:end_a] + bcolors.ENDC + line[end_a:]
                    if card_position >= 2:
                        line = the_flop[index_line][:start_a] + line
                    self.the_flop_copy.insert(index_line, line)

            # Prints 'highlighted' cards on screen
            for line in self.the_flop_copy:
                print(f'{self.MARGIN_LEFT}' + line)

            # <-- Should be arrow key press Right or Left
            if card_position < self.NR_OF_CARDS:
                listener = keyboard.Listener(on_press=on_press)
                listener.start()  # start to listen on a separate thread
                listener.join()  # remove if main thread is polling self.keys
            else:
                listener = keyboard.Listener(on_press=on_press)
                listener.start()  # start to listen on a separate thread
                listener.join()

    def replace_select(self, the_flop):
        pass


class Bet(object):
    pass


class bcolors:
    BLUE = '\033[95m'
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


def on_press(key):
    try:
        k = key.char  # single-char keys
    except Exception:
        k = key.name  # other keys
    if k in ['right']:  # keys of interest
        global start_a, end_a, start_b, end_b, end_c, index_line, card_position

        if card_position > 4:
            return start_a, end_a, start_b, end_b, end_c, index_line, card_position
        else:
            card_position += 1
            start_a += (13)
            end_a += (13)
            start_b += (22)
            end_b += (22)
            end_c += (22)
            index_line = 0
            return False
    elif k in ['left']:  # keys of interest

        if card_position < 2:
            return start_a, end_a, start_b, end_b, end_c, index_line, card_position
        else:
            card_position -= 1
            start_a -= (13)
            end_a -= (13)
            start_b -= (22)
            end_b -= (22)
            end_c -= (22)
            index_line = 0
            return False
    else:
        return start_a, end_a, start_b, end_b, end_c, index_line, card_position
        # return False  # stop listener; remove this if want more keys

def sys_clear(OnScreen=None):
    ''' Clears terminal screen for diffrent OS's '''
    import os

    if 'ipad' in platform.platform().lower():
        import console
        console.clear()
    elif 'Linux' in platform.platform().capitalize()[:5] or 'Darwin' in platform.platform().capitalize()[:6]:
        os.system('clear')
    elif 'Windows' in platform.platform().capitalize()[:7]:
        os.system('cls')
    else:
        print(f"Sorry, OS: {platform.platform()} is not known to me yet.")

    if OnScreen is not None:
        print(f'{OnScreen}')
