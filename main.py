# Importing required modules
# Imports 'random' for random number generation
import random
# Imports 'json' for options file management
import json
# Imports 'os' for file management
import os
# Imports 'platform' for terminal clearing
import platform
# Imports 'time' 
import time
# Imports 'datetime' for accessing date and time
import datetime

try:
    from pytz import timezone
except ModuleNotFoundError:
    print("pytz not found. Please install it before running.")
    f = open("error.log", "x")
    f.write("pytz not found. Please install it via running pip install pytz in Windows Command Prompt, "
            "or Powershell.\n\n\nPythonError: Traceback (most recent call last)\nFile "
            "'/lib/python3.8/asyncio/futures.py', line 178, in result\n    raise self._exception\nFile "
            "'/lib/python3.8/asyncio/tasks.py', line 280, in __step\n    result = coro.send(None)\nFile "
            "'/lib/python3.8/site-packages/pyodide/_base.py', line 419, in eval_code_async\n    return await "
            "CodeRunner(\nFile '/lib/python3.8/site-packages/pyodide/_base.py', line 270, in run_async\n    coro = "
            "eval(mod, self.globals, self.locals)\nFile '<exec>', line 15, in <module>\nModuleNotFoundError: No "
            "module named 'pytz'")

    f.close()
    exit()
# Handles options
# Opening JSON file
options = 'options.json'
if os.path.exists(options):
    f = open(options, 'r')

else:
    try:
        f = open(options, )
    except FileNotFoundError:
        print('File not found: ' + options +
              '. Please reinstall code from Github')
        print(
            "https://github.com/Veillax135/python-dice-testing/archive/refs/heads/main.zip"
        )
# returns JSON object as a dictionary
data = json.load(f)

# Iterating through the json list
for i in data['options']:
    verify = str(i).split()
    printverify = str(verify)
debugverify1 = verify[1].strip(',')
tz = verify[5].strip(',')
system = str(platform.uname())
syssplit = system.split()
syssplit1 = syssplit[0].split("'")
print('Device debug information. Will clear in 5 seconds')


# Handles device debug printing
def debugprint():
    print(system)
    time.sleep(6)


if debugverify1 == 'true':
    debugprint()

# Main loop
while True:

    # Handles terminal clearing
    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')


    # using now() to get current time
    try:
        tz = 'America/Denver'
        current_time = datetime.datetime.now(timezone(tz))
        monthcheck = int(current_time.month) - 9
        daycheck = int(current_time.day) - 9
        yearcheck = int(current_time.year) - 9
        hourcheck = int(current_time.hour) - 9
        mincheck = int(current_time.minute) - 9
        secondcheck = int(current_time.second) - 9
        # Time formatting for datetime
        if current_time.hour > 12:
            hour = int(current_time.hour) - 12
            ampm = 'PM'
            if hourcheck < 0:
                hour = '0' + str(hour)
            elif hourcheck > 0:
                hour = str(hour)
        elif current_time.hour < 12:
            hour = current_time.hour
            ampm = 'AM'
            if hourcheck < 0:
                hour = '0' + str(hour)
            elif hourcheck > 0:
                hour = str(hour)
        if monthcheck < 0:
            month = '0' + str(current_time.month)
        elif monthcheck > 0:
            month = str(current_time.month)
        if daycheck < 0:
            day = '0' + str(current_time.day)
        elif daycheck > 0:
            day = str(current_time.day)
        if yearcheck < 0:
            year = '0' + str(current_time.year)
        elif yearcheck > 0:
            year = str(current_time.year)
        if mincheck < 0:
            minute = '0' + str(current_time.minute)
        elif mincheck > 0:
            minute = str(current_time.minute)
        if secondcheck < 0:
            second = '0' + str(current_time.second)
        elif secondcheck > 0:
            second = str(current_time.second)
        ctime = str(month) + '/' + str(day) + '/' + str(year) + '\n' + str(
            hour) + ':' + str(minute) + str(ampm)
    # Handles date and time printing
    except:
        ctime = 'Sorry, an error occurred while trying to access the current date and time, please try again later.'


    def timenow():
        # prints the date and time
        print(ctime)


    cls()
    # Program introduction
    print(
        "Welcome to my Multi-Functional Python Application! Please choose one of the following options:\nDice Roller("
        "dice)\nEarth Circumference Calculator(ecc)\nIf you would ever like to come back to this menu, please type "
        "'Main Menu'\n "
    )

    timenow()
    try:
        option = input('\nPrompt: ').strip(' ')
    except KeyboardInterrupt:
        print('^C\nKeyboard Interrupt requested. Terminating session...')
        break
        # Opens Dice rolling program
    if option.lower() == 'dice':
        cls()
        try:
            # prints all device info if debug is set to true in 'options.json'
            if debugverify1 == 'True':
                print('Debug options enabled. OS Details:')
                system = str(platform.uname())
                split1 = system.split()
                split2 = split1[0].split("'")
                print(system)


            # Program intro
            # Title
            def title():
                print(
                    "____________________________________________________________\n|      ___        _                "
                    "        _           _   |\n|     / _ \      | |                      | |         | |  |\n|    / "
                    "/_\ \_   _| |_ ___  _ __ ___   __ _| |_ ___  __| |  |\n|    |  _  | | | | __/ _ \| '_ ` _ \ / _` "
                    "| __/ _ \/ _` |  |\n|    | | | | |_| | || (_) | | | | | | (_| | ||  __/ (_| |  |\n|    \_| "
                    "|_/\__,_|\__\___/|_| |_| |_|\__,_|\__\___|\__,_|  |\n|                                           "
                    "               |\n|                                                          |\n|    ______ _    "
                    "       ______      _ _                    |\n|    |  _  (_)          | ___ \    | | |            "
                    "       |\n|    | | | |_  ___ ___  | |_/ /___ | | | ___ _ __          |\n|    | | | | |/ __/ _ \ "
                    "|    // _ \| | |/ _ \ '__|         |\n|    | |/ /| | _|  __/  | |\ \ (_) | | |  __/ |            "
                    "|\n|    |___/ |_|\___\___| \_| \_\___/|_|_|\___|_|            |\n|                               "
                    "                           |\n|__________________________________________________________|\n     "
                    "                  ________     \n            ______    | .   . |\    \n           /     /\   |   "
                    ".   |.\   \n          /  '  /  \  | .   . |.'|  \n         /_____/. . \ |_______|.'|  \n         "
                    "\ . . \    /  \ ' .   \.|  \n          \ . . \  /    \____'__\|  \n           \_____\/           "
                    "    \n "
                )
                # Program instructions
                print(
                    "Please enter the dice you want to roll in the following format: \n<Die Amount> <Die "
                    "Type>.\n\nYou can roll any die type you want by inputting the following cmd format:\nroll "
                    "<amount> d<type>\n\nIf you would like to end the program, type 'end'. \nIf you would like to see "
                    "the commands this program can run, type 'help', 'commands', or '?'.\n\nControls for custom "
                    "rolls: custom <min> <max>\n\nThanks, and hope you enjoy!\n "
                )


            # Targets, opens, and extracts data from 'options.json'
            title()
            options = 'options.json'
            if os.path.exists(options):
                print(
                    'Options loaded, download from Github and edit the options using options.json'
                )
            debugverify1 = verify[1].strip(',')
            if debugverify1 == 'True':
                timenow()
                print('Debug Enabled\n' + printverify + '\n')
            printverify1 = verify[3].strip('}')
            if printverify1 == 'True':
                print('Iteration printing Enabled\n' + printverify + '\n')
            # Declares variables needed
            commands = ['']
            endcode = ''
            cmd = ''
            num = 0
            roll = 0
            i = 1
            # Main-sub-loop
            while True:
                # Command input and parsing
                try:
                    prompt = input('Cmd: ')
                except KeyboardInterrupt:
                    print(
                        '^C\nKeyboard Interrupt requested. Terminating session...'
                    )
                    time.sleep(2)
                    break
                cmd = prompt.split(' ')
                # Handles cmd listing
                if cmd[0] == 'help' or cmd[0] == 'commands' or cmd[0] == '?':
                    print('')
                    print(
                        '._________________________________________________________________________________________________________________________. '
                    )
                    print(
                        '|                                               Commands list                                '
                        '                             | '
                    )
                    print(
                        '|                                                                                                                         |'
                    )
                    print(
                        '|roll    || arguments: roll <amt> <type>   || Rolls dice based on the included arguments   '
                        '|| aliases:                    | '
                    )
                    print(
                        '|end     || arguments: end                 || use: Ends the program                        '
                        '|| aliases: main menu          | '
                    )
                    print(
                        '|cls     || arguments: cls <os> (optional) || use: Clears the screen                       '
                        '|| aliases: clear, clearscreen | '
                    )
                    print(
                        '|help    || arguments: help                || prints out the command list                  '
                        '|| aliases: ?, commands        | '
                    )
                    print(
                        '|                                                                                            '
                        '                             | '
                    )
                    print(
                        '\_________________________________________________________________________________________________________________________/ '
                    )
                    continue
                # Handles ending the program
                if cmd[0].lower() == 'main' and cmd[1].lower() == 'menu' or cmd[0] == 'end':
                    confirm = input(
                        "Are you sure you want to end the current session? Y/N "
                    )
                    if confirm == 'Y' or confirm == 'y':
                        print(
                            "CMD 'sessionend' called. Confirmation true. Terminating session."
                        )
                        time.sleep(2)
                        break
                    elif confirm == 'N' or confirm == 'n':
                        print(
                            "CMD 'sessionend' called. Confirmation false. Session termination cancled."
                        )
                        time.sleep(2)
                        continue

                # Handles clearing the screen
                if cmd[0] == 'cls' or cmd[0] == 'clear' or cmd[0] == 'clearscreen':
                    cls()
                    title()
                    continue

                if cmd[0] == 'roll':
                    if len(cmd) == 3:
                        roll = int(cmd[2].lower().strip('d'))
                        i = 1
                        while int(i) < (int(cmd[1]) + 1):
                            tmp = random.randint(1, int(roll))
                            num += tmp
                            i += 1
                            if debugverify1 == 'True':
                                print(
                                    'Die {} rolled a d{}.\nDie output: {}\nCurrent total output: {}\n'.format(
                                        i,
                                        roll,
                                        tmp,
                                        num
                                    ))
                        print('Final output: ' + str(num))
                    num = 0
        except:
            print('')

    if option.lower() == 'Earth Circumfrence Calculator' or option.lower() == 'ecc':
        cls()
        # Main-subloop
        while True:
            try:
                # Angle and Distance input
                angle1 = input('Input measured angle 1: ')
                angle2 = int(input('Input measured angle 2: '))
                distance1 = input('Input measured distance 1: ')
                distance2 = input('Input measured distance 2: ')
                cir = 24902
                if angle1.lower() == 'main menu':
                    break

                # Main computational proccess
                if int(angle1) > angle2:
                    Difference = int(angle1) - angle2
                    Difference2 = int(angle1) - angle2
                elif int(angle1) < angle2:
                    Difference = angle2 - int(angle1)
                    Difference2 = int(angle1) - angle2
                eadivide2 = round(360 / Difference2)
                eadivide = round(360 / Difference)
                if int(angle1) > angle2:
                    print('|' + str(angle1) + ' - ' + str(angle2) + '| = ' +
                          str(Difference) + '\n360 / ' + str(Difference) +
                          ' = ' + str(eadivide))
                elif int(angle1) < angle2:
                    print('|' + str(angle2) + ' - ' + str(angle1) + '| = ' +
                          str(Difference) + '\n360 / ' + str(Difference) +
                          ' = ' + str(eadivide))
                if float(distance1) > float(float(distance2)):
                    distancesum = round(float(distance1) - float(float(distance2)), 2)
                    distancesum2 = round(float(distance1) - float(float(distance2)), 2)
                elif float(distance1) < float(float(distance2)):
                    distancesum = round(float(float(distance2)) - float(distance1), 2)
                    distancesum2 = round(float(distance1) - float(float(distance2)), 2)
                print('|' + str(distance1) + ' - ' + str(distance2) + '| = ' +
                      str(distancesum))

                fullsum = round(abs(distancesum * eadivide), 2)
                print('|' + str(distancesum) + ' * ' + str(eadivide) + '| = ' +
                      str(fullsum))
                print('Final sum: ' + str(fullsum))
                print("Earth's Cricumfrence: " + str(cir))
                print('Calculated circumfrence was ' + str(abs(int(cir) - int(fullsum))) + ' off.')

            # Error prevention
            except ValueError:
                print('Improper Value. Please try again.')
                time.sleep(2)
                cls()
                continue
            except IndexError:
                print('Value Index not found. Please try again.')
                time.sleep(2)
                cls()
                continue
