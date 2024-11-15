# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Lab 3: Linear Regression
Question #3 - Creating Correlation Matrices
Author: Kendall Whitbeck
San Diego College of Continuing Education (SDCCE) Student ID: 5550203278
COMP 663: Python for Data Science
"""

import pandas as pd

def main():

    # Read in nbaallelo_slr.csv
    nba = pd.read_csv(rf'nbaallelo_slr.csv', sep=',')

    # Display the correlation matrix for the columns elo_i, pts, and opp_pts
    print(nba[['elo_i', 'pts', 'opp_pts']].corr())

    # Create a new column in the data frame that is the difference between pts and opp_pts
    nba['y'] = nba['pts'] - nba['opp_pts']

    # Display the correlation matrix for elo_i and y
    print(nba[['elo_i', 'y']].corr())

# Ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file)
if __name__ == "__main__":
    main()