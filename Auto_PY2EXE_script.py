from pathlib import Path

import time

# !!! I should probely use subprocesses instead of os.
import os
# Listdr will let you know everything that is in a directory.
from os import listdir
from os.path import isfile, join

# Makes a string of this file's filepath.
filePath = str(Path(__file__).absolute())

# Gets the file extention as a string (via string slicing).
fileExtention = filePath[len(filePath) - 3:]

# Gets the directoryPath as a string.
directoryPath = str(os.path.dirname(os.path.abspath(__file__)))


def run_Setup():
    # Lists all the files in the directory of this script.
    onlyFiles = [f for f in listdir(directoryPath)
                 if isfile(join(directoryPath, f))]

    # Lists only the .py files in the directory of this script.
    onlyPfiles = [p for p in onlyFiles if fileExtention in p]

    # This variable needs to hold the correct filepath to uses for py2exe.
    fileName = ''  # LEAVE EMPTY!

    # If the program detects more then one Python file to convert to EXE.
    if len(onlyPfiles) > 2:
        num = len(onlyPfiles)
        if 'setup.py' in onlyPfiles:
            num -= 1
        print("\n\tI've detected", num,
              "more files.\n\tWhich one do you want to use?\n\n")

        # Prints .py files to choose from.
        while True:
            num = 1
            for i in onlyPfiles:
                if i == 'setup.py':
                    continue
                elif num < 10 and fileExtention == ".py":
                    print(str(num) + ". ", i)
                elif num >= 10 and fileExtention == ".py":
                    print(str(num) + ".", i)
                else:
                    num -= 1
                num += 1

            num = int(input('\n:> '))
            time.sleep(2)

            # Expect usr value to be greater then max_index of onlyPfile list.
            if num >= len(onlyPfiles):
                num == len(onlyPfiles)

            answer = input("\nTurn '" + str(onlyPfiles[(num - 1)]
                                            ) + "' into a executable file? (Y/N) :> ")
            if answer in ('Y', 'y', 'yes', 'Yes', 'YES', 'ok', 'Ok', 'OK', 'sure', 'Sure', 'SURE'):
                fileName = onlyPfiles[(num - 1)]

                # Making sure the setup.py will be inside the same directory as this script.
                os.chdir(directoryPath)
                # Creates a new Python file
                f = open("setup.py", "w+")
                # Writes content to setup.py file.
                f.write(f'''from distutils.core import setup
import py2exe

setup(console="[{fileName}]")
''')
                # Closes the file
                f.close()
                break
            else:
                print('\n')
                continue

    # If there are NO .py files next to this script.
    elif len(onlyPfiles) == 0:
        print("There are no files to use in this directory!\n\nEXITING THE SCRIPT!")
        time.sleep(5)
        quit(0)

    # If there is 1 .py file next to this script.
    else:
        print(f'\n{fileName} found!\nExecuting py2exe')


run_Setup()

# Executes the command in PowerShell to start the py2exe process.
os.system(f'python {directoryPath}/setup.py py2exe')

# Should delete the 'setup.py' file after 10 seconds (Assuming the py2exe process takes LESS the 10 seconds to finish)
print('EXITING PROGRAM IN 10 SECONDS!') 
time.sleep(10)
os.remove(f'python {directoryPath}/setup.py')

quit()
