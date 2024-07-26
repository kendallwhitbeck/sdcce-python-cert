# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Assignment 5: Visualizing Data
Author: Kendall Whitbeck
San Diego College of Continuing Education (SDCCE) Student ID: 5550203278
COMP 662: Programming Databases with Python

Pre-requisites:
    - Save db_utils.py file in Python import paths:
        - Colocating db_utils.py with the current Python script is the simplest method.
    - degrees2.db exists with correct path specified in main() function variable `dbfile`.

Usage (Bash):
    python Whitbeck_assignment5.py
"""

# TODO before delivering, comment out below and place db_utils.py in same folder instead.
# import sys
# sys.path.append("C:\\Users\\kenda\\Google Drive\\Kendalls Flashdrive\\Computer Science\\GitHub\\sdcce-python-cert")
# TODO comment out above

import os  # clear terminal window text based on Windows or Linux/Mac OS.
import sqlite3
import logging
import db_utils_mod5_submission as db  # Logging sqlite3 database functions.

def main():
    """ Plot the percentage of degrees conferred to women in the USA by major (1970-2011).
    """
    # Clear terminal window text.
    if os.name == 'nt':  # Windows OS
        os.system('cls')
    else:  # Linux or MacOS.
        os.system('clear')

    # Use name of this Python script to name log file.
    script_filename = os.path.splitext(os.path.basename(__file__))[0]
    log_filename = f"{script_filename}.log"

    # Configure logging (NOTE: currently hardcoded to set root logger at DEBUG level).
    db.log_config(log_filename)

    # Start program.
    programname = "Welcome to the Degree Data Visualization Program!"
    print(f"{programname}\n")

    # Assign database metadata.
    dbfile = "degrees2.db"  # NOTE: if placing in a different folder, must ensure that folder exists.
    table1_name = "degrees"  # Name of Table in DB

    # Check database file exists, create it if not.
    db.db_checkfile(dbfile)

    # Perform database operations.
    try:
        conn = db.db_connect(dbfile)  # Connect to database.
        cur = db.db_cursor(conn)  # Get cursor in database.

        # Define Database SELECT query.
        degree_labels = ["Engineering", "English", "Business", "Architecture"]  # NOTE: update w/ desired degrees
        query = f"SELECT Year, {degree_labels[0]}, {degree_labels[1]}, {degree_labels[2]}, {degree_labels[3]} FROM {table1_name}"

        # Run query.
        rows, _ = db.db_runquery(cur, query)

        # Plot results.
        db.db_plot_line(rows, degree_labels)  # TODO could pass in headers and parse instead of degree_labels

    except sqlite3.Error as error:
        logging.error(f"Error establishing database connection or cursor: {error}".format())
    finally:
        if conn:
            conn.commit()  # Commit any tranasactions to database.
            logging.debug("Transactions committed".format())
            conn.close()
            logging.debug("DB Closed".format())

    # Close program.
    logging.info("Completed database operations".format())
    print('Plots complete, exiting program.')

# Ensure main() is executed only if this .py file is executed directly
# (i.e., not imported by another .py file)
if __name__ == "__main__":
    main()
    # print(f"# TODO before delivering, comment out sys.path.append lines and place db_utils.py in same folder instead.")