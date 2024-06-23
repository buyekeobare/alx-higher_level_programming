#!/usr/bin/python3
"""
This module connects a python script to a database.
script should take 3 arguments:
mysql username, mysql password and database name
script should connect to a MySQL server running on localhost at port 3306
"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    my_db = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])

    my_cursor = my_db.cursor()
    my_cursor.execute(
        "SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})

    rows_selected = my_cursor.fetchall()

    for row in rows_selected:
        print(row)
