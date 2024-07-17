#!/usr/bin/env python3
########################################
### Simple visualization Example
### Comp 662 - SDCCD CCE  Spring 2021
########################################
import sqlite3
import os
import logging
import matplotlib.pyplot as plt
import numpy as np



def debug_config():
    logging.basicConfig(level=logging.ERROR,format = "[Artists]:%(asctime)s:%(levelname)s:%(message)s")  #DEBUG,INFO,ERROR,WARNING,CRITICAL

def db_checkfile(dbfile):
    if os.path.exists(dbfile) and os.path.getsize(dbfile) > 0:
        logging.debug("{a} found and not zero size".format(a=dbfile))
    else:
        logging.error("{a} not found or zero size".format(a=dbfile))

def db_connect(dbfile):
    con = sqlite3.connect(dbfile)
    logging.debug("DB Connected".format())
    return con

def db_cursor(con):
    cur = con.cursor()
    logging.debug("Cursor set".format())
    return cur

def db_runquery(cur,query):
    cur.execute(query)
    result = cur.fetchall()
    logging.debug("DB Query executed and returned".format())
    return result

def print_years(res):
    plt.hist(res, bins=40)
    plt.ylabel('Number of Movies')
    plt.xlabel('Year Released')
    plt.locator_params(axis='y', integer=True)
    plt.title('COMP662 Movie Database')
    plt.show()

def main():
    dbfile = '../db/dbmovies.sqlite'
    programname = "Simple Visualization Example"
    debug_config()

    print(programname)
    db_checkfile(dbfile)
    try:
        con = db_connect(dbfile)
        cur = db_cursor(con)
        allyears = []
        query = 'SELECT year from Movie'
        res = db_runquery(cur, query )
        for result in res:
            allyears.append(result[0])
        print_years(allyears)
    except sqlite3.Error as error:   
        logging.error("Error executing query", error)
    finally:
        if con:
            con.close()
            logging.debug("[Info] DB Closed".format())

    print('Done - check completed')
    logging.info("Completed.")
#38 years

if __name__ == '__main__':
    main()