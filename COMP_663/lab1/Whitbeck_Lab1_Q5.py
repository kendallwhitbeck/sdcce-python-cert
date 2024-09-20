# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
1.2 LAB 1 - Data Visualization
Question #5 - Line Charts
Author: Kendall Whitbeck
San Diego College of Continuing Education (SDCCE) Student ID: 5550203278
COMP 663: Python for Data Science
"""

import pandas as pd
import matplotlib.pyplot as plt

def main():
    # load the target.csv file
    tgt = pd.read_csv('target.csv')  

    # subset the last 19 days of the dataframe
    tgt_march = tgt.iloc[-19:]

    # subset tgt_march and create a data frame that contains the columns: Date and Volume
    tgt_vol = tgt_march[['Date', 'Volume']]

    # subset tgt_march and create a data frame that contains the columns: Date and Close
    tgt_close = tgt_march[['Date', 'Close']]

    # user defined value for the day
    day = int(input('Enter the day as an integer (e.g., `3`): ')) - 1

    # subset the specific row of tgt_vol for the given day
    volume_row = tgt_vol.iloc[[day]]
    volume = volume_row.iloc[0].iloc[1] # gets the volume for the given day

    # subset the specific row of tgt_close for the given day
    close_row = tgt_close.iloc[[day]]
    close = close_row.iloc[0].iloc[1] # gets the closing stock price for the given day

    # gets the date
    date = tgt_march.iloc[[day]].iloc[0].iloc[0]

    # output the volume and closing stock price
    print(f'\nThe volume of TGT on {date} is {volume:.0f}.')
    print(f'The closing stock price of TGT on {date} is ${close}.')

    # create figure with two subplots
    _, (ax1, ax2) = plt.subplots(2, 1, sharex=True, sharey=False)

    # create line chart for Volume
    ax1.plot(tgt_march['Date'], tgt_march['Volume'], color='black')
    ax1.set_ylabel('Number of Trades')
    ax1.legend(['Volume'])
    ax1.set_title('March 2018 Trading Volume for Target Stock')
    ax1.grid()

    # create line chart for Close
    ax2.plot(tgt_march['Date'], tgt_march['Close'], color='red')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Price')
    ax2.legend(['Price'])
    ax2.set_title('March 2018 Market Closing Price for Target Stock')
    ax2.grid()

    # show the figure
    plt.show()

# ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file)
if __name__ == '__main__':
    main()