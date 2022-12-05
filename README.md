[![python logo](https://www.python.org/static/img/python-logo.png)](https://python.org)

# **Starting out:**
You'll need the latest version of JetBrains PyCharm or another IDE suitable for Python3 installed, and you must have the
link to this repository, because you will need to clone it in the IDE.
## **Downloading:**
[![pycharm banner](https://i1.wp.com/www.webprecious.com/wp-content/uploads/2019/09/Pycharm.png?fit=1350%2C500&ssl=1)](https://www.jetbrains.com/pycharm/download/)
#### On Ubuntu
Open the Terminal, then run `sudo snap install pycharm-community --classic` to install PyCharm via Snap
#### On Windows
Click on the "PyCharm" banner, then click on the black "Download" button to initiate the download. You should be able to
run the .exe file that downloaded.
### **Pre-run changes & Installation**
Before running the program, you'll need to install Python 3.8, do so from https://www.python.org/downloads/, you'll also
want to install `pytz`, then set your timezone in `options.json`(choose from one of the timezones in `timezones.txt`).

If anything occurs such as an error just after running `main.py`, a debug log will be created in the root directory
(`debug.log`). 

### **Installing `pytz`**
Install pytz my opening the PyCharm Package Manager, search `pytz`, then click install for `pytz 2022.6`

---
## **Running the program**
Thanks to PyCharm, it's simple, just press [Alt]+[Shift]+[F10]


# How to use:

You will get prompted to choose an option, currently there is only one option:

    dice
More will be added in the future, and updated versions can be downloaded here onx GitHub.

## Prompts:
### **Dice**
If you choose "dice" as the initial input prompt, the following will explain how to use

#### What this does:
This program is a dice roller, allowing for multiple dice, such as 7 d10s, including the ability of custom dice types, 
such as 10 d7s.

#### Commands

    .__________________________________________________________________________________________.
    |                                               Commands list                              |
    |                                                                                          |
    |roll    || arguments: roll <amt> <type>   || Rolls dice based on the included arguments   |
    |end     || arguments: end                 || use: Ends the program                        |
    |cls     || arguments: cls                 || use: Clears the screen                       |
    |help    || arguments: help                || prints out the command list                  |
    |                                                                                          |
    \_________________________________________________________________________________________/

#### Commands (In Depth)

roll:  
Used to roll the amount and type of custom dice that you want. How to use: roll `<amt>` `<type>` 
    Example: `roll 3 d20`, `roll 5 d17`
    
end:  
Used to end the program instead of ^C. How to use: `end`  

help: 
        
Used to open the commands index so that you can view possible commands and args. How to use: `help` , `?` , `commands`

cls:

Used to clear the screen. 
How to use: `cls`
