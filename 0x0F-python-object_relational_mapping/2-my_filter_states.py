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
        host='localhost',
        user=argv[1],
        password=argv[2],
        db=argv[3],
        port=3306
        )

    my_cursor = my_db.cursor()

    my_cursor.execute(
        """
        SELECT * FROM states  WHERE name LIKE BINARY '{}'
        ORDER BY states.id ASC
        """.format(argv[4])
        )

    my_data = my_cursor.fetchall()

    for row in my_data:
        print(row)

    my_cursor.close()

    my_db.close()
