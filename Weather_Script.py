# !/usr/bin/python3

from pathlib import Path
import sys
import requests
import platform
import time
import os

txtSpeed = 0.05
# This block gets the filename and uses it in the program.
# It doesn't matter were the file is located or what the filename is or will be.
filePath = str(Path(__file__).absolute())
fileExtention = filePath[len(filePath) - 4:]
directoryPath = str(os.path.dirname(os.path.abspath(__file__)))

scriptName = '\t\t' + \
    filePath[(len(directoryPath) + 1):-len(fileExtention)] + '\n\n\n'
option1Name = 'Current Weather'
option2Name = '\tTemprature Converter'
menuName = '\tMenu'


def sys_clear(name=None):
    ''' Clears terminal screen for diffrent OS's
    and takes a argument to print a string before clearing terminal screen'''

    if 'linux' or 'darwin' in platform.platform().lower():
        os.system('clear')
    elif 'windows' in platform.platform().lower():
        os.system('cls')
    else:
        # !!! Try to make a code that sends a message to your twitter. Just because you can.
        Typing(txtSpeed, "Sorry, Your OS is not known to me yet.")

    # This function can take more the 1 text to be displayed after a system clear call.
    if name == None:
        []
    else:
        name = ''.join(name).split(',')
        for i in name:
            Typing.text_decor(None, ['bold', 'underline'], i)


class WeatherBaloon(object):

    @staticmethod
    def menu():
        ''' Class WeatherBaloon menu. The number of methodes this class has'''

        sys_clear([scriptName, menuName])

        try:
            answer = int(input('''
1. Weather Baloon
2. Temprature Converter (°C <---> °F )

3. Quit

:> '''))
            while True:
                if answer == 1:
                    WeatherBaloon.get_localweahter()
                    break
                elif answer == 2:
                    WeatherBaloon.get_tConv(option2Name)
                elif answer == 3:
                    WeatherBaloon.quit()
                    break
                else:
                    WeatherBaloon.menu()
        except (ValueError, KeyboardInterrupt):
            print("\nThat's not a number!")
            time.sleep(3)
            WeatherBaloon.menu()

    @staticmethod
    def get_localweahter():
        ''' Get's local weather data from a weather API '''

        sys_clear([scriptName, option1Name])

        try:
            answer = input(
                "\nFor which " + bcolors.UNDERLINE + "location" + bcolors.ENDC + " do you want to get the current weather information?\n\n:> ").capitalize()

            api_accesskey = f'http://api.weatherstack.com/current?access_key=f4ec8c3283872a7de69e9ec1129bfebf&query={answer}'

            json_data = requests.get(api_accesskey).json()
            # print(json_data)

            city = ''.join([json_data['location']['name']])
            country = ''.join([json_data['location']['country']])
            # country_city = ','.join(x for x in [json_data['request']['query']])

            # Clears the screen, displays special text. DO NOT MOVE THIS LINE UP!
            sys_clear([scriptName, option1Name, ' in ', city, ' - ', country])

            temperature = ''.join(str(x)
                                  for x in [json_data['current']['temperature']])

            weather_description = ''.join(
                [json_data['current']['weather_descriptions'][0]])

            observation_time = [json_data['current']['observation_time']][0]

            local_time = ''.join(
                [json_data['location']['localtime']]).split()[1] + ' ' + observation_time.split()[1]

            pressure = ''.join(str(x)
                               for x in [json_data['current']['pressure']])
            humidity = ''.join(str(x)
                               for x in [json_data['current']['humidity']])
            cloudcover = ''.join(str(x)
                                 for x in [json_data['current']['cloudcover']])
            feelslike = ''.join(str(x)
                                for x in [json_data['current']['feelslike']])
            precip = ''.join(str(x) for x in [json_data['current']['precip']])

            visibility = ''.join(str(x)
                                 for x in [json_data['current']['visibility']])
            wind_speed = ''.join(str(x)
                                 for x in [json_data['current']['wind_speed']])
            wind_degree = ''.join(
                str(x) for x in [json_data['current']['wind_degree']]) + '°'

            wind_dir = ''.join([json_data['current']['wind_dir']])

            if wind_dir == 'S':
                wind_dir = 'South'
            elif wind_dir == 'SSE':
                wind_dir = 'South / South East'
            elif wind_dir == 'SE':
                wind_dir = 'South East'
            elif wind_dir == 'ESE':
                wind_dir = 'East / South East'
            elif wind_dir == 'E':
                wind_dir = 'East'
            elif wind_dir == 'ENE':
                wind_dir = 'East / North East'
            elif wind_dir == 'NE':
                wind_dir = 'North East'
            elif wind_dir == 'NNE':
                wind_dir = 'Norht / North East'
            elif wind_dir == 'N':
                wind_dir = 'North'
            elif wind_dir == 'NNW':
                wind_dir = 'North / North West'
            elif wind_dir == 'NW':
                wind_dir = 'Nort West'
            elif wind_dir == 'WNW':
                wind_dir = 'West / North West'
            elif wind_dir == 'W':
                wind_dir = 'West'
            elif wind_dir == 'WSW':
                wind_dir = 'West / South West'
            elif wind_dir == 'SW':
                wind_dir = 'South West'
            elif wind_dir == 'SSW':
                wind_dir = 'South / South West'

            unit = ''.join(json_data['request']['unit'])

            if unit == 'm':
                unit = 'C'
            elif unit == 'f':
                unit = 'F'
            elif unit == 's':
                unit = 'S'

            print(f'''
Local Time:\t\t {local_time}
Observation Time:\t {observation_time}

Temprature:\t\t {temperature}°{unit} - {weather_description}
Feels Like:\t\t {feelslike}°{unit}

Wind Speed:\t\t {wind_speed} Kph
Wind Degree:\t\t {wind_degree}
Wind Direction:\t\t {wind_dir}

Cloud Cover:\t\t {cloudcover}%
Precipitation:\t\t {precip}%
Air Pressure:\t\t {pressure} MB (millibar)
Humidity:\t\t {humidity}%
Visibility:\t\t {visibility} Km
''')

            input('\n\t\t' + bcolors.BOLD +
                  bcolors.UNDERLINE + 'CONTINUE' + bcolors.ENDC)

            sys_clear([scriptName, option1Name])

            while True:
                answer = input('\nSelect another location?: (Y/N)\n\n:> ')

                if answer.lower() in ('y', 'yes', 'ok', 'oke', 'okee', 'sure', 'cool'):
                    WeatherBaloon.get_localweahter()
                    break
                else:
                    sys_clear([scriptName, option1Name])
                    answer = input('\nBack to main menu?: (Y/N)\n\n:> ')

                    if answer.lower() in ('y', 'yes', 'ok', 'oke', 'okee', 'sure', 'cool'):
                        WeatherBaloon.menu()
                        break
                    else:
                        sys_clear([scriptName, option1Name])
                        WeatherBaloon.quit()
                        break
                    break
        except KeyboardInterrupt:
            WeatherBaloon.quit()
        except (ValueError):
            print('\nThat is not a number!')
            time.sleep(3)
            WeatherBaloon.get_localweahter()
        except (KeyError):
            print("\nI don't know were or what that is.")
            time.sleep(3)
            WeatherBaloon.get_localweahter()

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
                    break
                else:
                    sys_clear([scriptName, option2Name])
                    answer = input('\nBack to main menu?: (Y/N)\n\n:> ')
                    if answer.lower() in ('y', 'yes', 'ok', 'oke', 'okee', 'sure', 'cool'):
                        WeatherBaloon.menu()
                        break
                    else:
                        sys_clear([scriptName, option2Name])
                        WeatherBaloon.quit()
        except (ValueError, KeyboardInterrupt):
            WeatherBaloon.quit()

    @staticmethod
    def quit():
        sys_clear(scriptName)
        print('Goodbye\n')
        quit(0)


class bcolors(object):
    ''' Text colors to use in the Terminal '''
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Typing(bcolors):
    ''' Game txt is being typed on screen. CTRL to increase speed '''

    def __init__(self, txtSpeed, text=None):
        self.text = text

        if text is None:
            self.text == []
        else:
            self.text = text

        self.txtSpeed = txtSpeed
        self.bcolors = bcolors

        text = ''.join(self.text)

        for l in text:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(txtSpeed)

        sys.stdout.write('\n')
        sys.stdout.flush()

    @classmethod
    def text_decor(cls, color, decor=None, text=None):
        ''' This function decorates text with UNDERLINE and/or BOLD '''

        if text == None:
            text = []
        elif color == 'red':
            text = bcolors.FAIL + text + bcolors.ENDC
        elif color == 'green':
            text = bcolors.OKGREEN + text + bcolors.ENDC
        elif color == 'blue':
            text = bcolors.OKBLUE + text + bcolors.ENDC
        elif color == 'orange':
            text = bcolors.WARNING + text + bcolors.ENDC
        else:
            text = text + bcolors.ENDC

        if decor == None:
            decor == []
        elif decor == ['bold', 'underline']:
            for i in decor:
                if i == 'bold':
                    text = bcolors.BOLD + text
                if i == 'underline':
                    text = bcolors.UNDERLINE + text
        else:
            if decor == 'bold':
                text = bcolors.BOLD + text
        if decor == 'underline':
            text = bcolors.UNDERLINE + text

        print(text)


WeatherBaloon.menu()
