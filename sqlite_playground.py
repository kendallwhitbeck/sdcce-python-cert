#!"C:\Windows\py.exe"

### Program Name: sqlite_playground.py
### Author: Kendall Whitbeck

import sqlite3

def main():
    # basic database
    con = sqlite3.connect('/C:/Users/kenda/Google Drive/Kendalls Flashdrive/Adulting/Education/San Diego CCE/COMP 662/data/movies.sqlite')  # Full path to different folder
    # con = sqlite3.connect('db\movies.sqlite')  # CWD subfolder
    cur = con.cursor()

    # query to select all the elements from the movie table
    query = '''SELECT * FROM Movie'''

    # run the query
    cur.execute(query)

    # Save the results in list, movies.
    movies = cur.fetchall()

    # Loop through and print all the movies.
    for movie in movies:
        print(movie[2] , " " ,movie[3] , " " ,  movie[4])

    # Close the connection to the database file.
    if con:
        con.close()

if __name__ == "__main__":
    main()