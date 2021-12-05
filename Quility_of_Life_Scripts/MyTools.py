# Mike Tools

import sys
import time
import os

confirm = ("Y","y","YES","Yes","yes","J","JA","Ja","j","ja")
deny = ("N","No","n","no","NO","Nee","NEE","nee")

class bcolor:
  '''Add colors and types to text'''
  
    ALL_OFF = '\033[0m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[36m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BOLD = '\033[1m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    CONCEALED = '\033[7m'
    END = '\033[0m'

def removeSpaces(txt):
  '''Remove Spaces from text'''
  
    '''Removes spaces from a string'''
    txt = str(txt)
    return txt.replace(" ", "")

def platform():
  '''Returns system platform'''
  
    import platform  
    return platform.system()

def clear(system=platform()):
  '''Clears txt on screen for diffrent systems'''
  
    import subprocess
    if system == 'Windows' or system == 'Darwin':
        
        # Use (shell==True) only with command directly from programmer. Can be a security hazard
        subprocess.run('cls', shell=True)

    elif system == 'Linux':
        subprocess.run('clear', shell=True)
    
    else:
        sys.stdout.write(f"This is platform: {system}!\n")
        sys.stdout.flush()
        time.sleep(5)

    '''Block off access to this module'''
    
    del subprocess

def activate_venv(system, print_activation):
  '''Starts an Virtual Enviroment'''

    import sys
    import os
    import time
    import threading
    
    if system == 'Windows':

        if print_activation in confirm:
            clear()
            sys.stdout.write(bcolors.BLUE + bcolors.BOLD + "Starting Virtual Environment..\n" + bcolors.ENDC)
            sys.stdout.flush()
            # threading to not show installation attempt
            # os.system("pip install virtualenv --no-warn-script-location")
            os.system("py -m venv VenV")
        time.sleep(.5)
        os.system(os.getcwd() + "\\Venv\\Scripts\\activate.bat")
        os.system("cls")
    
    elif system == 'Darwin' or system == 'Linux':

        if print_activation in confirm:
            sys.stdout.write(bcolors.BLUE + bcolors.BOLD + "Starting Virtual Environment..\n" + bcolors.ENDC)
            sys.stdout.flush()

        os.system("python3 -m venv VenV")
        time.sleep(.5)
        os.system("source VenV/bin/activate")

def deactivate_venv(system, print_activation):
  '''Deactivates and Virtual Enviroment'''

    import sys
    import os
    
    if 'shutil' not in sys.modules:
        os.system("pip install shutil")

    import shutil

    if system == 'Windows':
        os.system(os.getcwd() + "\\VenV\\Scripts\\deactivate.bat")
        time.sleep(0.5)
        shutil.rmtree(os.getcwd() + "\\VenV", ignore_errors=True)
        
        if print_activation in confirm:
            sys.stdout.write(bcolors.BLUE + bcolors.BOLD + bcolors.BLINK + "Virtual Environmet Deactivated...\n" + bcolors.ENDC)
            sys.stdout.flush()
    
    elif system == 'Darwin':
        os.system('deactivate')
        time.sleep(.5)
        os.system("rmvirtualenv VenV")
        time.sleep(.5)
        sys.stdout.write(bcolors.BLUE + bcolors.BOLD + bcolors.UNDERLINE + bcolors.BLINK + "Virtual Environmet Deactivated...\n" + bcolors.ENDC)
        sys.stdout.flush()
    
    elif system == 'Linux':
        os.system('deactivate')
        os.system("rmvirtualenv VenV")
        sys.stdout.write(bcolors.BLUE + bcolors.BOLD + bcolors.UNDERLINE + bcolors.BLINK + "Virtual Environmet Deactivated...\n" + bcolors.ENDC)
        sys.stdout.flush()
    
    time.sleep(3)
    clear()

def update_pip(system):
  '''Updates PIP for python'''

    import os
    if system == "Windows":
        os.system("python.exe -m pip install --upgrade pip")
    else:
        sys.stdout.write(bcolors.BLUE + bcolors.BOLD + bcolors.UNDERLINE + bcolors.BLINK + "Please update your version of PIP manualy..\n" + bcolors.ENDC)
        sys.stdout.flush()
        time.sleep(5)

def read_file(file, mode):
    ''' Read a File, mode(r=read, w=write, etc)'''
    
    f = open(file, mode)
    file_content = f.read()
    f.close()

    return file_content

def create_file(data, mode, createVar=None):
    '''Creats a file'''
    
    filename = input(str("Wat wordt het bestandsnaam? :> "))
    
    bestandsExtentie = input(str("Wat wordt het bestandsextentie? :> "))
    if "." not in bestandsExtentie:
        bestandsExtentie += "." + bestandsExtentie
    
    filename += bestandsExtentie
    
    # If 'data' are items in a dictionary..   
    with open(filename, "w+") as f:
        if type(data) == type({}):
            for k,v in data.items():
                f.write(f"{k}:{v}\n")
        else:
            for i in data:
                f.write(str(i))    
    f.close()
    
    print("Je bestand: " + bcolors.BOLD + f"'{filename}'" + bcolors.ENDC + " is aangemaakt en opgeslagen!")
    wait(3)
    clear()
    
    if createVar == True or createVar == False:
        return createVar

def findExtention(fileExtention, path=None):
  '''Gets extiont from a file?'''
  
    if path == None:
        path = str(os.getcwd()) + '\\'
    
    for i in os.listdir(path):
        if fileExtention not in i:
            continue
        elif fileExtention in i:
            return True
        
def listAllFiles(fileExtention=None, workingDirectory=None):
    '''List all filepaths with a specific file extention'''
    
    allFilePaths = {}
    
    if workingDirectory is None:
        workingDirectory = os.getcwd()
    
    for root, dirs, files in os.walk(workingDirectory):    
        for file in files:
            if fileExtention is None:
                '''Çode for Dict'''
                allFilePaths[file] = root
                '''Code for List'''
                # allFilePaths.append(f"{root}\\{file}")
            else:
                if fileExtention in file:
                    '''Çode for Dict'''
                    allFilePaths[file] = root
                    '''Code for List'''
                    # allFilePaths.append(f"{root}\\{file}")
        
    print(bcolors.BOLD + bcolors.BLUE + f"\nFound {len(allFilePaths)} saved files:\n" + bcolors.ENDC)
    
    for n in range(len(allFilePaths)):
        for i in allFilePaths:
            print(bcolors.BOLD +bcolors.BLUE + f"{(n + 1)}" + bcolors.ENDC + "\t" + bcolors.BOLD + bcolors.PURPLE + f"{i[:-5]}".capitalize() + bcolors.ENDC)
    
    return allFilePaths

def wait(number=None):
    time.sleep(number)

def rtLine(printStatment=None):
    '''Return Line Cursor Begin Of Line'''
    
    import sys
    sys.stdout.write(printStatment)
    return printStatment
