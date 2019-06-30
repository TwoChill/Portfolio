def start(usrName):
    print('\n############################')
    print('#  Rise of the Dragon Rider  #')
    print('############################\n')
    print('          - Play -          ')
    print('          - Help -          ')
    print('          - Quit -          ')
    print('\n          Made by:          ')
    print('       M.L. de France       ')
    print('\n############################\n')
###
    start_answer = str(input(':> ')).capitalize()
###
    while True:

        if start_answer == 'Play':
            player_info()
            break
        elif start_answer == 'Help':
            help()
        elif start_answer == 'Quit':
            quit()
        else:
            print('\nI din\'t get that!\n')
            start_answer = str(input(':> ')).capitalize()

    return start_answer

def help():
        print('\n############################')
        print('#         - Help -         #')
        print('############################\n')
        print('- Use up, down, left, right to move  ')
        print('- Type your commands to do them  ')
#        print('- Use "look" to inspect surrounding  ')
        print('- Use "dig" to investigate area  ')
        print('- Good luck and have fun!  ')
        print('\n############################\n')
        help_answer = str(input('\nPress ENTER to continue\n:>'))
        while True:
            if help_answer == "":
                start(usrName)
            else:
                help_answer = str(input('\nPress ENTER to continue\n:>'))

def quit():
        print('\nThank you for trying Rise of the Dragon Rider!\n')
        exit(0)


def player_info():
    usrName = str(input("\nChoose character name:\t")).title()
    answer = str(input((f'Is "{usrName}" correct?\tY/N: ')).upper())

    if answer == 'Y':
        home(usrName, 'Home')
    elif answer == 'N':
        while answer == 'N':
            usrName = str(input("\nChoose character name:\t")).title()
            answer = str(input((f'Is "{usrName}" correct?\tY/N: ')).upper())
            if answer == 'Y':
                home('Home')

    return usrName


def home(usrName, location):
    print(f'\n\nWelcome {usrName} you are {location}.')

    # Your home
    # Your mentor
    # Your room with Lore read    functie

# def outside_home():
#     # Serrounding like god of war
#     # go to central
#     # dig
#
# def mentor(location):
#     # parameter tells were you are in game and what to print
#     # go outside and inside get basic_quest to dig outside find map() for mentor.
#     ##got_quest = True (and shows in menu)
#
# def dig(location, quest1, quest2, quest3):
#     #  can dig anywhere to find something or certain lores
#     #  droprate of items depends on were you are in stroy
#     #  depending on location, items to find
#     #  there's a time delay for this action
#
# def shoptrader(location):
#     # first static at calmlands()
#     # later based on player location moves around inc 3 or 4.
#     # when shoptraders moves, has found mysterious stone, gives it to you for some gil
#
# def menu(got_quest, got_spellbook, lorefound)():
#     # Inventory()
#     # Map()
#     # Quest()
#     # Spellbook()
#     # lore_books('all')
#     # help
#
# def lore_books(book_nr):
#     # book_nr == 1:
#     #   print(''' Book 1 ''')
#     #  etc

usrName = ''
start(usrName)
