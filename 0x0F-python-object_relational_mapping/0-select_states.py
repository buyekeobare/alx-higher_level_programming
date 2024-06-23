#!/usr/bin/python3

"""
Module that connects a python script to the database hbtn_0e_0_usa.
It should take 3 arguments:
mysql username, mysql password and database name
script should connect to a MySQL server running on localhost at port 3306
"""

if __name__ == "__main__":
    import sys
    import MySQLdb
    my_db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )

    my_cursor = my_db.cursor()

    my_cursor.execute("""SELECT * FROM states ORDER BY id ASC""")

    rows = my_cursor.fetchall()

    for row in rows:
        print(row)

    my_cursor.close()
    my_db.close()
