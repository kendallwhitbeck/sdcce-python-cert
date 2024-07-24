#!/usr/bin/env python3

# plotting_db.py

# import matplotlib as mpl
import matplotlib.pyplot as plt

import db_utils as db

def plot_years(allyears, bins=40):
    plt.hist(allyears, bins)
    plt.ylabel('Number of Movies')
    plt.xlabel('Year Released')
    plt.locator_params(axis='y', integer=True)
    plt.title('COMP662 Movie Database')
    plt.show()

def main():
    dbfile = 'db/dbmovies.sqlite'
    db.log_config()
    db.db_checkfile(dbfile)

    # Connect to db
    conn = db.db_connect(dbfile)
    cur = db.db_cursor(conn)

    allyears = []
    query = 'SELECT year from Movie'
    rows, headers = db.db_runquery(cur, query)
    db.db_print_table(headers, rows)
    for row in rows:
        allyears.append(row[0])

    plot_years(allyears, 40)
    # plot_years(allyears, 100)
    # plot_years(allyears, 10)
    plot_years(allyears, 51)  # 2013-1962=51 is the range from largest to smallest year;
                              # thus the most accurate # of bins

if __name__ == "__main__":
    main()