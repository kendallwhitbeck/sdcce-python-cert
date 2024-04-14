# -*- coding: utf-8 -*-
"""
Author: Kendall Whitbeck
Student ID: 5550203278
Assignment: Module 1, Question 3
Description: This program uses datetime to calculate the elapsed time for an aribitrary algorithm to complete various problem sizes.
"""

import os  # os.system('cls'): clear terminal window text in Windows OS
from datetime import datetime
import time

def algorithm(problem_size):
    """Modularize the algorithm as a function

    Args:
        problem_size (int): size of the problem
    """
    work = 1
    for x in range(problem_size):
        work += 5
        work -= 5

def main():
    # Clear terminal window text in Windows OS
    os.system('cls')

    list_problem_size = [1000000, 3000000, 9000000, 27000000]

    print(f"Problem Size             Seconds")

    for problem_size in list_problem_size:
        # Record the start time
        # start_time = datetime.now()  # datetime.now() from datetime module
        start_time = time.time()  # time.time() from time module

        # Run the algorithm with the current problem size
        algorithm(problem_size)

        # Record the end time
        # end_time = datetime.now()  # datetime.now() from datetime module
        end_time = time.time()  # time.time() from time module

        # Calculate the elapsed time
        elapsed_time = end_time - start_time

        # Display the problem size and corresponding elapsed time
        # print(f"Problem size: {problem_size:,}, elapsed time: {elapsed_time}")
        print(f"{problem_size:12,}             {elapsed_time:1.4f}")

# Ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file)
if __name__ == "__main__":
    main()
