"""
Author: Kendall Whitbeck
Student ID: 5550203278
Assignment: Module 2 Question 3
Description: This program calculates and prints various conversions of a user-input weight.
"""

# Assigns mass in lbs from user input
mass_lbs = float(input("Please enter the mass in lb that you would like to convert to kg: "))

# Converts lbs to kg
mass_kg = mass_lbs / 2.20462
print("The converted mass in kg is:", mass_kg)

# Converts kg to Earth weight in Newtons
weight_earth_newtons = mass_kg * 9.807
print("Your weight on Earth is:", weight_earth_newtons, "Newtons")

# Converts kg to Moon weight in Newtons
weight_moon_newtons = mass_kg * 1.62 
print("Your weight on the Moon is:", weight_moon_newtons, "Newtons")

# Calculates ratio of Moon weight to Earth weight as percentage
weight_ratio_moon_earth = weight_moon_newtons / weight_earth_newtons * 100
print("The percentage of the weight on the Moon in comparison to what is experienced on Earth:", weight_ratio_moon_earth, "%")

# Calculates ratio of Moon weight to Earth weight as percentage
int_weight_ratio_moon_earth = round(weight_ratio_moon_earth)
print("The percentage of the weight on the Moon in comparison to what is experienced on Earth as an integer is", int_weight_ratio_moon_earth, "%")