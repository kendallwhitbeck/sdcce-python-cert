# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Lab 5 - Supervised Learning
Question #1 - Logistic Regression using `logit`
Author: Kendall Whitbeck
San Diego College of Continuing Education (SDCCE) Student ID: 5550203278
COMP 663: Python for Data Science
"""
import pandas as pd, numpy as np
import statsmodels.formula.api as smf
import matplotlib as plt  # TODO needed?
import seaborn as sns  # TODO needed?

from sklearn.model_selection import train_test_split
# from matplotlib.colors import ListedColorMap  # TODO needed?
from sklearn import neighbors, datasets  # TODO needed?
from sklearn.pipeline import Pipeline  # TODO needed?
from sklearn.linear_model import LogisticRegression  # TODO needed?

def main():
    # load nbaallelo.csv into a dataframe 
    df = pd.read_csv(rf'nbaallelo.csv', sep=',') # code to load csv file

    # Converts the feature "game_result" to a binary feature and adds as new column "wins"
    wins = df.game_result == "W"
    bool_val = np.multiply(wins, 1)
    wins = pd.DataFrame(bool_val, columns = ["game_result"])
    wins_new = wins.rename(columns = {"game_result": "wins"})
    df_final = pd.concat([df, wins_new], axis=1) 

    # split the data df_final into training and test sets with a test size of 0.3 and random_state = 0
    train, test = train_test_split(df_final, test_size=0.3, random_state=0)  # code to split df_final into training and test sets

    # construct a logistic regression model with wins as the target and elo_i as the predictor, using the training set
    # lm = smf.logit(formula = 'wins ~ elo_i', data=train).fit()  # code to construct logistic model using the logit function
    lm = smf.logit(formula = 'wins ~ pts', data=train).fit()  # code to construct logistic model using the logit function

    # print coefficients for the model
    print(lm.params)  # code to return coefficients

# Ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file)
if __name__ == "__main__":
    main()