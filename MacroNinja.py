import keyboard; import time
from termcolor import colored
from colorama import init
import re; import os

init() # Initilizing colors

macrosSoft = {}
macrosHard = {}

# Available modifiers: ALT, CTRL, SHIFT, WINDOWS
softModifier = "CTRL"
hardModifier = "CTRL + ALT"


def macroMatch(self):
    for entryKey in chosenDict:
        if self.name == entryKey:
            keyboard.write(chosenDict[entryKey])
    keyboard.unhook_all()


def macroGuide():
    print(colored(f"\n{'Soft Macros':^20}\n", "green"))
    for keyS, valueS in macrosSoft.items():
        print(colored(f"{softModifier} + {keyS:-<5}{valueS}", "green"))
    print(colored(f"\n{'Hard Macros':^20}\n", "red"))
    for keyH, valueH in macrosHard.items():
        print(colored(f"{hardModifier} + {keyH:-<5}{valueH}", "red"))


######################### Main #########################

if __name__ == "__main__":

    init()

    with open("Soft Macros.cfg", "r") as file:
        tempString = file.read()
        tempListSoft = re.findall(r"~+[0-9]+\.\s(.+)", tempString)
        for index, element in enumerate(tempListSoft):
            if tempListSoft[index] == "empty":
                tempListSoft[index] = ""

    with open("Hard Macros.cfg", "r") as file:
        tempString = file.read()
        tempListHard = re.findall(r"~+[0-9]+\.\s(.+)", tempString)
        for index, element in enumerate(tempListHard):
            if tempListHard[index] == "empty":
                tempListHard[index] = ""

    for index, element in enumerate(tempListSoft, start=1):
        if index != 10:
            macrosSoft[str(index)] = element
        else:
            macrosSoft["0"] = element

    for index, element in enumerate(tempListHard, start=1):
        if index != 10:
            macrosHard[f"{str(index)}"] = element
        else:
            macrosHard["0"] = element

    macroGuide()

    while True:
        if keyboard.is_pressed(softModifier):
            chosenDict = macrosSoft
            keyboard.on_press(macroMatch)
        if keyboard.is_pressed(hardModifier):
            chosenDict = macrosHard
            keyboard.on_press(macroMatch)
        time.sleep(0.0001)
