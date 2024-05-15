# -*- coding: utf-8 -*-
"""
Author: Kendall Whitbeck
San Diego College of Continuing Education (SDCCE) Student ID: 5550203278
COMP 661: Programming with Python II
Assignment: Module 5
Description: This program keeps track of the inventory of items that a wizard can carry.
Specifications:
 This program should read the text file named wizard_all_items.txt that contains all the items a wizard can carry. When the user selects the walk command, the program should randomly pick one of the items that were read from the text file and give the user the option to grab it.
 The current items that the wizard is carrying should be saved in an inventory file. Make sure to update this file every time the user grabs or drops an item.
 The wizard can only carry four items at a time. For the drop command, display an error message if the user enters an invalid integer or an integer that doesn't correspond with an item.
 Handle all exceptions that might occur so that the user can't cause the program to crash. If the wizard_all_items.txt file is missing, display an appropriate error message and exit the program.
 If the inventory file is missing, display an appropriate error message and continue with an empty inventory for the user. That way, the program will write a new inventory file when the user adds items to the inventory.

"""

import random

ITEMS_FILENAME = "wizard_all_items.txt"
INVENTORY_FILENAME = "wizard_inventory.txt"

def read_items():
    items = []
    try:
        with open(ITEMS_FILENAME) as file:
            for line in file:
                line = line.strip()  # NOTE: Use strip() instead of replace("\n", "")
                items.append(line)
    except FileNotFoundError as e:
        print("Could not find items file.")
        print("Exiting program. Bye!")
        # exit()
        raise SystemExit  # TODO: try this
    return items

def read_inventory():
    inventory = []
    try:
        with open(INVENTORY_FILENAME) as file:
            for line in file:
                line = line.strip()  # NOTE: Use strip() instead of replace("\n", "")
                inventory.append(line)
    except FileNotFoundError as e:
        with open(INVENTORY_FILENAME, "w+") as file:
            print("Could not find inventory file!")
            print("Wizard is starting with no inventory.\n")
    return inventory

def write_inventory(inventory):
    with open(INVENTORY_FILENAME, "w") as file:
        for item in inventory:
            file.write(item + "\n")

def display_title():
    print("The Wizard Inventory program")
    print()

def display_menu():
    print("COMMAND MENU")
    print("walk - Walk down the path")
    print("show - Show all items")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()

def walk(inventory):
    items = read_items()
    item = random.choice(items)
    print("While walking down a path, you see " + item + ".")
    choice = input("Do you want to grab it? (y/n): ").strip().lower()  # NOTE: Remove leading/trailing whitespace & convert to lowercase for obvious typos
    if choice == "y":
        if len(inventory) >= 4:
            print("You can't carry any more items. " +
                  "Drop something first.\n")
        else:
            inventory.append(item)
            print("You picked up " + item + ".\n")
            write_inventory(inventory)

def show(inventory):
    for i in range(len(inventory)):
        item = inventory[i]
        number = i + 1
        print(str(number) + ". " + item)
    print()

def drop_item(inventory):
    try:
        number = int(input("Number: "))
        if number < 1 or number > len(inventory):
            print("Invalid item number.\n")
        else:
            item = inventory.pop(number-1)
            print("You dropped " + item + ".\n")
            write_inventory(inventory)
    except ValueError as e:
        print("Invalid item number.\n")

def main():
    display_title()
    read_items()  # NOTE: check if items file exists before starting program loop
    display_menu()

    inventory = read_inventory()
    # Enter program loop.
    while True:
        command = input("Command: ").strip().lower()  # NOTE: Remove leading/trailing whitespace & convert to lowercase for obvious typos
        if command == "walk":
            walk(inventory)
        elif command == "show":
            show(inventory)
        elif command == "drop":
            drop_item(inventory)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
