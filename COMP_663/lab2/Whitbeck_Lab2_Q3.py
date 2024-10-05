# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
2.3 LAB 2 - Descriptive Statistics
Question #3 - Five Number Summary
Author: Kendall Whitbeck
San Diego College of Continuing Education (SDCCE) Student ID: 5550203278
COMP 663: Python for Data Science
"""
import pandas as pd

# read in the file internetusage.csv
df = pd.read_csv("internetusage.csv")

# subset the column internet_usage
internet = df['internet_usage']

# find the five number summary and print column title at the top
five_num = internet.describe()
print(five_num)
