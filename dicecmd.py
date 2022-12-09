import time


def dicehelp():
    print('')
    print(
        '._____________________________________________________________________________________________________________'
        '____________. '
    )
    print(
        '|                                               Commands list                                                '
        '             | '
    )
    print(
        '|                                                                                                            '
        '             | '
    )
    print(
        '|roll    || arguments: roll <amt> <type>   || Rolls dice based on the included arguments   || aliases:       '
        '             | '
    )
    print(
        '|end     || arguments: end                 || use: Ends the program                        || aliases: main '
        'menu          | '
    )
    print(
        '|cls     || arguments: cls                 || use: Clears the screen                       || aliases: '
        'clear, clearscreen | '
    )
    print(
        '|help    || arguments: help                || prints out the command list                  || aliases: ?, '
        'commands        | '
    )
    print(
        '|                                                                                                            '
        '             | '
    )
    print(
        '\_________________________________________________________________________________________________________________________/ '
    )


def end():
    confirm = input(
        "Are you sure you want to end the current session? Y/N "
    )
    if confirm == 'Y' or confirm == 'y':
        print(
            "CMD 'sessionend' called. Confirmation true. Terminating session."
        )
        enddice = True
        time.sleep(2)

    elif confirm == 'N' or confirm == 'n':
        print(
            "CMD 'sessionend' called. Confirmation false. Session termination cancled."
        )
        enddice = False
        time.sleep(2)
