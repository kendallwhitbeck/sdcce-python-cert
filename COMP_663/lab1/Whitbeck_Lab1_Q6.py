# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
1.2 LAB 1 - Data Visualization
Question #6 - Strip Plots
Author: Kendall Whitbeck
San Diego College of Continuing Education (SDCCE) Student ID: 5550203278
COMP 663: Python for Data Science
"""

import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

def main():
    # load the titanic.csv dataset
    titanic = pd.read_csv('titanic.csv')

    # subset titanic to include male passengers in first class over 18 years old
    df = titanic.loc[(titanic.sex == 'male') & (titanic.pclass == 1) & (titanic.age > 18)]

    # print the first five rows and size of the new data frame
    print(df.head())
    print(f'\n[{df.shape[0]} rows x {df.shape[1]} columns]')

    # create strip plot where the data is grouped by the city the 
    # passengers embarked and by survival status with age on the y-axis
    fig = px.strip(df, x="embark_town", y="age", color="survived", stripmode="overlay")

    # update layout
    fig.update_layout(
        title="Strip Plot",
        xaxis_title="Embark Town",
        yaxis_title="Age",
        legend_title="survive",
    )

    # update legend entry labels
    fig.data[0].name = "No"
    fig.data[1].name = "Yes"

    # show the plot
    fig.show()

# ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file)
if __name__ == '__main__':
    main()