import os, json, platform
def load(file):
    # Handles options
    # Opening JSON file
    options = file
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
    debug1 = verify[1].strip(',')
    if debug1.lower() == 'true':
        debug = True
    tz = verify[5].strip(',')
    system = str(platform.uname())
    print('Device debug information. Will clear in 5 seconds')
    if debug:
        print('Debug options enabled. OS Details:')
        system = str(platform.uname())
        split1 = system.split()
        split2 = split1[0].split("'")
        print(system)