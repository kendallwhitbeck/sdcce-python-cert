import sqlite3
from contextlib import closing
conn = sqlite3.connect("books.sqlite")
conn.row_factory = sqlite3.Row
with closing(conn.cursor()) as c:
    query = '''SELECT * FROM Book
               WHERE pages > ?'''
    c.execute(query, (100,))
    books = c.fetchall()
for book in books:
    print(book["name"], "|", book["author"], "|", book["pages"])
name = "The Case of the Killer Kangaroo"
author = "Jane Doe"
pages = 408
genreID = 1
with closing(conn.cursor()) as c:
    query = '''INSERT INTO Book
               (name, author, pages, genreID)
               VALUES (?, ?, ?, ?)'''
    c.execute(query, (name, author, pages, genreID))
    conn.commit()
print(name, "inserted.")
author = "Katie Kanga"
with closing(conn.cursor()) as c:
    query = '''UPDATE Book
               SET author = ?
               WHERE name = ?'''
    c.execute(query, (author, name))
    conn.commit()
print(name, "updated.")
