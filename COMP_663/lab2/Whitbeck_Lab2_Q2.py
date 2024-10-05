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
import scipy.stats as st

# NOTE: Uncomment `dbg = True` to expedite development
dbg = False
# dbg = True  # TODO comment out before submitting

# read in the file NBA2019.csv
NBA2019_df = pd.read_csv('NBA2019.csv')

# Input desired column. Ex: AGE, 2P%, or PointsPerGame.
if dbg:
    chosen_column = 'PointsPerGame'
else:
    chosen_column = str(input('Enter desired column. Ex: `AGE`, `2P%`, or `PointsPerGame`: '))

# Create subset of NBA2019_df based on input.
NBA2019_df_column = NBA2019_df[chosen_column]

# Find standard deviation and round to two decimal places. 
sample_s = st.tstd(NBA2019_df_column)
sample_s_rounded = round(sample_s, 2)

# Output
print(f'\nThe standard deviation for {chosen_column} is: {sample_s_rounded}')