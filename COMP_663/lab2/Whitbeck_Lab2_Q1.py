# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
2.3 LAB 2 - Descriptive Statistics
Question #1 - Measures of Center
Author: Kendall Whitbeck
San Diego College of Continuing Education (SDCCE) Student ID: 5550203278
COMP 663: Python for Data Science
"""
import pandas as pd

# NOTE: Uncomment `dbg = True` to compare results to expected results
dbg = False
# dbg = True

# read in the file mtcars.csv
df = pd.read_csv('mtcars.csv')

# find the mean of the column wt
mean = df['wt'].mean()

# find the median of the column wt
median = df['wt'].median()

# find the mode of the column wt
mode = df['wt'].mode()

print("mean = ", mean, ", median = ", median, ", mode = ", mode)

if dbg:
    # find the mean of the column wt
    mean = df['qsec'].mean()

    # find the median of the column wt
    median = df['qsec'].median()

    # find the mode of the column wt
    mode = df['qsec'].mode()

    print("mean = ", mean, ", median = ", median, ", mode = ", mode)