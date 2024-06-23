#!/usr/bin/python3
"""
This module connects a python script to a database.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    my_db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    my_cursor = my_db.cursor()
    state_name = sys.argv[4]

    query = "SELECT * FROM states WHERE BINARY name = '{}'".format(state_name)
    my_cursor.execute(query)

    rows = my_cursor.fetchall()

    for row in rows:
        print(row)
