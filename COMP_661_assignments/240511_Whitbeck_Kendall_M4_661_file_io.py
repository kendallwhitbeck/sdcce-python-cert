# -*- coding: utf-8 -*-
"""
Author: Kendall Whitbeck
San Diego College of Continuing Education (SDCCE) Student ID: 5550203278
COMP 661: Programming with Python II
Assignment: Module 4, Questions 1-6
Description: This program exercises the use of file I/O.
"""

import os  # os.system('cls'): clear terminal window text in Windows OS.

def file_count_lines(filename):
    """ Count the number of lines in the file. """

    with open(filename) as fp:
        print(f"There are {len(fp.readlines())} lines in '{filename}'.")

def file_count_5_letter_words(filename):
    """ Count the number of 5-letter words in the file. """
    count = 0
    with open(filename) as fp:
        for line in fp:
            words = line.split()
            for word in words:
                if len(word) == 5:
                    count += 1
    print(f"There are {count} five-letter words in '{filename}'.")

def print_cwd_contents():
    """ Print the contents of the current working directory. """
    print(f"The current working directory is: {os.getcwd()}")
    print(f"The contents of the current working directory are:")
    for item in os.listdir():
        print("    " + item)

def print_user_file():
    """ Print the contents of a user-specified file. """
    try:
        filename = input("Enter path to file: ")
        with open(filename) as fp:
            print(fp.read())
    except FileNotFoundError:
        print(f"ERROR: file not found: '{filename}'")

def update_accounts():
    """ Update accounts.txt file as follows:
            - update the name 'Zoltar' to 'Robert'
            - create a tempfile with the new data
            - remove accounts.txt file from the directory
            - rename the tempfile to a new file called myaccounts.txt

    """
    try:
        accounts_file = "../data/accounts.txt"
        with open(accounts_file) as fp:
            # Update the name 'Zoltar' to 'Robert'.
            data = fp.read().replace("Zoltar", "Robert")

            # Create a tempfile with the new data.
            tempfile = "../data/tempfile.txt"
            with open(tempfile, mode="w+") as fp2:
                fp2.write(data)

        # Remove accounts.txt file from the directory.
        os.remove(accounts_file)

        # Rename the tempfile to a new file called myaccounts.txt.
        os.rename(tempfile, "../data/myaccounts.txt")

    except FileNotFoundError:
        print(f"ERROR: file not found: '{accounts_file}'")
        print(f" |---> Most likely, you did not recreate the accounts.txt file after the last time running this program.")

    except FileExistsError:
        print(f"ERROR: file already exists: '{tempfile}'")
        print(f" |---> Most likely, you did not remove the myaccounts.txt file after the last time running this program.")

def main():
    # Clear terminal window text if in Windows OS.
    if os.name == 'nt':
        os.system('cls')

    # Set path to file.
    filename = "../data/file.txt"

    # Count the number of lines in the file.
    file_count_lines(filename)

    # Count the number of 5-letter words in the file.
    file_count_5_letter_words(filename)

    # Print the contents of the current working directory.
    print_cwd_contents()

    # Print the contents of a user-specified file.
    print_user_file()

    # Update accounts.txt file.
    update_accounts()

# Ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file)
if __name__ == "__main__":
    main()