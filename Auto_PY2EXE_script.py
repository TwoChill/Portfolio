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

    # This variable needs to hold the correct filepath to uses for py2exe.
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

            # Expect a number inside the index range.    
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
                fileName = onlyPfiles[(num - 1)]

                # Making sure the setup.py will be inside the same directory as this script.
                os.chdir(directoryPath)
                # Creates a new Python file
                f = open("setup.py", "w+")
############### # Writes content to setup.py file. # ##################################################
                f.write(f"""from distutils.core import setup
import time
import os
import sys
import platform
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

try:
    import py2exe
except ImportError as e:
    print('\nYou don't seem to have PY2EXE installed!\n')
    time.sleep(4)
    
    print('Installing now..')
    time.sleep(3)
    
    version = sys.version[0]
    if int(version) <= 1:
        os.system(f'pip install py2exe')
        time.sleep(4)
        sys_clear()
    else:
        os.system(f'pip{version} install pyinstaller')
        time.sleep(4)
        sys_clear()

setup(console="[{fileName}]")
""")
############### # Closes the file. # ##################################################################
                f.close()
                break
            else:
                sys_clear()
                continue

    # If there are NO .py files next to this script.
    elif len(onlyPfiles) == 0:
        sys.stdout.write(
            "\nThere are no files to use in this directory!\n\nEXITING THE SCRIPT!")
        time.sleep(5)
        quit(0)

    # If there is 1 .py file next to this script.
    else:
        sys.stdout.write(f'\n{fileName} found!\nExecuting py2exe\n')

#######################################################################################################


# Run the function
run_Setup()

# Executes the command in PowerShell to start the py2exe process.
os.system(f'python {directoryPath}/setup.py py2exe')

# Should delete the 'setup.py' file after 10 seconds (Assuming the py2exe process takes LESS the 10 seconds to finish)
time.sleep(5)
sys_clear()

os.remove(f'{directoryPath}/setup.py')
sys.stdout.write('\DONE!\n\n')
time.sleep(10)

quit()
