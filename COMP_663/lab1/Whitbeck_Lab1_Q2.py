# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
1.2 LAB 1 - Data Visualization
Question #2 - Data Frames
Author: Kendall Whitbeck
San Diego College of Continuing Education (SDCCE) Student ID: 5550203278
COMP 663: Python for Data Science
"""

import pandas as pd

def main():
    # load the data Cars.csv into a data frame
    cars_df = pd.read_csv("Cars.csv")# Import the CSV file Cars.csv

    # subset the first userNum rows of the data frame
    userNum = int(input("Enter number of rows as an integer: "))
    cars_df_subset = cars_df.head(userNum)

    # find and print the maximum values of each column in the subset 
    print(cars_df_subset.max())

# ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file)
if __name__ == "__main__":
    main()