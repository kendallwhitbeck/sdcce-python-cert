# -*- coding: utf-8 -*-
"""
Author: Kendall Whitbeck
Student ID: 5550203278
Assignment: Module 5, Questions: 2, 3, 5, 6, 7, 8
Description: This program answers the assigment questions specified above. Answers can be identified by respective "Q<#>:" comments.
"""
import math # math.pi constant (Q6, Q7)

# Q2: Write a recursive function for calculating factorial of n ("n!")
def factorial(n):
    # Round n to integer
    if not (isinstance(n, int)):
        n = int(round(float(n)))
        print(f"Q2 WARNING: value `n` was rounded to n={n}")
    # Check if n is negative, which is not allowed for factorials
    if n < 0:
        return "Factorial is not defined for negative numbers"
    # Base case: factorial of 0 is 1
    elif n == 0:
        return 1
    # Recursive case: factorial of n is n multiplied by factorial of n-1
    else:
        return n * factorial(n - 1)

# Q3: Write a recursive Python function that returns the sum of the first n integers
def sum_nint(n):
    count = 0
    # Base case
    if n == 0:
        return 0
    # Recursive case
    else:
        return n + sum_nint(n - 1)

# Q5: Create lambda function that takes 1 parameter `a` and returns it
return_a = lambda a: a # NOTE: this line works when placed in main() before being invoked

# Q6: Write a simple function (area_circle) that returns the area of a circle of a given radius
def area_circle(radius):
    return math.pi * radius ** 2

# Q7: Write a lambda function (area_circle_lambda) that returns the area of a circle of a given radius.
area_circle_lambda = lambda radius: math.pi * radius ** 2

# Q8b: Doubling Time lambda function where a is the APR of an investment
# NOTE: The return value only represents years if the rate provided represents annually compounding interest.
# If the rate provided represents monthly compounding, then the return value will be in months.
doubling_time_yrs = lambda a: math.log10(2) / math.log10(1 + a)

def main():
    # Q2 demonstration
    number = 4
    number_factorial = factorial(number)
    print(f"Q2: n! = {int(round(float(number)))}! = {number_factorial}")
    
    # Q3 demonstration    
    number = 4
    result = sum_nint(number)
    print(f"Q3: sum of first n={number} integers is: {result}")
    
    # Q5 demonstration
    a = return_a(7)
    print(f"Q5: a = {a}")
    
    # Q6 Demonstration
    radius = 2
    area = area_circle(radius)
    print(f"Q6: area of cirlce with radius {radius} is: {area}")

    # Q7 Demonstration
    radius_lambda = 2
    area_lambda = area_circle_lambda(radius_lambda)
    print(f"Q7: area of cirlce with radius {radius_lambda} is: {area_lambda}")

    # Q8a: Marc's Doubling Time w/ BMO's 1.85% APR
    rate_apr = 1.85 / 100 # converts % to decimal
    rate_monthly = rate_apr / 12
    doubling_time_months = round(math.log10(2) / math.log10(1 + rate_monthly),1)
    doubling_time_years = round(doubling_time_months / 12, 1)
    print(f"Q8a: It will take {doubling_time_months} months ({doubling_time_years} years) for Marc to double his money with BMO's 1.85% APR.")

    # Q8c: Marc's Doubling Time w/ 3% APR
    rate_apr = 3 / 100 # converts % to decimal
    rate_monthly = rate_apr / 12
    doubling_time_months = round(doubling_time_yrs(rate_monthly),1)
    doubling_time_years = round(doubling_time_months / 12, 1)
    print(f"Q8c: It will take {doubling_time_months} months ({doubling_time_years} years) for Marc to double his money with 3% APR.")

# Ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file)
if __name__ == "__main__":
    main()