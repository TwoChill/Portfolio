import base as clss
import time

clss.sys_clear(OnScreen=clss.payout)

# Objects
cards = clss.Cards()
dealer = clss.Dealer()

# TWEAKER VARIABLES
NR_OF_CARDS = 5
MARGIN_LEFT = ' ' * 1
MARGIN_BETWEEN = ' ' * 2

ascii_cards, random_card_lines = cards.create_cards(NR_OF_CARDS)
suit_names, suit_symbols_dict = cards.get_all_combinations()
card_lines = []
combi_card_list = []
start = 5
end = 6
start_cardNr = 1
end_cardNr = 2

for next_down in range(9):
    card_lines.append(MARGIN_BETWEEN.join(ascii_cards[1][next_down]))
for line in card_lines:
    # Change AND to OR and all colors disapears. Good to know when building function to turn of color
    if line != card_lines[1] and line != card_lines[4] and line != card_lines[7]:
        print(MARGIN_LEFT, line)
    else:
        # Color for the upper card numbers
        if line == card_lines[1]:
            for nr_of_card in range(NR_OF_CARDS):

                # Change 'Clubs' and 'Spades' to color BLACK
                if suit_symbols_dict['Clubs'] in card_lines[4][start:end] or suit_symbols_dict['Spades'] in card_lines[4][start:end]:
                    startLine = line[:start_cardNr]
                    colorLine = clss.bcolors.GREY + \
                        line[start_cardNr:end_cardNr] + clss.bcolors.ENDC
                    if '10' in line[start_cardNr:(end_cardNr + 1)]:
                        end_cardNr += 1
                        colorLine = clss.bcolors.GREY + \
                            line[start_cardNr:end_cardNr] + \
                            clss.bcolors.ENDC
                    endLine = line[end_cardNr:]
                    line = startLine + colorLine + endLine

                # Change 'Heart' and 'Diamonds' to color RED
                elif suit_symbols_dict['Hearts'] in card_lines[4][start:end] or suit_symbols_dict['Diamonds'] in card_lines[4][start:end]:
                    startLine = line[:start_cardNr]
                    colorLine = clss.bcolors.RED + \
                        line[start_cardNr:end_cardNr] + clss.bcolors.ENDC
                    if '10' in line[start_cardNr:(end_cardNr + 1)]:
                        end_cardNr += 1
                        colorLine = clss.bcolors.RED + \
                            line[start_cardNr:end_cardNr] + \
                            clss.bcolors.ENDC
                    endLine = line[end_cardNr:]
                    line = startLine + colorLine + endLine

                # If Joker on the Turn, change them all to 1 color
                elif suit_symbols_dict['Joker'] in card_lines[4] and 'mJoker' not in line:
                    line = line.replace(
                        'Joker', clss.bcolors.ORANGE + 'Joker' + clss.bcolors.ENDC)

                start += 13
                end += 13
                start_cardNr += 22
                end_cardNr += 22
            print(MARGIN_LEFT, line)
        if line == card_lines[4]:

            for suit_name in suit_names:
                if 'Clubs' in suit_name or 'Spades' in suit_name:
                    line = line.replace(
                        suit_symbols_dict[f'{suit_name}'], clss.bcolors.GREY + suit_symbols_dict[f'{suit_name}'] + clss.bcolors.ENDC)
                elif 'Hearts' in suit_name or 'Diamonds' in suit_name:
                    line = line.replace(
                        suit_symbols_dict[f'{suit_name}'], clss.bcolors.RED + suit_symbols_dict[f'{suit_name}'] + clss.bcolors.ENDC)
                else:  # Make ELIF
                    line = line.replace(
                        suit_symbols_dict[f'{suit_name}'], clss.bcolors.ORANGE + suit_symbols_dict[f'{suit_name}'] + clss.bcolors.ENDC)
            print(MARGIN_LEFT, line)

        if line == card_lines[7]:
            # Resetting values of these variables for the last line in the card
            start = 5
            end = 6
            start_cardNr = 9
            end_cardNr = 10

            for nr_of_card in range(NR_OF_CARDS):

                # Change 'Clubs' and 'Spades' to color BLACK
                if suit_symbols_dict['Clubs'] in card_lines[4][start:end] or suit_symbols_dict['Spades'] in card_lines[4][start:end]:
                    startLine = line[:(start_cardNr - 1)]
                    colorLine = clss.bcolors.GREY + \
                        line[start_cardNr - 1:end_cardNr] + \
                        clss.bcolors.ENDC
                    if '10' in line[start_cardNr:(end_cardNr + 1)]:
                        end_cardNr += 1
                        colorLine = clss.bcolors.GREY + \
                            line[start_cardNr:end_cardNr] + \
                            clss.bcolors.ENDC
                    endLine = line[end_cardNr:]
                    line = startLine + colorLine + endLine

                # Change 'Heart' and 'Diamonds' to color RED
                elif suit_symbols_dict['Hearts'] in card_lines[4][start:end] or suit_symbols_dict['Diamonds'] in card_lines[4][start:end]:
                    startLine = line[:(start_cardNr - 1)]
                    colorLine = clss.bcolors.RED + \
                        line[(start_cardNr - 1):end_cardNr] + \
                        clss.bcolors.ENDC
                    if '10' in line[start_cardNr:(end_cardNr + 1)]:
                        end_cardNr += 1
                        colorLine = clss.bcolors.RED + \
                            line[start_cardNr:end_cardNr] + \
                            clss.bcolors.ENDC
                    endLine = line[end_cardNr:]
                    line = startLine + colorLine + endLine

                # If Joker on the Turn, change them all to 1 color
                elif suit_symbols_dict['Joker'] in card_lines[4] and 'mJoker' not in line:
                    line = line.replace(
                        'Joker', clss.bcolors.ORANGE + 'Joker' + clss.bcolors.ENDC)

                start += 13
                end += 13
                start_cardNr += 22
                end_cardNr += 22
            print(MARGIN_LEFT, line)

