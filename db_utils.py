# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Module: db_utils
Description: SQLite3 database functions with logging.
COMP 662: Programming Databases with Python - SDCCD CCE  Spring 2024
Original author: Kathy Herring Hayashi
Revised by: Kendall Whitbeck
"""

import sqlite3
import os
import logging

def log_config(logfile=None, table_topic="Movies"):  # TODO consider adding logging level as an input parameter
    """ Configure logging. """
    if logfile is None:
        # If desired .log file not provided, use the name of this Python script to name the log file.
        filename = os.path.splitext(os.path.basename(__file__))[0]
        logfile = f"{filename}.log" ## NOTE this returns db_utils.log, not the calling script's <name>.log

    # Configure logging.
    logging.basicConfig(
        filename=logfile,
        level=logging.DEBUG,  # Options: DEBUG, INFO, ERROR, WARNING, CRITICAL
        format = f"[{table_topic}] : %(asctime)s : %(levelname)s : %(message)s")

def db_checkfile(dbfile):
    """ Check if database file exists and not zero size. """
    abspath_to_dbfile = os.path.abspath(dbfile)
    if os.path.exists(dbfile) and os.path.getsize(dbfile) > 0:
        logging.debug(f"DB file found and not zero size: {abspath_to_dbfile}".format())
    else:
        logging.error(f"DB file NOT found or zero size: {abspath_to_dbfile}".format())

def db_connect(dbfile):
    """ Connect to database. """
    conn = sqlite3.connect(dbfile)
    conn.row_factory = sqlite3.Row  # NOTE: enable this line to return rows as a dictionary rather than list of tuples.
    logging.debug("DB Connected".format())
    return conn

def db_cursor(con):
    """ Get cursor in database. """
    cur = con.cursor()
    logging.debug("Cursor set".format())
    return cur

def db_runquery(cur, query):
    """ Run query and return results (if any). """
    try:
        cur.execute(query)
        rows = cur.fetchall()
        headers = []
        if rows:
            headers = [desc[0] for desc in cur.description]
        logging.debug(f"DB Query executed and returned:\n\tQuery: {query}".format())
        return rows, headers
    except sqlite3.Error as error:
            logging.error(f"Error executing query:\n\tError: {error}\n\tQuery: {query}".format())

def db_select(cur, table, header):  # TODO finish SELECT function if needed
    pass # TODO

def db_insert(cur, table, headers, values):  # TODO finish Insert function if needed
    """ Insert SQL Query """
    query_insert = f"INSERT into {table} ({headers}) VALUES ({values})"
    print(query_insert)
    pass # TODO

def main():
    """ Demonstration of the logging and sqlite3 functions that are defined in this module. """
    dbfile = 'chinook.db'
    programname = f"Logfile SQLite3 Example Using {dbfile}"
    log_config()

    print(programname)
    db_checkfile(dbfile)
    try:
        con = db_connect(dbfile)
        cur = db_cursor(con)
        query = 'SELECT SQLITE_VERSION()'
        res = db_runquery(cur, query )
        print("SQLLITE version: " , res[0][0])
    except sqlite3.Error as error:
        logging.error("Error executing query", error)
    finally:
        if con:
            con.commit()  # Commit changes to database.
            con.close()
            logging.debug("[Info] DB Closed".format())

    print('Done - check completed')
    logging.info("Completed.")

if __name__ == '__main__':
    main()