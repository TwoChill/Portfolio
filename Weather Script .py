from pathlib import Path
import platform
import time
import os

# This block gets the filename and uses it in the program.
# It doesn't matter were the file is located or what the filename is or will be.
filePath = str(Path(__file__).absolute())
fileExtention = filePath[len(filePath) - 4:]
directoryPath = str(os.path.dirname(os.path.abspath(__file__)))

scriptName = filePath[(len(directoryPath) + 1):-len(fileExtention)] + '\n\n\n'
option1Name = 'Current Weather'
option2Name = 'Temprature Converter'
menuName = 'Menu'


def sys_clear(name=None):
    ''' Clears terminal screen for diffrent OS's
    and takes a argument to print a string before clearing terminal screen'''

    if 'linux' or 'darwin' in platform.platform().lower():
        os.system('clear')
    elif 'windows' in platform.platform().lower():
        os.system('cls')
    else:
        # !!! Try to make a code that sends a message to your twitter. Just because you can.
        print("Sorry, Your OS is not known to me yet.")

    # This function can take more the 1 text to be displayed after a system clear call.
    if name == None:
        []
    else:
        name = ''.join(name).split(',')
        for i in name:
            print(i)


class WeatherBaloon(object):
    # localWeather arg might be for data that we'll get from the API outside of the class

    def __init__(self, localWeather):
        self.localWeather = localWeather

    @staticmethod
    def menu():
        ''' Class WeatherBaloon menu. The number of methodes this class has'''

        sys_clear([scriptName, menuName])

        try:
            answer = int(input('''
1. Current Weather
2. Temprature Converter (°C <---> °F )


3. Quit

:> '''))

            while True:
                if answer == 1:
                    # WeatherBaloon.get_localweahter()
                    sys_clear([scriptName, option1Name])
                    print("\nI am working on this. Comming soon")
                    itime.sleep(5)
                    WeatherBaloon.menu()
                    break
                elif answer == 2:
                    WeatherBaloon.get_tConv(option2Name)
                elif answer == 3:
                    WeatherBaloon.quit()
                    break
                else:
                    WeatherBaloon.menu()
        except:
            if ValueError:
                print("\n\nThat's not a number\n")
                time.sleep(3)
                WeatherBaloon.menu()

    @classmethod
    def get_localweahter(cls):
        ''' Get's local weather data from OpenWeather's API '''
        pass

    @staticmethod
    def get_tConv(option2Name):
        ''' Converts Fahrenheit to Celsius and vice versa'''

        sys_clear([scriptName, option2Name])

        try:
            answer = int(input('''
1. Fahrenheit --> Celsius
2. Celsius --> Fahrenheit

3. Back
4. Quit

:> '''))
            while True:
                if answer == 1:
                    answer = '°F'
                elif answer == 2:
                    answer = '°C'
                elif answer == 3:
                    WeatherBaloon.menu()
                    break
                elif answer == 4:
                    WeatherBaloon.quit()
                else:
                    WeatherBaloon.get_tConv(option2Name)

                sys_clear([scriptName, option2Name])
                temp = int(input(f"\nHow much {answer}?\n\n:> "))

                sys_clear([scriptName, option2Name])

                if answer == '°F':
                    degree = int(round((temp - 32) * 5 / 9))

                    print(f"\n{temp}°F is {degree}°C\n")
                else:
                    degree = int(round((9 * temp) / 5 + 32))
                    print(f"\n{temp}°C is {degree}°F.\n")

                time.sleep(5)
                sys_clear([scriptName, option2Name])

                answer = input('\nContinue?: (Y/N)\n\n:> ')
                if answer.lower() in ('y', 'yes', 'ok', 'oke', 'okee', 'sure', 'cool'):
                    WeatherBaloon.menu()
                else:
                    sys_clear([scriptName, option2Name])
                    WeatherBaloon.quit()
        except:
            if ValueError:
                print("\n\nThat's not a number\n")
                time.sleep(3)
                WeatherBaloon.menu()

    @staticmethod
    def quit():
        sys_clear(scriptName)
        print('\nGoodbye\n')
        quit()


WeatherBaloon.menu()
