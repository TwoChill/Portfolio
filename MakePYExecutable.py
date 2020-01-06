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
    answer = input("\nIs Pyinstaller installed on your Debian system? (Y/N) :> ")

    # Clears the terminal of previous outputs.
    sys_clear()

    if answer in usr_answer[0]:
        break
    else:
        answer = input('''\nInstall Pyinstaller now? (Y/N) :> ''')

        # Clears the terminal of previous outputs.
        sys.stdout.write("\n")
        sys_clear()

        if answer in usr_answer[0]:
            # Checking current Python version.
            version = sys.version[0]
            if int(version) <= 1:
                os.system(f'pip install pyinstaller')
                time.sleep(4)
                sys_clear()
                break
            else:
                os.system(f'pip{version} install pyinstaller')
                time.sleep(4)
                sys_clear()
                break
        else:
            answer = input('\nDo you want to exit this script? (Y/N) :> ')

            if answer in usr_answer[0]:
                time.sleep(3)
                sys_clear()
                print('\nExiting script!')
                quit()
            else:
                time.sleep(1)
                sys_clear()
                continue

#######################################################################################################

# Makes a string of this file's filepath.
filePath = str(Path(__file__).absolute())

# Gets the file extention as a string (via string slicing).
fileExtention = filePath[len(filePath) - 3:]

# Gets the directoryPath as a string.
directoryPath = str(os.path.dirname(os.path.abspath(__file__)))
print(directoryPath)
#######################################################################################################


def run_Setup():
    # Lists all the files in the directory of this script.
    onlyFiles = [f for f in listdir(directoryPath)
                 if isfile(join(directoryPath, f))]

    # Lists only the .py files in the directory of this script.
    onlyFiles = [f for f in onlyFiles if fileExtention in f]

    # File names can't have whitespaces in them. This loop replaces them with a underscore.
    num = 0
    for fn in onlyFiles:
        if ' ' in onlyFiles[num]:
            onlyFiles[num] = onlyFiles[num].replace(' ', "_")

            # Makes sure all files end with '.py' (and not '_.py')
            if '_.py' in onlyFiles[num]:
                onlyFiles[num] = onlyFiles[num][:(
                    len(onlyFiles[num]) - 4)] + '.py'

            # Writes the underscore filenames to the file.
            os.rename(fn, onlyFiles[num])
            num += 1

    # This variable will hold the correct filepath to uses for py2exe.
    fileName = ''  # LEAVE EMPTY!

    # If the program detects more then one Python file to convert to EXE.
    if len(onlyFiles) > 2:
        num = len(onlyFiles)

        # Prints .py files to choose from.
        while True:
            print("\n\tI've detected", num,
                  "more files.\n\tWhich one do you want to use?\n\n")
            num = 1
            for fn in onlyFiles:

                # Replaces the '_' with whitespaces. Doesn't change the filename.
                fn = fn.replace('_', " ")

                if num < 10 and fileExtention == ".py":
                    print(str(num) + ". ", fn)
                elif num >= 10 and fileExtention == ".py":
                    print(str(num) + ".", fn)
                else:
                    # When a file doesn't end with .py.
                    num -= 1
                num += 1

            # User input error handeling.
            while True:
                try:
                    num = int(input('\n:> '))
                    if num > len(onlyFiles):
                        print(f"\n{num} is not a valid number")
                        continue
                    else:
                        break
                except ValueError as e:
                    print("\nThat's not a number at all!")
                    continue

            answer = input("\nTurn '" + str(onlyFiles[(num - 1)]
                                            ) + "' into a executable file? (Y/N) :> ")
            if answer in usr_answer[0]:
                sys_clear()
                fileName = onlyFiles[(num - 1)]

                # Execute Chmod.
                os.system(f'chmod +x {fileName}')
                print(f'\nExecuting command: "chmod +x {fileName}"\n')
                time.sleep(6)
                sys_clear()

                # Execute Pyinstaller with parameter; onefile and onedirectory.
                print(f'\nExecuting command: "pyinstaller {fileName} --onefile --onedir"\n')
                time.sleep(6)
                sys_clear()
                os.system(
                    f'pyinstaller {fileName} --onefile --onedir')
                break
            else:
                sys_clear()
                continue

    # If there are NO .py files next to this script.
    elif len(onlyFiles) == 0:
        sys.stdout.write(
            "\nThere are no files to use in this directory!\n\nEXITING THE SCRIPT!")
        time.sleep(5)
        quit(0)

    # If there is 1 .py file next to this script.
    else:
        fileName = onlyFiles[0]
        sys.stdout.write(f'\n{fileName} found!\n\nExecuting Pyinstaller!\n')
    return fileName

#######################################################################################################


# Run the function
run_Setup()


# Should delete the 'setup.py' file after 10 seconds (Assuming the py2exe process takes LESS the 10 seconds to finish)
time.sleep(2)

print(f'\n\nYour file can be found in {directoryPath}/dist\n\nSCRIPT IS DONE!\n\n')

time.sleep(10)

quit()