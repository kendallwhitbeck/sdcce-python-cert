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

    # create bar charts for the following:

    # passengers in first class who embarked in Southampton grouped by sex
    # fig_first_south_sex =px.bar(first_south, x='sex') # create bar chart
    # fig_first_south_sex.show()  # show bar chart

    first_south['sex'].value_counts().plot(kind='bar')
    # plt.bar(first_south['sex'].value_counts().index, first_south['sex'].value_counts().values)
    plt.xlabel('First')
    plt.ylabel('Count')
    plt.title('Passenger Class')
    plt.xticks(rotation=0)
    plt.grid(axis='y', which='major', linestyle='--', linewidth=0.5, zorder=0)
    plt.show()

    # passengers in second and third class grouped by survival status

# ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file)
if __name__ == '__main__':
    main()