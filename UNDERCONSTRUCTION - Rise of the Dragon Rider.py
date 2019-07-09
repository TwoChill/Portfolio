import random
import time
import sys


def start(usrName, usrGendr, location):
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
        start_answer = enter_command(usrName, usrGendr, location)
        if start_answer == 'PLAY':
            player_info(usrName, usrGendr, location)
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
                start(usrName, usrGendr, location)
            else:
                help_answer = str(input('\nPress ENTER to continue\n:>'))
    # else:
    #     print('Else in help fucntion')
    #     return None

def player_info(usrName, usrGendr, location):
    print("\n# INTRO GAME HERE #")
    # this is told from a 'god' perspective

    print("\n\nBut first let's create a character!\n\n")

    usrGendr = str(input("Are you a boy or a girl?\n:> ")).upper()

    if usrGendr == 'BOY':
        print('\nA boy has been made!\n\n')
        usrGendr = usrGendr_boy
    elif usrGendr == 'GIRL':
        print('\nA girl has been made!\n\n')
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
            usrName = str(input("\nChoose your characters name:\n:> ")).capitalize()
            continue
        elif usrName == "":
            print('\nI just need one strong name...\n')
            usrName = str(input("\nChoose your characters name:\n:> ")).capitalize()
            continue
        else:
            answer = str(input((f'\nIs "{usrName}" correct? (Y/N):\n:> ')).upper())
            if answer == "":
                continue
            elif (answer == 'Y') or (answer == 'YES'):
                outside_home(usrName, usrGendr, 'Outside Home')
            elif (answer == 'N') or (answer == 'NO'):
                usrName = str(input("\nChoose your characters name:\n:> ")).capitalize()
                continue
            else:
                continue
        break

    return usrName, usrGendr


def enter_command(usrName, usrGendr, location):
    start_answer = str(input(':> ').upper())
    if start_answer == 'LOOK':
        look(usrName, usrGendr, location)

    elif start_answer == 'DIG':
        dig(usrName, usrGendr, location)

    elif start_answer == 'MAP':
        map(usrName, usrGendr, location)

    elif start_answer == 'HELP':
        start_answer = help(false)
        return usrName, usrGendr, location, start_answer
    else:
        return start_answer

def typing_text(text):
    typing_text = text

    for l in typing_text:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0)

    return typing_text

def first_enterd(location, bool):
    dic_first_enterd = {
    'Home': true,
    'Outside Home': true,
    'usrName_room': true,
    'Wildland': true,
    'North': true,
    'North_West': true,
    'West': true,
    'South_West': true,
    'South': true,
    'South_East': true,
    'East': true,
    'DarkLands': true,
    }
    # if bool == False:
    #     for location in dic_first_enterd:
    #         x = dic_first_enterd.keys()
    #         print(x)
    # bool = true

    return dic_first_enterd.get(location)

def dig(usrName, usrGendr, location):
    print('dig fucntion')
    # here should be a dict with every lil stuf that can be found on the floo
    # every land has a diffrent dict with value to use for shop shoptrader

    # dig
    # randomnr chooses wich item is RETURND with value




def look(usrName, usrGendr, location):
    print("look menu")
    # (location = "") and (first_enterd(location, bool) == True):
    # (location = "") and (first_enterd(location, bool) == True):
    # (location = "") and (first_enterd(location, bool) == True):
    # (location = "") and (first_enterd(location, bool) == True):
    # (location = "") and (first_enterd(location, bool) == True):
    # (location = "") and (first_enterd(location, bool) == True):
    # (location = "") and (first_enterd(location, bool) == True):



def intro_setting(usrName, location):

    dic_intros = {
'Home':f'''\n{location} INTRO HERE\n'''.upper(),
'Outside Home':f'''\n{location} INTRO HERE\n'''.upper(),
'usrName_room':f'''\n{location} INTRO HERE\n'''.upper(),
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



def outside_home(usrName, usrGendr, location):

    if first_enterd(location, false) == True:
        print(intro_setting(usrName, location))
        text = f'''
{usrName} slowly opens {usrGendr[3]} eyes from {usrGendr[3]} hammock.

The first thing {usrName} notice
is the warm sun on {usrGendr[2]} face
birds chirping faintly in the background
and a lukewarm breeze,
that carries a sweet scent of primrose roses.

Afther a few seconds
you hear the sound of a door opening.
You look up and see your {mentorName} standing in a doorway.
'''; typing_text(text); bool = False
    tutorial_quest_look(usrName, usrGendr, location)
    print(bool)
    return usrName, usrGendr, location, bool



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
#     # when called shows a list of things to click
#     # when click on inventory, when accesd from here, show list of items in inventory in inv().
#     # inventory()
#     # map()
    # show map if possible
#     # quests()
#     # Spellbook()
    #   only availibe afther the quest
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

def tutorial_quest_look(usrName, usrGendr, location):

    time.sleep(1)
    print("\n\n# Tutorial: LOOK #")
    time.sleep(3)
    print("\nType 'look' to look around")

    input(":> ")

    text = f'''
{usrName} looks around at {location}
and sees a big tree inside a grass field
surrounded by a man-made wooden fence.
There's a wooden chop-block at the end of the grassfield
next to a stands sturdy man-made wooden log.

A feeling of familiarity came over {usrName} as {usrGendr[0]} sees
{usrGendr[3]} {mentorName} standing in the doorway of the log.

With a confuced face, {usrName}'s {mentorName} walks up to {usrGendr[2]}.
He asks {usrName} to help him find a map that he burried
somewhere around {location}.

You decide to help your {mentorName} and he places his hand
on {usrName}'s' forhead while mumbling some kind of mantra.

Afther a few seconds,
{usrGendr[3]} {mentorName}'s hand flashes with rainbow-colored light.

A warm feeling came over {usrName}.

=================================
{usrGendr[0].capitalize()} accuired the abillity to DIG!
=================================

{usrName}'s {mentorName} pukes from excaustion! But also looks happy.
Probeply beacuse now you can help him find his map.
'''; typing_text(text); bool = False
    tutorial_quest_dig(usrName, usrGendr, location)

    return usrName, usrGendr, location, bool


def tutorial_quest_dig(usrName, usrGendr, location):

    time.sleep(1)
    print("\n\n# Tutorial DIG #")
    time.sleep(3)
    print("\nType 'dig' to dig for the map.")

    input(':>')

    text = f'''
{usrName} uses dig! And finds the the map laying around {location}.
{usrName} gives the map to {usrGendr[3]} {mentorName}.
'''; typing_text(text); bool = False


    time.sleep(1)
    print("\n\n# Tutorial: MAP #")
    time.sleep(3)
    print("\nType 'map' to see the map")
    enter_command(usrName, usrGendr, location)
    return usrName, usrGendr, location, bool

def tutorial_quest_map(usrName, usrGendr, location):
    print('loc3 =', location)
    print(f'{usrName} looks at map!' )
    map(usrName, usrGendr, location)


def map(usrName, usrGendr, location):
    land_name = []
    # if location == 'NORTH':
    #     land_name = ['NORTH','           ','    ','           ','     ','           ','    ','         ','         ','     ','    ']
    #     norht(usrName, usrGendr, location)
    # elif location == 'NORTH_WEST':
    #     north_west(usrName, usrGendr, location)
    # elif location == 'WEST':
    #     west(usrName, usrGendr, location)
    # elif location == 'SOUTH_WEST':
    #     south_west(usrName, usrGendr, location)
    # elif location == 'SOUTH':
    #     south(usrName, usrGendr, location)
    # elif location == 'SOUTH=_EAST':
    #     south_east(usrName, usrGendr, location)
    # elif location == 'EAST':
    #     east(usrName, usrGendr, location)
    # elif location == 'DARKLANDS':
    #     darklands(usrName, usrGendr, location)
    # elif location == 'WILDLANDS':
    #     wildlands(usrName, usrGendr, location)
    # elif location == 'TOWER'::
    #     tower(usrName, usrGendr, location)
    if ((location == 'Home' or location == 'Outside Home') and (first_enterd(location, bool) == True)):
        land_name = ['     ','           ','    ','           ','     ','           ','    ','         ','         ','     ','HOME']
        print('>>> HomeTrue')

    elif ((location == 'Home' or location == 'Outside Home') and (first_enterd(location, bool) == False)):
        land_name = ['     ','           ','    ','           ','     ','           ','    ','         ','         ','     ','HOME']
        print('>>> False')
        home(usrName, usrGendr, location)

    map = f'''
{usrName} opens {usrGendr[3]} map. (in {location})
                                   -----------
                                  |           |
                  -----------     |           |
                 |           |  → |   {land_name[9]}   |
                 |           |     -----------
                 |   {land_name[0]}   |
                  -----------
                    ↓    ↑
 -----------      -----------      -----------
|           |  ← |           |  ← |           |
|           |    |           |    |           |
|{land_name[1]}| →  | {land_name[8]} | →  | {land_name[7]} |
 -----------      -----------      -----------
   ↓    ↑           ↓    ↑           ↓    ↑
 -----------      -----------      -----------
|           |  ← |           |  ← |           |
|           |    |           |    |           |
|    {land_name[2]}   | →  |    {land_name[10]}   | →  |    {land_name[6]}   |
 -----------      -----------      -----------
   ↓    ↑                            ↓    ↑
 -----------      -----------      -----------
|           |  ← |           |  ← |           |
|           |    |           |    |           |
|{land_name[3]}| →  |   {land_name[4]}   | →  |{land_name[5]}|
 -----------      -----------      -----------
'''
    print(map)
    # press enter to close map
    if location == 'Outside Home':
        outside_home(usrName, usrGendr, location)
    return usrName, usrGendr, location







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
location = ''
usrName = ''
usrGendr = []
usrGendr_boy = ["he", "his", "him", "his"]
usrGendr_girl = ["she", "hers", "her", "her"]
true = True
false = False


#outside_home('Michael', 'BOY', 'Outside_home')
start(usrName, usrGendr, location)
