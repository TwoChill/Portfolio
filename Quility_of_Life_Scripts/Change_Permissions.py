from pathlib import Path
import time
import platform
import os
import sys
from sys import argv
if len(argv) > 1:
    argv_pressent = True
else:
    argv_pressent = False


class MyClass(object):

    def __init__(self):
        pass

    def loadingAnimation(self):
        for x in range(0, 5):
            b = "Loading" + "." * x
            print(b, end="\r")
            time.sleep(.5)

    def change_permissions(self, dir_path, argv_pressent):
        if 'linux' in platform.platform().lower():
            os.system('ls -al')

        # Get basename of 1 folder INSIDE os.getcwd()
        basename = f'{os.path.basename(dirNameGood)}'

        # ask for OCTALS if argv is NOT FOUND:
        if argv_pressent is False:
            argv_pressent = int(input(
                f'\nWhich permissions should be given to all files in \'{basename}\'?'))

            # Confirmation
            while True:
                answer = input(
                    f'\nAre you sure you want to give \'{argv_pressent[0]}\' to \'{basename}\'? (Y/N) :> ').upper()

                # AFTHER AND IS A MINI-FIX OR WORKAROUND. SHOULD ACCEPT ONLY CHMOD OCTALS AND NOT JUST ANY 3 DIGITS.
                if answer in ('Y', 'YES') and 4 > len(argv_pressent[0]) == 3:

                    if 'linux' in platform.platform().lower():
                        sys_clear()
                        os.system('ls -al')

                        self.loadingAnimation()
                        os.chmod(os.getcwd(), int(argv_pressent))
                        sys_clear()
                        os.system('ls -al')

                    # Other platforms
                    else:
                        sys_clear()
                        self.loadingAnimation()
                        os.chmod(os.getcwd(), int(argv_pressent))

                elif answer in ('N', 'NO'):
                    break
                else:
                    sys.stdout.write('\nThat\'s not correct. Try Again\n')
                    sys.stdout.flush()
            # directly use chmod to change all files inside that directory
            # display current permissions
        elif argv_pressent is True:
            self.loadingAnimation()
            os.chmod(dirNameGood, int(argv[1]))
            sys_clear()
            os.system("ls -al")

    def get_folder_path(self):
        # 1. change to file's working directory
        # Can you change permissions if cwd is the target?

        # CHANGE CODE TO FILEPATH
        os.chdir(os.path.dirname(Path(__file__)))

        # 2. make a list of directories in cwd
        name_of_dirs = next(os.walk('.'))[1]
        nr_of_dirs = len(name_of_dirs)

        # source: https://stackoverflow.com/questions/141291/how-to-list-only-top-level-directories-in-python
        # If there's MORe then 1 directory next to this scirpt.

        # sys_clear('\n')
        # self.loadingAnimation()

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

            for n in range(1, (nr_of_dirs + 1)):
                if answer == n:
                    return f'{os.getcwd()}/{dir_names[n]}'

        # get DELETEME
        elif nr_of_dirs == 1:
            return f'{os.getcwd()}/{name_of_dirs[0]}'

        else:
            sys.stdout.write('\nNo directories found!\n')
            sys.stdout.flush()


def sys_clear(print_statement=None):
    ''' Clears terminal screen for diffrent OS's '''
    os.system('cls||clear')

    if type(print_statement) == 'str':
        sys.stdout.write(print_statement + '\n')
        sys.stdout.flush()
    else:
        print_statement


# Dual functionality of script.
sys_clear()

# Standard first item in argv is the scripts name
# If script is run with argument variable

# Create instance
clss = MyClass()

# If 777 is given
if len(argv) > 1:
    argv[1] = '0' + argv[1]
    print(argv)
    time.sleep(3)

    dirNameGood = clss.get_folder_path()

    clss.change_permissions(dirNameGood, argv_pressent)
    # get path of file
else:
    print('ARGV NOT found')
    time.sleep(3)
    clss.get_folder_path()


# Source: https://stackoverflow.com/questions/15607903/python-module-os-chmodfile-664-does-not-change-the-permission-to-rw-rw-r-bu#17776766

# Note: Although Windows supports chmod(),
# you can only set the file’s read-only flag with it
# (via the stat.S_IWRITE and stat.S_IREAD constants or a corresponding integer value).
# All other bits are ignored.
