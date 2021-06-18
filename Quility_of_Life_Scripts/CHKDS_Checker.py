import time
import os
import platform

# VAR
onlyC = None

def clear(currentSystem=None):
    currentSystem = platform.system().capitalize()
    if 'Windows' in currentSystem:
        os.system('cls')
    elif 'Linux' in currentSystem:
        os.system('clear')
    elif 'Darwin' in currentSystem:
        os.system('clear')
class bcolors:
    BLUE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'
    BLACK = '\033[30m'
    GREY = '\33[90m'
    BLINK1 = '\33[5m'
    BLINK2 = '\33[6m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Display avalible Drive Letters (Make for C: a reboot quest)

# USER popen IPV OS.SYS
txt = os.popen('wmic logicaldisk list').read()
# input(txt)
for i in txt:
    if i != ":":
        continue
    else:
        # This always finds only the FIRST ':', thus the first index, thus only C: drive
        # block rusn when i is found.. remove line 41. dont use .find methode
        b = txt.find(':')
        a = b - 1
        driveLetter = txt[a:(b+1)]
        if txt[a:(b+1)][0:1] == driveLetter[0:1]:
            onlyC = True
            continue
        else:
            print(bcolors.BOLD + 'Beschikbare Drive Letters: \t' + f'{driveLetter}' + bcolors.ENDC)
            onlyC = False

if onlyC == True:
    input('\nAlleen C: is beschikbaar.. :> ')

checkDrive = input("\nWelke drive letter wil je controleren? :> ")
clear()

try:
    if 'Windows' in platform.system().capitalize():
        os.system(f"chkdsk {checkDrive}: /x /r")
    elif 'Linux' in platform.system().capitalize():
        pass
    elif 'Darwin' in platform.system().capitalize():
        pass
except:
    print("There's been a error in system:")
# Check system
