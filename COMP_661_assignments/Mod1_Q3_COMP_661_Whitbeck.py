# -*- coding: utf-8 -*-
"""
Author: Kendall Whitbeck
Student ID: 5550203278
Assignment: Module 1, Question 3
Description: This program uses datetime to calculate the elapsed time for an arbitrary algorithm to complete various problem sizes.
"""

import os  # os.system('cls'): clear terminal window text in Windows OS
import matplotlib.pyplot as plt  # for plotting
from datetime import datetime


def algorithm(problem_size):
    """Modularize the algorithm as a function.

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

    # Create a list of problem sizes and empty list of elapsed times
    problem_sizes = [1000000, 3000000, 9000000, 27000000]
    # extend proiblem_sizes with half the problem sizes
    problem_sizes.extend([problem_size // 2 for problem_size in problem_sizes])
    # problem_sizes.extend(problem_sizes/2)
    elapsed_times = []

    # Print the heading for the problem size and corresponding elapsed time
    print(f"Problem Size             Seconds")

    for problem_size in problem_sizes:
        # Record the start time
        start_time = datetime.now()

        # Run the algorithm with the current problem size
        algorithm(problem_size)

        # Record the end time
        end_time = datetime.now()

        # Calculate the elapsed time
        elapsed_time = end_time - start_time

        # Display the problem size and corresponding elapsed time
        print(f"{problem_size:12,}              {(elapsed_time.total_seconds()):1.4f}")

        # Collect the elapsed time for each problem size
        elapsed_times.append(elapsed_time.total_seconds())

    # Create a scatter plot of problem size vs. elapsed time
    plt.scatter(problem_sizes, elapsed_times, marker='o')
    plt.show()

# Ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file)
if __name__ == "__main__":
    main()


