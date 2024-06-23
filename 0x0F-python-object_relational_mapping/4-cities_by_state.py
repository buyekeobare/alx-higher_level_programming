#!/usr/bin/python3

"""
This module connects python script to a database.
This script lists all states with a name starting with N.
Script should take 3 arguments:
mysql username, mysql password and database name
script should connect to a MySQL server running on localhost at port 3306
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':

    my_db = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])

    with my_db.cursor() as my_cursor:
        my_cursor.execute("SELECT cities.id, cities.name, states.name \
                                FROM cities JOIN states ON cities.state_id \
                                = states.id ORDER BY cities.id ASC")
        rows_selected = my_cursor.fetchall()

    if rows_selected is not None:
        for row in rows_selected:
            print(row)
