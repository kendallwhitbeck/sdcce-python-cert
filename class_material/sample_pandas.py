#!/usr/bin/env python3
########################################
### Pandas Example
### Comp 662 - SDCCD CCE  Spring 2021
########################################
import sqlite3
import os
import logging
import pandas as pd
import matplotlib.pyplot as plt

def debug_config():
    logging.basicConfig(level=logging.DEBUG,format = "[Artists]:%(asctime)s:%(levelname)s:%(message)s")  #DEBUG,INFO,ERROR,WARNING,CRITICAL
    logging.getLogger('matplotlib.font_manager').disabled = True

def db_checkfile(dbfile):
    if os.path.exists(dbfile) and os.path.getsize(dbfile) > 0:
        logging.debug("{a} found and not zero size".format(a=dbfile))
    else:
        logging.error("{a} not found or zero size".format(a=dbfile))

def db_connect(dbfile):
    con = sqlite3.connect(dbfile)
    logging.debug("DB Connected".format())
    return con

def main():
    dbfile = '..\COMP_662_assignments\mod5\degrees2.db'
    programname = "Pandas Example"
    debug_config()

    print(programname)
    db_checkfile(dbfile)
    try:
        con = db_connect(dbfile)
        # Read sqlite query results into a pandas DataFrame
        df = pd.read_sql_query("SELECT * from degrees", con)

        #gca means "get current axes". "Current" here means that it provides a handle to the last active axes.
        ax = plt.gca()
        #select 4 columns to plot
        for degree in df.columns[1:10]:
          df.plot(x="Year", y=degree, kind='line', ax=ax)
        plt.show()

        print(df)
        print(df.columns.values)

    except sqlite3.Error as error:
        logging.error("Error executing query", error)
    finally:
        if con:
            con.close()
            logging.debug("[Info] DB Closed".format())

    print('Done - check completed')
    logging.info("Completed.")

if __name__ == '__main__':
    main()