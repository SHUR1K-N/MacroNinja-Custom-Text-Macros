import keyboard; import time
import re; import os


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


######################### Main #########################

if __name__ == "__main__":

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

    while True:
        if keyboard.is_pressed(softModifier):
            chosenDict = macrosSoft
            keyboard.on_press(macroMatch)
        if keyboard.is_pressed(hardModifier):
            chosenDict = macrosHard
            keyboard.on_press(macroMatch)
        time.sleep(0.0001)
