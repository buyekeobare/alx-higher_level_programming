#!/usr/bin/python3
"""
This module connects a python script to a database
"""

    import MySQLdb
    from sys import argv


    if __name__ == "__main__":

    # Connect database using command-line args
    db_db = MySQLdb.connect(host='localhost', user=argv[1], password=argv[2],
                            db=argv[3], port=3306)
    # Create cursor object to interact with db
    db_cursor = db_db.cursor()

    # Execute a SELECT query to fetch data
    db_cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")

    # fetch all the data returned by the query
    db_data = db_cursor.fetchall()

    # Iterate through the fetched data and print each row
    for row in db_data:
        print(row)

    # Close all cursors
    db_cursor.close()

    # Close all databases
    db_db.close()
