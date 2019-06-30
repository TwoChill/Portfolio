def start(usrName):
    print('\n############################')
    print('#  Rise of the Dragon Rider #')
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
        print('- Type your commands to do them  ')
        print('- Use up, down, left, right to move  ')
#        print('- Use "look" to inspect surrounding  ')
        print('- Use "dig" to investigate area  ')
        print('- Good luck and have fun!  ')
        print('\n############################')

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

    while True:

        if " " in usrName:
            print('Only one name is allowd.\n')
            usrName = str(input("\nChoose character name:\t")).title()
        else:
            answer = str(input((f'Is "{usrName}" correct? (Y/N): ')).upper())

            if answer == 'Y':
                home(usrName, 'Home')
            elif answer == 'N':
                while answer == 'N':
                    usrName = str(input("\nChoose character name:\t")).title()
                    if " " in usrName:
                        break
                    else:
                        answer = str(input((f'Is "{usrName}" correct? (Y/N): ')).upper())
                        if answer == 'Y':
                            home(usrName, 'Home')

            break

    return usrName


def home(usrName, location):
    print(f'\n\nWelcome {usrName} you are {location}.')
    # Your home
    # Your mentor
    # Your room with Lore read    functie
#
# def outside_home():
#     # Serrounding like god of war
#     # go to central
#     # dig
#
# def usrName_room():
#     # here are some books with lore
#     # rest (saves the game)
#
# def mentor(location, quest1, quest2, quest3,):
#     # parameter tells were you are in game and what to print
#     # go outside and inside get basic_quest to dig outside find map() for mentor.
#     ##got_quest = True (and shows in menu)
#     # asked about quest and gives a hint an what to do next?
#
# def save_game():
#     # saves items, qeusts done, progression order
#     # saves game manualy
#     # ask to overwrite or create new save.
#
# def auto_save():
#     # auto saves afther certain points and quests
#     # auto saves every room entry.
#
# def progression():
#     # keeps a record of the main story so far
#     # order can change depending on how the game is played.
#
# def dig(location, quest1, quest2, quest3):
#     #  can dig anywhere to find something or certain lores
#     #  droprate of items depends on were you are in stroy
#     #  depending on location, items to find
#     #  there's a time delay for this action
#     # some books are only found throudigging
#
# def shoptrader(location):
#     # first static at calmlands()
#     # later based on player location moves around inc 3 or 4.
#     # when shoptraders moves, has found mysterious stone, gives it to you for some gil
#     # combine items to get new items wich can be used to do maby secret things
#
# def menu(got_quest, got_spellbook, lorefound):
#     # Inventory()
#     # Map()
#     # Quest()
#     # Spellbook()
#     # lore_books('all')
#     # Progression
#     # Save game
#     # Exit Game
#     # help
#     # q to quit
#
# def lore_books(location, book_nr):
#     # book_nr == 1:
#     #   print(''' Book 1 ''')
#     #  etc
#     # some books are only found through digging
#
# def game_over():
#     # depending on how, game over msg is displayd
#     # can coninue from last save or auto_save (which is every room enter)
#
# def spellbook():
#     # menu of:
#     # How to lift grandcloaking spellbook
#     # How to make a invisable grandcloaking
#     # wand, claok, t-stone ...
#     # How to make a t-stone
#     # other way to - dark invisable cloak - use ???
#     # etc
#
#
# def inventory():
#     # usrname list of items with amout
#     # this can be used to append to shoptrader and other quest dudes
#     # so prorgram knows what to have and not?
#
#
# def spellbook_quest():
#     # everything about this quest
#     # if quest is done.. msg for some thing else
#     # secondary action is for t stone
#
#
# def wand_quest():
#     # everything about this quest
#     # have to dig
#
# def invisableCloak_quest():
#     # everything about this quest
#     # can use w to obtain but this evil act will cause cloak to be dark
#     # and gets banashed from dragon riders land for ever
#
usrName = ''
start(usrName)
