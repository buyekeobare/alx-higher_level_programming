#!/usr/bin/python3

"""
Module that connects python script to a database.
This script lists all states with a name starting with N.
Script should take 3 arguments:
mysql username, mysql password and database name
script should connect to a MySQL server running on localhost at port 3306
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    my_db_connect = my_db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    my_db_cursor = my_db_connect.cursor()

    my_db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")

    rows_selected = my_db_cursor.fetchall()

    for row in rows_selected:
        print(row) 
