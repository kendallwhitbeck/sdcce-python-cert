# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Assignment 7: Database Analytics of a Beer Review Database Using pandas
Author: Kendall Whitbeck
San Diego College of Continuing Education (SDCCE) Student ID: 5550203278
COMP 662: Programming Databases with Python

Pre-requisites:
    - Save db_utils_Whitbeck.py file in Python import paths:
        - Collocating db_utils_Whitbeck.py with the current Python script is the simplest method.
    - beers.db exists with correct path specified in main() function variable `dbfile`.

Usage (Bash):
    python Whitbeck_assignment7.py
"""
import os
import sqlite3
import logging
import pandas as pd
import matplotlib.pyplot as plt
import db_utils_Whitbeck as db  # Logging sqlite3 database functions.

def main():
    # Clear terminal window text.
    if os.name == 'nt':  # Windows OS
        os.system('cls')
    else:  # Linux or MacOS.
        os.system('clear')

    # Configure logging using name of this Python script to name log file
    # (NOTE: currently hardcoded to set root logger at DEBUG level). 
    script_filename = os.path.splitext(os.path.basename(__file__))[0]
    log_filename = f"{script_filename}.log"
    db.log_config(log_filename, "Beers")

    # Start program.
    programname = "Database Analytics of a Beer Review Database Using pandas"
    print(f"{programname}\n")

    # Assign database metadata.
    dbfile = "beers.db"  # NOTE: if placing in a different folder, must ensure that folder exists.

    # Check database file exists, create it if not.
    db.db_checkfile(dbfile)

    # Perform database operations.
    try:
        conn = db.db_connect(dbfile)  # Connect to database.

        # Read the SQLite query results into a pandas dataframe.
        df = pd.read_sql_query("SELECT * from reviews", conn)

        # Print and answer questions.
        print("Question 1: How many rows are in the table?")
        print(str(len(df)))

        print("\nQuestion 2: Describe the table:")
        print(df.describe())

        print("\nQuestion 3: How many entries are there for each brewery?")
        print(df.groupby(['brewery_name']).size())

        print("\nQuestion 4: Find all entries that are low alcohol; Alcohol by Volume (ABV) less than 1%:")
        low_abv = df[df.beer_abv < 1]
        db.print_full_table(low_abv)

        print("\nQuestion 5: How many reviews are there for low ABV beers?")
        print(len(low_abv))

        print("\nQuestion 6: Group the low ABV beers by beer name and count:")
        grouping = low_abv.groupby('beer_name')
        print(grouping.size())

        print("\nQuestion 7: How consistent are the O'Doul's overall scores?")
        odouls = low_abv[low_abv.beer_name == "O'Doul's"]['review_overall']
        print(f"-> With a standard deviation of {odouls.std():.4f} and a possible score ranging from 0 to 5, "
              "the O'Doul's overall scores are somewhat consistent.\n-> See following details:"
              )
        print(odouls.describe())

        print("\nQuestion 8: Plot a histogram of O'Doul's overall scores:\n(see plot)\n(close window to continue)")
        odouls.hist()
        plt.title("O'Doul's Overall Scores")
        plt.xlabel("Overall Score")
        plt.ylabel("Number of Reviews")
        plt.show()

        print("\nQuestion 9: For O'Doul's, what are the mean and standard deviation for the O'Doul's overall scores?")
        print(f"-> Mean: {odouls.mean()}")
        print(f"-> Standard deviation: {odouls.std():.4f}")

        print("\nQuestion 10: Draw a box plot of the low_abv data:\n(see plot)\n(close window to continue)")
        low_abv.boxplot(figsize=(12,10))
        plt.title("Low ABV Beers")
        plt.xlabel("Review Type")
        plt.ylabel("Score Out of 5")
        plt.show()

    except sqlite3.Error as error:
        logging.error(f"Error establishing database connection: {error}".format())
    finally:
        if conn:
            conn.commit()  # Commit any transactions to database.
            logging.debug("Transactions committed (if any)".format())
            conn.close()
            logging.debug("DB Connection Closed".format())

    # Close program.
    logging.info("Completed database operations".format())
    print('\nExiting program.')

# Ensure main() is executed only if this .py file is executed directly
# (i.e., not imported by another .py file)
if __name__ == "__main__":
    main()