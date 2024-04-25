# -*- coding: utf-8 -*-
"""
Author: Kendall Whitbeck
San Diego College of Continuing Education (SDCCE) Student ID: 5550203278
COMP 661: Programming with Python II
Assignment: Module 2, Question 3
Description:
    This program creates a contacts manager the user can use to manage the primary email address and phone number for a contact.
    a. Use a multi-dimensional list to store the data for the contacts. Provide starting data for two or more contacts.
    b. For the view and del commands, display an error message if the user enters an invalid contact number.
    c. When you exit the program, all changes that you made to the contact list are lost.
    An example of a contacts list:
        contacts = [
            [1, "Marilyn Monroe", "MarilynMonroe@hollywood.com", "+1 234 567 8901"],
            [2, "Abraham Lincoln", "AbrahamLincoln@whitehouse.org", "+22 33 4567 4587"]
        ]

"""

import os  # os.system('cls'): clear terminal window text in Windows OS

def display_commands():
    """Display the command menu.

    """
    print("COMMAND MENU\n"
          "list - Display all contacts\n"
          "view - View a contact\n"
          "add  - Add a contact\n"
          "del  - Delete a contact\n"
          "exit - Exit program")

def list_contacts(contacts):
    """ Display the number and name of all contacts.

    """
    for contact in contacts:
        print(f"{contact[0]}. {contact[1]}")

def view_contact(contacts):
    """Prompt user for contact number and display the contact's name, email and phone.

    """
    contact_number = int(input("Number: "))  # Get contact number from user as integer
    valid_numbers = [contact[0] for contact in contacts]  # Extract valid contact numbers as list
    # Check if input contact number is invalid
    if contact_number not in valid_numbers:
        print("Error: Invalid contact number.")
        return
    else:
        # Print contact information accoring to number
        contact = contacts[contact_number - 1]  # Account for indexing starting at 0 and list of numbers starting at 1
        print(f"Name: {contact[1]}\n"
              f"Email: {contact[2]}\n"
              f"Phone: {contact[3]}"
        )

def add_contact(contacts):
    """ Add a new contact to the contacts list.

    """
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")

    # Add new contact to end of contacts list
    contacts.append([len(contacts) + 1, name, email, phone])  # increment contact number by 1 to account for new contact
    print(f"{name} was added.")

def delete_contact(contacts):
    """ Delete a contact from the contacts list based on the contact number provided by the user.

    """
    contact_number = int(input("Number: "))  # Get contact number from user as integer.
    valid_numbers = [contact[0] for contact in contacts]  # Extract valid contact numbers as list.
    # Check if input contact number is invalid.
    if contact_number not in valid_numbers:
        print("Error: Invalid contact number.")
        return
    else:
        # Delete contact from contacts list and update contact numbers.
        index = contact_number - 1  # Convert number in contacts list to Python-friendly, 0-based index.
        name = contacts[index][1]

        # If not the last contact in the list.
        if len(contacts) > contact_number:
            # Decrement subsequent numbers in contacts list by 1 to account for removal of contact.
            for x in range(index + 1, len(contacts)):
                contacts[x][0] -= 1

        # Delete the specified contact from the contacts list.
        contacts.pop(index)  # Use pop since contact number was converted to index.
        print(f"{name} was deleted.")

def main():
    """ Run the contact manager program.

    """
    # Clear terminal window text in Windows OS.
    os.system('cls')

    # Start contact manager program.
    print("Contact Manager\n")
    display_commands()

    # Populate multi-dimensional list of contacts with default values for number, name, email and phone (in that order).
    # By populating the list with starting data, all changes made to the list will be lost when the program exits.
    contacts = [
        [1, "Marilyn Monroe", "MarilynMonroe@hollywood.com", "+1 234 567 8901"],
        [2, "Abraham Lincoln", "AbrahamLincoln@whitehouse.org", "+22 33 4567 4587"]
    ]

    # Enter user-input loop.
    while True:
        command = input("\nCommand: ").lower()  # prompt user for command
        if command == "list":
            list_contacts(contacts)
        elif command == "view":
            view_contact(contacts)
        elif command == "add":
            add_contact(contacts)
        elif command == "del":
            delete_contact(contacts)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Invalid command. Please try again.")

# Ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file)
if __name__ == "__main__":
    main()
