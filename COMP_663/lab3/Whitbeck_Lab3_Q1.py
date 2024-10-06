# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Lab 3: Linear Regression
Question #1 - Creating SLR Models
Author: Kendall Whitbeck
San Diego College of Continuing Education (SDCCE) Student ID: 5550203278
COMP 663: Python for Data Science
"""

import pandas as pd
from statsmodels.formula.api import ols  # may require `pip install statsmodels`
import statsmodels.api as sm

def main():

    # Read in nbaallelo_slr.csv
    nba = pd.read_csv('nbaallelo_slr.csv')

    # Create a new column in the data frame that is the difference between pts and opp_pts
    nba['y'] = nba['pts'] - nba['opp_pts']

    # Perform simple linear regression on y and elo_i using statsmodels ols
    results = ols('y ~ elo_i', data=nba).fit()

    # Create an analysis of variance (ANOVA) table, use Type 2 since no interaction effect is assumed between the independent variables
    aov_table = sm.stats.anova_lm(results, typ=2)

    # Print the analysis of variance table
    print(aov_table)

# Ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file)
if __name__ == "__main__":
    main()