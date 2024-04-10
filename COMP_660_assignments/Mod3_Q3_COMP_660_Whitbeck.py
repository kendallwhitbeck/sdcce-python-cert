"""
Author: Kendall Whitbeck
Student ID: 5550203278
Assignment: Module 3 Question 3
Description: This program recommends the user what to wear based on the user-input temperature.
"""

print("What shall I wear today?\n")

first_name = input("Please Enter Your First Name: ")
temperature = float(input("What is Today's Temperature: "))

if temperature < 70:
    print("\nHi", first_name, ", You should probably bring a sweater")
else:
    print("\nHi", first_name, ", It will be a warm day , T-shirt time!")
