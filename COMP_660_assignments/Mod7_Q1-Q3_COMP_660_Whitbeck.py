# -*- coding: utf-8 -*-
"""
Author: Kendall Whitbeck
Student ID: 5550203278
Assignment: Module 7: Question(s) 1-3
Description: This program answers the assigment questions specified above, exploring the use of string formatting and decimal objects.
"""

import os  # os.system('cls'): clear terminal window text in Windows OS
import math  # Tau
import decimal # decimal object
import scipy.constants  # R (molar gas constant)

# Mod 7, Question 1
def print_tau():
    """
    Print the value of Tau and half the value of Tau.

    This function prints the value of Tau (τ) and half the value of Tau.
    The values are printed with a center-aligned width of 8 characters and a precision of 6 and 4 decimal places, respectively.
    """

    # fill available field width w/ decimal precision
    print(f"The value of Tau is {math.tau:^8.6f}, which is two times {math.tau/2:^8.6f}.")

    # demonstrate center alignment by using fewer decimal points than field width
    print(f"The value of Tau is {math.tau:^8.4f}, which is two times {math.tau/2:^8.4f}.")

# Mod 7, Question 2
def integer_byte_range(num_bytes):
    """
    Calculate the signed range of integers based on the number of bytes.

    Parameters:
    num_bytes (int): The number of bytes used to represent the integer type.

    This function calculates the unsigned and signed range of integers that can be represented using the specified number of bytes.
    It prints the range of integers based on the given number of bytes.
    """

    # formula determining total number of values that can be encoded by a given number of bytes
    unsigned_max =  int(2 ** (num_bytes * 8))

    # for signed integers, 0 is the first value so the max range (positive) will be 1 lower than half the unsigned max
    signed_max = int(unsigned_max / 2 - 1)

    # for signed integers, the min range (negative) will be the negation of half the unsigned max
    signed_min = int(-signed_max - 1)

    # print possible value range for integer w/ given # Bytes using comma-separated 1000s format
    print(f"{num_bytes} Byte(s) integral type with 8 bits can encode {unsigned_max:,} numbers. The signed range will be from {signed_min:,} to {signed_max:,}")

# Mod 7, Question 3
def gas_rms_velocity(temperature_celsius, molar_mass_kg_per_mol):
    """
    Calculate the root mean square (RMS) velocity of gas molecules.

    Parameters:
    temperature_celsius (int): The temperature in Celsius.
    molar_mass_kg_per_mol (float): The molar mass of the gas in kilograms per mole.

    This function calculates the RMS velocity of gas molecules at the given temperature and molar mass.
    It uses the ideal gas constant and the provided molar mass to perform the calculation.
    The result is quantized to match the format '1.000' and printed as the average velocity in meters per second.
    """

    # Convert temperature in Celsius to Kelvin
    temperature_kelvin = temperature_celsius + 273.15

    # Assign variable values as Decimal objects
    R = decimal.Decimal(scipy.constants.gas_constant)
    T = decimal.Decimal(temperature_kelvin)
    M = decimal.Decimal(molar_mass_kg_per_mol)

    # Use decmial module to calculate RMS Velocity and quantize the result to match format '1.000'
    rms_velocity = (3 * R * T / M).sqrt().quantize(decimal.Decimal('1.000'))

    # Print RMS Velocity in m/sec of a molecule in a sample of Oxygen along with temperature in Celsius
    print(f"The average velocity or root mean square velocity of a molecule in a sample of oxygen")
    print(f"at {temperature_celsius} degrees Celsius is {rms_velocity} m/sec")

def main():
    # Clear terminal window text in Windows OS
    os.system('cls')

    # Demonstrate completion of Module 7, Question 1
    print("Q1. Print Tau:")
    print_tau()

    # Demonstrate completion of Module 7, Question 2
    print("\nQ2. Integer Byte Range:")
    num_bytes = int(input("Enter number of Bytes you would like to determine the signed range of: "))
    integer_byte_range(num_bytes)

    # Demonstrate completion of Module 7, Question 3
    print("\nQ3. Gas Molecule RMS Velocity:")
    temperature_celsius = 25
    molar_mass_oxygen_kg_per_mol = 3.2e-2
    gas_rms_velocity(temperature_celsius, molar_mass_oxygen_kg_per_mol)

# Ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file)
if __name__ == "__main__":
    main()