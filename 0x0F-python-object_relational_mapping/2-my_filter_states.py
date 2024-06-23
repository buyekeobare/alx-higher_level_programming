#!/usr/bin/python3
"""
This module that connects a python script to a database.
Script should take 3 arguments:
mysql username, mysql password and database name
script should connect to a MySQL server running on localhost at port 3306
"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

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
