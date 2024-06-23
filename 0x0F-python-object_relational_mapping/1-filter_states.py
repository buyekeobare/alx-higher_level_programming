#!/usr/bin/python3

"""
Module that connects python script to a database.
This script lists all states with a name starting with N.
Script should take 3 arguments:
mysql username, mysql password and database name
script should connect to a MySQL server running on localhost at port 3306
"""

import MySQLdb as db
from sys import argv


if __name__ == '__main__':
    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()

    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
