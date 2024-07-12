# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Assignment 4: SQL Statements Using dbmovies.sqlite
Author: Kendall Whitbeck
San Diego College of Continuing Education (SDCCE) Student ID: 5550203278
COMP 662: Programming Databases with Python

Pre-requisites:
    - Save db_utils.py file in Python import paths:
        - Colocating db_utils.py with the current Python script is the simplest method.
    - dbmovies.sqlite exists with correct path specified in main() function variable `dbfile`.

Usage (Bash):
    python Whitbeck_assignment4.py
"""

# TODO before delivering, comment out below and place db_utils.py in same folder instead.
import sys
sys.path.append("C:\\Users\\kenda\\Google Drive\\Kendalls Flashdrive\\Computer Science\\GitHub\\sdcce-python-cert")
# TODO comment out above

import os  # clear terminal window text based on Windows or Linux/Mac OS.
import sqlite3
import logging
import db_utils as db  # Logging sqlite3 database functions.

def db_update(cur, table, update_attribute, update_value, where_attribute, where_value):
    """ Update database entry.
    """
    # Sanitize input and insert quoutes for strings to enable querying whitespace
    if type(table) == str: table = f"'{str(table)}'"
    if type(update_attribute) == str: update_attribute = f"'{str(update_attribute)}'"
    if type(update_value) == str: update_value = f"'{str(update_value)}'"
    if type(where_attribute) == str: where_attribute = f"'{str(where_attribute)}'"
    if type(where_value) == str: where_value = f"'{str(where_value)}'"

    # Define update query
    query_update = str(f"UPDATE {table} "
                       f"SET {update_attribute} = {update_value} "
                       f"WHERE {where_attribute} = {where_value};")
    # Execute update query
    db.db_runquery(cur, query_update)

def db_delete(cur, table, where_attribute, where_value):
    """ Delete database entry.
    """
    # Sanitize input and insert quoutes for strings to enable querying whitespace
    if type(table) == str: table = f"'{str(table)}'"
    if type(where_attribute) == str: where_attribute = f"'{str(where_attribute)}'"
    if type(where_value) == str: where_value = f"'{str(where_value)}'"

    # Define delete query
    query_delete = str(f"DELETE FROM {table} "
                       f"WHERE {where_attribute} = {where_value};")

    # Prompt user to confirm deletion
    run_deletion = str(input(f"Are you sure you want to delete {where_attribute}={where_value} from the `{table}` table (y/n)?"))
    print()  # newline

    # If user confirms deletion
    if run_deletion == "y":
        # Execute delete query
        db.db_runquery(cur, query_delete)
    else:
        # Abort deletion
        print("Deletion aborted.\n")

def db_lookup_by_year(cur):
    """ Look up movie by user-input year.
    """
    run_loopkup = "y"
    while run_loopkup == "y":
        try:
            year = int(input("Please enter the year to lookup:  "))
            print()  # newline
        except ValueError as e:
            print(f"ERROR! Please use numerical digits only.\n")
            continue  # ask user to input `year` again

        # Select results matching the `year` input.
        query_lookup_year = str(f"SELECT m.name as Title, m.year as Year, m.minutes as Length, c.name as Genre "
                                f"FROM Movie as m JOIN Category as c ON m.categoryID = c.categoryID "
                                f"WHERE year = {year};")
        rows, headers = db.db_runquery(cur, query_lookup_year)

        # If no matching results, inform user
        if not rows:
            print(f"Sorry, no movie in our database for {year}.\n")
        else:
            # Display results matching the `year` input.
            db_print_table(headers, rows)

        # Ask user if they want to look up another year.
        run_loopkup = str(input("Look up another year (y/n)? ")).strip().lower()
        print()  # newline

def db_print_table(headers, rows):
    """ Print table of results matching headers and rows returned by a SELECT query.
    """
    # Convert rows to a list of dictionaries.
    data_list = [dict(row) for row in rows]

    # Display header and row results in a tabular format.
    for index, header in enumerate(headers):
        if index == 0:  # First header.
            print(f"| __{header}__", end="\t")
        elif index == len(headers) - 1:  # Last header.
            print(f"__{header}__", end="\t|\n")
        else:
            print(f"__{header}__", end="\t")
    # Print value of each attribute in each row.
    for row in data_list:
        for index, value in enumerate(row.values()):
            if index == 0:  # First value in row.
                print("| ", value, end="\t")
            elif index == len(row.values()) - 1:  # Last value in row.
                print(value, end="\t|\n")
            else:
                print(value, end="\t")
    print()  # newline

def main():
    """ Connect to a database, update entries, and look up values.
    """
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

    # Start program.
    programname = "Welcome to the MovieDB!"
    print(f"{programname}\n")

    # Assign database metadata.
    dbfile = "dbmovies.sqlite"  # NOTE: if placing in a different folder, must ensure that folder exists.
    table2_name = "Movie"  # Name of 2nd Table in DB
    pk2_name = "movieID"  # Name of Primary Key (PK) for 2nd Table

    # Check database file exists, create it if not.
    db.db_checkfile(dbfile)

    # Perform database operations.
    try:
        conn = db.db_connect(dbfile)  # Connect to database.
        cur = db.db_cursor(conn)  # Get cursor in database.

        # Run Database update queries.
        db_update(cur, table2_name, "year", 1995, "name", "Toy Story")  # Toy Story movie DB values
        db_delete(cur, table2_name, "name", "Lawrence of Arabia")  # Lawrence of Arabia movie DB values

        # Run User Lookup by Year
        db_lookup_by_year(cur)

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
    print('Bye for now - see you at the movies!')

# Ensure main() is executed only if this .py file is executed directly
# (i.e., not imported by another .py file)
if __name__ == "__main__":
    main()
    print(f"# TODO before delivering, comment out sys.path.append lines and place db_utils.py in same folder instead.")