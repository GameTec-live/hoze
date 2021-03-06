import os
import tkinter as tk
from blocks import map
from textlib import banner, colored
import sys

line_offset = 3
world = ""
def change_value(value, file, item, index):
    item = item + line_offset
    with open(file, 'r') as f:
        lines = f.readlines()

    line = lines[item]
    array = line.split(",")
    array[index] = str(value)
    lines[item] = ",".join(array)

    with open(file, 'w') as f:
        f.writelines(lines)

def valid_invalid(value, file, item, index):
    with open(file, 'r') as f:
        lines = f.readlines()

    line = lines[item]
    array = line.split(",")
    array[index] = str(value)
    lines[item] = ",".join(array)

    with open(file, 'w') as f:
        f.writelines(lines)



def get_line(file, item):
    item = item + line_offset
    with open(file, 'r') as f:
        lines = f.readlines()
    return lines[item]

def readfile(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            array = line.split(",")
            try:
                print(colored(0, 255, 0, map[array[0]] + ": " + array[0]))
            except KeyError:
                print(colored(255, 0, 0, "not defined. refer to dictionary... (id: " + array[0] + ")"))

print(banner)
print(colored(0, 255, 0, "Welcome to hoze! \nA opensource hackable map editor for Zeepkist. \nUse help for help"))


while True:
    command = input(colored(214, 40, 0, "hoze#"))
    command = command.split(" ")
    if command[0] == "help":
        print(colored(0, 255, 0, "help: show this message"))
        print(colored(0, 255, 0, "exit: exit the program"))
        print(colored(0, 255, 0, "load: load the map"))
        print(colored(0, 255, 0, "set: set a value"))
        print(colored(0, 255, 0, "get: get a value"))
        print(colored(0, 255, 0, "list: list all values"))
        print(colored(0, 255, 0, "dict: show the dictionary of what name is what id"))
        print(colored(0, 255, 0, "validate: validate the map"))
        print(colored(0, 255, 0, "invalidate: invalidate the map"))
        print(colored(0, 255, 0, "settime: set the time needed for each medal"))
        print(colored(0, 255, 0, "setspeed: set the speed of an item... fan, booster, etc"))
        print(colored(0, 255, 0, "loadlive: load live from the games folder"))
        print(colored(0, 255, 0, "listlive: list all maps in the games folder"))
        print(colored(0, 255, 0, "sethelp"))
        print(colored(230, 120, 10, "remember! Computers count from 0, not 1"))
    if command[0] == "exit":
        exit(colored(0, 255, 0, "exiting..."))
    if command[0] == "load":
        if len(command) == 2:
            map_file = command[1]
            if os.path.isfile(map_file):
                print(colored(0, 255, 0, "loading map..."))
                world = command[1]
            else:
                print(colored(255, 0, 0, "map not found"))
        else:
            print(colored(255, 0, 0, "Map file not specified"))
    if command[0] == "set":
        if len(command) == 4:
            if world != "":
                change_value(command[1], world, int(command[2]), int(command[3]))
            else:
                print(colored(255, 0, 0, "No map loaded"))
        else:
            print(colored(255, 0, 0, "Not enough arguments, expected: new value, item, index"))
    if command[0] == "get":
        if len(command) == 2:
            if world != "":
                print(colored(0, 255, 0, get_line(world, int(command[1]))))
            else:
                print(colored(255, 0, 0, "No map loaded"))
        else:
            print(colored(255, 0, 0, "Not enough arguments, expected: item"))

    if command[0] == "list":
        if world != "":
            print(colored(0, 255, 0, "reading map..."))
            readfile(world)

    if command[0] == "dict":
        print(colored(0, 255, 0, "dictionary:"))
        for key in map:
            print(colored(0, 255, 0, key + ": " + map[key]))

    if command[0] == "validate":
        if world != "":
            print(colored(0, 255, 0, "validating map..."))
            valid_invalid(3, world, 2, 0)
            print(colored(0, 255, 0, "map validated"))
        else:
            print(colored(255, 0, 0, "No map loaded"))

    if command[0] == "invalidate":
        if world != "":
            print(colored(0, 255, 0, "invalidating map..."))
            valid_invalid("invalid track", world, 2, 0)
            print(colored(0, 255, 0, "map invalidated"))

    if command[0] == "settime":
        if len(command) == 3:
            if world != "":
                print(colored(0, 255, 0, "setting times..."))
                with open(world, 'r') as f:
                    lines = f.readlines()
                line = lines[2]
                array = line.split(",")
                array[1] = str("%.2f" % float(command[1]))
                array[2] = str("%.2f" % float(command[2]))
                array[3] = str("%.2f" % float(command[3]))
                lines[2] = ",".join(array)

                with open(world, 'w') as f:
                    f.writelines(lines)

            else:
                print(colored(255, 0, 0, "No map loaded"))
        else:
            print(colored(255, 0, 0, "Not enough arguments, expected: time, time, time"))

    if command[0] == "setspeed":
        if len(command) == 3:
            if world != "":
                print(colored(0, 255, 0, "setting speed..."))
                change_value(command[1], world, int(command[2]), 36)
            else:
                print(colored(255, 0, 0, "No map loaded"))
        else:
            print(colored(255, 0, 0, "Not enough arguments, expected: speed, item"))
    if command[0] == "loadlive":
        if len(command) == 2:
            map_file = os.getenv('APPDATA') + "\\Zeepkist\\Levels\\" + command[1].strip(".zeeplevel") + "\\" + command[1]
            if os.path.isfile(map_file):
                print(colored(0, 255, 0, "loading map..."))
                world = os.getenv('APPDATA') + "\\Zeepkist\\Levels\\" + command[1].strip(".zeeplevel") + "\\" + command[1]
            else:
                print(colored(255, 0, 0, "map not found"))
        else:
            print(colored(255, 0, 0, "Map file not specified"))
    if command[0] == "listlive":
        print(colored(0, 255, 0, "listing maps..."))
        for file in os.listdir(os.getenv('APPDATA') + "\\Zeepkist\\Levels\\"):
            print(colored(0, 255, 0, file + ".zeeplevel"))

    if command[0] == "sethelp":
        print(colored(0, 255, 0, "set help message:"))
        print(colored(0, 255, 0, """
        index:    0     1  2  3  4   5   6   7       8       9       10                            11             12             13                             14                               15                              16                                                              27            28                    29                                       36
        line:     1,    0, 0, 0, 0,  0,  0,  1,      1,      1,      0,                            5,             10,            24,                            30,                              24,                             30,                               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,            1,                    1,                     0, 0, 0, 0, 0, 0, 0,            0 
        function: type, x, y, z, rx, ry, rz, scalex, scaley, scalez, road lower barriers material, road material, ramp material, left barrier primary material, left barrier secondary material, right barrier primary material, right barrier secondary material, u, u, u, u, u, u, u, u, u, u, road visible, left barrier visible, right barrier visible, u, u, u, u, u, u, adjustvalue, u,
        """))