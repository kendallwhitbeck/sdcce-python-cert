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
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

def main():
    # load the file titanic.csv into a data frame
    titanic = pd.read_csv('titanic.csv')

    # subset the titanic dataset to include first class passengers who embarked in Southampton
    first_south = titanic[(titanic.pclass == 1) & (titanic.embarked == 'S')]

    # subset the titanic dataset to include either second or third class passengers
    second_third = titanic[titanic.pclass.isin([2,3])]

    # print the first five rows of both subsets
    print(first_south.head())
    print(second_third.head())

    # create bar chart for passengers in first class who embarked in Southampton grouped by sex
    first_south_counts = first_south['sex'].value_counts(normalize=False).sort_index()
    _, ax = plt.subplots()
    ax.bar(first_south_counts.index, first_south_counts.values, color=['blue', 'red'])

    # format bar chart
    ax.set_xlabel('Passenger Class: First')
    ax.set_ylabel('Count')
    ax.set_xticklabels(first_south_counts.index)
    ax.grid(axis='y')
    plt.show()

    # passengers in second and third class grouped by survived status
    second_third_survived = second_third[second_third.survived == 1]
    second_third_not_survived = second_third[second_third.survived == 0]

    # count number of passengers for each class (2nd and 3rd) who survived and did not survive
    survived_counts = second_third_survived['pclass'].value_counts().sort_index()
    not_survived_counts = second_third_not_survived['pclass'].value_counts().sort_index()

    # x locations for the groups
    x = np.arange(len(survived_counts))  # this gives positions for 2nd and 3rd classes (0 and 1)

    # create bar chart
    width = 0.35
    _, ax = plt.subplots()
    ax.bar(x - width/2, survived_counts, width, label='Survived', color='green')
    ax.bar(x + width/2, not_survived_counts, width, label='Not Survived', color='purple')

    # format bar chart
    ax.set_xlabel('Passenger Class')
    ax.set_ylabel('Count')
    ax.set_xticks(x)
    ax.set_xticklabels(['Second', 'Third'])
    ax.grid(axis='y')
    ax.legend(['Survived', 'Not Survived'])
    plt.show()

# ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file)
if __name__ == '__main__':
    main()