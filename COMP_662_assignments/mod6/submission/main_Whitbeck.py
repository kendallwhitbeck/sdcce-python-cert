from flask import Flask, render_template, request
import sqlite3 as sql
import logging
import os
import dbcalls_Whitbeck as db

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/view')
def view():
    try:
        # Establish database connection
        conn = db.db_connect(DBFILE)
        cur = db.db_cursor(conn)
        # SQL function to view data
        rows, headers = db.db_select(cur, TABLE)
    except sql.Error as error:
        logging.error(f"Error performing database operation: {error}".format())
        return render_template("view.html", rows=f"Error displaying data: {error}".format())
    finally:
        if conn:
            conn.commit()  # Commit any tranasactions to database.
            logging.debug("Transactions committed".format())
            conn.close()

    return render_template("view.html", rows=rows)

@app.route('/update')
def update():
    return render_template('update.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/delete')
def delete():
    return render_template("delete.html")

@app.route('/updaterec', methods=['POST', 'GET'])
def updaterec():
    if request.method == 'POST':
        nm = request.form['nm']
        addr = request.form['add']
        city = request.form['city']
        id = request.form['id']

        try:
            # Establish database connection
            conn = db.db_connect(DBFILE)
            cur = db.db_cursor(conn)
            # Insert user-input values into database
            values = (nm, addr, city, id)
            db.db_insert(cur, TABLE, HEADERS, values)
            msg = f"Record with ({nm}, {addr}, {city}, {id}) successfully added"
        except sql.Error as error:
            logging.error(f"Error performing database operation: {error}".format())
            return render_template("updateresult.html", message=f"Error updating record: {error}".format())
        finally:
            if conn:
                conn.commit()  # Commit any tranasactions to database.
                logging.debug("Transactions committed".format())
                conn.close()

        return render_template("updateresult.html", message=msg)

@app.route('/seachrec', methods=['POST', 'GET'])
def searchrec():
    if request.method == 'POST':
        nm = request.form['nm']
        addr = request.form['add']
        city = request.form['city']

        # Define search parameters
        where_attributes = ['name', 'addr', 'city']
        where_values = [nm, addr, city]

        try:
            # Establish database connection
            conn = db.db_connect(DBFILE)
            cur = db.db_cursor(conn)
            # SQL function to view data
            rows, headers = db.db_select(cur, TABLE, where_attributes=where_attributes, where_values=where_values)
        except sql.Error as error:
            logging.error(f"Error performing database operation: {error}".format())
            return render_template("searchresult.html", rows=f"Error displaying data: {error}".format())
        finally:
            if conn:
                conn.commit()  # Commit any tranasactions to database.
                logging.debug("Transactions committed".format())
                conn.close()

        return render_template("searchresult.html", rows=rows)

@app.route('/deleterec', methods=['POST', 'GET'])
def deleterec():
    if request.method == 'POST':
        nm = request.form['nm']

        # Define delete parameters
        where_attribute = 'name'
        where_value = nm

        try:
            # Establish database connection
            conn = db.db_connect(DBFILE)
            cur = db.db_cursor(conn)
            # SQL function to view data
            db.db_delete(cur, TABLE, where_attribute, where_value, True)
            num_rows_deleted = cur.rowcount
        except sql.Error as error:
            logging.error(f"Error performing database operation: {error}".format())
            return render_template("deleteresult.html", message=f"Error deleting data: {error}".format())
        finally:
            if conn:
                conn.commit()  # Commit any tranasactions to database.
                logging.debug("Transactions committed".format())
                conn.close()

        # Define return message based on whether or not a record was deleted
        if num_rows_deleted == 0:
            msg = f'Record with ("{where_attribute}" = "{nm}") not found'
        else:
            msg = f'Record with ("{where_attribute}" = "{nm}") successfully deleted'
        return render_template("deleteresult.html", message = msg)

if __name__ == '__main__':
    # Configure logging using name of this Python script to name log file
    # (NOTE: currently hardcoded to set root logger at DEBUG level).
    script_filename = os.path.splitext(os.path.basename(__file__))[0]
    log_filename = f"{script_filename}.log"
    db.log_config(log_filename)

    # Perform database setup
    DBFILE = "roster.db"
    TABLE = "students"
    HEADERS = ('name', 'addr', 'city', 'id')
    db.db_checkfile(DBFILE)

    # Run the database interface layer for the basic web-based application
    app.run(debug=True)