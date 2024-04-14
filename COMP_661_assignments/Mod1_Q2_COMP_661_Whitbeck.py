# -*- coding: utf-8 -*-
"""
Author: Kendall Whitbeck
Student ID: 5550203278
Assignment: Module 1, Question 2
Description: This program accepts a name and a birth date and displays the person's birthday,
the current day, the person's age, and the number of days until the person's next birthday.
"""

import os  # os.system('cls'): clear terminal window text in Windows OS
from datetime import datetime

def calculate_birthday(test_level=0):
    """Displays a person's birthday, the current day, the person's age, and the number of
    days until the person's next birthday given their birthday and name.

    Parameters:
        test_level (int):
            If 0 or unspecified, run the program in interactive mode with dynamic current_day.
            If 1, run the program in interactive mode with hard-coded current_day.
            If 2, run the program in iterative test mode (no user input).
    """
    # Collect inputs
    if test_level == 2:
        # Hard-coded test inputs to save time on iterative testing
        name_str = "Alison"  # Enter name
        birthday_str = "03/03/18"  # Enter birthday (MM/DD/YY)
        print(f"Enter name: {name_str}")
        print(f"Enter birthday (MM/DD/YY): {birthday_str}")
    else:
        name_str = input("Enter name: ")
        birthday_str = input("Enter birthday (MM/DD/YY): ")

    # Calculate birthday and current day.
    birthday = datetime.strptime(birthday_str, "%m/%d/%y")
    if test_level == 1:
        # Hard-coded current_day to match expected output
        current_day = datetime(2020, 3, 1)
    else:
        current_day = datetime.now()

    # Calculate age:
    # If the current month and day is before the birth month and day,
    # then subtract 1 from age since that birthday has not happened yet.
    age = current_day.year - birthday.year - ((current_day.month, current_day.day) < (birthday.month, birthday.day))
    # If age is less than 2 years old, calculate age in days.
    if age < 2:
        age_days = (current_day - birthday).days - 1  # subtract 1 to interpret birthday as 0 days old

    # Calculate number of days until next birthday
    next_birthday = birthday.replace(year=current_day.year)
    days_until_birthday = (next_birthday - current_day).days
    if next_birthday < current_day:  # if birthday has already passed this year
        next_birthday = next_birthday.replace(year=next_birthday.year + 1)  # increment year by 1
        days_until_birthday = (next_birthday - current_day).days - 1  # subtract 1 to exclude current day from count

    # Display birthday, current day, age, and number of days until next birthday
    print(f"Birthday:  {birthday.strftime('%A, %B %d, %Y')}")
    print(f"Today:     {current_day.strftime('%A, %B %d, %Y')}")
    if age >= 2:
        # If age is 2 or more years old, display age in years.
        print(f"{name_str} is {age} years old.")
    else:
        # If age is less than 2 years old, display age in days.
        print(f"{name_str} is {age_days} days old.")

    # Display number of days until next birthday colloquially for near birthdays and in number of days for distant birthdays.
    if days_until_birthday == 0:
        print(f"{name_str}'s birthday is today!")
    elif days_until_birthday == 1:
        print(f"{name_str}'s birthday is tomorrow!")
    elif days_until_birthday == 364:  # does not account for leap year
        print(f"{name_str}'s birthday was yesterday!")
    else:
        print(f"{name_str}'s birthday is in {days_until_birthday} days.")

def main():
    # Clear terminal window text in Windows OS
    os.system('cls')

    # Continuously prompt user for user's name and birthday until they choose to exit
    print("Birthday Calculator")
    while True:
        calculate_birthday(test_level=1) # NOTE set test_level according to function definition
        if input("\nContinue? (y/n): ").lower() != 'y':
            break
        print("")
    print("\nBye!")

# Ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file)
if __name__ == "__main__":
    main()