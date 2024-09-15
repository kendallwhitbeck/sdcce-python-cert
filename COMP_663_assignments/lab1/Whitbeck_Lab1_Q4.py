# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
1.2 LAB 1 - Data Visualization
Question #4 - Bar Charts
Author: Kendall Whitbeck
San Diego College of Continuing Education (SDCCE) Student ID: 5550203278
COMP 663: Python for Data Science
"""

import pandas as pd

def main():
    # load the file titanic.csv into a data frame
    titanic = pd.read_csv("titanic.csv")

    # subset the titanic dataset to include first class passengers who embarked in Southampton
    first_south = titanic[(titanic.pclass == 1) & (titanic.embarked == "S")]

    # subset the titanic dataset to include either second or third class passengers
    second_third_logOps = titanic[(titanic.pclass == 2) | (titanic.pclass == 3)]
    second_third = titanic[titanic.pclass.isin([2,3])]

    print(first_south.head())
    print(second_third.head())

# ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file)
if __name__ == "__main__":
    main()