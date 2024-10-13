# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Lab 3: Linear Regression
Question #4 - Multiple Regression
Author: Kendall Whitbeck
San Diego College of Continuing Education (SDCCE) Student ID: 5550203278
COMP 663: Python for Data Science
"""

import pandas as pd
from statsmodels.formula.api import ols  # may require `pip install statsmodels`
import statsmodels.api as sm

def main():

    # Read in nbaallelo_slr.csv
    nba = pd.read_csv(rf'nbaallelo_slr.csv', sep=',')

    # Perform multiple linear regression on pts, elo_i, and opp_pts using statsmodels ols
    results = ols('pts ~ elo_i + opp_pts', data=nba).fit()

    # Create an analysis of variance table
    aov_table = sm.stats.anova_lm(results, typ=2) # Code to create ANOVA table

    # Print the analysis of variance table
    print(aov_table)

# Ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file)
if __name__ == "__main__":
    main()