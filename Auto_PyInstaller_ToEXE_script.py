# !!! I should probably use subprocesses instead of os.
import os

# Listdr will let you know everything that is in a directory.
from os.path import isfile, join
from os import listdir

from pathlib import Path
import time
import sys

import platform

usr_answer = [('Y', 'y', 'yes', 'Yes', 'YES', 'ok',
               'Ok', 'OK', 'sure', 'Sure', 'SURE')]

#######################################################################################################

def sys_clear():
    ''' Clears terminal screen for diffrent OS's '''

    if 'linux' in platform.platform().lower():
        os.system('clear')
    elif 'windows' in platform.platform().lower():
        os.system('cls')
    else:
        print("Sorry, Your OS is not known to me yet.")

#######################################################################################################

sys_clear()

#######################################################################################################

# While loop check for installation Pyinstaller
while True:
    answer = input('''
Install Pyinstaller now? (Y/N) :> ''')

    os.system('clear')

    if answer in usr_answer[0]:
        # Checking current Python version.
        version = sys.version[0]
        if int(version) <= 1:
            os.system(f'pip install pyinstaller')
            time.sleep(6)
            os.system('clear')
            break
        else:
            os.system(f'pip{version} install pyinstaller')
            time.sleep(6)
            os.system('clear')
            break
    else:
        answer = input(
            "\nIs Pyinstaller already installed? (Y/N) :> ")
        if answer in usr_answer[0]:
            sys.stdout.write("\n")
            os.system('clear')
            break
        else:
            os.system('clear')
            answer = input("\nDo you want to quit? (Y/N) :> ")
            if answer in usr_answer[0]:
                sys.stdout.write("\n\nExiting in 5 seconds!\n\n")
                time.sleep(4)
                quit()
            else:
                # Restarts the while loop.
                os.system('clear')
                continue

#######################################################################################################

# Makes a string of this file's filepath.
filePath = str(Path(__file__).absolute())

# Gets the file extention as a string (via string slicing).
fileExtention = filePath[len(filePath) - 3:]

# Gets the directoryPath as a string.
directoryPath = str(os.path.dirname(os.path.abspath(__file__)))

#######################################################################################################


def run_Setup():
    # Lists all the files in the directory of this script.
    onlyFiles = [f for f in listdir(directoryPath)
                 if isfile(join(directoryPath, f))]

    # Lists only the .py files in the directory of this script.
    onlyPfiles = [f for f in onlyFiles if fileExtention in f]

    # File names can't have whitespaces in them. This loop replaces them with a underscore.
    num = 0
    for fn in onlyPfiles:
        if ' ' in onlyPfiles[num]:
            onlyPfiles[num] = onlyPfiles[num].replace(' ', "_")

            # Makes sure all files end with '.py' (and not '_.py')
            if '_.py' in onlyPfiles[num]:
                onlyPfiles[num] = onlyPfiles[num][:(
                    len(onlyPfiles[num]) - 4)] + '.py'
            
            # Writes the underscore filenames to the file.
            os.rename(fn, onlyPfiles[num])
            num += 1

    # This variable will hold the correct filepath to uses for py2exe.
    fileName = ''  # LEAVE EMPTY!

    # If the program detects more then one Python file to convert to EXE.
    if len(onlyPfiles) > 2:
        num = len(onlyPfiles)

        # Prints .py files to choose from.
        while True:
            print("\n\tI've detected", num,
                  "more files.\n\tWhich one do you want to use?\n\n")
            num = 1
            for i in onlyPfiles:
                if num < 10 and fileExtention == ".py":
                    print(str(num) + ". ", i)
                elif num >= 10 and fileExtention == ".py":
                    print(str(num) + ".", i)
                else:
                    num -= 1
                num += 1
            while True:
                try:
                    num = int(input('\n:> '))
                    if num > len(onlyPfiles):
                        print(f"\n{num} is not a valid number")
                        continue
                    else:
                        break
                except ValueError as e:
                    print("\nThat's not a number at all!")
                    continue
                
            # Expect usr input to be greater then max_index of onlyPfile list.
            if num >= len(onlyPfiles):
                num == len(onlyPfiles)

            answer = input("\nTurn '" + str(onlyPfiles[(num - 1)]
                                            ) + "' into a executable file? (Y/N) :> ")
            if answer in usr_answer[0]:
                os.system('clear')
                fileName = onlyPfiles[(num - 1)]
                # Execute Pyinstaller with parm; onefile.
                os.system(
                    f'pyinstaller {fileName} --onefile')
                break
            else:
                os.system('clear')
                continue

    # If there are NO .py files next to this script.
    elif len(onlyPfiles) == 0:
        sys.stdout.write(
            "\nThere are no files to use in this directory!\n\nEXITING THE SCRIPT!")
        time.sleep(5)
        quit(0)

    # If there is 1 .py file next to this script.
    else:
        sys.stdout.write(f'\n{fileName} found!\nExecuting Pyinstaller!\n')

#######################################################################################################


# Run the function
run_Setup()


# Should delete the 'setup.py' file after 10 seconds (Assuming the py2exe process takes LESS the 10 seconds to finish)
time.sleep(5)
os.system('clear')

sys.stdout.write('\n\SUCCESSFUL!\n\n')

time.sleep(10)

quit()
