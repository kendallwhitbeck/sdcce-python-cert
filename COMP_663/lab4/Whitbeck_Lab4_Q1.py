# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Lab 4 - Introduction to Data Mining, Data Cleansing and Preparation
Question #1 - dropna() and fillna()
Author: Kendall Whitbeck
San Diego College of Continuing Education (SDCCE) Student ID: 5550203278
COMP 663: Python for Data Science
"""

import pandas as pd

def main():
    # read in hmeq_small.csv
    hmeq = pd.read_csv("hmeq_small.csv")

    # Create a new data frame with the rows with missing values dropped
    df1 = hmeq.dropna()  # delete rows with missing values

    # Create a new data frame with the missing values filled in by the mean of the column
    df2 = hmeq.fillna(hmeq.mean())  # Code to fill in missing values

    # Print the means of the columns for each new data frame
    print("Means for df1 are ", df1.mean())

    print("Means for df2 are ", df2.mean())

# Ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file)
if __name__ == "__main__":
    main()