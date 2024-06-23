#!/usr/bin/python3
"""
This module connects a python script to a database.
"""

import MySQLdb as db
from sys import argv

if __name__ == "__main__":

    my_db = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])

    my_cursor = my_db.cursor()
    my_cursor.execute(
        "SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})

    rows_selected = my_cursor.fetchall()

    for row in rows_selected:
        print(row)
