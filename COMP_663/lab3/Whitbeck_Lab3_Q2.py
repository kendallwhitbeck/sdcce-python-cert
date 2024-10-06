# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Lab 3: Linear Regression
Question #2 - Making predictions using SLR Models
Author: Kendall Whitbeck
San Diego College of Continuing Education (SDCCE) Student ID: 5550203278
COMP 663: Python for Data Science
"""

import numpy as np
import pandas as pd
from statsmodels.formula.api import ols  # may require `pip install statsmodels`

def main():

    # load the file internetusage.csv
    internet = pd.read_csv(rf'internetusage.csv', sep=',')

    # fit a linear model using the sms.ols function and the internet dataframe
    # where internet_usage is the response variable (output) and bachelors_degree is the predictor variable (input)
    model = ols('internet_usage ~ bachelors_degree', data=internet).fit()

    bach_percent = float(input("Enter your bachelors degree percentage: "))

    # use the model.predict function to find the predicted value for internet_usage using the bach_percent value for the predictor
    x0 = pd.DataFrame(np.array([[bach_percent]]), columns=['bachelors_degree'])  # NOTE: `columns` name(s) must match OLS model
    model.predict(x0)
    prediction = model.predict(x0)

    print("\n", prediction)

# Ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file)
if __name__ == "__main__":
    main()