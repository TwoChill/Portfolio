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

    def change_permissions(self, path, argv_pressent):
        if 'linux' in platform.platform().lower():
            os.system('ls -d  -al */')

        # Get basename of 1 folder INSIDE os.getcwd()
        basename = f'{os.path.basename(path)}'

        # ask for OCTALS if argv is NOT FOUND:
        if argv_pressent is False:

            choose_flag = f'''
Which \'Flag\' should be assigned to \'{basename}\':

    User:\tr/w/x\t-->\t4/2/1\tsum = 7
    Group:\tr/w/x\t-->\t4/2/1\tsum = 7
    Other:\tr/w/x\t-->\t4/2/1\tsum = 7

(IF YOU DON\'T KNOW WHAT FLAGS ARE, PLEASE DISCONTINUE!)'''

            sys.stdout.write(choose_flag)
            sys.stdout.flush()

            # Confirmation
            while True:
                # Clear Screen with printstatement
                sys_clear()
                os.system("ls -d -al */")
                sys.stdout.write(choose_flag)
                sys.stdout.flush()

                usr_flag = int(input('\n\n\nEnter Flag :>\t'))

                if str(usr_flag) in flag_combinations():
                    pass
                else:
                    # Clear Screen with printstatement
                    sys_clear()
                    os.system("ls -d -al */")
                    sys.stdout.write(choose_flag)
                    sys.stdout.flush()

                    sys.stdout.write(
                        '\n\n\nThat\'s not a valid FLAG. Try Again...')
                    sys.stdout.flush()
                    time.sleep(3)
                    continue

                # Clear Screen with printstatement
                sys_clear()
                os.system("ls -d -al */")
                sys.stdout.write(choose_flag)
                sys.stdout.flush()

                answer = input(
                    f'\n\n\nEntered Flag :>\t\'{usr_flag}\'\n\n\nAre You Sure? (Y/N) :> ').upper()

                # AFTHER AND IS A MINI-FIX OR WORKAROUND. SHOULD ACCEPT ONLY CHMOD OCTAL AND NOT JUST ANY 3 DIGITS.
                if answer in ('Y', 'YES'):

                    if 'linux' in platform.platform().lower():
                        sys_clear()
                        os.system('ls -d  -al */')

                        self.loadingAnimation(loadingTxt, True)

                        os.chmod(os.getcwd(), usr_flag)
                        sys_clear()
                        os.system("ls -d  -al */")

                        break

                    # Other platforms
                    else:
                        sys_clear()
                        self.loadingAnimation(loadingTxt, True)
                        os.chmod(os.getcwd(), usr_flag)

                        # Think about other platforms
                        sys_clear()

                # Quits the script immediately.
                elif answer in ('N', 'NO'):
                    break
                else:
                    sys.stdout.write('\nThat\'s not correct. Try Again\n')
                    sys.stdout.flush()
                    continue

        elif argv_pressent is True:
            self.loadingAnimation(loadingTxt, True)

            # Maby Itertools has a better and faster way
            mode = []
            for i in range(len(argv[1])):
                for n in argv[1][i]:
                    mode.append(flags[i][int(n)])
            mode = sum(mode)

            # For each file in dir_path, change permission of file first.. // GOES ONLY 1 LEVEL DEEP FOR NOW
            for file in os.listdir(dir_path):
                os.chmod(f'{dir_path}/{file}', mode)

            # ..then change permission of parent directory
            os.chmod(f'{dir_path}', mode)

            sys_clear()
            os.system(f"ls -d  -al */;cd {os.path.basename(dir_path)};ls -l *")

            # Exit script
            time.sleep(1)
            sys.stdout.write('\nPermissions Change!\n\n')
            sys.stdout.flush()
            time.sleep(2)

    def get_folder_path(self):

        # Change directory to current file path.
        os.chdir(os.path.dirname(Path(__file__)))

        # Make a list of subdirectories in current working directory.
        name_of_dirs = [fn for fn in next(os.walk('.'))[1]]
        nr_of_dirs = len(name_of_dirs)

        # source: https://stackoverflow.com/questions/141291/how-to-list-only-top-level-directories-in-python
        # If there's MORe then 1 directory next to this scirpt.

        if nr_of_dirs > 1:

            sys.stdout.write(
                f'\nFound {nr_of_dirs} directories!\n\n\nWhich one to change permissions on?\n\n')
            dir_names = {}

            for n, i in enumerate(next(os.walk('.'))[1], 1):
                sys.stdout.write(f'{n}. {i}\n')
                sys.stdout.flush()

                # Append to dictionary to map numbers to directory names.
                dir_names[n] = i

            answer = int(input('\n:> '))

            sys_clear()

            for n in range(1, (nr_of_dirs + 1)):
                if answer == n:
                    return f'{os.getcwd()}/{dir_names[n]}'

        # get DELETEME
        elif nr_of_dirs == 1:
            return f'{os.getcwd()}/{name_of_dirs[0]}'

        else:
            sys.stdout.write('\nNo directories found!\n')
            sys.stdout.flush()


def flag_combinations():
    ''' Gets all CHMOD Flag combinations '''
    mode = []

    max_combinations = range(len(flags[0]))
    result = itertools.combinations_with_replacement(max_combinations, 3)

    for i in result:
        j = str(i)
        k = j.replace("(", "")
        y = k. replace(")", "")
        s = y.replace(", ", "")
        mode.append(s)

    return mode


def sys_clear():
    ''' Clears terminal screen for diffrent OS's '''
    os.system('cls||clear')


# Clears terminal screen
sys_clear()

# Create object
clss = MyClass()


# If an argument variable is given..
dir_path = clss.get_folder_path()
clss.change_permissions(dir_path, script_argv)


# Source: https://stackoverflow.com/questions/15607903/python-module-os-chmodfile-664-does-not-change-the-permission-to-rw-rw-r-bu#17776766

# Note: Although Windows supports chmod(),
# you can only set the file’s read-only flag with it
# (via the stat.S_IWRITE and stat.S_IREAD constants or a corresponding integer value).
# All other bits are ignored.
