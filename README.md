## [![python logo](https://www.python.org/static/img/python-logo.png)](python.org)

## **Starting out:**
(This docuentation will refer to using Windows Command Prompt(cmd) or PowerShell(Shell), but the same steps should be able to be followed in Linux Terminal. You might not be able to follow through on Mac though.)
### **Pre-run changes & Installation**
Before running the program, you'll need to install Python 3.8, do so from https://www.python.org/downloads/, you'll also want to install `pytz`, then set your timezone in `options.json`(choose from one of the timezones in `timezones.txt`).

If anything occurrs such as an error just after running `main.py`, a debug log will be created in the root directory(`debug.log`). 

### **Installing `pytz`**
Installing `pytz` is required to be able to show current time/date, if PowerShell can't find the module, the program will error out. 

To install `pytz`, copy the following Shell command and paste it (`[ctrl + shift + v]`) into Powershell

### **Command Prompt install command for `pytz`:** 
`pip install pytz`

---
## **Running the program**
## [![cmd icon](https://raw.githubusercontent.com/microsoft/terminal/main/res/terminal/images/StoreLogo.scale-200.png)](https://en.wikipedia.org/wiki/Cmd.exe)
Open CMD, navigate to the directory of the downloaded files after extracting using WinRar, 7Zip, or Window's default extractor(you'll have to find the install directory and navigate to it manually, you can find instructions on how to do so here https://www.lifewire.com/change-directories-in-command-prompt-5185508).
Once you've navigated to the folder containing the files, run `main.py` using `Python main.py`


# How to use:

You will get prompted to choose an option, currently there is only one option:

    dice
More will be added in the future, and updated versions can be downloaded here onx Github.

## Prompts:
### **Dice**
If you choose "dice" as the initial input prompt, the following will explain how to use

#### What this does:
This program is a dice roller, allowing for multiple dice, such as 7 d10s, including the ability of custom dice types, such as 10 d7s.

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
