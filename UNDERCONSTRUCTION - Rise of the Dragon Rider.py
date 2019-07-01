import random
import time

def enter_command():
    enter_command = str(input(":> "))
    return enter_command

def start(usrName, location, usrGendr):
    print('\n############################')
    print('# Rise of the Dragon Rider #')
    print('############################\n')
    print('          - Play -          ')
    print('          - Help -          ')
    print('          - Quit -          ')
    print('\n          Made by:          ')
    print('       M.L. de France       ')
    print('\n############################\n')

    while True:
        start_answer = enter_command().upper()

        if start_answer == 'PLAY':
            player_info(usrName, location, usrGendr)
            break
        elif start_answer == 'HELP':
            help(true)
        elif start_answer == 'QUIT':
            quit()
        else:
            print('\nI didn\'t get that!\n')

    return start_answer

def help(start_menu):
    print('\n\n############################')
    print('#         - Help -         #')
    print('############################\n')
    print('- Type your commands to do them.')
    print('- Use "look" to inspect surrounding.')
    print('- Use "dig" to investigate area.')
    print('- Good luck and have fun!.')
    print('\n############################')

    if start_menu == True:
        help_answer = str(input('\nPress ENTER to continue\n:>'))

        while True:
            if help_answer == "":
                start(usrName, location, usrGendr)
            else:
                help_answer = str(input('\nPress ENTER to continue\n:>'))

def player_info(usrName, location, usrGendr):
    print("\n# INTRO GAME HERE #")
    # this is told from a 'god' perspective

    print("\n\nBut first let's create a character!\n\n")

    usrGendr = str(input("Are you a boy or a girl?\n:> ")).upper()

    if usrGendr == 'BOY':
        print('\nI just made a boy from clay.\n\n')
        usrGendr = usrGendr_boy
    elif usrGendr == 'GIRL':
        print('\nI just made a girl from my rib.\n\n')
        usrGendr = usrGendr_girl
    else:
        randomnr = random.randint(1,3)

        if randomnr == 1:
            usrGendr = 'BOY'
            print("\nI think I'll make a boy from clay.\n\n")
            usrGendr = usrGendr_boy
        else:
            usrGendr == 'GIRL'
            print("\nI think I'll make a girl from my rib.\n\n")
            usrGendr = usrGendr_girl

    usrName = str(input("Now choose your characters name:\n:> ")).capitalize()

    while True:
        if " " in usrName:
            print('\nI just need one strong name...\n')
            usrName = str(input("\n1Choose your characters name:\n:> ")).capitalize()
        elif usrName == "":
            print('\nI just need one strong name...\n')
            usrName = str(input("\n2Choose your characters name:\n:> ")).capitalize()
            continue
        else:
            answer = str(input((f'\nIs "{usrName}" correct? (Y/N):\n:> ')).upper())
            if answer == "":
                continue
            elif (answer == 'Y') or (answer == 'YES'):
                outside_home(usrName, 'Outside_home', usrGendr)
            elif (answer == 'N') or (answer == 'NO'):
                usrName = str(input("\n3Choose your characters name:\n:> ")).capitalize()
                continue
            else:
                continue
        break

    return usrName, usrGendr

def look(usrName, location):
    print(f'{usrName} looks around at {location}')


def intro_setting(usrName, location):

    dic_intros = {
'Home':f'''\n{location} INTRO HERE\n'''.upper(),
'Outside_home':f'''\n{location} INTRO HERE\n'''.upper(),
'usrName_room': f'''\n{location} INTRO HERE\n'''.upper(),
'Wildland':f'''\n{location} INTRO HERE\n'''.upper(),
'North':f'''\n{location} INTRO HERE\n'''.upper(),
'North_West':f'''\n{location} INTRO HERE\n'''.upper(),
'West':f'''\n{location} INTRO HERE\n'''.upper(),
'South_West':f'''\n{location} INTRO HERE\n'''.upper(),
'South':f'''\n{location} INTRO HERE\n'''.upper(),
'South_East':f'''\n{location} INTRO HERE\n'''.upper(),
'East':f'''\n{location} INTRO HERE\n'''.upper(),
'DarkLands':f'''\n{location} INTRO HERE\n'''.upper(),
}
    intro_setting = dic_intros.get(location)
    return intro_setting



def outside_home(usrName, location, usrGendr):
    location = 'Outside_home'
    # This is not going to work becuase variable is local. maby dictonary
    first_enterd = 0
    if first_enterd == 0:
        print(intro_setting(usrName, location))
        first_enterd += 1

    print(f'''
{usrName} slowly opens {usrGendr[3]} eyes from {usrGendr[3]} hammock.

The first thing {usrName} notice
is the warm sun on {usrGendr[2]} face
birds chirping faintly in the background
and a lukewarm breeze,
that carries a sweet scent of primrose roses.
'''); time.sleep(15); print(f'''
Afther a few seconds
you hear the sound of a door opening.
You look up and see your {mentorName} standing in a doorway.
'''); time.sleep(10)
#     tutorial_menu(usrName, location)
#
#     # wake by mentor to go inside,
#     # options: look around, dig, go inside home
#     # Serrounding like god of war
#     # go to central
#     # dig
#
# def tutorial_menu(usrName, location):
#     time.sleep(10)
#     while True:
#         usr_command = str(input('''
# - Look
# - Help
# - Quit
# :> ''').upper())
#
#         if usr_command == 'LOOK':
#             look(usrName, location)
#         elif usr_command == 'HELP':
#             help(false)
#         elif usr_command == 'QUIT':
#             answer = str(input(f'\nSure to quit {gameName}? (Y/N):\t').upper())
#             if (answer == 'Y') or (answer == 'YES'):
#                 quit()
#             elif (answer == 'N') or (answer == 'NO'):
#                 continue
#             else:
#                 print("I didn't get that..")

# def home(location):
#     # location = 'Home'
#     # Your home
#     # Your mentor
#     # Your room with Lore read    functie
#
# def usrName_room(location):
#     location = 'usrName_room'
#     # here are some books with lore
#     # rest (saves the game)

#
# def mentor(location, quest1, quest2, quest3,):
#     location = Home
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
#     # dictonarie clasified by region cost as value
#
# def shoptrader(location):
#     location = 'Wildland'
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
# def princess_tower():
#     # can hear princess
#     # lock opens depends on items
#     #
#
# def wildlands(location):
#     location = 'Wildland'
#
#
# def north(location):
#     location = 'North'
#
# def norht_west(location):
#     location = 'North_West'
#
# def west(location):
#     location = 'West'
#
# def south_west(location):
#     location = 'South_West'
#
# def south(location):
#     location = 'South'
#
# def south_east(location):
#     location = 'South_East'
#
# def east(location):
#     location = 'East'
#
# def dark_lands(location):
#     location = 'DarkLands'

def quit():
        print('\nThank you for playing Rise of the Dragon Rider!\n')
        exit(0)

gameName = 'Rise of the Dragon Rider'
mentorName = 'mentor'
usrName = ''
location = ''
usrGendr = []
usrGendr_boy = ["he", "his", "him", "his"]
usrGendr_girl = ["she", "hers", "her", "her"]
true = True
false = False

start(usrName, location, usrGendr)
