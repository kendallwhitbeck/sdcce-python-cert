#!/usr/bin/env python3

# plotting_db.py

# import matplotlib as mpl
import matplotlib.pyplot as plt

import db_utils as db

def print_years(res):
    plt.hist(res, bins=40)
    # mpl.pyplot.hist(res, bins=40)
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
    res, headers = db.db_runquery(cur, query )
    for result in res:
        allyears.append(result[0])

    print_years(allyears)

if __name__ == "__main__":
    main()