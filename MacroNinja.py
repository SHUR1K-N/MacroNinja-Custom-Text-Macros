import keyboard; import time
import re; import os


macrosSoft = {}
macrosHard = {}

softModifier = "ctrl"
hardModifier = "ctrl + alt"


def macroMatch(self):
    for entryKey in chosenDict:
        if self.name == entryKey:
            keyboard.write(chosenDict[entryKey])
    keyboard.unhook_all()


def macroGuide():
    print(f"{'Soft Macros':^20}\n")
    for keyS, valueS in macrosSoft.items():
        print(f"CTRL + {keyS:-<5}|{valueS}")
    print(f"\n{'Hard Macros':^20}\n")
    for keyH, valueH in macrosHard.items():
        print(f"CTRL + ALT + {keyH:-<5}|{valueH}")


######################### Main #########################

if __name__ == "__main__":

    with open("Soft Macros.cfg", "r") as file:
        tempString = file.read()
        tempListSoft = re.findall(r"~+[0-9]+\.\s(.+)", tempString)
        for index, element in enumerate(tempListSoft):
            if tempListSoft[index] == "none":
                tempListSoft[index] = ""

    with open("Hard Macros.cfg", "r") as file:
        tempString = file.read()
        tempListHard = re.findall(r"~+[0-9]+\.\s(.+)", tempString)
        for index, element in enumerate(tempListHard):
            if tempListHard[index] == "none":
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
            keyboard.on_release(macroMatch)
        if keyboard.is_pressed(hardModifier):
            chosenDict = macrosHard
            keyboard.on_release(macroMatch)
        time.sleep(0.0001)
