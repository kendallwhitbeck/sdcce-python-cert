# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Assignment 1
Author: Kendall Whitbeck
San Diego College of Continuing Education (SDCCE) Student ID: 5550203278
COMP 662: Programming Databases with Python
"""

import os  # os.system('cls'): clear terminal window text in Windows OS.
import sqlite3

def main():
    # Clear terminal window text if in Windows OS.
    if os.name == 'nt':
        os.system('cls')

    # Connect to the chinook.db database.
    con = sqlite3.connect("chinook.db")  # NOTE: assumes .db file is located in current directory

    # Create a cursor object to interact with the database connection.
    cur = con.cursor()

    # Create a query to select all the elements from the artists table within the chinook database.
    query = '''SELECT * FROM artists'''

    # Execute the query and save the results.
    cur.execute(query)
    artists = cur.fetchall()

    # Loop through each entry in the table and print the artist's name.
    print("List of Artists:\n")
    for artist in artists:
        print(artist[1])
    print("\nDone - See you next time!")

    # Close the connection to the database file.
    if con:
        con.close()

# Ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file)
if __name__ == "__main__":
    main()