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

    my_db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )

    my_cursor = my_db.cursor()

    filter_by = 'N%'

    my_cursor.execute("""SELECT * FROM states WHERE name LIKE BINARY %s
            ORDER BY id ASC""", (filter_by,))

    rows = my_cursor.fetchall()

    for row in rows:
        print(row)

    my_cursor.close()
    my_db.close()
