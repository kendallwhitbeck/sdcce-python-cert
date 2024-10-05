# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
2.3 LAB 2 - Descriptive Statistics
Question #2 - Standard Deviation
Author: Kendall Whitbeck
San Diego College of Continuing Education (SDCCE) Student ID: 5550203278
COMP 663: Python for Data Science
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# NOTE: Uncomment `dbg = True` to expedite development
dbg = False
# dbg = True  # TODO comment out before submitting

# read in the file internetusage.csv
df = pd.read_csv("internetusage.csv")

population = df[['State', 'Population']] # subset the State and Population columns

if dbg:
    state_index = 5
else:
    state_index = int(input("Enter a row index corresponding to a state as an integer: "))

# subset the row given by state_index
state_data = population.iloc[[state_index]]
state_name = state_data.iloc[0].iloc[0]
state_pop = state_data.iloc[0].iloc[1]
print("The population of " + str(state_name) + " is " + str(state_pop)+ ".")

# create figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, sharex=False)

# create a box plot for the population data frame
sns.boxplot(y='Population', data=population, ax=ax2)

# add strip plot to match example plot
sns.stripplot(y='Population', data=population, ax=ax1)

# show the plot
fig.suptitle("Box Plot for State Populations in the US (Millions Excluding Territories)")
plt.show()