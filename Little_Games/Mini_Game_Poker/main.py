import base as clss
import time
sleeptime = 3
test_loop = 4

# # COMMENT IF TESTING #
# clss.sys_clear()
# nr_of_cards = 5
# # COMMENT IF TESTING #

try:
    # TESTING #
    while test_loop >= 0:
        while True:

            # Starts scriptwith a clear screen
            clss.sys_clear()

            # Tries left
            if test_loop <= 2:
                print(f'{test_loop} Tries Left!')
            else:
                print(f'{test_loop} Trie Left!')
            try:
                nr_of_cards = int(input('\nHow Many Cards to Generate? :> '))

                if nr_of_cards == 0:
                    clss.sys_clear()
                    print('\nWell Now.. Suit Yourself...')
                    time.sleep(sleeptime)
                    raise KeyboardInterrupt
                elif nr_of_cards > 5:
                    clss.sys_clear()
                    print('\nPoker Hands have a Maximum of \'5\'')
                    time.sleep(sleeptime)
                    continue
                break
            except ValueError:
                clss.sys_clear()
                print('\nI Only Need a Number ;)')
                time.sleep(sleeptime)
                continue
        # TESTING #

        cards = clss.Cards()
        dealer = clss.Dealer()
        combi_card_list = []
        # Create nr_of_cards
        ascii_cards, random_result = cards.create_cards(nr_of_cards)
        card_list, suit_names, suit_symbols_dict = cards.get_all_combinations()
        
        # List of Suit Symbols
        suit_symbols = [v for k, v in suit_symbols_dict.items()]

        

        result = []
        for next_down in range(9):
            for next_side in range(1):
                result.append('  '.join(ascii_cards[next_side][next_down]))
        print()

        loop = 0
        start_index = 1
        end_index = 2

        for line in result:
            for i in range(1, 10, 3):
                if line == result[i]:
                    if line[1:6] == 'Joker':
                        line = line.replace(line[1:6], clss.bcolors.ORANGE + line[1:6] + clss.bcolors.ENDC)
                    if line[5:10] == 'Joker':
                        line = line.replace(line[5:10], clss.bcolors.ORANGE + line[5:10] + clss.bcolors.ENDC)
                    if line[5:6] in suit_symbols:
                        line = line.replace(line[5:6], clss.bcolors.ORANGE + line[5:6] + clss.bcolors.ENDC)
            print(line)


        # TESTING and 1 TAB #
        input('\nPRESS ENTER')
        test_loop -= 1

        continue

    raise KeyboardInterrupt
        # TESTING and 1 TAB #
except KeyboardInterrupt:
    clss.sys_clear()
    print('\nGoodBye..\n')
    quit()
