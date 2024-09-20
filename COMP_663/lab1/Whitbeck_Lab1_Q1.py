# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
1.2 LAB 1 - Data Visualization
Question #1 - Importing Modules
Author: Kendall Whitbeck
San Diego College of Continuing Education (SDCCE) Student ID: 5550203278
COMP 663: Python for Data Science
"""

import numpy as np
import scipy.stats as st

def main():
    # user input integers 
    x1 = int(input())
    x2 = int(input())
    x3 = int(input())
    x4 = int(input())

    # create numpy arrays
    x = np.array([x1, x2, x3, x4])
    y = np.array([0, 10, 7, 25])

    # perform linear regression
    print(st.linregress(x,y))

# ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file)
if __name__ == "__main__":
    main()