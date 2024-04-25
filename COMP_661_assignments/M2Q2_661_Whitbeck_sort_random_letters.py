# -*- coding: utf-8 -*-
"""
Author: Kendall Whitbeck
Student ID: 5550203278
Assignment: Module 2, Question 2
Description:
    This program creates a list of 10 random letters, sorts the list, and gets unique values.

"""

import os  # os.system('cls'): clear terminal window text in Windows OS
import random

def random_letters():
    """Return list of 10 random letters in the range 'a' to 'z'.

    """
    letters = []
    for i in range(10):
        # random.randint(a, b) returns a random integer N such that a <= N <= b.
        # integers in the range 97 to 122 (inclusive) represent the ASCII codes for lowercase letters 'a' to 'z', respectively.
        # chr(int) converts an integer to a character.
        # letters.append() adds the next randomly-generated letter to the end of the list.
        letters.append(chr(random.randint(97, 122)))
    return letters

def sort_asc(letters):
    """Return ascending sorted list.

    """
    letters.sort()
    return letters

def sort_desc(letters):
    """Return descending sorted list.

    """
    letters.sort(reverse=True)
    return letters

def sort_unique(letters):
    """Return unique sorted list.

    """
    # Use set() to get unique values then convert back to list.
    letters = list(set(letters))
    letters.sort()
    return letters

def main():
    # Clear terminal window text in Windows OS
    os.system('cls')

    # Match console output with expected results
    test_run = True

    # Generate and print list of letters.
    if test_run:
        # Use list of letters from problem statement to compare console output with expected results.
        letters = ['e', 'h', 'f', 'h', 'j', 'b', 'j', 'b', 'a', 'c']
    else:
        # Randomly generate list of letters.
        letters = random_letters()
    print("Random Letters")
    print(letters)

    # Sort the list in ascending order
    print("Sort the list in ascending order.")
    print(sort_asc(letters))

    # Sort the list in descending order
    print("Sort the list in descending order.")
    print(sort_desc(letters))

    # Get the unique values and sort them in ascending order
    print("Unique values sorted in ascending order.")
    print(sort_unique(letters))


# Ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file)
if __name__ == "__main__":
    main()