#!/usr/bin/python3

"""
This module connects a python script to the database hbtn_0e_0_usa.
It should take 3 arguments:
mysql username, mysql password and database name
script should connect to a MySQL server running on localhost at port 3306
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    
    my_db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    my_cursor = my_db.cursor()

    my_cursor.execute("SELECT * FROM states")

    rows_selected = my_cursor.fetchall()

    for row in rows_selected:
        print(row)
