#!/bin/python3.7

from pathlib import Path
import time
import platform
import os
import sys
import stat
import itertools

# The script functionality changes depending on the variable argument.
from sys import argv
if len(argv) > 1:
    script_argv = True
else:
    script_argv = False

# Permissions Flags
# 0 = Owner, 1 = Group, 2 = Other
flags = {
    0: {
        0: 0,
        1: stat.S_IXUSR,
        2: stat.S_IWUSR,
        3: stat.S_IXUSR | stat.S_IWUSR,
        4: stat.S_IRUSR,
        5: stat.S_IXUSR | stat.S_IRUSR,
        6: stat.S_IWUSR | stat.S_IRUSR,
        7: stat.S_IRWXU
    },
    1: {
        0: 0,
        1: stat.S_IXGRP,
        2: stat.S_IWGRP,
        3: stat.S_IXGRP | stat.S_IWGRP,
        4: stat.S_IRGRP,
        5: stat.S_IXGRP | stat.S_IRGRP,
        6: stat.S_IWGRP | stat.S_IRGRP,
        7: stat.S_IRWXG
    },
    2: {
        0: 0,
        1: stat.S_IXOTH,
        2: stat.S_IWOTH,
        3: stat.S_IXOTH | stat.S_IWOTH,
        4: stat.S_IROTH,
        5: stat.S_IXOTH | stat.S_IROTH,
        6: stat.S_IWOTH | stat.S_IROTH,
        7: stat.S_IRWXO
    }
}

loadingTxt = "Changing Permissions"


class MyClass(object):

    def __init__(self):
        pass

    def loadingAnimation(self, txt=None, newline=None):
        if newline is True:
            sys.stdout.write('\n')
            sys.stdout.flush()

            if txt is None:
                txt = "Loading"

        for x in range(0, 5):
            b = txt + "." * x
            print(b, end="\r")
            time.sleep(.5)

    def change_permissions(self, path, path_basename, argv_pressent):
        if 'linux' in platform.platform().lower():
            os.system('ls -d  -al */')

        # ask for OCTALS if argv is NOT FOUND:
        if argv_pressent is False:

            choose_flag = f'''
Choose a \'''' + bcolors.BOLD + '''Flag''' + bcolors.ENDC + '''\' to be assigned to''' + bcolors.BOLD + ''' ALL''' + bcolors.ENDC + f''' files --> \'''' + bcolors.UNDERLINE + f'{os.path.basename(path)}' + bcolors.ENDC + ''' \':''' + bcolors.RED + '''

    User:\tr/w/x\t-->\t4/2/1\tsum = 7
    Group:\tr/w/x\t-->\t4/2/1\tsum = 7
    Other:\tr/w/x\t-->\t4/2/1\tsum = 7

''' + bcolors.ENDC + bcolors.BOLD + '''
(IF YOU DON\'T KNOW WHAT FLAGS ARE, PLEASE DISCONTINUE!)''' + bcolors.ENDC

            sys.stdout.write(choose_flag)
            sys.stdout.flush()

            while True:

                # Clear Screen
                sys_clear()
                if 'linux' in platform.platform().lower():

                    # Show current flag permissions of directory
                    os.system("ls -d -al */")

                sys.stdout.write(choose_flag)
                sys.stdout.flush()

                try:
                    usr_flag = int(input('\n\n\nEnter Flag :>\t'))
                except ValueError:
                    print('\nNot a valid input!')
                    time.sleep(3)

                    # Clear Screen
                    sys_clear()

                    continue

                # Checks if entered flag is a actual flag
                if str(usr_flag) in flag_combinations():
                    pass
                else:
                    # Clear Screen
                    sys_clear()

                    # Show current flag permissions of directory
                    os.system("ls -d -al */")

                    sys.stdout.write(choose_flag)
                    sys.stdout.flush()

                    sys.stdout.write(
                        '\n\n\nThat\'s not a valid FLAG. Try Again...')
                    sys.stdout.flush()
                    time.sleep(3)
                    continue

                # Clear Screen
                sys_clear()

                # Show current flag permissions of directory
                os.system("ls -d -al */")

                sys.stdout.write(choose_flag)
                sys.stdout.flush()

                answer = input(
                    f'\n\n\nEntered Flag :>\t\'{usr_flag}\'\n\n\nAre You Sure? (Y/N) :> ').upper()

                if answer in ('Y', 'YES'):

                    if 'linux' in platform.platform().lower():

                        # Clear Screen
                        sys_clear()

                        # Show current flag permissions of directory
                        os.system('ls -d  -al */')

                        self.loadingAnimation(loadingTxt, True)

                        # Get correct flag
                        usr_flag = flag_interpreter(usr_flag, flags)

                        # Change file permissions in parent directory
                        for file in os.listdir(path):
                            os.chmod(f'{path}/{file}', usr_flag)

                        # Change parent directory permissions
                        os.chmod(f'{path}', usr_flag)

                        # Clear Screen
                        sys_clear()

                        # Show current flag permissions of directory
                        os.system("ls -d  -al */")
                        break

                    # Other platforms
                    else:
                        sys_clear()
                        self.loadingAnimation(loadingTxt, True)

                        # Get correct flag
                        usr_flag = flag_interpreter(usr_flag, flags)

                        # Change file permissions in parent directory
                        for file in os.listdir(path):
                            os.chmod(f'{path}/{file}', usr_flag)

                        # Change parent directory permissions
                        os.chmod(f'{path}', usr_flag)

                        # Think about other platforms
                        sys_clear()

                # Quits the script immediately.
                elif answer in ('N', 'NO'):
                    break
                else:
                    sys.stdout.write('\nThat\'s not correct. Try Again\n')
                    sys.stdout.flush()
                    continue

            # Exit script
            sys.stdout.write('\nPermissions Change!\n\n')
            sys.stdout.flush()
            time.sleep(2)

        elif argv_pressent is True:
            self.loadingAnimation(loadingTxt, True)

            # Maby Itertools has a better and faster way
            usr_flag = flag_interpreter(int(argv[1]), flags)

            # For each file in dir_path, change permission of file first.. // GOES ONLY 1 LEVEL DEEP FOR NOW
            for file in os.listdir(dir_path):
                os.chmod(f'{dir_path}/{file}', usr_flag)

            # ..then change permission of parent directory
            os.chmod(f'{dir_path}', usr_flag)

            # Clear Screen
            sys_clear()
            os.system(f"ls -d -al */")

            # Exit script
            sys.stdout.write('\nPermissions Change!\n\n')
            sys.stdout.flush()
            time.sleep(2)

    def get_directory_path(self):
        ''' Get directory path of which to change permissions. '''

        # Change directory to current file path.
        os.chdir(os.path.dirname(Path(__file__)))

        # Make a list of subdirectories in current working directory.
        name_of_dirs = [fn for fn in next(os.walk('.'))[1]]
        nr_of_dirs = len(name_of_dirs)

        # source: https://stackoverflow.com/questions/141291/how-to-list-only-top-level-directories-in-python
        # If there's MORe then 1 directory next to this scirpt.

        if nr_of_dirs > 1:
            while True:

                sys.stdout.write(
                    bcolors.BOLD + f'\nFound {nr_of_dirs} directories!' + bcolors.ENDC + bcolors.UNDERLINE + '\n\n\nWhich directory to change permissions on?\n\n' + bcolors.ENDC)
                dir_names = {}

                for n, i in enumerate(next(os.walk('.'))[1], 1):
                    sys.stdout.write(
                        bcolors.RED + f'{n}. {i}\n' + bcolors.ENDC)
                    sys.stdout.flush()

                    # Append to dictionary to map numbers to directory names.
                    dir_names[n] = i

                try:
                    answer = int(input('\n:> '))
                    break
                except ValueError:
                    print('\nNot a valid input!')
                    time.sleep(3)

                    # Clear Screen
                    sys_clear()

                    continue
            # Clear Screen
            sys_clear()

            for n in range(1, (nr_of_dirs + 1)):
                if answer == n:
                    return f'{os.getcwd()}/{dir_names[n]}', f'{dir_names[n]}'

        # Get the directory's path
        elif nr_of_dirs == 1:
            return f'{os.getcwd()}/{name_of_dirs[0]}', f'{name_of_dirs[0]}'

        else:
            sys.stdout.write(bcolors.BOLD + '\nNo directories found!' + bcolors.ENDC + '\n\nPlace this script in the ' +
                             bcolors.BOLD + 'same ' + bcolors.ENDC + 'directory as the target\'s directory\n\n')
            time.sleep(6)
            sys.stdout.flush()

            # Exit script
            quit()


class bcolors:
    ''' Text colors to use in the Terminal '''
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    # create a option to press ENTER and skip the rolling text #


def flag_combinations():
    ''' Gets all CHMOD Flag combinations '''
    flag_combi = []

    nr_max_flag = range(len(flags[0]))
    result = itertools.product(nr_max_flag, repeat=3)

    for i in result:
        j = str(i)
        k = j.replace("(", "")
        y = k. replace(")", "")
        s = y.replace(", ", "")
        flag_combi.append(s)

    return flag_combi


def flag_interpreter(flag_int, flag_dict):
    ''' Get correct flag '''

    if len(argv) > 1:
        flag_int = int(argv[1])

    usr_flag = []

    for i in range(len(str(flag_int))):
        for n in str(flag_int)[i]:
            usr_flag.append(flag_dict[i][int(n)])

    return sum(usr_flag)


def sys_clear():
    ''' Clears terminal screen for diffrent OS's '''
    os.system('cls||clear')


# Clear Screen
sys_clear()

# Create object
clss = MyClass()

# If an argument variable is given..
dir_path, dir_name = clss.get_directory_path()
clss.change_permissions(dir_path, dir_name, script_argv)
