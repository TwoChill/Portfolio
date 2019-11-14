import platform
import os
import time

name = 'Temperature Conversion Calculator\n'


def sys_clear(name=None):
    ''' Clears terminal screen for diffrent OS's '''

    if 'linux' in platform.platform().lower():
        os.system('clear')
    elif 'windows' in platform.platform().lower():
        os.system('cls')
    else:
        print("Sorry, Your OS is not known to me yet.")

    if name == None:
        []
    else:
        print(name)


sys_clear(name)

try:
    while True:
        try:
            answer = int(input('''1. Fahrenheit --> Celsius
2. Celsius --> Fahrenheit

:> '''))
            if answer == 1:
                answer = '°F'
            elif answer == 2:
                answer = '°C'
        except ValueError:
            sys_clear(name)
            continue

        sys_clear(name)

        temp = int(input(f"\nHow much {answer}?\n\n:> "))

        sys_clear(name)

        if answer == '°F':
            degree = int(round((temp - 32) * 5 / 9))

            print(f"\n{temp}°F is {degree}°C\n")
        else:
            degree = int(round((9 * temp) / 5 + 32))
            print(f"\n{temp}°C is {degree}°F.\n")

        time.sleep(5)
        sys_clear(name)

        answer = input('\nContinue?: (Y/N)\n\n:> ')
        if answer.lower() in ('y', 'yes', 'ok', 'oke', 'okee', 'sure', 'cool'):
            continue
        else:
            sys_clear(name)
            print('\nGoodbye!\n')
            break
except KeyboardInterrupt:
    sys_clear(name)
    print('\nGoodbye')
