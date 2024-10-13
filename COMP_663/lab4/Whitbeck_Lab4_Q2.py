# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Lab 4 - Introduction to Data Mining, Data Cleansing and Preparation
Question #2 - scale() and MinMaxScaler()
Author: Kendall Whitbeck
San Diego College of Continuing Education (SDCCE) Student ID: 5550203278
COMP 663: Python for Data Science
"""

import pandas as pd
from sklearn import preprocessing  # Note: may require `pip install scikit-learn`

def main():
    # read in hmeq_small.csv
    hmeq = pd.read_csv("hmeq_lab412.csv")

    # Standardize the data
    standardized = preprocessing.scale(hmeq)  # Code to standardize the data

    # Output the standardized data as a data frame
    df1 = pd.DataFrame(standardized, columns=hmeq.columns)  # Code to output as a data frame

    # Normalize the data
    normalized = preprocessing.MinMaxScaler().fit_transform(hmeq)  # Code to normalize the data

    # Output the normalized data as a data frame
    df2 = pd.DataFrame(normalized, columns=hmeq.columns)  # Code to output as a data frame

    # Print the means and standard deviations of df1 and df2
    print("The means of df1 are ", df1.mean())
    print("The standard deviations of df1 are ", df1.std())
    print("The means of df2 are ", df2.mean())
    print("The standard deviations of df2 are ", df2.std())

# Ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file)
if __name__ == "__main__":
    main()