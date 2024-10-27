# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Lab 5 - Supervised Learning
Question #2 - Logistic Regression using Logistic Regression
Author: Kendall Whitbeck
San Diego College of Continuing Education (SDCCE) Student ID: 5550203278
COMP 663: Python for Data Science
"""
import pandas as pd, numpy as np
# import statsmodels.formula.api as smf  # TODO needed?
# import matplotlib as plt  # TODO needed?
# import seaborn as sns  # TODO needed?
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# from matplotlib.colors import ListedColorMap  # TODO needed?
# from sklearn import neighbors, datasets  # TODO needed?
# from sklearn.pipeline import Pipeline  # TODO needed?

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

    # build the logistic model using the LogisticRegression function with wins as the target variable and elo_i as the predictor.
    logisticRegr = LogisticRegression()
    # logisticRegr.fit(train[["elo_i"]], train["wins"])
    logisticRegr.fit(train[["pts"]], train["wins"])  # TODO debug only, remove before delivery

    # use the test set to predict the wins from the elo_i score
    # predictions = logisticRegr.predict(test[["elo_i"]])  # code to predict wins
    predictions = logisticRegr.predict(test[["pts"]])  # TODO debug only, remove before delivery

    # generate confusion matrix
    conf = metrics.confusion_matrix(test["wins"], predictions)  # code to generate confusion matrix

    print("confusion matrix is \n", conf)

    # define true positive, false positive, true negative, false negative of the confusion matrix
    tp = conf[1,1]
    fp = conf[0,1]
    tn = conf[0,0]
    fn = conf[1,0]

    # calculate the sensitivity
    sens = tp / (tp + fn)  # code to calculate the sensitivity
    print("Sensitivity is ", sens)

    # calculate the specificity
    spec = tn / (tn + fp)  # code to calculate the specificity
    print ("Specificity is ", spec)

# Ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file)
if __name__ == "__main__":
    main()