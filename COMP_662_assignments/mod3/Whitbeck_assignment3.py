# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Assignment 3: SQL Statements
Author: Kendall Whitbeck
San Diego College of Continuing Education (SDCCE) Student ID: 5550203278
COMP 662: Programming Databases with Python

Pre-requisites:
    - Install tabulate library (https://pypi.org/project/tabulate/)
    - Define queries in colocated movie_queries.sql file.
    - Define functions in colocated db_utils.py file.

Usage (Bash):
    python Whitbeck_assignment3.py
"""

import os  # os.system('cls'): clear terminal window text in Windows OS.
import sqlite3
import logging
import db_utils as db  # Logging sqlite3 database functions.
from tabulate import tabulate  # NOTE for printing tables; requires install (Bash): `pip install tabulate`

def main():
    # Clear terminal window text.
    if os.name == 'nt':  # Windows OS
        os.system('cls')
    else:  # Linux or MacOS.
        os.system('clear')

    # Use name of this Python script to name log file.
    script_filename = os.path.splitext(os.path.basename(__file__))[0]
    log_filename = f"{script_filename}.log"

    # Configure logging (NOTE: currently hardcoded to log at DEBUG level).
    db.log_config(log_filename)

    # Assign database filename and programname.
    dbfile = "movies.db"  # NOTE: if placing in a different folder, must ensure that folder exists.
    programname = "My Movie Database"
    print(f"{programname}\n")

    # Define queries in colocated SQL file. TODO consider modularizing this code as a function in db_utils.py and parsing on semicolons rather than newlines.
    queries = []
    with(open("movie_queries.sql", "r")) as queries_file:
        for line in queries_file:  # NOTE asssumes one query per line and queries are not split over lines.
            queries.append(line.strip())  # Strip newline from each list entry

    # Check database file exists, create it if not.
    db.db_checkfile(dbfile)

    # Perform database operations.
    try:
        conn = db.db_connect(dbfile)  # Connect to database.
        cur = db.db_cursor(conn)  # Get cursor in database.
        # Run queries.
        for query in queries:
            try:
                rows, headers = db.db_runquery(cur, query)
                # If rows exist, print the tabulated data.
                if rows:
                    print(tabulate(rows, headers, tablefmt="simple_grid", maxcolwidths=127))
            except sqlite3.Error as error:
                logging.error(f"Error executing query:\n\tError: {error}\n\tQuery: {query}".format())
    except sqlite3.Error as error:
        logging.error(f"Error establishing database connection or cursor: {error}".format())
    finally:
        if conn:
            conn.commit()  # Commit any tranasactions to database.
            logging.debug("Transactions committed".format())
            conn.close()
            logging.debug("DB Closed".format())

    # Close program and logging.
    print(f"See `{log_filename}` for log statements.\n")
    logging.info("Completed database operations.".format())
    print('All done!')

# Ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file)
if __name__ == "__main__":
    main()