# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
1.2 LAB 1 - Data Visualization
Question #3 - Subsetting Data Frames
Author: Kendall Whitbeck
San Diego College of Continuing Education (SDCCE) Student ID: 5550203278
COMP 663: Python for Data Science
"""

import pandas as pd

def main():
    # user defined value for the column cyl
    cylinders = int(input("Enter the number of cylinders: "))

    # load the file mtcars.csv into a data frame called df
    df = pd.read_csv("mtcars.csv")

    # create a new dataframe with only the rows where cyl = cylinders
    df_cyl = df[df.cyl == cylinders]

    # print the shape of the new data frame
    print(df_cyl.shape)

# ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file)
if __name__ == "__main__":
    main()