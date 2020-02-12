import os
import sys
from sys import argv
import platform
import time
from pathlib import Path

# Give all octals(key) there respective name(vale)
octal_permission_dir = (775)


class MyClass(object):

    def __init__(self):
        pass

    def loadingAnimation(self):
        # shows loading animation on screen
        pass

    def change_permissions(self, dir_path, argv=None):
        if 'linux' in platform.platform().lower():
            os.system('ls')
        # ask for OCTALS:
        usr_octal_input = int(input(
            f'\nWhich permissions should be given to all files in \'{os.path.basename(os.getcwd())}\''))

        # Confirmation
        while True:
            answer = input(
                f'\nAre you sure you want to give {octal_permission_dir}')
        # directly use chmod to change all files inside that directory
        # display current permissions
        pass

    def get_folder_path(self):
        # 1. change to file's working directory
        os.chdir(os.path.dirname(Path(__file__)))

        # 2. make a list of directories in cwd
        nr_of_dirs = len(next(os.walk('.'))[1])

        # source: https://stackoverflow.com/questions/141291/how-to-list-only-top-level-directories-in-python
        # If there's more then 1 directory next to this scirpt.
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

        elif nr_of_dirs == 1:
            # Change permission function
            pass
        else:
            print('Found 1')

        # 3. if more directory is found, ask usr to pick one.
        # 4. return and cwd of that directory
        pass


def sys_clear():
    ''' Clears terminal screen for diffrent OS's '''
    os.system('cls||clear')


# Dual functionality of script.
sys_clear()

# Standard first item in argv is the scripts name
# If script is run with argument variable

# Create instance
clss = MyClass()

# If 777 is given
if len(argv) > 1:
    usr_octal_input = argv[1:2]
    # Use instance method
    print('>')
    clss.change_permissions(clss.get_folder_path(), usr_octal_input)
    # get path of file
else:
    print('>>')
    clss.get_folder_path()
